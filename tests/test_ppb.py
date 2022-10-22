import unittest
from pathlib import Path

import norby
import npb


class TestNPB(unittest.TestCase):

    def test_upload(self):
        """
        Test if a file can be uploaded.
        """
        try:
            test_file = Path(__file__).parent / 'data/test_file.txt'
            npb.upload(file_path=test_file, lifetime=1)
        except Exception as e:
            norby.send_msg(whichbot='jimmy_watchdog', message=f'Test test_upload failed with: \n {e}')
            assert False, e


if __name__ == '__main__':
    unittest.main()
