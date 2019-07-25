#!/usr/bin/env python3
# horoscope feature testing

import unittest
import horoscopeGenerator


class TextprocTestCase(unittest.TestCase):

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

    """ tests for the personal traits generator """
    def test_horoscopeTraits(self):

        traitsLine = horoscope.horoscopeTraits()
        self.assertTrue(type(traitsLine) is str)
        self.assertTrue(len(traitsLine) > 0)
        
        
    """ tests for the fortune generator """
    def test_horoscopeFortuneGenerator(self):

        fortune = horoscope.horoscopeFortuneGenerator()
        self.assertTrue(type(fortune) is str)
        self.assertTrue(len(fortune) > 0)
        
        # check that such fortune exists in fortune database
        
        found = False
        txtfile = file('loveFortunes.txt')
        for line in txtfile:
            if fortune in line:
                found = True
                break
        
        txtfile = file('wealthFortunes.txt')
        for line in txtfile:
            if fortune in line:
                found = True
                break
                
        txtfile = file('healthFortunes.txt')
        for line in txtfile:
            if fortune in line:
                found = True
                break
        
        self.assertTrue(found)

if __name__ == '__main__':
    unittest.main()
