# Objetos Contêm Dados e Comportamento

O livro _Design Patterns: Elements of Reusable Object-Oriented Software_ de Erich Gamma, Richard Helm, Ralph Johnson e John Vlissides (Addison-Wesley, 1994), coloquialmente referido como o livro _The Gang of Four_, é um catálogo de padrões de design orientado a objetos. Ele define OOP da seguinte forma:

Programas orientados a objetos são compostos por objetos. Um _objeto_ empacota tanto dados quanto os procedimentos que operam nesses dados. Os procedimentos são tipicamente chamados de _métodos_ ou _operações_.

Usando esta definição, Rust é orientado a objetos: structs e enums têm dados, e blocos `impl` fornecem métodos em structs e enums. Embora structs e enums com métodos não sejam _chamados_ de objetos, eles fornecem a mesma funcionalidade, de acordo com a definição de objetos do Gang of Four.
