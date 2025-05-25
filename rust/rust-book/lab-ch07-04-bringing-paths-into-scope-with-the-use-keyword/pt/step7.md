# O Operador Glob

Se quisermos trazer _todos_ os itens públicos definidos em um caminho para o escopo, podemos especificar esse caminho seguido pelo operador glob `*`:

```rust
use std::collections::*;
```

Esta declaração `use` traz todos os itens públicos definidos em `std::collections` para o escopo atual. Tenha cuidado ao usar o operador glob! O glob pode dificultar a identificação de quais nomes estão no escopo e onde um nome usado em seu programa foi definido.

O operador glob é frequentemente usado ao testar para trazer tudo sob teste para o módulo `tests`; falaremos sobre isso em "Como Escrever Testes". O operador glob também é usado às vezes como parte do padrão prelude: consulte a documentação da biblioteca padrão para obter mais informações sobre esse padrão.
