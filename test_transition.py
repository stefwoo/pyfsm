
from unittest import TestCase
from fsm import State, Event, Transition

__author__ = 'NiCoretti'


class TestTransition(TestCase):

    def setUp(self):
        self.start_state = State("start_state")
        self.end_state = State("end_state")
        self.mock_enter_and_exit_methods_for_state(self.start_state)
        self.mock_enter_and_exit_methods_for_state(self.end_state)
        self.event = Event("Test event", "Event data")
        self.is_action_executed = False


    def test_execute_transition(self):
        # prepare data and set up pre conditions
        transition = Transition(self.start_state, self.end_state, None)

        # assert preconditions
        self.assertFalse(self.start_state.exit_state_was_called)
        self.assertFalse(self.end_state.enter_state_was_called)

        # run test sequence
        transition.execute_transition(self.event.data)

        # assert postconditions
        self.assertTrue(self.start_state.exit_state_was_called)
        self.assertTrue(self.end_state.enter_state_was_called)


    def test_execute_transition_with_action(self):
        # prepare data and set up pre conditions
        def test_action(): self.is_action_executed = True
        transition = Transition(self.start_state, self.end_state, test_action)

        # assert preconditions
        self.assertFalse(self.start_state.exit_state_was_called)
        self.assertFalse(self.end_state.enter_state_was_called)
        self.assertFalse(self.is_action_executed)

        # run test sequence
        transition.execute_transition(self.event.data)

        # assert postconditions
        self.assertTrue(self.start_state.exit_state_was_called)
        self.assertTrue(self.end_state.enter_state_was_called)
        self.assertTrue(self.is_action_executed)


    def mock_enter_and_exit_methods_for_state(self, state):
        self.mock_enter_method_for_state(state)
        self.mock_exit_method_for_state(state)


    def mock_enter_method_for_state(self, state):
        state.enter_state_was_called = False
        def mocked_enter_method(event_data): state.enter_state_was_called = True
        state.enter_state = mocked_enter_method


    def mock_exit_method_for_state(self, state):
        state.exit_state_was_called = False
        def mocked_exit_method(event_data): state.exit_state_was_called = True
        state.exit_state = mocked_exit_method
