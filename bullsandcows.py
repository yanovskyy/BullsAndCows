__author__ = "Vadim Janovskij"
__version__ = "1.0"
__email__ = "vadim.janovskij@mail.muni.cz"
__status__ = "Production"

import random
class BullsAndCows(object):

    def __init__(self, numOfNumbersToGuess):
        """
        Initializes a new instance of the BullsAndCows class
        :param numOfNumbersToGuess: indicates number of digits, that we want to generate and play with
        """
        self.__numOfNumbersToGuess = numOfNumbersToGuess

    def run(self):
        """
        Run the entire game
        """
        print "Hi there!"
        print "I've generated a random %d digit number for you." % self.__numOfNumbersToGuess
        print "Let's play a bulls and cows game."
        secretNumber = self.generate_secretNumber(self.__numOfNumbersToGuess)
        numberOfGuesses = 0
        while True:
            numberOfGuesses += 1
            print "Enter a number:"
            userInput = raw_input()
            while self.validate_input(userInput):
                print "Enter a number:"
                userInput = raw_input()

            inputNumber = [int(i) for i in str(userInput)]
            bulls_and_cows = self.compute_bulls_and_cows(secretNumber, inputNumber)
            if len(bulls_and_cows['Bulls']) == len(secretNumber):
                print "Correct, you've guessed the right number in {0} guesses!".format(numberOfGuesses)
                break
            else:
                print "%d bull%s, %d cow%s" % (len(bulls_and_cows['Bulls']), "s"[len(bulls_and_cows['Bulls']) == 1:],
                                               len(bulls_and_cows['Cows']), "s"[len(bulls_and_cows['Cows']) == 1:])
        self.evaluate_result(numberOfGuesses)

    def validate_input(self, userInput):
        """
        Validate input from user
        :param userInput: string, raw input from user
        :return: false - correct input, true - input with errors
        """
        if not userInput.isdigit():
            print "Input must include numbers only, please try again..."
            return 1
        elif len(userInput) < self.__numOfNumbersToGuess:
            print "Input number is too short, please try again..."
            return 1
        elif len(userInput) > self.__numOfNumbersToGuess:
            print "Input number is too long, please try again..."
            return 1
        return 0

    def evaluate_result(self, numOfGuesses):
        """
        Evaluate game results according the number of guesses
        :param numOfGuesses: number of player's guesses
        :return: void
        """
        if numOfGuesses < 5:
            print "Congratulations! That's amazing result!"
        elif numOfGuesses < 15:
            print "Well done! That's average result!"
        else:
            print "You can do better! That's not so good!"

    def generate_secretNumber(self, length):
        """
        Generate number of particular length
        :param length: length of number we want to generate
        :return: integer number
        """
        return random.sample(range(0, 9), length)

    def compute_bulls_and_cows(self, secretNumber, inputNumber):
        """
        Compute bulls and cows in player's input
        :param secretNumber: list, secret number, generated at the begining of the game
        :param inputNumber: list, actual number input by player
        :return: dictionary, contain list of bulls and list of cows
        """
        bulls = [i for i, j in zip(secretNumber, inputNumber) if i == j]
        cows = []
        for num in secretNumber:
            if num in inputNumber and num not in bulls:
                cows.append(num)
        bulls_and_cows = {'Bulls' : bulls, 'Cows' : cows}
        return bulls_and_cows

if __name__ == "__main__":
    bullsAndCows = BullsAndCows(4)
    bullsAndCows.run()
