# -*- coding: utf8 -*-

from lib.data.data import read_data

# 读数据
path = 'data/titanic/'
data_train, data_test = read_data(path)

# 模型