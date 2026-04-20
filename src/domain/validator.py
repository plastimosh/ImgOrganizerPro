import os

class DirectoryValidator:
    @staticmethod
    def validate(path: str) -> None:
        if not os.path.exists(path):
            raise FileNotFoundError(f"No existe: {path}")
        if not os.path.isdir(path):
            raise NotADirectoryError(f"No es carpeta: {path}")