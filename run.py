import random


def main():
    """
    This is the main function that will be used to run the game and
    it will have other function such as a way to get the username!
    """

    print("Welcome to Rock | paper | scissors!")
    print("rules: \n")
    print("rock beats scissors, paper beats rock and scissors beats paper.")
    print("Play by choosing and entering either rock, paper or scissors.")
    print("Please make sure that you enter one of the \n")
    print("3 options as any other entry will not be valid.\n")

    def get_username():
        """
        This function will be used to get the players username.
        """
        username = input("Please enter a username to get started \n")
        return username

    def get_winning_response():
        """
        This function will produce a random
        response if the player wins a round.
        """
        list_of_winning_responses = ["Well done!", "Wooo go you!",
                                     "That was impressive.",
                                     "Are you reading my mind?",
                                     "No way, how did you do that?",
                                     "Congratulations that a point to you.",
                                     "Expertly Done!"]

        show_winning_response = random.choice(list_of_winning_responses)
        return show_winning_response

    def get_losing_response():
        """
        This function will produce a random
        response if the player loses a round.
        """
        list_of_losing_responses = ["Unlucky!",
                                    "Oh no!",
                                    "What are you playing at? ;)",
                                    "Maybe you'll get it right next time?",
                                    "Better luck next time",
                                    "uh oh",
                                    "You need to get better at guessing"]

        show_losing_response = random.choice(list_of_losing_responses)
        return show_losing_response

    def has_won(player, opponent):
        """
        This function will be used to figure out who has won the
        round either the user or the opponent
        """
        if (player == "rock" and opponent == "scissors") or \
           (player == "scissors" and opponent == "paper") \
           or (player == "paper" and opponent == "rock"):
            return True

    players_score = 0
    computers_score = 0

    username = get_username()
    print(f"\nWelcome to Rock | Paper | Scissors {username}! \n \
    we hope you have a fun time")

    while True:
        try:
            input_choices = {"rock", "paper", "scissors"}
            players_input = input("Please type your choice \n").lower()

            winning_response = get_winning_response()
            losing_response = get_losing_response()

            if any(players_input in choice for choice in input_choices):
                print(f"You have chosen {players_input}")

                computers_choice = random.choice(["rock", "paper", "scissors"])
                print(f"The computer has chosen {computers_choice}")

                has_won(players_input, computers_choice)
                if players_input == computers_choice:
                    print("Ahh it's a draw! \n")
                    print(f"{username} your score is: {players_score} \
                        \nComputers score is: {computers_score}\n")
                elif has_won(players_input, computers_choice):
                    print(f"You did it, you won! \n {winning_response} \n")
                    players_score = players_score + 1
                    print(f"{username} your score is: {players_score} \
                        \nComputers score is: {computers_score}\n")
                elif has_won(computers_choice, players_input):
                    print(f"You lose! \n{losing_response} \n")
                    computers_score = computers_score + 1
                    print(f"{username} your score is: {players_score} \
                        \nComputers score is: {computers_score}\n")
            else:
                raise ValueError()
        except ValueError:
            print(f"Unfortunately that input was not valid\n Your input was {players_input}\n \
                Please enter either rock, paper or scissors!")


main()
