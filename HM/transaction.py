from datetime import datetime


class Transaction:
    """
    Класс Transaction содержит и обрабатывает поля отдельной трансакции
    """
    def __init__(self, transaction_id: int,
                 transaction_date: str,
                 transaction_description: str,
                 transaction_amount: dict,
                 transaction_to: str,
                 transaction_from: str) -> None:
        self.transaction_id: int = transaction_id
        self.transaction_date: str = self.convert_datetime_to_date(transaction_date)
        self.transaction_description: str = transaction_description
        self.transaction_from: str = self.numbers_masking(transaction_from) if transaction_from else ''
        self.transaction_to: str = self.numbers_masking(transaction_to)
        self.transaction_amount: str = transaction_amount['amount']
        self.transaction_currency: str = transaction_amount['currency']['name']

    @staticmethod
    def convert_datetime_to_date(transaction_date):
        """
        Метод принимает на входе строку с датой и временем
        и возвращает строку только с датой
        """
        date_: datetime = datetime.strptime(transaction_date, "%Y-%m-%dT%H:%M:%S.%f")
        return date_.strftime("%d.%m.%Y")

    @staticmethod
    def numbers_masking(account_number):
        """
        Метод принимает на входе строку с номером кредитной карты
        или номером счета и возвращает их с частично замаскированными
        символом '*' цифрами
        """
        if account_number.startswith('Счет'):
            list_card_number = account_number.split(' ')
            new_number = f'**{list_card_number[-1][-4:]}'
        else:
            list_card_number = account_number.split(' ')
            new_number = f'{list_card_number[-1][0: 4]} {list_card_number[-1][4: 6]}** **** {list_card_number[-1][-4:]}'
        list_card_number[-1] = new_number
        return ' '.join(list_card_number)

    def __repr__(self) :
        return f'ID: {self.transaction_id}\n' \
               f'Date: {self.transaction_date}\n' \
               f'Description: {self.transaction_description}\n' \
               f'From: {self.transaction_from}\n' \
               f'To: {self.transaction_to}\n' \
               f'Amount: {self.transaction_amount} {self.transaction_currency}\n'

    def __str__(self) :
        return f'{self.transaction_date } {self.transaction_description}\n' \
               f'{self.transaction_from} -> {self.transaction_to}\n' \
               f'{self.transaction_amount} {self.transaction_currency}\n'
