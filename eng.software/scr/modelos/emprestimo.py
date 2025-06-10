from datetime import date
from .livro import Livro
from .usuario import Usuario

class Emprestimo:
    """Representa um empréstimo de livro por um usuário."""
    
    def __init__(self, usuario: Usuario, livro: Livro, data_emprestimo: str):
        """
        Inicializa um empréstimo.
        
        Args:
            usuario: Usuário que está emprestando
            livro: Livro sendo emprestado
            data_emprestimo: Data do empréstimo (formato YYYY-MM-DD)
        """
        self.usuario = usuario
        self.livro = livro
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = None
        self.devolvido = False
        self.usuario.adicionar_emprestimo(self)

    def devolver(self, data_devolucao: str) -> None:
        """Registra a devolução do livro."""
        self.data_devolucao = data_devolucao
        self.devolvido = True
        self.livro.devolver()
        self.usuario.remover_emprestimo(self)

    def calcular_multa(self) -> float:
        """Calcula multa por atraso (implementação simplificada)."""
        # Em uma implementação real, calcularíamos dias de atraso
        return 10.0 if not self.devolvido else 0.0

    def __str__(self):
        status = "Devolvido" if self.devolvido else "Pendente"
        return f"{self.usuario.nome} -> {self.livro.titulo} ({status})"

    def __repr__(self):
        return f"Emprestimo(usuario={repr(self.usuario)}, livro={repr(self.livro)}, data='{self.data_emprestimo}')"