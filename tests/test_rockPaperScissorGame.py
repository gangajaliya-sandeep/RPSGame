import unittest
import xmlrunner
from game.rockPaperScissorGame import playerChoice


ROCK = 0
PAPER = 1
SCISSOR = 2
FAILURE = 'Incorrect input'
SUCCESS = 'Correct input'


class RockPaperScissorGameTest(unittest.TestCase):
    def setUp(self):
        self.playerChoice = playerChoice()

    def user_choice_rock_init(self):
        value = self.playerChoice.userChoice
        self.assertEqual(value, 0, FAILURE)

    def user_choice_paper_init(self):
        value = self.playerChoice.userChoice
        self.assertEqual(value, 1, SUCCESS)

    def user_choice_scissor_init(self):
        value = self.playerChoice.userChoice
        self.assertEqual(value, 2, SUCCESS)

    def user_choice_exit_init(self):
        value = self.playerChoice.userChoice
        self.assertEqual(value, 1, SUCCESS)

    def user_choice_failure1_init(self):
        value = self.playerChoice.userChoice
        self.assertEqual(value, -1, FAILURE)

    def user_choice_failure2_init(self):
        value = self.playerChoice.userChoice
        self.assertEqual(value, 4, FAILURE)

    def user_choice_failure3_init(self):
        value = self.playerChoice.userChoice
        self.assertEqual(value, 6, FAILURE)

    def user_check_result_init(self):
        value = self.playerChoice.checkResult
        self.assertEqual(value, -1, 4, FAILURE)


if __name__ == '__main__':

    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
        failfast=False,
        buffer=False,
        catchbreak=False)
