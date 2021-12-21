import subprocess
import unittest
from pathlib import Path

import norby
from modun.file_io import dict2json, json2dict


def get_ip():
    command = "ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1'"
    ip_address = subprocess.check_output(command, shell=True).decode('utf-8').replace('\n', '')

    return ip_address


class TestIpAddr(unittest.TestCase):
    """
    Test if IP Address has changed. If it has, send a message.
    """

    def test_ip(self):
        """
        Verify if current ip address is the same as in ip_addr file.
        If it does not exist, create it.
        """
        current_ip = {'ip_addr': get_ip()}

        ip_addr_fn = Path(__file__).parent / 'data/ip_addr.json'

        if not ip_addr_fn.exists():
            dict2json(out_path=ip_addr_fn, d=current_ip)
            return
        else:
            old_ip = json2dict(ip_addr_fn)['ip_addr']
            if old_ip != current_ip['ip_addr']:
                norby.send_msg(whichbot='jimmy_watchdog',
                               message=f'IP Address on Jimmy has changed from {old_ip} to: \n {current_ip["ip_addr"]}')

                assert False


if __name__ == '__main__':
    TestIpAddr().test_ip()
