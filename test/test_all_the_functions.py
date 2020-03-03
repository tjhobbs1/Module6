import unittest
import unittest.mock as mock

from source_files.functions_all_the_functions import average, average_list


class MyTestCase(unittest.TestCase):
    #Test Case
    def test_average_no_args(self):
        with mock.patch('builtins.input', side_effect=[12, 13]):
            assert average() == 12.5

    def test_average_list(self):
        s_list = [12, 13]
        self.assertEqual(12.5, average_list(s_list))


if __name__ == '__main__':
    unittest.main()
