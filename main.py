#coding=utf-8
__author__ = 'jiang'


import unittest
import datetime
import sys,os
import time
import subprocess
import collections



def test_decorator():
    def dec(_args):
        def wrapfunc(func):
            def wrap(*args,**kwargs):
                print '++++++++++++',_args
                func(*args,**kwargs)
            return wrap
        return wrapfunc
    @dec('/')
    def foo():
        print 'hello world!!!'
    foo()

def test_generator():
    pass

def test_lambda():
    print (lambda x:x**2)(5454)

def test_date():
    pass

def test_time():
    print time.strftime('%H:%M:%S')

def test_buildin():
    pass

def test_str():
    s = '套件'
    print(len(s))
    print(sys.subversion)

def test_subprocess():
    pass

def test_server():
    pass

def test_xrange():
    print xrange(10)
def test_member():
    class Test():

        def __init__(self):
            self.__dict__ = collections.OrderedDict()
            self.name = 'hello world!!!'
            self.age = 20
            self.data = [435,65,76,6,8,787,9,89,0,909,543,32,32]
        def __setattr__(self, key, value):
            self.__dict__[key] = value
        def __setitem__(self, key, value):
            print key,value

        def __iter__(self):
            return self
        def next(self):
            if len(self.data):
                return self.data.pop()
            else:
                raise StopIteration()
    t = Test()
    print t.__dict__
    print Test.__dict__
    t['language'] = 'java'

    for i in t:
        print i


if __name__ == '__main__':
    test_decorator()
    #test_member()
