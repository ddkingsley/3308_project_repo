#!/usr/bin/python
import sqlite3
import unittest
import os


class testDB(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        conn = sqlite3.connect('test')
        c = conn.cursor()
        f = open('app/schema.sql')
        c.executescript(f.read().decode('utf8'))
        c.execute("INSERT INTO user VALUES(1, 'greg', 'aquarius', 'gregiscool')")
        c.execute("INSERT INTO user VALUES(2, 'daniel', 'pisces', 'danieliscool')")
        c.execute("INSERT INTO user VALUES(3, 'florencia', 'taurus', 'florenciaiscool')")
        c.execute("INSERT INTO user VALUES(4, 'kristin', 'gemini', 'kristiniscool')")

        c.execute("INSERT INTO fortune VALUES(1, 1, 'youre going to be rich')")
        c.execute("INSERT INTO fortune VALUES(2, 2, 'youre going to be happy')")
        c.execute("INSERT INTO fortune VALUES(3, 3, 'youre going to be famous')")
        c.execute("INSERT INTO fortune VALUES(4, 4, 'youre going to be awesome')")

        conn.commit()
        conn.close()


    def tearDown(self):
        os.remove('test')

    def test_userInsert(self):
        conn = sqlite3.connect('test')
        c = conn.cursor()

        c.execute('SELECT * FROM user')
        rows = c.fetchall()

        self.assertEqual(rows[0], (1, 'greg', 'aquarius', 'gregiscool'), 'Row 1 wrong in user')
        self.assertEqual(rows[1], (2, 'daniel', 'pisces', 'danieliscool'), 'Row 2 wrong in user')	
        self.assertEqual(rows[2], (3, 'florencia', 'taurus', 'florenciaiscool'), 'Row 3 wrong in user')	
        self.assertEqual(rows[3], (4, 'kristin', 'gemini', 'kristiniscool'), 'Row 4 wrong in user')	

        conn.close()


    def test_fortuneInsert(self):
        conn = sqlite3.connect('test')
        c = conn.cursor()

        c.execute('SELECT * FROM fortune')
        rows = c.fetchall()

        self.assertEqual(rows[0], (1, 1, 'youre going to be rich'), 'Row 1 wrong in fortune')
        self.assertEqual(rows[1], (2, 2, 'youre going to be happy'), 'Row 2 wrong in fortune')	
        self.assertEqual(rows[2], (3, 3, 'youre going to be famous'), 'Row 3 wrong in fortune')	
        self.assertEqual(rows[3], (4, 4, 'youre going to be awesome'), 'Row 4 wrong in fortune')

        conn.close()

    
    def test_foreignKey(self):
        conn = sqlite3.connect('test')
        c = conn.cursor() 

        with self.assertRaises(sqlite3.IntegrityError):
            c.execute("INSERT INTO fortune VALUES(1, 20, 'youre going to be rich')")
            c.execute("INSERT INTO fortune VALUES(1, 'lala', 'youre going to be rich')")
        
        conn.close()


    def test_unique(self):
        conn = sqlite3.connect('test')
        c = conn.cursor() 

        with self.assertRaises(sqlite3.IntegrityError):
            c.execute("INSERT INTO user VALUES(5, 'greg', 'aquarius', 'webecool')")
            c.execute("INSERT INTO user VALUES(6, 'kristin', 'gemini', 'webecool')")
        
        conn.close()
    

if __name__ == '__main__':
    unittest.main()

