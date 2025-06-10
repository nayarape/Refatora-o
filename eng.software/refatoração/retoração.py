from typing import List, Dict, Optional
from datetime import date

class Biblioteca:
    def __init__(self):
        self._livros: List[Livro] = []
        self._usuarios: List[Usuario] = []
        self._emprestimos: List[Emprestimo] = []
    
    @property
    def livros(self) -> List[Livro]:
        return self._livros.copy()
    
    @property
    def usuarios(self) -> List[Usuario]:
        return self._usuarios.copy()
    
    @property
    def emprestimos(self) -> List[Emprestimo]:
        return self._emprestimos.copy()

    def adicionar_livro(self, livro: Livro) -> None:
        self._livros.append(livro)

    def cadastrar_usuario(self, usuario: Usuario) -> None:
        self._usuarios.append(usuario)

    def buscar_livro(self, titulo: str) -> Optional[Livro]:
        for livro in self._livros:
            if livro.titulo.lower() == titulo.lower():
                return livro
        return None

    def buscar_usuario(self, id_usuario: str) -> Optional[Usuario]:
        for usuario in self._usuarios:
            if usuario.id == id_usuario:
                return usuario
        return None

    def emprestar_livro(self, id_usuario: str, titulo_livro: str) -> Optional[Emprestimo]:
        usuario = self.buscar_usuario(id_usuario)
        livro = self.buscar_livro(titulo_livro)
        
        if not usuario:
            raise UsuarioNaoEncontradoError(id_usuario)
        if not livro:
            raise LivroNaoEncontradoError(titulo_livro)
        if not livro.emprestar():
            raise LivroIndisponivelError(titulo_livro)
        
        emprestimo = Emprestimo(usuario, livro, date.today().isoformat())
        self._emprestimos.append(emprestimo)
        usuario.adicionar_emprestimo(emprestimo)
        
        return emprestimo

    def devolver_livro(self, id_usuario: str, titulo_livro: str) -> None:
        usuario = self.buscar_usuario(id_usuario)
        livro = self.buscar_livro(titulo_livro)
        
        if not usuario:
            raise UsuarioNaoEncontradoError(id_usuario)
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
        usuario = self.buscar_usuario(id_usuario)
        if not usuario:
            raise UsuarioNaoEncontradoError(id_usuario)
        
        return sum(emp.calcular_multa() for emp in usuario.emprestimos_ativos)