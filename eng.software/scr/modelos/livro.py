class Livro:
    """Representa um livro no sistema da biblioteca."""
    
    def __init__(self, titulo: str, autor: str, ano: int, quantidade: int = 1):
        """
        Inicializa um livro.
        
        Args:
            titulo: Título do livro
            autor: Autor do livro
            ano: Ano de publicação
            quantidade: Quantidade total de cópias (default: 1)
        """
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.quantidade = quantidade
        self.quantidade_disponivel = quantidade

    def emprestar(self) -> bool:
        """Registra o empréstimo de uma cópia do livro."""
        if self.quantidade_disponivel > 0:
            self.quantidade_disponivel -= 1
            return True
        return False

    def devolver(self) -> None:
        """Registra a devolução de uma cópia do livro."""
        if self.quantidade_disponivel < self.quantidade:
            self.quantidade_disponivel += 1
        else:
            raise ValueError("Não é possível devolver mais cópias do que foram emprestadas")

    def __str__(self):
        return f"{self.titulo} ({self.autor}, {self.ano})"

    def __repr__(self):
        return f"Livro(titulo='{self.titulo}', autor='{self.autor}', ano={self.ano}, quantidade={self.quantidade})"