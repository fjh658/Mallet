#! /usr/bin/env python
# -*- coding: utf-8 -*-

# The MIT License (MIT)
#
# Copyright (c) 2014 Bartosz Janda
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

from ...scripts import helpers
from ..Foundation import NSObject
from .. import SummaryBase
import os.path


class UIStoryboardSyntheticProvider(NSObject.NSObjectSyntheticProvider):
    """
    Class representing UIStoryboard.
    """
    def __init__(self, value_obj, internal_dict):
        super(UIStoryboardSyntheticProvider, self).__init__(value_obj, internal_dict)
        self.type_name = "UIStoryboard"

        self.register_child_value("storyboard_file_name", ivar_name="storyboardFileName",
                                  primitive_value_function=SummaryBase.get_stripped_summary_value,
                                  summary_function=self.get_storyboard_file_name_summary)

    @staticmethod
    def get_storyboard_file_name_summary(value):
        file_name, _ = os.path.splitext(value)
        return "fileName=\"{}\"".format(file_name)

    def summary(self):
        return self.storyboard_file_name_summary


def summary_provider(value_obj, internal_dict):
    return helpers.generic_summary_provider(value_obj, internal_dict, UIStoryboardSyntheticProvider)


def lldb_init(debugger, dictionary):
    debugger.HandleCommand("type summary add -F {}.summary_provider \
                            --category UIKit \
                            UIStoryboard".format(__name__))
    debugger.HandleCommand("type category enable UIKit")