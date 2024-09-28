import unittest
from unittest.mock import patch

from rps_game import RockPaperScissors


class TestRockPaperScissors(unittest.TestCase):

    def setUp(self):
        # Set up the RockPaperScissors for testing.
        self.game = RockPaperScissors()

    def test_winner_tie(self):
        # Test the case when both player and computer make the same choice.
        for choice in self.game.choices:
            self.assertEqual(
                self.game.get_winner(choice, choice),
                "You both chose the same! What a coincidence!",
            )

    def test_player_wins(self):
        # Test cases where the player wins.
        for winning_choice, losing_choice in self.game.rules.items():
            self.assertEqual(
                self.game.get_winner(player=winning_choice, computer=losing_choice),
                "Nice choice! You outsmarted the computer!",
            )

    def test_computer_wins(self):
        # Test cases where the player wins.
        for winning_choice, losing_choice in self.game.rules.items():
            self.assertEqual(
                self.game.get_winner(player=losing_choice, computer=winning_choice),
                "Oh no! The computer won this round!",
            )

    @patch("builtins.print")
    @patch("builtins.input", side_effect=["1", "rock-paper"])
    def test_invalid_player_input(self, mock_input, mock_print):
        # Test case for invalid player input.
        self.game.play_game()
        mock_print.assert_any_call(
            "Invalid choice. Please select rock, paper, or scissors."
        )

    @patch("builtins.print")
    @patch("builtins.input", side_effect=["1", "rock", "paper", "scissors"])
    def test_play_game(self, mock_input, mock_print):
        # Test the final message after playing the game.
        self.game.play_game()
        mock_print.assert_any_call("Thanks for playing! Hope you had fun!")

    @patch("builtins.print")
    @patch("builtins.input", side_effect=["invalid"])
    def test_invalid_rounds_input(self, mock_input, mock_print):
        # Test the output message for invalid number of rounds.
        self.game.play_game()
        mock_print.assert_any_call(
            "Oops! You entered an invalid number for the rounds."
        )

    @patch("builtins.print")
    @patch("builtins.input", side_effect=["1", "q"])
    def test_quit_game(self, mock_input, mock_print):
        """Test quitting the game with 'q' input."""
        self.game.play_game()
        mock_print.assert_any_call("Thanks for playing! Hope you had fun!")
        self.assertEqual(mock_print.call_count, 2)


if __name__ == "__main__":
    unittest.main()
