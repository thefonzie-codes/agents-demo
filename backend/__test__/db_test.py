import unittest
from db import generate_db
import sqlite3

class DBTest(unittest.TestCase):
    
    def test_db(self):
        generate_db()
        self.assertEqual()