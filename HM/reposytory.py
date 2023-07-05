import json

from settings import DATA_PATH


class Repository:
    """
    Класс Repository содержит всё, что необходимо для чтения данных из
    файла и их подготовке для дальнейшей работы программы
    """
    def __init__(self):
        self.data_path: str = DATA_PATH

    def read_json(self):
        """
        Метод считывает все записи из json-файла.
        """
        with open(self.data_path) as file:
            return json.load(file)

    def remove_empty_transactions(self, all_transactions):
        """
        Метод удаляет пустые записи из всех полученных трансакций
        и возвращает только непустые
        """
        all_transactions.remove({})
        return all_transactions

    def get_last_five_transactions(self):
        """
        Метод возвращает пять последних по времени трансакций. Предварительно вычистив все
        трансакции от ошибочных, и отфильтровав их по выполненным
        """
        # Получаем из файла все записи трансакций
        all_transactions = self.read_json()
        # Удаляем из полученных записей пустые
        non_empty_transaction = self.remove_empty_transactions(all_transactions)
        # И возвращаем пять последних трансакций, отсортировав список по статусу и дате
        return sorted(non_empty_transaction, key=lambda dictionary: (dict['status'], dictionary['date']), reverse=True)[:5]
