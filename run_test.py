import unittest

if __name__ == "__main__":
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover("./test", pattern="test_*.py")
    unittest.TextTestRunner().run(test_suite)
