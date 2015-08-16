#! /usr/bin/env python
# -*- coding: utf-8 -*-

# The MIT License (MIT)
#
# Copyright (c) 2013 Bartosz Janda
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from ..common import SummaryBase


class CGSizeSyntheticProvider(SummaryBase.SummaryBaseSyntheticProvider):
    """
    Class representing CGSize structure.
    """
    # struct CGSize {
    #   CGFloat width;
    #   CGFloat height;
    # };
    # typedef struct CGSize CGSize;
    def __init__(self, value_obj, internal_dict):
        super(CGSizeSyntheticProvider, self).__init__(value_obj, internal_dict)

        self.register_child_value("width", ivar_name="width", primitive_value_function=SummaryBase.get_float_value)
        self.register_child_value("height", ivar_name="height", primitive_value_function=SummaryBase.get_float_value)