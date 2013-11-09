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

import lldb


def SKProductsResponse_SummaryProvider(valobj, dict):
    stream = lldb.SBStream()
    valobj.GetExpressionPath(stream)
    num_valid_products_o = valobj.CreateValueFromExpression("valid_count",
                                                            "(NSUInteger)[[" + stream.GetData() +
                                                            " products] count]")
    num_valid_products = num_valid_products_o.GetValueAsUnsigned()
    num_not_valid_products_o = valobj.CreateValueFromExpression("not_valid_count",
                                                                "(NSUInteger)[[" + stream.GetData() +
                                                                " invalidProductIdentifiers] count]")
    num_not_valid_products = num_not_valid_products_o.GetValueAsUnsigned()

    return "@\"Valid: {}, not valid: {}\"".format(num_valid_products, num_not_valid_products)


def __lldb_init_module(debugger, dict):
    debugger.HandleCommand("type summary add -F SKProductsResponse.SKProductsResponse_SummaryProvider \
                            --category StoreKit \
                            SKProductsResponse")
    debugger.HandleCommand("type category enable StoreKit")