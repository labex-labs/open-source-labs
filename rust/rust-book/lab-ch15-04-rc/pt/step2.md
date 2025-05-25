# Usando Rc`<T>`{=html} para Compartilhar Dados

Vamos retornar ao nosso exemplo de lista cons em Listing 15-5. Lembre-se de que o definimos usando `Box<T>`. Desta vez, criaremos duas listas que compartilham a propriedade de uma terceira lista. Conceitualmente, isso se assemelha à Figura 15-3.

Figura 15-3: Duas listas, `b` e `c`, compartilhando a propriedade de uma terceira lista, `a`

Criaremos a lista `a` que contém `5` e depois `10`. Em seguida, faremos mais duas listas: `b` que começa com `3` e `c` que começa com `4`. Ambas as listas `b` e `c` continuarão para a primeira lista `a` contendo `5` e `10`. Em outras palavras, ambas as listas compartilharão a primeira lista contendo `5` e `10`.

Tentar implementar este cenário usando nossa definição de `List` com `Box<T>` não funcionará, como mostrado no Listing 15-17.

Nome do arquivo: `src/main.rs`

```rust
enum List {
    Cons(i32, Box<List>),
    Nil,
}

use crate::List::{Cons, Nil};

fn main() {
    let a = Cons(5, Box::new(Cons(10, Box::new(Nil))));
  1 let b = Cons(3, Box::new(a));
  2 let c = Cons(4, Box::new(a));
}
```

Listing 15-17: Demonstrando que não podemos ter duas listas usando `Box<T>` que tentam compartilhar a propriedade de uma terceira lista

Quando compilamos este código, obtemos este erro:

```bash
error[E0382]: use of moved value: `a`
  --> src/main.rs:11:30
   |
9  |     let a = Cons(5, Box::new(Cons(10, Box::new(Nil))));
   |         - move occurs because `a` has type `List`, which
does not implement the `Copy` trait
10 |     let b = Cons(3, Box::new(a));
   |                              - value moved here
11 |     let c = Cons(4, Box::new(a));
   |                              ^ value used here after move
```

As variantes `Cons` possuem os dados que contêm, então, quando criamos a lista `b` \[1\], `a` é movido para `b` e `b` possui `a`. Então, quando tentamos usar `a` novamente ao criar `c` \[2\], não podemos porque `a` foi movido.

Poderíamos alterar a definição de `Cons` para conter referências em vez disso, mas então teríamos que especificar parâmetros de tempo de vida. Ao especificar parâmetros de tempo de vida, estaríamos especificando que cada elemento na lista viverá pelo menos tanto tempo quanto a lista inteira. Este é o caso dos elementos e listas no Listing 15-17, mas não em todos os cenários.

Em vez disso, mudaremos nossa definição de `List` para usar `Rc<T>` em vez de `Box<T>`, como mostrado no Listing 15-18. Cada variante `Cons` agora conterá um valor e um `Rc<T>` apontando para um `List`. Quando criamos `b`, em vez de assumir a propriedade de `a`, clonaremos o `Rc<List>` que `a` está contendo, aumentando assim o número de referências de um para dois e permitindo que `a` e `b` compartilhem a propriedade dos dados nesse `Rc<List>`. Também clonaremos `a` ao criar `c`, aumentando o número de referências de dois para três. Toda vez que chamamos `Rc::clone`, a contagem de referência para os dados dentro do `Rc<List>` aumentará, e os dados não serão limpos a menos que haja zero referências a eles.

Nome do arquivo: `src/main.rs`

```rust
enum List {
    Cons(i32, Rc<List>),
    Nil,
}

use crate::List::{Cons, Nil};
1 use std::rc::Rc;

fn main() {
  2 let a = Rc::new(Cons(5, Rc::new(Cons(10, Rc::new(Nil)))));
  3 let b = Cons(3, Rc::clone(&a));
  4 let c = Cons(4, Rc::clone(&a));
}
```

Listing 15-18: Uma definição de `List` que usa `Rc<T>`

Precisamos adicionar uma instrução `use` para trazer `Rc<T>` para o escopo \[1] porque não está no preâmbulo. Em `main`, criamos a lista contendo `5` e `10` e a armazenamos em um novo `Rc<List>` em `a` \[2]. Então, quando criamos `b` \[3] e `c` \[4], chamamos a função `Rc::clone` e passamos uma referência ao `Rc<List>` em `a` como um argumento.

Poderíamos ter chamado `a.clone()` em vez de `Rc::clone(&a)`, mas a convenção do Rust é usar `Rc::clone` neste caso. A implementação de `Rc::clone` não faz uma cópia profunda de todos os dados como a maioria das implementações de `clone` dos tipos fazem. A chamada para `Rc::clone` apenas incrementa a contagem de referência, o que não leva muito tempo. Cópias profundas de dados podem levar muito tempo. Ao usar `Rc::clone` para contagem de referência, podemos distinguir visualmente entre os tipos de clones de cópia profunda e os tipos de clones que aumentam a contagem de referência. Ao procurar problemas de desempenho no código, só precisamos considerar os clones de cópia profunda e podemos desconsiderar as chamadas para `Rc::clone`.
