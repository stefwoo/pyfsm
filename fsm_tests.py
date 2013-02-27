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

# fsm imports
from fsm import *

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


class TestTransition(unittest.TestCase):
    """
    Tests the basic functionality of the Transition class.
    """


    def setUp(self):

        self.state1 = State()
        self.state2 = State()
    
        self.transition1 = Transition()
        self.transition2 = Transition()
        self.transition3 = Transition()
    
    def test_execute_transition_test1(self):
        pass

    def test_execute_transition_test2(self):
        pass

    def test_execute_transition_test3(self):
        pass


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
