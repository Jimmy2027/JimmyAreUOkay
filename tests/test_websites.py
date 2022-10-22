import subprocess
import time
import unittest

import norby


def get_website_status(which_website: str):
    return subprocess.check_output(f"curl -I {which_website} | grep HTTP", shell=True).decode('utf-8').replace('\n', '')


class TestWebsites(unittest.TestCase):
    """
    Test if websites are available.
    Check if curl to a website return http 200 response:
    HTTP 200 OK success status response code indicates that the request has succeeded
    """

    def website_verify(self, website_url: str):
        website_status = get_website_status(website_url)

        if '200' in website_status:
            return

        # wait for 10 seconds before trying again
        time.sleep(10)

        norby.send_msg(whichbot='jimmy_watchdog',
                       message=f'{website_url} is unavailable:\n {website_status}')
        assert False

    def test_hendrikklug(self):
        """
        Check if hendrikklug.xyz is up.
        """
        self.website_verify('https://hendrikklug.xyz')

    def test_nextcloud(self):
        """
        Check if nextcloud is up.
        """
        self.website_verify('http://jimmy123.hopto.org:2095/nextcloud')

    def test_personal_photoprism(self):
        """
        Check if personal_photprism is up.
        """
        self.website_verify('http://jimmy123.hopto.org:2343')

    def test_photoprism(self):
        """
        Check if photprism is up.
        """
        self.website_verify('http://jimmy123.hopto.org:2342')

    def test_dokuwiki(self):
        """
        Check if docuwiki is up.
        """
        self.website_verify('http://jimmy123.hopto.org:2095/dokuwiki/')


if __name__ == '__main__':
    TestWebsites().test_hendrikklug()
