import unittest
import run_2
import run_1

def frozen_test(func):
    def wrapper(self):
        if self.is_frozen:
            print('Тесты в этом кейсе заморожены.')
            self.skipTest('Тесты заморожены')
        return func(self)
    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @frozen_test
    def test_walk(self):
        runner = run_1.Runner('Petr')
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @frozen_test
    def test_run(self):
        is_frozen = False
        runner = run_1.Runner('Kolya')
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @frozen_test
    def test_challenge(self):
        is_frozen = False
        runner1 = run_1.Runner("Vasya")
        runner2 = run_1.Runner("Dima")
        for i in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == '__main__':
    unittest.main()

class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runners = {
            'Usain': run_2.Runner('Usain', speed=10),
            'Andrey': run_2.Runner('Andrey', speed=9),
            'Nick': run_2.Runner('Nick', speed=3)
        }

    @classmethod
    def tearDownClass(cls):
        for place, runner in sorted(cls.all_results.items()):
            print(f'Место {place}: {runner.name}')

    @frozen_test
    def test_first_tournament(self):
        is_frozen = True
        tournament = run_2.Tournament(1540, self.runners['Usain'], self.runners['Andrey'], self.runners['Nick'])
        results = tournament.start()
        self.all_results.update(results)
        last_runner = results[max(results.keys())]  # Самый последний бегун
        self.assertTrue(last_runner.name == 'Nick')

    @frozen_test
    def test_second_tournament(self):
        is_frozen = True
        tournament = run_2.Tournament(90, self.runners['Andrey'], self.runners['Nick'])
        results = tournament.start()
        self.all_results.update(results)
        last_runner = results[max(results.keys())]  # Самый последний бегун
        self.assertTrue(last_runner.name == 'Nick')

    @frozen_test
    def test_third_tournament(self):
        is_frozen = True
        tournament = run_2.Tournament(90, self.runners['Usain'], self.runners['Andrey'], self.runners['Nick'])
        results = tournament.start()
        self.all_results.update(results)
        last_runner = results[max(results.keys())]  # Самый последний бегун
        self.assertTrue(last_runner.name == 'Nick')



if __name__ == '__main__':
    unittest.main()