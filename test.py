import unittest
from main import validate_card_number, find_card_numbers_in_text, find_card_numbers_in_file

class TestCardValidation(unittest.TestCase):
    def test_validate_card_number(self):
        self.assertTrue(validate_card_number("1234-5678-9012-3456"))
        self.assertTrue(validate_card_number("1234 5678 9012 3456"))
        self.assertFalse(validate_card_number("1234-5678-9012-345a"))

    def test_find_card_numbers_in_text(self):
        text = "My cards are 1234-5678-9012-3456 and 1234 5678 9012 3456."
        expected = ["1234-5678-9012-3456", "1234 5678 9012 3456"]
        self.assertEqual(find_card_numbers_in_text(text), expected)

    def test_find_card_numbers_in_file(self):
        with open('test_file.txt', 'w') as file:
            file.write("Card: 1234-5678-9012-3456")
        self.assertEqual(find_card_numbers_in_file('test_file.txt'), ["1234-5678-9012-3456"])

        # # Проверка с пустым файлом
        # with open('empty_file.txt', 'w') as file:
        #     file.write("")
        # self.assertEqual(find_card_numbers_in_file('empty_file.txt'), [])

        # # Проверка с несуществующим файлом
        # self.assertEqual(find_card_numbers_in_file('non_existent_file.txt'), [])

if __name__ == '__main__':
    unittest.main()
