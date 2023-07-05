from HM.reposytory import Repository
from HM.transaction import Transaction
from settings import DATA_PATH


def main():
    #  Инициализируем класс с данными по трансакциям
    repository: Repository = Repository()
    # Используя его методы получаем список из последних пяти успешных трансакций
    last_five_transaction = repository.get_last_five_transactions()
    # Инициализируем пять экземпляров класса Transaction
    for transaction in last_five_transaction:
        transaction = Transaction(transaction_id=transaction['id'],
                                  transaction_date=transaction['date'],
                                  transaction_description=transaction['description'],
                                  transaction_amount=transaction['operationAmount'],
                                  transaction_to=transaction['to'],
                                  transaction_from=transaction.get('from'))
        print(transaction)  # Одновременно выводим на печать созданный экземпляр


if __name__ == '__main__':
    main()
