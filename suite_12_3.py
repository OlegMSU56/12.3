import unittest

import test_12_3

kekST = unittest.TestSuite()
kekST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.RunnerTest))
kekST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(kekST)
