from unittest import TestCase
from fsm import State, FsmException, Event

__author__ = 'NiCoretti'


class TestState(TestCase):

    def test_enter_state(self):
        state = State("Test state")
        event = Event("Test event", None)

        self.assertRaises(FsmException, state.enter_state, [event.data])


    def test_exit_state(self):
        state = State("Test state")
        event = Event("Test event", None)

        self.assertRaises(FsmException, state.exit_state, [event.data])