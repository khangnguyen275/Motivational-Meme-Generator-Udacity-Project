from pathlib import Path

default_path = Path(__file__).resolve().parent.parent / '_data'/ 'photos' /'dog'
print([x for x in default_path.iterdir()])