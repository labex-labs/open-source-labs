# Adicionando uma Referência de um Filho para seu Pai

Para que o nó filho esteja ciente de seu pai, precisamos adicionar um campo `parent` à nossa definição de struct `Node`. O problema está em decidir qual deve ser o tipo de `parent`. Sabemos que ele não pode conter um `Rc<T>` porque isso criaria um ciclo de referência com `leaf.parent` apontando para `branch` e `branch.children` apontando para `leaf`, o que faria com que seus valores `strong_count` nunca fossem 0.

Pensando nas relações de outra forma, um nó pai deve possuir seus filhos: se um nó pai for descartado, seus nós filhos também devem ser descartados. No entanto, um filho não deve possuir seu pai: se descartarmos um nó filho, o pai ainda deve existir. Este é um caso para referências fracas!

Então, em vez de `Rc<T>`, faremos com que o tipo de `parent` use `Weak<T>`, especificamente um `RefCell<Weak<Node>>`. Agora, nossa definição de struct `Node` se parece com isto:

Nome do arquivo: `src/main.rs`

```rust
use std::cell::RefCell;
use std::rc::{Rc, Weak};

#[derive(Debug)]
struct Node {
    value: i32,
    parent: RefCell<Weak<Node>>,
    children: RefCell<Vec<Rc<Node>>>,
}
```

Um nó poderá se referir ao seu nó pai, mas não possui seu pai. Na Listagem 15-28, atualizamos `main` para usar esta nova definição, de modo que o nó `leaf` terá uma maneira de se referir ao seu pai, `branch`.

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let leaf = Rc::new(Node {
        value: 3,
      1 parent: RefCell::new(Weak::new()),
        children: RefCell::new(vec![]),
    });

  2 println!(
        "leaf parent = {:?}",
        leaf.parent.borrow().upgrade()
    );

    let branch = Rc::new(Node {
        value: 5,
      3 parent: RefCell::new(Weak::new()),
        children: RefCell::new(vec![Rc::clone(&leaf)]),
    });

  4 *leaf.parent.borrow_mut() = Rc::downgrade(&branch);

  5 println!(
        "leaf parent = {:?}",
        leaf.parent.borrow().upgrade()
    );
}
```

Listagem 15-28: Um nó `leaf` com uma referência fraca ao seu nó pai, `branch`

Criar o nó `leaf` se parece com a Listagem 15-27, com a exceção do campo `parent`: `leaf` começa sem um pai, então criamos uma nova instância de referência `Weak<Node>` vazia \[1].

Neste ponto, quando tentamos obter uma referência ao pai de `leaf` usando o método `upgrade`, obtemos um valor `None`. Vemos isso na saída da primeira instrução `println!` \[2]:

```rust
leaf parent = None
```

Quando criamos o nó `branch`, ele também terá uma nova referência `Weak<Node>` no campo `parent` \[3] porque `branch` não tem um nó pai. Ainda temos `leaf` como um dos filhos de `branch`. Depois de termos a instância `Node` em `branch`, podemos modificar `leaf` para dar a ele uma referência `Weak<Node>` ao seu pai \[4]. Usamos o método `borrow_mut` no `RefCell<Weak<Node>>` no campo `parent` de `leaf`, e então usamos a função `Rc::downgrade` para criar uma referência `Weak<Node>` para `branch` a partir do `Rc<Node>` em `branch`.

Quando imprimimos o pai de `leaf` novamente \[5], desta vez obteremos uma variante `Some` contendo `branch`: agora `leaf` pode acessar seu pai! Quando imprimimos `leaf`, também evitamos o ciclo que eventualmente terminou em um estouro de pilha como tínhamos na Listagem 15-26; as referências `Weak<Node>` são impressas como `(Weak)`:

    leaf parent = Some(Node { value: 5, parent: RefCell { value: (Weak) },
    children: RefCell { value: [Node { value: 3, parent: RefCell { value: (Weak) },
    children: RefCell { value: [] } }] } })

A falta de saída infinita indica que este código não criou um ciclo de referência. Também podemos dizer isso olhando para os valores que obtemos ao chamar `Rc::strong_count` e `Rc::weak_count`.
