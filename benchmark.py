#!/usr/bin/env python
# -*- coding: utf-8 -*-

# benchmark.py
# Copyright 2017 Christopher Simpkins
#
# Used for benchmarking single process compiles

from fmp import build_fonts

test_paths = ('tests/Hack-Regular.ufo', 'tests/Hack-Italic.ufo', 'tests/Hack-Bold.ufo', 'tests/Hack-BoldItalic.ufo')

if __name__ == '__main__':
    for ufo_path in test_paths:
        build_fonts(ufo_path)