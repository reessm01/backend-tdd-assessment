#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo
import subprocess

# Your test case class goes here

class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual(echo.to_upper("foo"), "FOO")

    def test_lower(self):
        self.assertEqual(echo.to_lower("FOO"), "foo")

    def test_title(self):
        self.assertEqual(echo.to_titlecase("whats up dude"), "Whats Up Dude")

    def test_all_options(self):
        process = subprocess.Popen(
            ["python", "./echo.py", "whats up dude", "-utl"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()

        self.assertEqual(stdout, "Whats Up Dude\n")

    def test_no_options(self):
        process = subprocess.Popen(
            ["python", "./echo.py", "whats up dude"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()

        self.assertEqual(stdout, "whats up dude\n")

    def test_help(self):
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()

        self.assertEquals(stdout, usage)

if __name__ == '__main__':
    unittest.main()
