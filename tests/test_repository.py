from pathlib import Path

import pytest

from HM.reposytory import Repository
from settings import FIXTURE_PATH


 def test_correct_data():
     all_transactions = Repository().get_all_transactions()
     assert isinstance(all_transactions, list)
     assert len(all_transactions) == 101


def test_open_file():
    repository = Repository()
    repository.data_path = Path.joinpath(FIXTURE_PATH, 'transaction.json')
    with pytest.raises(SystemExit):
        repository.read_json()


 def test_get_executed_transactions(data_for_tests):
     executed_transactions = Repository().get_executed_transactions(data_for_tests)
     assert len(executed_transactions) == 6
     assert executed_transactions[1]['state'] == 'EXECUTED'
     assert executed_transactions[2]['date'] == '2019-09-11T17:30:34.445824'
     assert executed_transactions[3]['operationAmount']['amount'] == '45849.53'
     assert executed_transactions[4]['from'] == 'МИР 8201420097886664'


def test_last_five_transactions(data_for_tests):
    last_five_transactions = Repository().get_last_five_transactions()
    assert len(last_five_transactions) == 5
    assert last_five_transactions[0]['description'] == 'Открытие вклада'
    assert last_five_transactions[1]['date'] == '2019-12-07T06:17:14.634890'
    assert last_five_transactions[2]['operationAmount']['amount'] == '30153.72'
    assert last_five_transactions[3]['from'] == 'Счет 38611439522855669794'
    assert last_five_transactions[4]['to'] == 'Счет 77613226829885488381'
