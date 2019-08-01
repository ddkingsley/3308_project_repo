#!/usr/bin/env python3
# horoscope feature testing

import unittest
import horoscope


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

    """ test that the personal traits generator returns a string """
    def test_horoscopeTraits(self):

        traitsLine = horoscope.horoscopeTraits(self)
        assert isinstance(traitsLine, str)
        self.assertTrue(len(traitsLine) > 0)
        
        
    """ test that the fortunes generator returns a string """
    def test_horoscopeFortuneGenerator(self):
        
        fortune = horoscope.horoscopeFortuneGenerator(self)
        assert isinstance(fortune, str)
        self.assertTrue(len(fortune) > 0)
        
        # check that such fortune exists in fortune database
        
        found = False
        txtfile = open('loveFortunes.txt')
        for line in txtfile:
            if fortune in line:
                found = True
                break
        
        txtfile = open('wealthFortunes.txt')
        for line in txtfile:
            if fortune in line:
                found = True
                break
                
        txtfile = open('healthFortunes.txt')
        for line in txtfile:
            if fortune in line:
                found = True
                break
        
        self.assertTrue(found)

if __name__ == '__main__':
    unittest.main()
