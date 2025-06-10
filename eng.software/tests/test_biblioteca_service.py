import pytest
from datetime import date
from src.services.biblioteca_service import Biblioteca
from src.modelos import Livro, Usuario
from src.modelos.exceptions import (
    UsuarioNaoEncontradoError,
    LivroNaoEncontradoError,
    LivroIndisponivelError,
    EmprestimoNaoEncontradoError
)

class TestBibliotecaService:
    """Testes unitários para o serviço Biblioteca"""
    
    @pytest.fixture
    def biblioteca(self):
        return Biblioteca()
    
    @pytest.fixture
    def livros_exemplo(self):
        return [
            Livro("Livro 1", "Autor 1", 2000, 2),
            Livro("Livro 2", "Autor 2", 2005, 1)
        ]
    
    @pytest.fixture
    def usuarios_exemplo(self):
        return [
            Usuario("User 1", "001"),
            Usuario("User 2", "002")
        ]
    
    @pytest.fixture
    def biblioteca_populada(self, biblioteca, livros_exemplo, usuarios_exemplo):
        for livro in livros_exemplo:
            biblioteca.adicionar_livro(livro)
        for usuario in usuarios_exemplo:
            biblioteca.cadastrar_usuario(usuario)
        return biblioteca
    
    def test_adicionar_livro(self, biblioteca):
        """Testa adição de livro à biblioteca"""
        livro = Livro("Novo Livro", "Autor", 2023)
        biblioteca.adicionar_livro(livro)
        assert livro in biblioteca.livros
    
    def test_cadastrar_usuario(self, biblioteca):
        """Testa cadastro de usuário na biblioteca"""
        usuario = Usuario("Novo Usuário", "999")
        biblioteca.cadastrar_usuario(usuario)
        assert usuario in biblioteca.usuarios
    
    def test_buscar_livro_existente(self, biblioteca_populada):
        """Testa busca de livro existente"""
        livro = biblioteca_populada.buscar_livro("Livro 1")
        assert livro is not None
        assert livro.titulo == "Livro 1"
    
    def test_buscar_livro_inexistente(self, biblioteca_populada):
        """Testa busca de livro inexistente"""
        assert biblioteca_populada.buscar_livro("Inexistente") is None
    
    def test_buscar_usuario_existente(self, biblioteca_populada):
        """Testa busca de usuário existente"""
        usuario = biblioteca_populada.buscar_usuario("001")
        assert usuario is not None
        assert usuario.nome == "User 1"
    
    def test_buscar_usuario_inexistente(self, biblioteca_populada):
        """Testa busca de usuário inexistente"""
        assert biblioteca_populada.buscar_usuario("999") is None
    
    def test_emprestar_livro_sucesso(self, biblioteca_populada):
        """Testa empréstimo bem-sucedido"""
        emprestimo = biblioteca_populada.emprestar_livro("001", "Livro 1")
        assert emprestimo is not None
        assert emprestimo.usuario.id == "001"
        assert emprestimo.livro.titulo == "Livro 1"
        assert emprestimo.livro.quantidade_disponivel == 1
    
    def test_emprestar_livro_usuario_inexistente(self, biblioteca_populada):
        """Testa empréstimo com usuário inexistente"""
        with pytest.raises(UsuarioNaoEncontradoError):
            biblioteca_populada.emprestar_livro("999", "Livro 1")
    
    def test_emprestar_livro_inexistente(self, biblioteca_populada):
        """Testa empréstimo de livro inexistente"""
        with pytest.raises(LivroNaoEncontradoError):
            biblioteca_populada.emprestar_livro("001", "Inexistente")
    
    def test_emprestar_livro_indisponivel(self, biblioteca_populada):
        """Testa empréstimo de livro indisponível"""
        biblioteca_populada.emprestar_livro("001", "Livro 2")  # Esgota o estoque
        with pytest.raises(LivroIndisponivelError):
            biblioteca_populada.emprestar_livro("002", "Livro 2")
    
    def test_devolver_livro_sucesso(self, biblioteca_populada):
        """Testa devolução bem-sucedida"""
        biblioteca_populada.emprestar_livro("001", "Livro 1")
        biblioteca_populada.devolver_livro("001", "Livro 1")
        
        # Verifica se a quantidade foi restaurada
        livro = biblioteca_populada.buscar_livro("Livro 1")
        assert livro.quantidade_disponivel == 2
    
    def test_devolver_livro_emprestimo_inexistente(self, biblioteca_populada):
        """Testa devolução de empréstimo inexistente"""
        with pytest.raises(EmprestimoNaoEncontradoError):
            biblioteca_populada.devolver_livro("001", "Livro 1")
    
    def test_calcular_multa_usuario(self, biblioteca_populada):
        """Testa cálculo de multa para usuário"""
        # Usuário sem empréstimos
        assert biblioteca_populada.calcular_multa_usuario("001") == 0.0
        
        # Usuário com empréstimo ativo
        biblioteca_populada.emprestar_livro("001", "Livro 1")
        assert biblioteca_populada.calcular_multa_usuario("001") == 10.0
        
        # Usuário com empréstimo devolvido
        biblioteca_populada.devolver_livro("001", "Livro 1")
        assert biblioteca_populada.calcular_multa_usuario("001") == 0.0
    
    def test_calcular_multa_usuario_inexistente(self, biblioteca_populada):
        """Testa cálculo de multa para usuário inexistente"""
        with pytest.raises(UsuarioNaoEncontradoError):
            biblioteca_populada.calcular_multa_usuario("999")