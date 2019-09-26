import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_mysql_port(host):
    mysql = host.addr("127.0.0.1")
    mysql.port(25).is_reachable


def test_postfix_file(host):
    f = host.file('/etc/postfix/main.cf')
    assert f.exists
    assert f.is_file
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o644


def test_postfix_is_running(host):
    service = host.service('postfix')
    assert service.is_running
