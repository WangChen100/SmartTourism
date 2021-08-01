#!/usr/bin/python

import os
import pandas as pd




def read_data(path):
    '''
    Read train/test data from corresponding CSV files
    parameter:
        path: floder path of data
    return:
        train: train data in DataFrame (pandas format)
        test:  test data in DataFrame (pandas format)
    '''
    if not os.path.exists(path):
        raise ValueError('This path is not existed!')
    
    train = pd.read_csv(path + 'train.csv')
    test = pd.read_csv(path + 'test.csv')

    print('Read data successfully!')

    # print ('***********Train*************')
    # print ('test')
    # print (train.isnull().sum())
    # print ('***********test*************')
    # print (test.isnull().sum())

    return train, test


def count_data(train, test):
    print ('***********Train*************')
    print ('test')
    print (train.isnull().sum())
    print ('***********test*************')
    print (test.isnull().sum())


if __name__=='__main__':
    # Here is an example to use function read_data()
    path = 'data/titanic/'
    data_trian, data_test = read_data(path)
    count_data(data_trian, data_test)
