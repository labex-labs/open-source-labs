# Criando Caminhos `use` Idiomáticos

Na Listagem 7-11, você pode ter se perguntado por que especificamos `use crate::front_of_house::hosting` e, em seguida, chamamos `hosting::add_to_waitlist` em `eat_at_restaurant`, em vez de especificar o caminho `use` até a função `add_to_waitlist` para obter o mesmo resultado, como na Listagem 7-13.

Nome do arquivo: `src/lib.rs`

```rust
mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

use crate::front_of_house::hosting::add_to_waitlist;

pub fn eat_at_restaurant() {
    add_to_waitlist();
}
```

Listagem 7-13: Trazendo a função `add_to_waitlist` para o escopo com `use`, o que não é idiomático

Embora tanto a Listagem 7-11 quanto a Listagem 7-13 realizem a mesma tarefa, a Listagem 7-11 é a maneira idiomática de trazer uma função para o escopo com `use`. Trazer o módulo pai da função para o escopo com `use` significa que temos que especificar o módulo pai ao chamar a função. Especificar o módulo pai ao chamar a função deixa claro que a função não é definida localmente, ao mesmo tempo em que minimiza a repetição do caminho completo. O código na Listagem 7-13 não deixa claro onde `add_to_waitlist` é definido.

Por outro lado, ao trazer structs, enums e outros itens com `use`, é idiomático especificar o caminho completo. A Listagem 7-14 mostra a maneira idiomática de trazer a struct `HashMap` da biblioteca padrão para o escopo de um crate binário.

Nome do arquivo: `src/main.rs`

```rust
use std::collections::HashMap;

fn main() {
    let mut map = HashMap::new();
    map.insert(1, 2);
}
```

Listagem 7-14: Trazendo `HashMap` para o escopo de maneira idiomática

Não há uma razão forte por trás desse idioma: é apenas a convenção que surgiu, e as pessoas se acostumaram a ler e escrever código Rust dessa maneira.

A exceção a esse idioma é se estivermos trazendo dois itens com o mesmo nome para o escopo com instruções `use`, porque o Rust não permite isso. A Listagem 7-15 mostra como trazer dois tipos `Result` para o escopo que têm o mesmo nome, mas módulos pai diferentes, e como se referir a eles.

Nome do arquivo: `src/lib.rs`

```rust
use std::fmt;
use std::io;

fn function1() -> fmt::Result {
    --snip--
}

fn function2() -> io::Result<()> {
    --snip--
}
```

Listagem 7-15: Trazer dois tipos com o mesmo nome para o mesmo escopo requer o uso de seus módulos pai.

Como você pode ver, usar os módulos pai distingue os dois tipos `Result`. Se, em vez disso, especificássemos `use std::fmt::Result` e `use std::io::Result`, teríamos dois tipos `Result` no mesmo escopo, e o Rust não saberia a qual nos referíamos quando usássemos `Result`.
