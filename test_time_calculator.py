"""
test_time_calculator.py
"""

import unittest
from time_calculator import add_time


class UnitTests(unittest.TestCase):
    maxDiff = None

    def test_three_ten_pm(self):
        actual = add_time("3:00 PM", "3:10")
        expected = "6:10 PM"
        self.assertEqual(actual, expected)

    def test_eleven_thirty_am_monday(self):
        actual = add_time("11:30 AM", "2:32", "Monday")
        expected = "2:02 PM, Monday"
        self.assertEqual(actual, expected)

    def test_eleven_forty_three_am(self):
        actual = add_time("11:43 AM", "00:20")
        expected = "12:03 PM"
        self.assertEqual(actual, expected)

    def test_ten_ten_pm_next_day(self):
        actual = add_time("10:10 PM", "3:30")
        expected = "1:40 AM (next day)"
        self.assertEqual(actual, expected)

    def test_eleven_forty_three_pm_two_days_later(self):
        actual = add_time("11:43 PM", "24:20", "tueSday")
        expected = "12:03 AM, Thursday (2 days later)"
        self.assertEqual(actual, expected)

    def test_six_thirty_pm_nine_days_later(self):
        actual = add_time("6:30 PM", "205:12")
        expected = "7:42 AM (9 days later)"
        self.assertEqual(actual, expected)

    def test_three_thirty_pm(self):
        actual = add_time("3:30 PM", "2:12")
        expected = "5:42 PM"
        self.assertEqual(actual, expected)

    def test_eleven_fifty_five_am(self):
        actual = add_time("11:55 AM", "3:12")
        expected = "3:07 PM"
        self.assertEqual(actual, expected)

    def test_nine_fifteen_pm_next_day(self):
        actual = add_time("9:15 PM", "5:30")
        expected = "2:45 AM (next day)"
        self.assertEqual(actual, expected)

    def test_eleven_forty_am(self):
        actual = add_time("11:40 AM", "0:25")
        expected = "12:05 PM"
        self.assertEqual(actual, expected)

    def test_two_fifty_nine_am_next_day(self):
        actual = add_time("2:59 AM", "24:00")
        expected = "2:59 AM (next day)"
        self.assertEqual(actual, expected)

    def test_eleven_fifty_nine_pm_two_days_later(self):
        actual = add_time("11:59 PM", "24:05")
        expected = "12:04 AM (2 days later)"
        self.assertEqual(actual, expected)

    def test_eight_sixteen_pm_twenty_days_later(self):
        actual = add_time("8:16 PM", "466:02")
        expected = "6:18 AM (20 days later)"
        self.assertEqual(actual, expected)

    def test_five_oh_one_am(self):
        actual = add_time("5:01 AM", "0:00")
        expected = "5:01 AM"
        self.assertEqual(actual, expected)

    def test_three_thirty_pm_monday(self):
        actual = add_time("3:30 PM", "2:12", "Monday")
        expected = "5:42 PM, Monday"
        self.assertEqual(actual, expected)

    def test_two_fifty_nine_am_sunday_next_day(self):
        actual = add_time("2:59 AM", "24:00", "saturDay")
        expected = "2:59 AM, Sunday (next day)"
        self.assertEqual(actual, expected)

    def test_eleven_fifty_nine_pm_friday_two_days_later(self):
        actual = add_time("11:59 PM", "24:05", "Wednesday")
        expected = "12:04 AM, Friday (2 days later)"
        self.assertEqual(actual, expected)

    def test_eight_sixteen_pm_monday_twenty_days_later(self):
        actual = add_time("8:16 PM", "466:02", "tuesday")
        expected = "6:18 AM, Monday (20 days later)"
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
