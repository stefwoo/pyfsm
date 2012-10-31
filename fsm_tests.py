#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
This module contains --- 

    Exports:
    Constants:            -
    Functions:            -
    Classes:              -
    Exceptions:           -
    Decorators:           -
        
@author: Nicola Coretti
@contact: 
@version: 
'''
__all__ = []

# Python imports
import unittest

class TestState(State):
    """
    A subclass of the state class for test purposes.
    """

    def __init__(self, name):
        super(TestState, self).__init__(name)

    def enter_state(event_data):
        event_data["enter_state"] = True 
        event_data["exit_state"]  = False
        event_data["in_state"]    = False

    def exit_state(event_data):
        event_data["enter_state"] = False
        event_data["exit_state"]  = True
        event_data["in_state"]    = False

    def in_state(event_data):
        event_data["enter_state"] = False 
        event_data["exit_state"]  = False
        event_data["in_state"]    = True

class TestStateMachine(unittest.TestCase):


    def setUp(self):
        pass


class TestStateBasicFunctionality(unittest.TestCase):

    def setUp(self):
        pass

class TestEventData(unittest.TestCase):

    def setUp(self):
        pass
# Logger setup

# -- Module Constants ---------------------------------------------------------
# -- Module Functions ---------------------------------------------------------
# -- Module Classes -----------------------------------------------------------
# -- Module Decorators ---------------------------------------------------------
# -- Module Exceptions --------------------------------------------------------


if __name__ == '__main__':
   
    # execute the tests 
    unittest.main()
