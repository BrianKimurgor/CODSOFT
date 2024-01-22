import unittest
from unittest.mock import patch
import tkinter as tk
from tkinter import ttk
from calc import CalculatorApp

class TestCalculatorApp(unittest.TestCase):
    @patch('calc.ttk.Button')
    @patch('calc.ttk.Entry')

    def setUp(self, mock_entry, mock_button):
        self.master = tk.Tk()
        self.app = CalculatorApp(self.master)

    def test_button_click_digit(self):
        # Simulate clicking a digit button
        self.app.button_click('1')
        self.assertEqual(self.app.result_var.get(), '1')

        self.app.button_click('2')
        self.assertEqual(self.app.result_var.get(), '2')

        self.app.button_click('3')
        self.assertEqual(self.app.result_var.get(), '3')

        self.app.button_click('4')
        self.assertEqual(self.app.result_var.get(), '4')

        self.app.button_click('5')
        self.assertEqual(self.app.result_var.get(), '5')

        self.app.button_click('6')
        self.assertEqual(self.app.result_var.get(), '6')

        self.app.button_click('7')
        self.assertEqual(self.app.result_var.get(), '7')

        self.app.button_click('8')
        self.assertEqual(self.app.result_var.get(), '8')

        self.app.button_click('9')
        self.assertEqual(self.app.result_var.get(), '9')


    def test_button_click_operator(self):
        # Simulate clicking an operator button
        self.app.button_click('+')
        self.assertEqual(self.app.result_var.get(), '+')

        self.app.button_click('-')
        self.assertEqual(self.app.result_var.get(), '-')

        self.app.button_click('*')
        self.assertEqual(self.app.result_var.get(), '*')

        self.app.button_click('/')
        self.assertEqual(self.app.result_var.get(), '/')

    def test_button_click_clear(self):
        # Simulate clicking the clear button
        self.app.button_click('C')
        # Check that the result variable was cleared
        self.assertEqual(self.app.result_var.get(), '')

    def test_button_click_equals(self):
        # Simulate clicking the equals button
        self.app.button_click('=')
        # Check that the result variable was updated correctly
        # This will depend on what the previous input was
        # For simplicity, let's assume the previous input was '2+2'
        self.assertEqual(self.app.result_var.get(), 'Error')

if __name__ == '__main__':
    unittest.main()
