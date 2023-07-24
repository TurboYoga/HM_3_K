from HM.reposytory import Repository


def test_correct_data():
    all_transactions = Repository().read_json()
    assert isinstance(all_transactions, list)
    assert len(all_transactions) == 101


def test_get_filtered_data(data_for_tests):
    filtered_transactions = Repository().remove_empty_transactions(data_for_tests)
    assert {} not in filtered_transactions


def test_last_five_transactions(data_for_tests):
    last_five_transactions = Repository().get_last_five_transactions()
    assert len(last_five_transactions) == 5
    print(last_five_transactions)
    assert last_five_transactions[0]['description'] == 'Открытие вклада'
    assert last_five_transactions[1]['date'] == '2019-12-07T06:17:14.634890'
    assert last_five_transactions[2]['operationAmount']['amount'] == '17628.50'
    assert last_five_transactions[3]['from'] == 'Maestro 7810846596785568'
    assert last_five_transactions[4]['to'] == 'Счет 46765464282437878125'