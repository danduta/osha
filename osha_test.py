import unittest
from osha.osha import hash


class TestOshaFunction(unittest.TestCase):

    message = bytes("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent finibus sollicitudin mauris ut pellentesque. Curabitur vel \
        augue quis magna placerat ultrices vel id leo. Fusce eget dignissim ex. Fusce non luctus felis, nec fringilla lectus. Quisque \
        accumsan tristique ipsum, at placerat lectus. Ut leo sem, sagittis id condimentum nec, venenatis vel mi. Donec vehicula mauris \
        mattis, suscipit eros ac, pellentesque odio. Donec euismod a mauris maximus fermentum. Sed iaculis fermentum arcu, sit amet \
        lobortis est molestie quis. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.", 'utf-8')

    def setUp(self):
        pass

    def test_simple_consistency_1(self):
        h1 = hash(self.message, 8)
        h2 = hash(self.message, 8)
        from time import time_ns, time

        self.assertEqual(h1, h2)
        self.assertLessEqual(int(h1, 16).bit_length(), 8)
        self.assertLessEqual(int(h2, 16).bit_length(), 8)

    def test_simple_consistency_2(self):
        h1 = hash(self.message, 16)
        h2 = hash(self.message, 16)
        from time import time_ns, time

        self.assertEqual(h1, h2)
        self.assertLessEqual(int(h1, 16).bit_length(), 16)
        self.assertLessEqual(int(h2, 16).bit_length(), 16)

    def test_simple_consistency_3(self):
        h1 = hash(self.message, 256)
        h2 = hash(self.message, 256)
        from time import time_ns, time

        self.assertEqual(h1, h2)
        self.assertLessEqual(int(h1, 16).bit_length(), 256)
        self.assertLessEqual(int(h2, 16).bit_length(), 256)

    def test_simple_consistency_4(self):
        h1 = hash(self.message, 512)
        h2 = hash(self.message, 512)
        from time import time_ns, time

        self.assertEqual(h1, h2)
        self.assertLessEqual(int(h1, 16).bit_length(), 512)
        self.assertLessEqual(int(h2, 16).bit_length(), 512)


if __name__ == '__main__':
    unittest.main()
