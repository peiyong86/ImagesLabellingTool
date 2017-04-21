#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Usage:
    This file is used to define labels, you may modify it to suit your needs.
    Please note labels_all is used by main script, so it must exist and include all labels dict.
"""
labels_age = {ord('1'):'1-10', ord('2'):'11-18', ord('3'):'19-26', ord('4'):'26-100'}
labels_gender = {ord('1'):'male', ord('2'):'female', ord('3'):'other'}
labels_race = {ord('1'):'yellow', ord('2'):'white', ord('3'):'black', ord('4'):'other'}
labels_all = [labels_age, labels_gender, labels_race]
