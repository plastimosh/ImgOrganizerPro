from application.select_directory import SelectDirectoryUseCase
from infrastructure.tkinter_gateway import TkinterDirectoryGateway

from application.services.file_explorer import FileExplorer
from pathlib import Path

def main():
    gateway = TkinterDirectoryGateway()
    use_case = SelectDirectoryUseCase(gateway)
    explorer = FileExplorer()

    try:
        directory = use_case.execute()

        path = Path(directory.path)

        if not path.exists() or not path.is_dir():
            print("Ruta inválida")
            return

        images = explorer.explore(path)

        print("Exploración completada")
        print(f"Directorio: {path}")
        print(f"Total imágenes encontradas: {len(images)}")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()