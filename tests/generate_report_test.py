#from unittest import TestCase
import unittest
from generate_report import Cowrie

class TestCowrie(unittest.TestCase):
  def setUp(self):
    self.cowrie = Cowrie()

  def test_first_char(self):
    self.assertEqual(self.cowrie.first_char(), 'c')

  @unittest.skip("I should create mock and reseponse from Mock")
  def test_file_name(self):
    pass
    # Mock 使用してdatetime.now()の挙動を同じにする。
    self.assertEqual(self.cowrie.file_name(), 'something write.')

