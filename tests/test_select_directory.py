from application.select_directory import SelectDirectoryUseCase

class FakeGateway:
    def select_directory(self):
        return "."

def test_select_directory():
    use_case = SelectDirectoryUseCase(FakeGateway())
    result = use_case.execute()
    assert result.path == "."