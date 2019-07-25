#!/usr/bin/env python3
# fortune cookie app testing

import unittest
import cookie

class CookieTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_getAFortune(self):
        fortune1 = cookie.getAFortune(True)
        fortune2 = cookie.getAFortune(True)
        self.assertTrue(len(fortune1) > 0)
        self.assertTrue(len(fortune2) > 0)
        self.assertTrue(type(fortune1) is str)
        self.assertTrue(type(fortune2) is str)

    def test_getLuckyNumbers(self):
        nums = cookie.getLuckyNumbers()
        self.assertTrue(len(nums) > 11 and len(nums) < 19)
        numlist = nums.split()
        self.assertEqual(len(numlist), 6)
        for i in range(len(numlist) - 1):
            self.assertTrue(int(numlist[i]) < 70)
        self.assertTrue(int(numlist[5]) < 27)

if __name__ == '__main__':
    unittest.main()
