import os
from pathlib import Path
from typing import Generator

class FileSystemService:

    def walk(self, directory: Path) -> Generator[Path, None, None]:
        for entry in os.scandir(directory):
            try:
                if entry.is_file():
                    yield Path(entry.path)
                elif entry.is_dir():
                    yield from self.walk(Path(entry.path))
            except PermissionError:
                continue