import unittest
from unittest.mock import patch
import expense_tracker

class TestExpenseTracker(unittest.TestCase):

    def setUp(self):
        expense_tracker.expenses.clear()

    def test_add_expense(self):
        with patch("builtins.input", side_effect=["Lunch", "Food", "150"]):
            expense_tracker.add_expense()

        self.assertEqual(len(expense_tracker.expenses), 1)
        self.assertEqual(
            expense_tracker.expenses[0]["description"], "Lunch"
        )
        self.assertEqual(expense_tracker.expenses[0]["amount"], 150.0)

    def test_reject_invalid_amount(self):
        with patch("builtins.input", side_effect=["Bus fare", "Transport", "abc"]):
            expense_tracker.add_expense()

        self.assertEqual(len(expense_tracker.expenses), 0)

    def test_delete_expense(self):
        expense_tracker.expenses.append({
            "description": "Lunch",
            "category": "Food",
            "amount": 150.0
        })

        with patch("builtins.input", return_value="1"):
            expense_tracker.delete_expense()

        self.assertEqual(len(expense_tracker.expenses), 0)

if __name__ == "__main__":
    unittest.main()