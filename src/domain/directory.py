class Directory:
    def __init__(self, path: str):
        if not path:
            raise ValueError("Path vacío no permitido")
        self.path = path