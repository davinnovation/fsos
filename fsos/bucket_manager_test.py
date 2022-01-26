import unittest
import tempfile
import pathlib

from fsos import bucket_manager as bm


class BMTests(unittest.TestCase):
    def test_bucket(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            TEST_BUCKET_NAME = "test_bucket"
            bm.make_bucket(TEST_BUCKET_NAME, temp_dir)
            self.assertEqual(pathlib.Path(temp_dir, TEST_BUCKET_NAME).exists(), True)

            self.assertEqual(bm.bucket_exists(TEST_BUCKET_NAME, temp_dir), True)

            self.assertEqual(bm.bucket_list(temp_dir), [TEST_BUCKET_NAME])

            bm.remove_bucket(TEST_BUCKET_NAME, temp_dir)
            self.assertEqual(pathlib.Path(temp_dir, TEST_BUCKET_NAME).exists(), False)


if __name__ == "__main__":
    unittest.main()
