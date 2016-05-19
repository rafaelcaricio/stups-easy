from collections import namedtuple
from unittest.mock import MagicMock

import easy.run
import pytest
from easy.run import main


@pytest.fixture()
def popen(monkeypatch):
    fake_popen = MagicMock()
    fake_popen.return_value = fake_popen
    fake_popen.communicate = MagicMock(name='Popen.communicate',
                                       return_value=('', ''))
    monkeypatch.setattr(easy.run, 'Popen', fake_popen)
    return fake_popen


class UseCase(namedtuple('UseCase', ['popen', 'monkeypatch'])):
    def result_of_running(self, cmd: str):
        '''
        Returns the command that would be actually executed in the subprocess.
        '''
        self.monkeypatch.setattr(easy.run.sys, 'argv', cmd.split(' '))
        main()
        return ' '.join(self.popen.call_args[0][0])


def test_login_with_mai(popen, monkeypatch):
    use_case = UseCase(popen, monkeypatch)
    assert use_case.result_of_running('easy login') == 'mai'


def test_deploy_with_senza(popen, monkeypatch):
    use_case = UseCase(popen, monkeypatch)
    assert use_case.result_of_running(
        'easy deploy create lizzy.yaml 1') == 'senza create lizzy.yaml 1'


def test_artifacts_with_pierone(popen, monkeypatch):
    use_case = UseCase(popen, monkeypatch)
    assert use_case.result_of_running(
        'easy artifacts list bus') == 'pierone artifacts bus'


def test_ssh_with_piu(popen, monkeypatch):
    use_case = UseCase(popen, monkeypatch)
    assert use_case.result_of_running(
        'easy ssh request-access 127.0.0.1') == 'piu request-access 127.0.0.1'


def test_compliance_with_fullstop(popen, monkeypatch):
    use_case = UseCase(popen, monkeypatch)
    assert use_case.result_of_running(
        'easy compliance list-violations') == 'fullstop list-violations'


def test_versions_with_kio(popen, monkeypatch):
    use_case = UseCase(popen, monkeypatch)
    assert use_case.result_of_running(
        'easy versions list hello-bus') == 'kio versions list hello-bus'
