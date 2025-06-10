# Contratos das Classes

## Classe Livro

**Responsabilidade**: Representar um livro no sistema, gerenciando sua disponibilidade.

**Métodos**:
- `emprestar()`: Diminui a quantidade disponível. Retorna True se bem-sucedido.
- `devolver()`: Aumenta a quantidade disponível. Lança exceção se quantidade exceder o total.

## Classe Usuario

**Responsabilidade**: Representar um usuário do sistema e gerenciar seus empréstimos ativos.

**Métodos**:
- `adicionar_emprestimo()`: Adiciona um empréstimo à lista de ativos.
- `remover_emprestimo()`: Remove um empréstimo da lista de ativos.

## Classe Emprestimo

**Responsabilidade**: Representar a relação de empréstimo entre usuário e livro.

**Métodos**:
- `devolver()`: Marca o empréstimo como devolvido e atualiza o livro e usuário.
- `calcular_multa()`: Calcula o valor da multa por atraso.

## Classe Biblioteca

**Responsabilidade**: Coordenar as operações do sistema de biblioteca.

**Métodos**:
- `emprestar_livro()`: Cria um novo empréstimo se condições forem atendidas.
- `devolver_livro()`: Registra a devolução de um livro.
- `calcular_multa_usuario()`: Retorna o total de multas pendentes do usuário.

**Exceções**:
- `UsuarioNaoEncontradoError`: Quando usuário não existe.
- `LivroNaoEncontradoError`: Quando livro não existe.
- `LivroIndisponivelError`: Quando livro não está disponível.
- `EmprestimoNaoEncontradoError`: Quando empréstimo não existe.