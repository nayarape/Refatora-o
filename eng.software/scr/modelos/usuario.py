from typing import List
from .emprestimo import Emprestimo

class Usuario:
    """Representa um usuário da biblioteca."""
    
    def __init__(self, nome: str, id_usuario: str):
        """
        Inicializa um usuário.
        
        Args:
            nome: Nome completo do usuário
            id_usuario: Identificação única do usuário
        """
        self.nome = nome
        self.id = id_usuario
        self.emprestimos_ativos: List[Emprestimo] = []

    def adicionar_emprestimo(self, emprestimo: Emprestimo) -> None:
        """Adiciona um empréstimo à lista de empréstimos ativos."""
        if emprestimo not in self.emprestimos_ativos:
            self.emprestimos_ativos.append(emprestimo)

    def remover_emprestimo(self, emprestimo: Emprestimo) -> None:
        """Remove um empréstimo da lista de empréstimos ativos."""
        if emprestimo in self.emprestimos_ativos:
            self.emprestimos_ativos.remove(emprestimo)

    def __str__(self):
        return f"{self.nome} (ID: {self.id})"

    def __repr__(self):
        return f"Usuario(nome='{self.nome}', id='{self.id}')"