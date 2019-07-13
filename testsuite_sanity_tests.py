import unittest
from lost_hat_login_page_tests import LostHatLoginPageTests

def sanity_test():
    test_suite = unittest.TestSuite()
    test_suite.addTest(LostHatLoginPageTests('test_login_to_my_account'))
    return test_suite

runner = unittest.TextTestRunner(verbosity=2)
runner.run(sanity_test())
