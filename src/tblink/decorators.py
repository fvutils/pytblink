'''
Created on Jul 8, 2020

@author: ballance
'''

import ctypes
from typing import Generic, TypeVar, List
import typing

from .impl.test_rgy import TestRgy


def test(*args, **kwargs):
    class test_w(object):
        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs
            
        def __call__(self, T):
            TestRgy.inst().add_test(T)
            return T
            
    if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
        # Called as @test
        TestRgy.inst().add_test(args[0])
        return args[0]
    else:
        # Called as @test(...)
        return test_w(args, kwargs)
        
    

# def if_class(T):
#     """Defines a class as an interface class"""
#     return T
# 
# def imp_task(T):
#     """Decorator for a task callable from Python"""
#     print("imp_task")
#     if not hasattr(T, "__annotations__"):
#         raise Exception("Import-task " + T.name + " does not have annotations")
#     if hasattr(T, "__annotations__"):
#         ann = T.__annotations__
#         if "return" in ann.keys():
#             raise Exception("Import task " + T.name + " incorrectly specifies a return")
#         
#         for a in ann.keys():
#             print("arg: " + a + " " + str(ann[a]))
#     return T
#     
#     return T
# 
# def exp_task(T):
#     """Decoroator for a task callable from HVL"""
#     if hasattr(T, "__annotations__"):
#         ann = T.__annotations__
#         if "return" in ann.keys():
#             raise Exception("Export task " + T.name + " incorrectly specifies a return")
#         
#         for a in ann.keys():
#             print("arg: " + a + " " + str(ann[a]))
#         
#     return T
# 
# def imp_function(T):
#     """Decorator for a function callable from Python"""
#     return T
# 
# def exp_function(T):
#     """Decoroator for a task callable from HVL"""
#     return T
# 
# T = TypeVar('T')
# #N = TypeVar('N')
# class Ref(Generic[T]):
#     pass
# 
# @if_class
# class foo(object):
# 
#     # Annotations of class fields    
#     x : ctypes.c_uint64
#     
#     def __init__(self):
#         self.x = 0;
# 
#     @exp_task
#     def my_task(self, a : ctypes.c_uint64, b : List[ctypes.c_uint8], c : Ref[List[ctypes.c_uint16]]):
#         pass

