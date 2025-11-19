class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        
    def __str__(self):
        return f"Autor {self.autor} - titulo {self.titulo}"