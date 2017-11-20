import json

import logging
import pprint

from nose.tools import assert_dict_equal

from .base import BaseTransitionCondition


logger = logging.getLogger(__name__)


class DictEqual(BaseTransitionCondition):
    def __init__(self, type, expected):
        self.expected = expected

    def is_met(self, values):
        expected = json.loads(self.expected)

        pprint.pprint(expected)
        pprint.pprint(values)
        logger.info({
            'class': self.__class__,
            'expected': expected,
            'received': json.dumps(values),
        })
        assert_dict_equal(values, expected, '{} != {}'.format(values, expected))
        return values


class LengthEqual(BaseTransitionCondition):

    def __init__(self, type, length):
        self.length = length

    def is_met(self, collection):
        logger.info({
            'class': self.__class__,
            'collection': collection,
            'length': self.length,
        })
        assert len(collection) == self.length, 'collection ({}) != expected ({})'.format(
            len(collection), self.length
        )
        return collection


class ParseJSON(BaseTransitionCondition):

    def __init__(self, type, value_property=None):
        self.value_property = value_property

    def is_met(self, values):
        vs = []
        for v in values:
            vs.append(self.parse(v))
        return vs

    def parse(self, value):
        to_load = value
        if self.value_property:
            to_load = getattr(value, self.value_property)
        return json.loads(to_load)


class HasKeys(BaseTransitionCondition):

    def __init__(self, type, value_property=None, keys=()):
        self.keys = keys
        self.value_property = value_property

    def is_met(self, value):
        to_assert = value
        if self.value_property:
            to_assert = getattr(value, self.value_property)

        logger.info({
            'type': self,
            'to_assert': to_assert,
            'keys': self.keys,
        })
        assert set(to_assert) == set(self.keys)
        return to_assert
