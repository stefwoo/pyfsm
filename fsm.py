#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
This module provides various classes to crate finite state machines.

    Exports:              -
    Constants:            -
    Functions:            -
    Classes:              -
    Exceptions:           -
    Decorators:           -
        
@author: Nicola Coretti
@contact: nico.coretti@googlemail.com
@version: 0.0.1 
'''
__all__ = ['State', 'Event', 'EventData', 'Transition', 'TransitionTable', 'StateMachine', 'FsmException']



# TODO's:
# 1. add __str__, __unicode__ methods to all classes

# Python imports
from UserDict import UserDict

# Logger setup

# TODO: add optional logging for states and transitions ...
# TODO: 

# -- Module Constants ---------------------------------------------------------
# -- Module Functions ---------------------------------------------------------
# -- Module Classes -----------------------------------------------------------

class State(object):
    """
    A state with a name and an description.
    """
    
    def __init__(self, name, description=""):
        """
        Creates a new state.
        
        @param name: an unique name which identifies this state and it's purpose.
        
        @param description: a detailed description what this state is all about.
        """
        self.name = name 
        self.description = description
        # maybe add final and error state indicator

    def enter_state(self, event_data):
        """
        This method is invoked every time this state will be entered.
        """
        raise Exception("Not implemented.")


    def exit_state(self, event_data):
        """
        This method is invoked every time before this state will be left.
        """
        raise Exception("Not implemented.")


class Event(object):
    """
    An Event consists of a name and associated data, it represents an external 
    or internal stimulus which has to be handled by a state machine. 
    """
    
    def __init__(self, name, event_data):
        """
        Creates a new event.
        
        @param name: an unique name which identifies the event.
        @type name: string
        
        @param event_data: data associated with this event.
        """
        self.name = name
        self.data = event_data 


class Transition(object):
    """
    A Transition with a source state and a destination state.  
    """

    def __init__(self, src_state, dst_state, action=None):
        """
        Creates a new Transition object.
        
        @param src_state:
        @type src_state: State
        
        @param dst_state: state which will be occupied after this transition.
        @param dst_state: State
        """
        self.event_name = event_name
        self.src_state = src_state
        self.dst_state = dst_state

    
    def execute_transition(event_data):
        """
        Makes the transition from src_state to dst_state.

        @return: new active state.
        """
        self.src_state.exit_state(event_data)
        if action != None: action()
        self.dst_state.enter_state(event_data)
    
        return self.dst_state


class TransitionTable(object):
    """
    A TransitionTable with various transitions.
    """

    def __init__(self, transitions):
        """
        Creates a new TransitionTable.
        """
        # key: class name of the state  value: transition dict
        # transition dict = key event class name, value: transition
        self.transition_table = {}


    # TODO: comment
    def add_transition(src_state, event, dst_state, action=None):
        """
        Adds a state to this transition manager.

        @param transition: which will be added.
        @type transition: Transition 

        @raise:
        """
        pass


    # TODO: comment 
    def remove_transition(src_state, event, dst_state, action=None):
        """
        Removes a transition from this transition manager.

        @param transition: which will be remvoed.
        @type Transition

        @raise:
        """
        pass

   
    # TODO: comment 
    def get_transition(self, state, event):
        """
        Gets the transition for the specified state
        with the given event. If no transition is available
        an exception will be thrown.

        @param state:
        @type state:

        @param event:
        @type event: 

        @return the transition suitable for the specified state/event combination.
        @rtype: Transition
        """
        pass


class StateMachine(object):
    """
    A simple finite state machine with a current state and transitions
    which will be used to switch between states.
    """

    def __init__(self, transition_table):
        """
        Creates a new StateMachine.
        """
        self._current_state = None
        self._transition_table = TransitionTable()


    def add_transition(src_state, event, dst_state):
        """
        Adds a transition to this state machine.

        @param transition: which will be added to this state machine.
        @type transition: Transition
        """
        pass


    def remove_transition(src_state, event, dst_state):
        """
        Remvoes a transition from this state machine.

        @param transition: which will be removed from this state machine.
        @type transition: Transition
        """
        pass


    def trigger_event(self, event):
        """
        Triggers an event in this state machine.

        @param event: which will be triggered.
        @type event: Event
        """
        pass

    
    def print_state_machine(self):
        """
        """
        pass


# -- Module Decorators ---------------------------------------------------------
# -- Module Exceptions -------------------------------------------------------- 
class FsmException(Exception):
    """
    Base class for all exceptions of the fsm module.
    """
   
    def __init__(self, *args, **kwargs):
        """
        Creates a new FsmException.
        """
        super(FsmException, self).__init__(*args, **kwargs) 


# TODO: Add example code
if __name__ == '__main__':
    pass
