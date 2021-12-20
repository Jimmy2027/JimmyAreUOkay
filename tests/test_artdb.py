import unittest
from pathlib import Path

import norby
from modun.file_io import json2dict
from pymongo import MongoClient


class TestArtdb(unittest.TestCase):
    def test_artdb(self):
        """
        Test if a connection to the db can be established.
        """
        try:
            db_url = json2dict(Path('~/.config/artdb.json').expanduser())['mongodb_URI']
            client = MongoClient(db_url)
            db = client.artdb
            collection = db.ReverseDixit
            print(list(collection.find({})))
        except Exception as e:
            norby.send_msg(whichbot='jimmy_watchdog', message=f'Test test_ppb_db failed with: \n {e}')
            assert False, e


if __name__ == '__main__':
    unittest.main()
