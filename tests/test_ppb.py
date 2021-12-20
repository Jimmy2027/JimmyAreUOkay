import unittest
from pathlib import Path

import norby
import ppb
from ppb.MongoDB import MongoDatabase
from ppb.utils import get_config


class TestPPB(unittest.TestCase):
    def test_ppb_db(self):
        """
        Test if a connection to the db can be established.
        """
        try:
            config = get_config()
            ppb_config = config['ppb_config']
            mongodb = MongoDatabase(mongodb_uri=ppb_config['PPB_TARGET_HOST_DB_URI'])
            print(list(mongodb.collection.find({})))
        except Exception as e:
            norby.send_msg(whichbot='jimmy_watchdog', message=f'Test test_ppb_db failed with: \n {e}')
            assert False, e

    def test_upload(self):
        """
        Test if a file can be uploaded.
        """
        try:
            test_file = Path(__file__).parent / 'data/test_file.txt'
            ppb.upload(file_path=test_file, lifetime=1)
        except Exception as e:
            norby.send_msg(whichbot='jimmy_watchdog', message=f'Test test_upload failed with: \n {e}')
            assert False, e


if __name__ == '__main__':
    unittest.main()
