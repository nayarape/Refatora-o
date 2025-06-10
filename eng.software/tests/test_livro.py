import pytest
from datetime import date
from src.modelos.livro import Livro
from src.modelos.exceptions import OperacaoLivroError

class TestLivro:
    """Testes unitários para a classe Livro"""
    
    @pytest.fixture
    def livro_exemplo(self):
        return Livro("Clean Code", "Robert Martin", 2008, 3)
    
    def test_criacao_livro(self, livro_exemplo):
        """Testa a criação correta de um livro"""
        assert livro_exemplo.titulo == "Clean Code"
        assert livro_exemplo.autor == "Robert Martin"
        assert livro_exemplo.ano == 2008
        assert livro_exemplo.quantidade == 3
        assert livro_exemplo.quantidade_disponivel == 3
    
    def test_emprestar_livro_disponivel(self, livro_exemplo):
        """Testa empréstimo de livro disponível"""
        assert livro_exemplo.emprestar() is True
        assert livro_exemplo.quantidade_disponivel == 2
    
    def test_emprestar_livro_indisponivel(self):
        """Testa tentativa de empréstimo de livro indisponível"""
        livro = Livro("Domain-Driven Design", "Eric Evans", 2003, 1)
        livro.emprestar()  # Esgota o estoque
        
        with pytest.raises(OperacaoLivroError):
            livro.emprestar()
    
    def test_devolver_livro(self, livro_exemplo):
        """Testa devolução de livro"""
        livro_exemplo.emprestar()
        livro_exemplo.emprestar()
        assert livro_exemplo.quantidade_disponivel == 1
        
        livro_exemplo.devolver()
        assert livro_exemplo.quantidade_disponivel == 2
        
        livro_exemplo.devolver()
        assert livro_exemplo.quantidade_disponivel == 3
        
        # Não deve permitir devolver além do estoque original
        with pytest.raises(OperacaoLivroError):
            livro_exemplo.devolver()
    
    def test_str_representation(self, livro_exemplo):
        """Testa a representação em string do livro"""
        assert str(livro_exemplo) == "Clean Code (Robert Martin, 2008)"