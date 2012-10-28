#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
This module contains all exceptions/errors of the cca api.

    Exports:
    Constants:            -
    Functions:            -
    Classes:              -
    Exceptions:           -
    Decorators:           -
        
@author: Nicola Coretti
@contact: nico.coretti@googlemail.com
@version: 0.0.1 
'''
__all__ = []

# Python imports

# Logger setup

# -- Module Constants ---------------------------------------------------------
# -- Module Functions ---------------------------------------------------------
# -- Module Classes -----------------------------------------------------------

class StateFactory(object):
    """
    A StateFactory can be used to create state objects without subclassing the 
    State class.
    """

    def __init__(self):
        """
        """
        pass


    def create_state(name, enter_state_func=None, in_state_func=None, exit_state_func=None):
        """
        """
        pass

# TODO: create factory state class which provides hooks for the provided funcitons


class State(object):
    """
    A state with 
    """

    def __init__(self, name):
        """
        Creates a new state.

        @param name: an unique name which identifies this state.
        """
        self.name = name 
    

    def enter_state(self, event_data):
        """
        This method is invoked every time this state will be entered.
        """
        pass


    def exit_state(self, event_data):
        """
        This method is invoked every time before this state will be left.
        """
        pass


    def in_state(self, event_data):
        """
        This method is invoked periodically.
        """
        pass

    

    
class Event(object):
    """
    An event represents an external or internal stimulus which has to 
    be handled by a state machine. Usualy an event will cause an state change
    of the fsm.
    """

    # TODO: Comment 
    def __init__(self, name, event_data)
        """
        Creates a new event.

        @param name: an unique name which identifies the event.
        @type name: string

        @param event_params: 
        @type event_params:
        """
        self.name = name
        self.data = event_data 


class EventData(object):
    """
    This class is a container for various kinds of event data.
    Event data is used to provide further information for an event.
    """
    pass


class Transition(object):
    """
    A transition with a source state an event name and 
    a destionation state. Transition are used by state machines
    to determine when and how a state will and can be changed. 
    """

    def __init__(self, src_state, event_name,  dst_state):
        """
        Creates a new Transition object.

        @param src_state:
        @type src_state: State

        @param event_name: name of the event which triggers this transition.
        @type event_name: string

        @param dst_state: state which will be occupied after this transition.
        @param dst_state: State
        """
        self._event_name = event_name
        self._src_state = src_state
        self._dst_state = dst_state

    
    def execute_transition(event_data):
        """
        Makes the transition from src_state to dst_state.
        """
        src_state.exit_state(event_data)
        dst_state.enter_state(event_data)


# TODO: Implement python container methods/behaviour
class TransitionManager(object):
    """
    A TransitionManager with various transitions.
    """

    def __init__(self, transitions):
        """
        Creates a new TransitionManager.
        """
        self._src_states = {}
        self._dst_states = {}
        self._transitions = {}


    def add_transition(transition):
        """
        """
        pass

    
    def remove_transition(transition):
        """
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

    def __init__(self):
        """
        Creates a new StateMachine.
        """
        self._current_state = None
        self._transition_mgr = TransitionManager()


    def add_transition(transition):
        """
        """
        pass


    def remove_transition(transition):
        """
        """
        pass 


    def trigger_event(self, event):
        """
        """
        transition = self._transition_mgr.get_transition(self._current_state, event)
        transition.execute_transition(event.data)

    def execute_current_state():
        """
        Periodically calls the in_state method of the current state.
        """
        event = Event()
        self._current_state.in_state(event.data)


# -- Module Decorators ---------------------------------------------------------
# -- Module Exceptions --------------------------------------------------------

class FsmException(Exception):
    """
    """
    pass
    

# TODO: Add example code
if __name__ == '__main__':
    pass
    

# TODO: Add unit tests
