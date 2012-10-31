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
__all__ = ['State', 'Event', 'EventData', 'Transition', 'TransitionManager', 'StateMachine', 'FsmException']



# TODO's:
# 1. add __str__, __unicode__ methods to all classes

# Python imports
from UserDict import UserDict

# Logger setup

# -- Module Constants ---------------------------------------------------------
# -- Module Functions ---------------------------------------------------------
# -- Module Classes -----------------------------------------------------------

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

    def __init__(self, name, event_data=None):
        """
        Creates a new event.

        @param name: an unique name which identifies the event.
        @type name: string

        @param event_data: data associated with this event.
        """
        self.name = name
        if event_data == None: event_data = EventData()
        self.data = event_data 


class EventData(UserDict):
    """
    This class is a container for various kinds of event data.
    Event data is used to provide further information for an event.
    """

    # TODO: comment
    def __init__(self, data_dict={}):
        """
        Creates a new EventData object.
        
        @param data_dict:
        """ 
        self.data = data_dict


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
        self.event_name = event_name
        self.src_state = src_state
        self.dst_state = dst_state

    
    def execute_transition(event_data):
        """
        Makes the transition from src_state to dst_state.

        @return: new active state.
        """
        self.src_state.exit_state(event_data)
        self.dst_state.enter_state(event_data)
    
        return self.dst_state


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


    # TODO: comment
    def add_transition(transition):
        """
        Adds a state to this transition manager.

        @param transition: which will be added.
        @type transition: Transition 

        @raise:
        """
        self._src_states[transition.src_state.name] = transition.src_state
        self._dst_states[transition.dst_state.name] = transition.dst_state
        
        event_name = transition.event_name
        src_sate   = transition.src_state

        if (event_name in self._transitions) and (src_state.name in self._transitions[event_name]):
            # report error => the given source state already has a transition
            # from src state trigger by this event
            raise FsmException("src_state/event_name combination already in use.")
        else:
            self._transitions[event_name][src_state.name] = transition.src_state

    
    # TODO: comment 
    def remove_transition(transition):
        """
        Removes a transition from this transition manager.

        @param transition: which will be remvoed.
        @type Transition

        @raise:
        """
        event_name = transition.event_name
        src_state  = transition.src_state
        dst_state  = transition.dst_state
        del self._src_states[src_state.name]
        del self._dst_states[dst_state.name]
        del self._transitions[event_name][src_state.name]

   
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
        transition = None
        if (event.name in self._transitions) and (state.name in self._transitions[event.name]):
            transition = self._transitions[event.name][state.name]
        else:
            err_msg = "No transition for the specified state/event combination available."
            raise FsmException(err_msg)

        return transition


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
        Adds a transition to this state machine.

        @param transition: which will be added to this state machine.
        @type transition: Transition
        """
        self._transition_mgr.add_transition(transition)


    def remove_transition(transition):
        """
        Remvoes a transition from this state machine.

        @param transition: which will be removed from this state machine.
        @type transition: Transition
        """
        self._transition_mgr.remove_transition(transition) 


    def trigger_event(self, event):
        """
        Triggers an event in this state machine.

        @param event: which will be triggered.
        @type event: Event
        """
        transition = self._transition_mgr.get_transition(self._current_state, event)
        self._current_state = transition.execute_transition(event.data)


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
