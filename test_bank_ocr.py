import unittest

from bank_ocr import BankOCR


class TestBankOCR(unittest.TestCase):

    def setUp(self):
        self.ocr = BankOCR()

    def test_recognizes_zero(self):
        self.assertEqual('0 ERR', self.ocr.convert(
            " _ \n" +
            "| |\n" +
            "|_|\n" +
            "   ")
        )

    def test_recognizes_one(self):
        self.assertEqual('1 ERR', self.ocr.convert(
            "   \n" +
            "  |\n" +
            "  |\n" +
            "   "
        ))

    def test_converts_a_line_of_zeroes(self):
        self.assertEqual('000000000', self.ocr.convert(
            " _  _  _  _  _  _  _  _  _ \n" +
            "| || || || || || || || || |\n" +
            "|_||_||_||_||_||_||_||_||_|\n" +
            "                           "
        ))

    def test_can_parse_multiple_entries(self):
        self.assertEqual(
            "111111111 ERR\n" +
            "222222222 ERR\n" +
            "333333333 ERR\n" +
            "444444444 ERR\n" +
            "555555555 ERR\n" +
            "666666666 ERR\n" +
            "777777777 ERR\n" +
            "888888888 ERR\n" +
            "999999999 ERR", self.ocr.convert(
                "                           \n" +
                "  |  |  |  |  |  |  |  |  |\n" +
                "  |  |  |  |  |  |  |  |  |\n" +
                "                           \n" +
                " _  _  _  _  _  _  _  _  _ \n" +
                " _| _| _| _| _| _| _| _| _|\n" +
                "|_ |_ |_ |_ |_ |_ |_ |_ |_ \n" +
                "                           \n" +
                " _  _  _  _  _  _  _  _  _ \n" +
                " _| _| _| _| _| _| _| _| _|\n" +
                " _| _| _| _| _| _| _| _| _|\n" +
                "                           \n" +
                "                           \n" +
                "|_||_||_||_||_||_||_||_||_|\n" +
                "  |  |  |  |  |  |  |  |  |\n" +
                "                           \n" +
                " _  _  _  _  _  _  _  _  _ \n" +
                "|_ |_ |_ |_ |_ |_ |_ |_ |_ \n" +
                " _| _| _| _| _| _| _| _| _|\n" +
                "                           \n" +
                " _  _  _  _  _  _  _  _  _ \n" +
                "|_ |_ |_ |_ |_ |_ |_ |_ |_ \n" +
                "|_||_||_||_||_||_||_||_||_|\n" +
                "                           \n" +
                " _  _  _  _  _  _  _  _  _ \n" +
                "  |  |  |  |  |  |  |  |  |\n" +
                "  |  |  |  |  |  |  |  |  |\n" +
                "                           \n" +
                " _  _  _  _  _  _  _  _  _ \n" +
                "|_||_||_||_||_||_||_||_||_|\n" +
                "|_||_||_||_||_||_||_||_||_|\n" +
                "                           \n" +
                " _  _  _  _  _  _  _  _  _ \n" +
                "|_||_||_||_||_||_||_||_||_|\n" +
                " _| _| _| _| _| _| _| _| _|\n" +
                "                           "
        ))


if __name__ == '__main__':
    unittest.main()
