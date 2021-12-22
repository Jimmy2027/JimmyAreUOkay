import subprocess
import time
import unittest

import norby


def get_website_status(which_website: str):
    return subprocess.check_output(f"curl -I {which_website} | grep HTTP", shell=True).decode('utf-8').replace('\n', '')


class TestWebsites(unittest.TestCase):
    """
    Test if websites are available.
    """

    def test_hendrikklug(self):
        """
        Check if hendrikklug.xyz is up.
        """
        for _ in range(5):
            website_status = get_website_status('https://hendrikklug.xyz')

            if '200' in website_status:
                return

            # wait for 10 seconds before trying again
            time.sleep(10)

        norby.send_msg(whichbot='jimmy_watchdog',
                       message=f'hendrikklug.xyz is unavailable:\n {website_status}')
        assert False


if __name__ == '__main__':
    TestWebsites().test_hendrikklug()
