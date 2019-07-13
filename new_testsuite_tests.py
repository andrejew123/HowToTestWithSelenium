import unittest
from lost_hat_exercise_smoke_test import SmokeTestForSearrchBox
from lost_hat_front_page_tests import LostHatFrontPAgeTests

def sanity_test():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(SmokeTestForSearrchBox))
    return test_suite

def sanity_one_test():
    test_suite = unittest.TestSuite()
    test_suite.addTest(LostHatFrontPAgeTests('test_pln_in_price'))
    return test_suite

runner2 = unittest.TextTestRunner(verbosity=2)
runner2.run(sanity_one_test())
