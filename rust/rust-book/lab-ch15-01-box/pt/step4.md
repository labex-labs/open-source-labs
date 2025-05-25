# Mais Informações Sobre a Lista Cons

Uma _lista cons_ (cons list) é uma estrutura de dados que vem da linguagem de programação Lisp e seus dialetos, é composta por pares aninhados e é a versão Lisp de uma lista encadeada. Seu nome vem da função `cons` (abreviação de _função construtora_) em Lisp, que constrói um novo par a partir de seus dois argumentos. Ao chamar `cons` em um par consistindo em um valor e outro par, podemos construir listas cons compostas por pares recursivos.

Por exemplo, aqui está uma representação em pseudocódigo de uma lista cons contendo a lista `1, 2, 3` com cada par entre parênteses:

```rust
(1, (2, (3, Nil)))
```

Cada item em uma lista cons contém dois elementos: o valor do item atual e o próximo item. O último item da lista contém apenas um valor chamado `Nil` sem um próximo item. Uma lista cons é produzida chamando recursivamente a função `cons`. O nome canônico para denotar o caso base da recursão é `Nil`. Observe que isso não é o mesmo que o conceito "null" ou "nil" no Capítulo 6, que é um valor inválido ou ausente.

A lista cons não é uma estrutura de dados comumente usada em Rust. Na maioria das vezes, quando você tem uma lista de itens em Rust, `Vec<T>` é uma escolha melhor para usar. Outros tipos de dados recursivos mais complexos _são_ úteis em várias situações, mas, começando com a lista cons neste capítulo, podemos explorar como as boxes nos permitem definir um tipo de dado recursivo sem muita distração.

A Listagem 15-2 contém uma definição de enum para uma lista cons. Observe que este código ainda não compilará porque o tipo `List` não tem um tamanho conhecido, o que demonstraremos.

Nome do arquivo: `src/main.rs`

```rust
enum List {
    Cons(i32, List),
    Nil,
}
```

Listagem 15-2: A primeira tentativa de definir um enum para representar uma estrutura de dados de lista cons de valores `i32`

> Nota: Estamos implementando uma lista cons que contém apenas valores `i32` para os propósitos deste exemplo. Poderíamos tê-la implementado usando genéricos, como discutimos no Capítulo 10, para definir um tipo de lista cons que pudesse armazenar valores de qualquer tipo.

Usar o tipo `List` para armazenar a lista `1, 2, 3` seria semelhante ao código na Listagem 15-3.

Nome do arquivo: `src/main.rs`

```rust
--snip--

use crate::List::{Cons, Nil};

fn main() {
    let list = Cons(1, Cons(2, Cons(3, Nil)));
}
```

Listagem 15-3: Usando o enum `List` para armazenar a lista `1, 2, 3`

O primeiro valor `Cons` contém `1` e outro valor `List`. Este valor `List` é outro valor `Cons` que contém `2` e outro valor `List`. Este valor `List` é mais um valor `Cons` que contém `3` e um valor `List`, que é finalmente `Nil`, a variante não recursiva que sinaliza o fim da lista.

Se tentarmos compilar o código na Listagem 15-3, obteremos o erro mostrado na Listagem 15-4.

```bash
error[E0072]: recursive type `List` has infinite size
 --> src/main.rs:1:1
  |
1 | enum List {
  | ^^^^^^^^^ recursive type has infinite size
2 |     Cons(i32, List),
  |               ---- recursive without indirection
  |
help: insert some indirection (e.g., a `Box`, `Rc`, or `&`) to make `List`
representable
  |
2 |     Cons(i32, Box<List>),
  |               ++++    +
```

Listagem 15-4: O erro que obtemos ao tentar definir um enum recursivo

O erro mostra que este tipo "tem tamanho infinito". A razão é que definimos `List` com uma variante que é recursiva: ela contém outro valor de si mesma diretamente. Como resultado, o Rust não consegue descobrir quanto espaço precisa para armazenar um valor `List`. Vamos detalhar por que obtemos esse erro. Primeiro, veremos como o Rust decide quanto espaço precisa para armazenar um valor de um tipo não recursivo.
