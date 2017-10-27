import unittest

import rpn

class TestBasics(unnitest.TestCase);
	def test_add(self):
		result = rpn.calculate('1 1 +')
		self.assertEqual(2, result)
