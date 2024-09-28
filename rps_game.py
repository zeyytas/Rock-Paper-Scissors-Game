import random


class RockPaperScissors:

    def __init__(self) -> None:
        self.choices = ["rock", "paper", "scissors"]
        self.rules = {"rock": "scissors", "scissors": "paper", "paper": "rock"}

    def get_computer_choice(self) -> str:
        """Return a random choice for the computer."""
        return random.choice(self.choices)

    def get_winner(self, player: str, computer: str) -> str:
        """
        Determine the winner of the game.

        Args:
            player (str): The player's choice.
            computer (str): The computer's choice.

        Returns:
            str: A message indicating the outcome of the round.
        """
        if player == computer:
            return "You both chose the same! What a coincidence!"
        elif self.rules[player] == computer:
            return "Nice choice! You outsmarted the computer!"
        else:
            return "Oh no! The computer won this round!"

    @staticmethod
    def display_rules() -> None:
        """Display the rules of the game."""
        rules = (
            "Welcome to Rock-Paper-Scissors!\n"
            "Rules:\n"
            " - Rock beats Scissors\n"
            " - Scissors beats Paper\n"
            " - Paper beats Rock\n"
            "Type 'q' at any time during the game to quit."
        )
        print(rules)

    def play_game(self) -> None:
        """Main method to play the game."""
        self.display_rules()
        try:
            n_rounds = int(input("How many rounds would you like to play? "))
            for _ in range(n_rounds):
                player_choice = input("Enter rock, paper or scissors: ").lower()

                if player_choice == "q":
                    break

                if player_choice not in self.choices:
                    print("Invalid choice. Please select rock, paper, or scissors.")
                    continue

                computer_choice = self.get_computer_choice()
                print(f"Computer chose: {computer_choice}")

                result = self.get_winner(player_choice, computer_choice)
                print(result)

        except ValueError:
            print("Oops! You entered an invalid number for the rounds.")

        finally:
            print("Thanks for playing! Hope you had fun!")


if __name__ == "__main__":
    game = RockPaperScissors()
    game.play_game()
