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
        print(service_status)

        # if 'running' in service_status:
        #     return
        # else:
        #     norby.send_msg(whichbot='jimmy_watchdog',
        #                    message=f'DDclient service not running:\n {service_status}')
        #
        #     assert False


if __name__ == '__main__':
    TestService().test_ddclient()
