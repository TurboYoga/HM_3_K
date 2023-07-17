from HM.transaction import Transaction


def test_executed_transaction(data_for_tests):
    transactions = []
    for transaction in data_for_tests:
        transactions.append(Transaction(transaction['id'], transaction['date'], transaction['description'],
                                        transaction['operationAmount'], transaction['to'], transaction.get('from')))
    assert isinstance(transactions, list)
    assert len(transactions) == 8
    assert transactions[0].transaction_id == 716496732
    assert transactions[1].transaction_date == '08.12.2019'
    assert transactions[2].transaction_from == 'Visa Platinum 1246 37** **** 3588'
    assert transactions[3].transaction_to == 'Счет **3493'

def test_repr(data_for_tests):
    transaction = Transaction(data_for_tests[0]['id'], data_for_tests[0]['date'], data_for_tests[0]['description'],
                                        data_for_tests[0]['operationAmount'], data_for_tests[0]['to'], data_for_tests[0].get('from'))
    assert repr(transaction) == 'ID: 716496732\n' \
                                'Date: 04.04.2018\n' \
                                'Description: Перевод организации\n' \
                                'From: Visa Gold 5999 41** **** 6353\n' \
                                'To: Счет **4472\n' \
                                'Amount: 40701.91 USD\n'
    assert str(transaction) == '04.04.2018 Перевод организации\n' \
                               'Visa Gold 5999 41** **** 6353 -> Счет **4472\n' \
                               '40701.91 USD\n'
