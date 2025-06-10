# 📚 Sistema de Gerenciamento de Biblioteca

Este projeto é uma refatoração de um sistema de biblioteca inicialmente monolítico, reestruturado com foco em **design orientado a objetos**, **princípios SOLID**, e **testes automatizados**. A proposta é tornar o sistema mais modular, legível e de fácil manutenção, além de facilitar a evolução futura com segurança.

---

## 🧩 Objetivos Gerais

- ✅ Extrair entidades do domínio em classes coesas (`Livro`, `Usuário`, `Empréstimo`);
- ✅ Aplicar o **Princípio da Responsabilidade Única (SRP)** em cada classe e serviço;
- ✅ Usar os **Princípios SOLID** para garantir modularidade:
  - **OCP**: Abertura para extensão, sem modificar código existente;
  - **LSP**: Uso seguro de subtipos (não aplicável diretamente, mas respeitado em estrutura);
  - **ISP**: Interface mínima por classe (sem acoplamento desnecessário);
  - **DIP**: Camadas separadas entre modelos e serviço principal;
- ✅ Implementar **tratamento de erros robusto** por meio de exceções específicas;
- ✅ Criar **testes automatizados de integração** usando `unittest`;
- ✅ Estruturar código para facilitar **modelagem UML**.
