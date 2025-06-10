class BibliotecaError(Exception):
    """Classe base para erros da biblioteca."""
    pass

class UsuarioNaoEncontradoError(BibliotecaError):
    def __init__(self, id_usuario):
        super().__init__(f"Usuário com ID {id_usuario} não encontrado")
        self.id_usuario = id_usuario

class LivroNaoEncontradoError(BibliotecaError):
    def __init__(self, titulo):
        super().__init__(f"Livro '{titulo}' não encontrado")
        self.titulo = titulo

class LivroIndisponivelError(BibliotecaError):
    def __init__(self, titulo):
        super().__init__(f"Livro '{titulo}' não disponível para empréstimo")
        self.titulo = titulo

class EmprestimoNaoEncontradoError(BibliotecaError):
    def __init__(self, id_usuario, titulo):
        super().__init__(f"Empréstimo não encontrado para usuário {id_usuario} e livro '{titulo}'")
        self.id_usuario = id_usuario
        self.titulo = titulo

class OperacaoLivroError(BibliotecaError):
    """Erro durante operação com livro (emprestar/devolver)"""
    pass

__all__ = [
    'BibliotecaError',
    'UsuarioNaoEncontradoError', 
    'LivroNaoEncontradoError',
    'LivroIndisponivelError',
    'EmprestimoNaoEncontradoError',
    'OperacaoLivroError'
]