from dataclasses import dataclass
from pathlib import Path

@dataclass
class FileEntity:
    path: Path
    extension: str
    size: int