import unittest
import urllib.request

import norby


def get_website_status(which_website: str) -> int:
    return urllib.request.urlopen(which_website).getcode()


class TestWebsites(unittest.TestCase):
    """
    Test if websites are available.
    Check if curl to a website returns http 200 response:

    """

    def website_verify(self, website_url: str):
        http_return_code = get_website_status(website_url)
        if http_return_code in {
            200,  # HTTP 200 OK success status response code indicates that the request has succeeded
            302,  # performing URL redirection
            301,  # 301 Moved Permanently is used for permanent redirecting
        }:
            return

        norby.send_msg(whichbot='jimmy_watchdog',
                       message=f'{website_url} is unavailable:\n {http_return_code}')
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
    unittest.main()
