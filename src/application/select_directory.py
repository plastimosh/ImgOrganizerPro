from domain.directory import Directory
from domain.validator import DirectoryValidator

class SelectDirectoryUseCase:
    def __init__(self, directory_gateway):
        self.directory_gateway = directory_gateway

    def execute(self):
        path = self.directory_gateway.select_directory()
        DirectoryValidator.validate(path)
        return Directory(path)