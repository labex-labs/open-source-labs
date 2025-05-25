# Usando `Box`<T>`{=html} para Obter um Tipo Recursivo com um Tamanho Conhecido

Como o Rust não consegue descobrir quanto espaço alocar para tipos definidos recursivamente, o compilador fornece um erro com esta sugestão útil:

    help: insert some indirection (e.g., a `Box`, `Rc`, or `&`) to make `List`
    representable
      |
    2 |     Cons(i32, Box<List>),
      |               ++++    +

Nesta sugestão, _indireção_ (indirection) significa que, em vez de armazenar um valor diretamente, devemos alterar a estrutura de dados para armazenar o valor indiretamente, armazenando um ponteiro para o valor em vez disso.

Como um `Box<T>` é um ponteiro, o Rust sempre sabe quanto espaço um `Box<T>` precisa: o tamanho de um ponteiro não muda com base na quantidade de dados que ele está apontando. Isso significa que podemos colocar um `Box<T>` dentro da variante `Cons` em vez de outro valor `List` diretamente. O `Box<T>` apontará para o próximo valor `List` que estará no heap em vez de dentro da variante `Cons`. Conceitualmente, ainda temos uma lista, criada com listas contendo outras listas, mas esta implementação agora é mais parecida com a colocação dos itens um ao lado do outro em vez de dentro um do outro.

Podemos alterar a definição do enum `List` na Listagem 15-2 e o uso do `List` na Listagem 15-3 para o código na Listagem 15-5, que compilará.

Nome do arquivo: `src/main.rs`

```rust
enum List {
    Cons(i32, Box<List>),
    Nil,
}

use crate::List::{Cons, Nil};

fn main() {
    let list = Cons(
        1,
        Box::new(Cons(
            2,
            Box::new(Cons(
                3,
                Box::new(Nil)
            ))
        ))
    );
}
```

Listagem 15-5: Definição de `List` que usa `Box<T>` para ter um tamanho conhecido

A variante `Cons` precisa do tamanho de um `i32` mais o espaço para armazenar os dados do ponteiro da box. A variante `Nil` não armazena nenhum valor, então precisa de menos espaço do que a variante `Cons`. Agora sabemos que qualquer valor `List` ocupará o tamanho de um `i32` mais o tamanho dos dados do ponteiro de uma box. Ao usar uma box, quebramos a cadeia recursiva infinita, para que o compilador possa descobrir o tamanho que precisa para armazenar um valor `List`. A Figura 15-2 mostra como a variante `Cons` se parece agora.

Figura 15-2: Uma `List` que não tem tamanho infinito, porque `Cons` contém um `Box`

As boxes fornecem apenas a indireção e a alocação no heap; elas não têm nenhuma outra capacidade especial, como as que veremos com os outros tipos de ponteiros inteligentes. Elas também não têm a sobrecarga de desempenho que essas capacidades especiais incorrem, então podem ser úteis em casos como a lista cons, onde a indireção é o único recurso que precisamos. Veremos mais casos de uso para boxes no Capítulo 17.

O tipo `Box<T>` é um ponteiro inteligente porque implementa a trait `Deref`, que permite que valores `Box<T>` sejam tratados como referências. Quando um valor `Box<T>` sai do escopo, os dados do heap para os quais a box está apontando também são limpos devido à implementação da trait `Drop`. Essas duas traits serão ainda mais importantes para a funcionalidade fornecida pelos outros tipos de ponteiros inteligentes que discutiremos no restante deste capítulo. Vamos explorar essas duas traits com mais detalhes.
