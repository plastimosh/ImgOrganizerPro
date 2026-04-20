from tkinter import filedialog
from infrastructure.directory_gateway import DirectoryGateway

class TkinterDirectoryGateway(DirectoryGateway):
    def select_directory(self) -> str:
        return filedialog.askdirectory()