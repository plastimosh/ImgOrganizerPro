from pathlib import Path
from typing import List
from src.domain.entities.file_entity import FileEntity
from src.infrastructure.filesystem.file_system_service import FileSystemService

class FileExplorer:

    IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".gif"}

    def __init__(self):
        self.fs = FileSystemService()

    def explore(self, directory: Path) -> List[FileEntity]:
        images = []

        for file_path in self.fs.walk(directory):
            ext = file_path.suffix.lower()

            # 🔥 FILTRADO CLAVE
            if ext not in self.IMAGE_EXTENSIONS:
                continue

            try:
                images.append(
                    FileEntity(
                        path=file_path,
                        extension=ext,
                        size=file_path.stat().st_size
                    )
                )
            except Exception:
                continue

        return images