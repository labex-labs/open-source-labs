# Trazendo Caminhos para o Escopo com a Palavra-chave `use`

Ter que escrever os caminhos para chamar funções pode parecer inconveniente e repetitivo. Na Listagem 7-7, independentemente de termos escolhido o caminho absoluto ou relativo para a função `add_to_waitlist`, toda vez que queríamos chamar `add_to_waitlist`, tínhamos que especificar `front_of_house` e `hosting` também. Felizmente, existe uma maneira de simplificar esse processo: podemos criar um atalho para um caminho com a palavra-chave `use` uma vez e, em seguida, usar o nome mais curto em todos os outros lugares no escopo.

Na Listagem 7-11, trazemos o módulo `crate::front_of_house::hosting` para o escopo da função `eat_at_restaurant`, para que só tenhamos que especificar `hosting::add_to_waitlist` para chamar a função `add_to_waitlist` em `eat_at_restaurant`.

Nome do arquivo: `src/lib.rs`

```rust
mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

use crate::front_of_house::hosting;

pub fn eat_at_restaurant() {
    hosting::add_to_waitlist();
}
```

Listagem 7-11: Trazendo um módulo para o escopo com `use`

Adicionar `use` e um caminho em um escopo é semelhante a criar um link simbólico no sistema de arquivos. Ao adicionar `use crate::front_of_house::hosting` na raiz do crate, `hosting` agora é um nome válido nesse escopo, como se o módulo `hosting` tivesse sido definido na raiz do crate. Caminhos trazidos para o escopo com `use` também verificam a privacidade, como quaisquer outros caminhos.

Observe que `use` apenas cria o atalho para o escopo específico em que o `use` ocorre. A Listagem 7-12 move a função `eat_at_restaurant` para um novo módulo filho chamado `customer`, que então é um escopo diferente da instrução `use`, portanto, o corpo da função não compilará.

Nome do arquivo: `src/lib.rs`

```rust
mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

use crate::front_of_house::hosting;

mod customer {
    pub fn eat_at_restaurant() {
        hosting::add_to_waitlist();
    }
}
```

Listagem 7-12: Uma instrução `use` só se aplica no escopo em que está.

O erro do compilador mostra que o atalho não se aplica mais dentro do módulo `customer`:

```bash
error[E0433]: failed to resolve: use of undeclared crate or module `hosting`
  --> src/lib.rs:11:9
   |
11 |         hosting::add_to_waitlist();
   |         ^^^^^^^ use of undeclared crate or module `hosting`

warning: unused import: `crate::front_of_house::hosting`
 --> src/lib.rs:7:5
  |
7 | use crate::front_of_house::hosting;
  |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  |
  = note: `#[warn(unused_imports)]` on by default
```

Observe que também há um aviso de que o `use` não é mais usado em seu escopo! Para corrigir esse problema, mova o `use` para dentro do módulo `customer` também, ou referencie o atalho no módulo pai com `super::hosting` dentro do módulo filho `customer`.
