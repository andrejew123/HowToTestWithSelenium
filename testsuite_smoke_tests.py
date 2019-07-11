import unittest
from lost_hat_smoke_tests import LostHatSmokeTests  #import klasy z modulu
from unittest.loader import makeSuite

def smoke_suite():
    test_suite = unittest.TestSuite()
    #adding test classes
    test_suite.addTest(makeSuite(LostHatSmokeTests))
    return test_suite
runner = unittest.TextTestRunner(verbosity=2)
runner.run(smoke_suite())