import subprocess
import unittest

import norby


def get_service_status(which_client: str):
    return subprocess.check_output(f"rc-status | grep {which_client}", shell=True).decode('utf-8').replace('\n', '')


class TestService(unittest.TestCase):
    """
    Test if services are running by parsing "rc-status".
    """

    def test_ddclient(self):
        """
        Verify if ddclient is running.
        """
        service_status = get_service_status('ddclient')

        if 'started' in service_status:
            return

        norby.send_msg(whichbot='jimmy_watchdog',
                       message=f'ddclient service not running:\n {service_status}')
        assert False

    def test_mongodb(self):
        """
        Verify if mongodb is running.
        """
        service_status = get_service_status('mongodb')

        if 'started' in service_status:
            return

        norby.send_msg(whichbot='jimmy_watchdog',
                       message=f'mongodb service not running:\n {service_status}')
        assert False

    def test_apache2(self):
        """
        Verify if apache2 is running.
        """
        service_status = get_service_status('apache2')

        if 'started' in service_status:
            return

        norby.send_msg(whichbot='jimmy_watchdog',
                       message=f'apache2 service not running:\n {service_status}')
        assert False

    def test_haproxy(self):
        """
        Verify if apache2 is running.
        """
        service_status = get_service_status('haproxy')

        if 'started' in service_status:
            return

        norby.send_msg(whichbot='jimmy_watchdog',
                       message=f'haproxy service not running:\n {service_status}')
        assert False


if __name__ == '__main__':
    TestService().test_ddclient()
