#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
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
"""

__all__ = ['State', 'Event', 'EventData', 'Transition', 'TransitionTable', 'StateMachine', 'FsmException']


# Logger setup


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


    def enter_state(self, event_data):
        """
        This method is invoked every time this state will be entered.

        @param event_data: which was provided by the event which provoked to
                           switch into this state.
        """
        raise FsmException("Not implemented.")


    def exit_state(self, event_data):
        """
        This method is invoked every time before this state will be left.

        @param event_data: which was provided by the event which provoked to
                           leave this state.
        """
        raise FsmException("Not implemented.")


    def  __str__(self):
        """
        @return: a human readable representation of this object.
        """
        str_repr = "State: {0}, Description: {1}"
        str_repr = str_repr.format(self.name, self.description)

        return str_repr


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


    def __str__(self):
        """
        @return: a human readable representation of this object.
        """
        str_repr = "Event: {0}, Event-Args: {1}"
        str_repr = str_repr.format(self.name, self.data)

        return str_repr


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
        self.src_state = src_state
        self.dst_state = dst_state
        self.action = action

    
    def execute_transition(self, event_data):
        """
        Makes the transition from src_state to dst_state.

        @return: new active state.
        """
        self.src_state.exit_state(event_data)
        if self.action is not None: self.action()
        self.dst_state.enter_state(event_data)
    
        return self.dst_state


    def  __str__(self):
        """
        @return: a human readable representation of this object.
        """
        str_repr = "{0: 300<} => {1: 30<}, Action: {2}"
        str_repr = str_repr.format(self.src_state, self.dst_state, self.action)

        return str_repr


class TransitionTable(object):
    """
    A TransitionTable with various transitions and their associated events to trigger them.
    """

    def __init__(self):
        """
        Creates a new empty TransitionTable.
        """
        # key: class name of the state  value: transition dict
        # transition dict = key event class name, value: transition
        self.transition_table = {}


    # TODO: comment param action
    def add_transition(self, src_state, event, dst_state, action=None):
        """
        Adds a transition to this transition table.

        @param src_state: which will be used to create the transition.
        @param event: which shall trigger the created transition.
        @param dst_state: which will be used to create the transition.

        @return: a reference to the new created and added transition.
        """
        transition = Transition(src_state, dst_state, action)
        if event.name in self.transition_table:
            self.transition_table[event.name][src_state.name] = transition
        else:
            self.transition_table[event.name] = {}
            self.transition_table[event.name][src_state.name] = transition

        return transition


    # TODO: comment / bugfix => dst_state is not considered in deletion
    def remove_transition(self, src_state, event, dst_state):
        """
        Removes a transition from this transition manager.
        """
        if event.name in self.transition_table and src_state.name in self.transition_table[event.name]:
            del self.transition_table[event.name][src_state.name]

   
    def get_transition(self, current_state, event):
        """
        Gets the transition for the specified state
        with the given event. If no transition is available
        an exception will be thrown.

        @param current_state: source state of the transition.
        @type current_state: State

        @param event: which triggers the transition.
        @type event: Event

        @return the transition suitable for the specified state/event combination.
        @rtype: Transition

        @raise if no suitable transition was found an FsmException will be thrown.
        """
        transition = None
        if event.name in self.transition_table:
            if current_state.name in self.transition_table[event.name]:
                transition = self.transition_table[event.name][current_state.name]
            else:
                err_msg = "No transition available for Event: {0} in State: {1}"
                err_msg = err_msg.format(event.name, current_state.name)
                raise FsmException(err_msg)
        else:
            err_msg = "No transitions available for this Event ({0})"
            err_msg = err_msg.format()
            raise FsmException(err_msg)

        return transition


    def  __str__(self):
        """
        @return: a human readable representation of this object.
        """
        err_msg = "Not implemented yet."
        raise Exception(err_msg)


class StateMachine(object):
    """
    A simple finite state machine with a current state and transitions
    which will be used to switch between states.
    """

    def __init__(self, start_state, transition_table):
        """
        Creates a new StateMachine.

        @param start_state: of this state machine.
        @param transition_table: which is used to switch states.

        @raise: FsmException if invalid initializer arguments are specified.
        """
        if start_state is None:
            err_msg = "No initial state specified"
            raise FsmException(err_msg)
        if transition_table is None:
            err_msg = "No transition table specified"
            raise FsmException(err_msg)

        self.current_state = start_state
        self.transition_table = transition_table


    # TODO: comment param action
    def add_transition(self, src_state, event, dst_state, action=None):
        """
        Adds a transition to this state machine.

        @param src_state: which will be used to create the transition.
        @param event: which shall trigger the created transition.
        @param dst_state: which will be used to create the transition.

        @return: a reference to the new created and added transition.
        """
        return self.transition_table.add_transition(src_state, event, dst_state, action)


    # TODO: provide comment for parameters
    def remove_transition(self, src_state, event, dst_state):
        """
        Removes a transition from this state machine.
        """
        return self.transition_table.remove_transition(src_state, event, dst_state)


    def trigger_event(self, event):
        """
        Triggers an event in this state machine.

        @param event: which will be triggered.
        @type event: Event
        """
        transition = self.transition_table.get_transition(self.current_state, event)
        self.current_state = transition.execute_transition(event.data)

        return self.current_state

    
    def print_state_machine(self):
        """
        Prints a human readable representation of this state machine to std out.
        """
        state_machine_str = ""
        print(state_machine_str)


    def  __str__(self):
        """
        @return: a human readable representation of this object.
        """
        str_repr = "Current-State: {0}\n\nTransition-Table:\n--------------------\n{1}"
        str_repr = str_repr.format(self.current_state, self.transition_table)

        return str_repr


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
