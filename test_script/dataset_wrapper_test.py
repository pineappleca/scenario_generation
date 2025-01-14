#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@file:dataset_wrapper_test.py
@time:2025/01/13 10:48:20
@author:Yao Yongrui
'''

'''
test magicdrive/dataset/dataset_wrapper.py 
'''

import sys
sys.path.append("./")
from magicdrive.dataset import collate_fn, ListSetWrapper, FolderSetWrapper

def test_FolderSetWrapper():
    val_dataset = FolderSetWrapper("demo/data")
    data_pth = val_dataset.get_data(0)
    return data_pth.keys()

print(test_FolderSetWrapper())