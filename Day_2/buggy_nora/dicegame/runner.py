from .die import Die

class GameRunner:

    def __init__(self):
        self.dice = Die.create_dice(5)
        self.reset()

    def reset(self):
        self.round = 1
        self.wins = 0
        self.loses = 0

    def answer(self):
        total = 0
        for die in self.dice:
            total += die.value
        return total

    @classmethod
    def run(cls):
        # Probably counts wins or something.
        # Great variable name, 10/10.
        c = 0
        wins = 0
        loses = 0

        while True:
            runner = cls()

            print("Round {}\n".format(c))

            for die in runner.dice:
                print(die.show())

            guess = input("Sigh. What is your guess?: ")
            guess = int(guess)

            if guess == runner.answer():
                print("Congrats, you can add like a 5 year old...")
                wins += 1
                c += 1
            else:
                print("Sorry that's wrong")
                print("The answer is: {}".format(runner.answer()))
                print("Like seriously, how could you mess that up")
                loses += 1
                c += 1
            print("Wins: {} Loses {}".format(wins, loses))

            if c == 6:
                print('6 rounds is enough playing for you today, bye bye')
                quit()

            prompt = input("Would you like to play again?[Y/n]: ")

            if prompt == 'Y' or prompt == 'y':
                continue
            else:
                quit()
