import unittest
from gamestate import GameState


class testGameState(unittest.TestCase):
    def setUp(self):
        self.state = GameState()

    def test_get_round_returns_round(self):
        state = GameState(4)
        self.assertEqual(state.get_round(), 4)

    def test_get_throw_returns_throw(self):
        state = GameState(1, 2)
        self.assertEqual(state.get_throw(), 2)

    def test_get_score_returns_score(self):
        state = GameState(1, 1, 52)
        self.assertEqual(state.get_score(), 52)

    def test_set_score_updates_score(self):
        self.state.set_score(32)
        self.assertEqual(self.state.get_score(), 32)

    def test_next_round_updates_round(self):
        self.state.next_round()
        self.assertEqual(self.state.get_round(), 2)

    def test_next_round_resets_throw(self):
        state = GameState(1, 2)
        state.next_round()
        self.assertEqual(state.get_throw(), 1)

    def test_next_throw_updates_throw(self):
        self.state.next_throw()
        self.assertEqual(self.state.get_throw(), 2)

    def test_update_resets_throw_after_three_throws(self):
        state = GameState(1, 3)
        state.update()
        self.assertEqual(state.get_throw(), 1)

    def test_update_doesnt_reset_throw_before_three_throws(self):
        state = GameState(1, 2)
        self.state.update()
        self.assertNotEqual(state.get_throw(), 1)

    def test_update_updates_round_after_three_throws(self):
        state = GameState(1, 3)
        state.update()
        self.assertEqual(state.get_round(), 2)

    def test_update_returns_true_after_three_throws(self):
        state = GameState(1, 3)
        self.assertEqual(state.update(), True)

    def test_update_returns_false_before_three_throws(self):
        self.assertEqual(self.state.update(), False)
