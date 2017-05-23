from unittest import TestCase


class TestBuild(TestCase):
    def test_build(self):
        try:
            from build import longest_substr
        except ImportError:
            self.assertFalse("no function found")

        self.assertRaises(TypeError, longest_substr, None)
        self.assertEqual(longest_substr('', k=3), 0)
        self.assertEqual(longest_substr('abcabcdefgghiij', k=3), 6)
        self.assertEqual(longest_substr('abcabcdefgghighij', k=3), 7)