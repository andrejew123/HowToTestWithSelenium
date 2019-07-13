import unittest
from lost_hat_smoke_tests import LostHatSmokeTests
from lost_hat_front_page_tests import LostHatFrontPAgeTests
from lost_hat_login_page_tests import LostHatLoginPageTests
from lost_hat_product_page_tests import LostHatProductPage

def smoke_multi_test():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(LostHatSmokeTests))
    test_suite.addTest(unittest.makeSuite(LostHatLoginPageTests))
    test_suite.addTest(unittest.makeSuite(LostHatProductPage))
    test_suite.addTest(unittest.makeSuite(LostHatFrontPAgeTests))
    return test_suite

if  __name__ == '__main__':
        runner = unittest.TextTestRunner(verbosity=2)
        runner.run(smoke_multi_test())
