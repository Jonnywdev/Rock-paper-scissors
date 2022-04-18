import random

def main():
    """
    This is the main function that will be used to run the game and
    it will have other function such as a way to get the username!
    """

    print("Welcome to Rock | paper | scissors!")
    print("rules: \n")
    print("rock beats scissors, paper beats \
    rock and scissors beats paper.")
    print("Play by choosing and entering either rock, paper or scissors.")
    print("Please make sure that you enter one of the 3 \
        options as any other entry will not be valid.\n")

    def get_username():
        """
        This function will be used to get the players username.
        """
        username = input("Please enter a username to get started\n")
        return username

    def get_winning_response():
        """
        This function will produce a random response if the player wins a round.
        """
        list_of_winning_responses = ["Well done!", "Wooo go you!", "That was impressive.", "Are you reading my mind?", "No way, how did you do that?", "Congratulations that a point to you.", "Expertly Done!"]

        show_winning_response = random.choice(list_of_winning_responses)
        return show_winning_response
    
    def get_losing_response():
        """
        This function will produce a random response if the player loses a round.
        """
        list_of_losing_responses = ["Unlucky!", "Oh no!", "What are you playing at? ;)", "Maybe you'll get it right next time?", "Better luck next time", "uh oh", "You need to get better at guessing"]

        show_losing_response = random.choice(list_of_losing_responses)
        return show_losing_response

    def has_won():