import pytest
from src.modelos.usuario import Usuario
from src.modelos.emprestimo import Emprestimo
from src.modelos.livro import Livro

class TestUsuario:
    """Testes unitários para a classe Usuario"""
    
    @pytest.fixture
    def usuario_exemplo(self):
        return Usuario("John Doe", "123")
    
    @pytest.fixture
    def emprestimo_exemplo(self):
        livro = Livro("Refactoring", "Martin Fowler", 1999)
        usuario = Usuario("Test User", "999")
        return Emprestimo(usuario, livro, "2023-01-01")
    
    def test_criacao_usuario(self, usuario_exemplo):
        """Testa a criação correta de um usuário"""
        assert usuario_exemplo.nome == "John Doe"
        assert usuario_exemplo.id == "123"
        assert usuario_exemplo.emprestimos_ativos == []
    
    def test_adicionar_emprestimo(self, usuario_exemplo, emprestimo_exemplo):
        """Testa adição de empréstimo ao usuário"""
        usuario_exemplo.adicionar_emprestimo(emprestimo_exemplo)
        assert len(usuario_exemplo.emprestimos_ativos) == 1
        assert emprestimo_exemplo in usuario_exemplo.emprestimos_ativos
    
    def test_remover_emprestimo(self, usuario_exemplo, emprestimo_exemplo):
        """Testa remoção de empréstimo do usuário"""
        usuario_exemplo.adicionar_emprestimo(emprestimo_exemplo)
        usuario_exemplo.remover_emprestimo(emprestimo_exemplo)
        assert len(usuario_exemplo.emprestimos_ativos) == 0
    
    def test_str_representation(self, usuario_exemplo):
        """Testa a representação em string do usuário"""
        assert str(usuario_exemplo) == "John Doe (ID: 123)"