"""To Unit test then Integration Test for Text-Translate Application"""
import unittest
from unittest import TestCase
import doctest
import main

# to test:
# python test.py
# coverage:
# coverage run --omit=env/* test.py
# for report:
# coverage report -m
# coverage html


######################################################
def load_tests(loader, tests, ignore):
    """Also run our doctests and file-based doctests."""

    tests.addTests(doctest.DocTestSuite(main))
    # tests.addTests(doctest.DocFileSuite("tests.txt"))
    return tests



if __name__ == '__main__':
    unittest.main()
    # from main import app
