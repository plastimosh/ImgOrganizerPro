from application.select_directory import SelectDirectoryUseCase
from infrastructure.tkinter_gateway import TkinterDirectoryGateway

def main():
    gateway = TkinterDirectoryGateway()
    use_case = SelectDirectoryUseCase(gateway)

    try:
        directory = use_case.execute()
        print(f"Directorio seleccionado: {directory.path}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()