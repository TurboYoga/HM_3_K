from pathlib import Path

# Создание пути к файлу с трансакциями
ROOT = Path(__file__).resolve().parent
FIXTURE_PATH = Path.joinpath(ROOT, 'fixture')
DATA_PATH = Path.joinpath(FIXTURE_PATH, 'operations.json')
