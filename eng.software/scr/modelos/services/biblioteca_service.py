from typing import List, Optional
from datetime import date
from modelos.services import Livro, Usuario, Emprestimo
from modelos import (
    UsuarioNaoEncontradoError,
    LivroNaoEncontradoError,
    LivroIndisponivelError,
    EmprestimoNaoEncontradoError
)

class Biblioteca:
    """Classe principal que gerencia as operações da biblioteca."""
    
    def __init__(self):
        self._livros: List[Livro] = []
        self._usuarios: List[Usuario] = []
        self._emprestimos: List[Emprestimo] = []
    
    @property
    def livros(self) -> List[Livro]:
        """Retorna uma cópia da lista de livros."""
        return self._livros.copy()
    
    @property
    def usuarios(self) -> List[Usuario]:
        """Retorna uma cópia da lista de usuários."""
        return self._usuarios.copy()
    
    @property
    def emprestimos(self) -> List[Emprestimo]:
        """Retorna uma cópia da lista de empréstimos."""
        return self._emprestimos.copy()

    def adicionar_livro(self, livro: Livro) -> None:
        """Adiciona um livro ao acervo da biblioteca."""
        self._livros.append(livro)

    def cadastrar_usuario(self, usuario: Usuario) -> None:
        """Cadastra um novo usuário na biblioteca."""
        self._usuarios.append(usuario)

    def buscar_livro(self, titulo: str) -> Optional[Livro]:
        """Busca um livro pelo título (case insensitive)."""
        for livro in self._livros:
            if livro.titulo.lower() == titulo.lower():
                return livro
        return None

    def buscar_usuario(self, id_usuario: str) -> Optional[Usuario]:
        """Busca um usuário pelo ID."""
        for usuario in self._usuarios:
            if usuario.id == id_usuario:
                return usuario
        return None

    def emprestar_livro(self, id_usuario: str, titulo_livro: str) -> Emprestimo:
        """
        Realiza o empréstimo de um livro para um usuário.
        
        Args:
            id_usuario: ID do usuário
            titulo_livro: Título do livro a ser emprestado
            
        Returns:
            Objeto Emprestimo criado
            
        Raises:
            UsuarioNaoEncontradoError: Se usuário não existe
            LivroNaoEncontradoError: Se livro não existe
            LivroIndisponivelError: Se livro não está disponível
        """
        usuario = self.buscar_usuario(id_usuario)
        if not usuario:
            raise UsuarioNaoEncontradoError(id_usuario)
            
        livro = self.buscar_livro(titulo_livro)
        if not livro:
            raise LivroNaoEncontradoError(titulo_livro)
            
        if not livro.emprestar():
            raise LivroIndisponivelError(titulo_livro)
            
        emprestimo = Emprestimo(usuario, livro, date.today().isoformat())
        self._emprestimos.append(emprestimo)
        
        return emprestimo

    def devolver_livro(self, id_usuario: str, titulo_livro: str) -> None:
        """
        Registra a devolução de um livro.
        
        Args:
            id_usuario: ID do usuário
            titulo_livro: Título do livro a ser devolvido
            
        Raises:
            UsuarioNaoEncontradoError: Se usuário não existe
            LivroNaoEncontradoError: Se livro não existe
            EmprestimoNaoEncontradoError: Se empréstimo não existe
        """
        usuario = self.buscar_usuario(id_usuario)
        if not usuario:
            raise UsuarioNaoEncontradoError(id_usuario)
            
        livro = self.buscar_livro(titulo_livro)
        if not livro:
            raise LivroNaoEncontradoError(titulo_livro)
            
        for emprestimo in self._emprestimos:
            if (emprestimo.usuario == usuario and 
                emprestimo.livro == livro and 
                not emprestimo.devolvido):
                emprestimo.devolver(date.today().isoformat())
                return
                
        raise EmprestimoNaoEncontradoError(id_usuario, titulo_livro)

    def calcular_multa_usuario(self, id_usuario: str) -> float:
        """
        Calcula o total de multas pendentes de um usuário.
        
        Args:
            id_usuario: ID do usuário
            
        Returns:
            Valor total das multas
            
        Raises:
            UsuarioNaoEncontradoError: Se usuário não existe
        """
        usuario = self.buscar_usuario(id_usuario)
        if not usuario:
            raise UsuarioNaoEncontradoError(id_usuario)
            
        return sum(emp.calcular_multa() for emp in usuario.emprestimos_ativos)