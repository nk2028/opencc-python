#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import json
import io
import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

from opencc import OpenCC


class UpstreamTestcasesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        testcases_path = os.path.join(
            os.path.dirname(__file__),
            os.pardir,
            'opencc',
            'testcases',
            'testcases.json',
        )
        with io.open(testcases_path, encoding='utf-8') as f:
            cls.testcases = json.load(f)['cases']

    def test_upstream_conversion_cases(self):
        converters = {}

        for case in self.testcases:
            input_text = case['input']
            for conversion, expected in case['expected'].items():
                with self.subTest(case_id=case['id'], conversion=conversion):
                    converter = converters.setdefault(conversion, OpenCC(conversion))
                    self.assertEqual(converter.convert(input_text), expected)


if __name__ == '__main__':
    unittest.main()
