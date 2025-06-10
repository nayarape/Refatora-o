import unittest
from services.biblioteca import Biblioteca

class TestIntegracaoBiblioteca(unittest.TestCase):

    def setUp(self):
        self.biblioteca = Biblioteca()
        self.biblioteca.cadastrar_usuario("João", 1)
        self.biblioteca.adicionar_livro("1984", "George Orwell", 1949, 2)

    def test_emprestar_e_devolver_livro(self):
        emprestimo = self.biblioteca.emprestar_livro(1, "1984")
        self.assertEqual(emprestimo.livro.titulo, "1984")
        self.assertFalse(emprestimo.devolvido)
        self.assertEqual(emprestimo.livro.quantidade, 1)

        self.biblioteca.devolver_livro(1, "1984")
        self.assertTrue(emprestimo.devolvido)
        self.assertEqual(emprestimo.livro.quantidade, 2)

    def test_multa_para_usuario(self):
        self.biblioteca.emprestar_livro(1, "1984")
        multa = self.biblioteca.calcular_multa(1)
        self.assertEqual(multa, 10)

        self.biblioteca.devolver_livro(1, "1984")
        multa_pos_devolucao = self.biblioteca.calcular_multa(1)
        self.assertEqual(multa_pos_devolucao, 0)

if __name__ == '__main__':
    unittest.main()
