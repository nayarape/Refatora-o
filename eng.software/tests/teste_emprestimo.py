import pytest
from datetime import date
from src.modelos.emprestimo import Emprestimo
from src.modelos.usuario import Usuario
from src.modelos.livro import Livro

class TestEmprestimo:
    """Testes unitários para a classe Emprestimo"""
    
    @pytest.fixture
    def emprestimo_exemplo(self):
        usuario = Usuario("Alice", "456")
        livro = Livro("Design Patterns", "GoF", 1994)
        return Emprestimo(usuario, livro, "2023-01-15")
    
    def test_criacao_emprestimo(self, emprestimo_exemplo):
        """Testa a criação correta de um empréstimo"""
        assert emprestimo_exemplo.usuario.nome == "Alice"
        assert emprestimo_exemplo.livro.titulo == "Design Patterns"
        assert emprestimo_exemplo.data_emprestimo == "2023-01-15"
        assert emprestimo_exemplo.devolvido is False
        assert emprestimo_exemplo.data_devolucao is None
    
    def test_devolver_emprestimo(self, emprestimo_exemplo):
        """Testa a devolução de um empréstimo"""
        data_devolucao = "2023-02-01"
        emprestimo_exemplo.devolver(data_devolucao)
        
        assert emprestimo_exemplo.devolvido is True
        assert emprestimo_exemplo.data_devolucao == data_devolucao
        assert emprestimo_exemplo not in emprestimo_exemplo.usuario.emprestimos_ativos
        assert emprestimo_exemplo.livro.quantidade_disponivel == 1
    
    def test_calcular_multa(self, emprestimo_exemplo):
        """Testa cálculo de multa"""
        # Empréstimo ativo deve ter multa
        assert emprestimo_exemplo.calcular_multa() == 10.0
        
        # Empréstimo devolvido não deve ter multa
        emprestimo_exemplo.devolver("2023-01-20")
        assert emprestimo_exemplo.calcular_multa() == 0.0
    
    def test_str_representation(self, emprestimo_exemplo):
        """Testa a representação em string do empréstimo"""
        assert str(emprestimo_exemplo) == "Alice -> Design Patterns (Pendente)"
        emprestimo_exemplo.devolver("2023-01-20")
        assert "Devolvido" in str(emprestimo_exemplo)