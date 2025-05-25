# Tornando Structs e Enums Públicos

Também podemos usar `pub` para designar structs e enums como públicos, mas há alguns detalhes extras no uso de `pub` com structs e enums. Se usarmos `pub` antes de uma definição de struct, tornamos a struct pública, mas os campos da struct ainda serão privados. Podemos tornar cada campo público ou não, caso a caso. Na Listagem 7-9, definimos uma struct `back_of_house::Breakfast` pública com um campo `toast` público, mas um campo `seasonal_fruit` privado. Isso modela o caso em um restaurante onde o cliente pode escolher o tipo de pão que acompanha a refeição, mas o chef decide qual fruta acompanha a refeição com base no que está na estação e em estoque. A fruta disponível muda rapidamente, então os clientes não podem escolher a fruta ou mesmo ver qual fruta receberão.

Nome do arquivo: `src/lib.rs`

```rust
mod back_of_house {
    pub struct Breakfast {
        pub toast: String,
        seasonal_fruit: String,
    }

    impl Breakfast {
        pub fn summer(toast: &str) -> Breakfast {
            Breakfast {
                toast: String::from(toast),
                seasonal_fruit: String::from("peaches"),
            }
        }
    }
}

pub fn eat_at_restaurant() {
    // Order a breakfast in the summer with Rye toast
    let mut meal = back_of_house::Breakfast::summer("Rye");
    // Change our mind about what bread we'd like
    meal.toast = String::from("Wheat");
    println!("I'd like {} toast please", meal.toast);

    // The next line won't compile if we uncomment it; we're not
    // allowed to see or modify the seasonal fruit that comes
    // with the meal
    // meal.seasonal_fruit = String::from("blueberries");
}
```

Listagem 7-9: Uma struct com alguns campos públicos e alguns campos privados

Como o campo `toast` na struct `back_of_house::Breakfast` é público, em `eat_at_restaurant` podemos escrever e ler no campo `toast` usando a notação de ponto. Observe que não podemos usar o campo `seasonal_fruit` em `eat_at_restaurant`, porque `seasonal_fruit` é privado. Tente descomentar a linha que modifica o valor do campo `seasonal_fruit` para ver qual erro você obtém!

Além disso, observe que, como `back_of_house::Breakfast` tem um campo privado, a struct precisa fornecer uma função associada pública que constrói uma instância de `Breakfast` (nós a nomeamos `summer` aqui). Se `Breakfast` não tivesse tal função, não poderíamos criar uma instância de `Breakfast` em `eat_at_restaurant` porque não poderíamos definir o valor do campo `seasonal_fruit` privado em `eat_at_restaurant`.

Em contraste, se tornarmos um enum público, todas as suas variantes serão públicas. Precisamos apenas do `pub` antes da palavra-chave `enum`, conforme mostrado na Listagem 7-10.

Nome do arquivo: `src/lib.rs`

```rust
mod back_of_house {
    pub enum Appetizer {
        Soup,
        Salad,
    }
}

pub fn eat_at_restaurant() {
    let order1 = back_of_house::Appetizer::Soup;
    let order2 = back_of_house::Appetizer::Salad;
}
```

Listagem 7-10: Designar um enum como público torna todas as suas variantes públicas.

Como tornamos o enum `Appetizer` público, podemos usar as variantes `Soup` e `Salad` em `eat_at_restaurant`.

Enums não são muito úteis a menos que suas variantes sejam públicas; seria irritante ter que anotar todas as variantes de enum com `pub` em todos os casos, então o padrão para variantes de enum é ser público. Structs são frequentemente úteis sem que seus campos sejam públicos, então os campos de struct seguem a regra geral de que tudo é privado por padrão, a menos que seja anotado com `pub`.

Há mais uma situação envolvendo `pub` que não cobrimos, e essa é nosso último recurso do sistema de módulos: a palavra-chave `use`. Cobriremos `use` por si só primeiro, e então mostraremos como combinar `pub` e `use`.
