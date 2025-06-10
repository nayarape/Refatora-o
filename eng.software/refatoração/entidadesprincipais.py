class Livro:
    def __init__(self, titulo: str, autor: str, ano: int, quantidade: int = 1):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.quantidade = quantidade
        self.quantidade_disponivel = quantidade

    def emprestar(self) -> bool:
        if self.quantidade_disponivel > 0:
            self.quantidade_disponivel -= 1
            return True
        return False

    def devolver(self) -> None:
        if self.quantidade_disponivel < self.quantidade:
            self.quantidade_disponivel += 1

    def __str__(self):
        return f"{self.titulo} ({self.autor}, {self.ano})"

class Usuario:
    def __init__(self, nome: str, id_usuario: str):
        self.nome = nome
        self.id = id_usuario
        self.emprestimos_ativos = []

    def adicionar_emprestimo(self, emprestimo):
        self.emprestimos_ativos.append(emprestimo)

    def remover_emprestimo(self, emprestimo):
        if emprestimo in self.emprestimos_ativos:
            self.emprestimos_ativos.remove(emprestimo)

    def __str__(self):
        return f"{self.nome} (ID: {self.id})"

class Emprestimo:
    def __init__(self, usuario: Usuario, livro: Livro, data_emprestimo: str):
        self.usuario = usuario
        self.livro = livro
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = None
        self.devolvido = False

    def devolver(self, data_devolucao: str) -> None:
        self.data_devolucao = data_devolucao
        self.devolvido = True
        self.livro.devolver()
        self.usuario.remover_emprestimo(self)

    def calcular_multa(self) -> float:
        # Implementação real calcularia dias de atraso, etc.
        return 10.0 if not self.devolvido else 0.0

    def __str__(self):
        status = "Devolvido" if self.devolvido else "Pendente"
        return f"{self.usuario.nome} -> {self.livro.titulo} ({status})"