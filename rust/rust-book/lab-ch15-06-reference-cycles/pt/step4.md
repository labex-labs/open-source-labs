# Criando uma Estrutura de Dados de Árvore: Um Nó com Nós Filhos

Para começar, construiremos uma árvore com nós que conhecem seus nós filhos. Criaremos uma struct chamada `Node` que contém seu próprio valor `i32`, bem como referências aos seus valores `Node` filhos:

Nome do arquivo: `src/main.rs`

```rust
use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug)]
struct Node {
    value: i32,
    children: RefCell<Vec<Rc<Node>>>,
}
```

Queremos que um `Node` possua seus filhos, e queremos compartilhar essa propriedade com variáveis para que possamos acessar cada `Node` na árvore diretamente. Para fazer isso, definimos os itens `Vec<T>` para serem valores do tipo `Rc<Node>`. Também queremos modificar quais nós são filhos de outro nó, então temos um `RefCell<T>` em `children` em torno do `Vec<Rc<Node>>`.

Em seguida, usaremos nossa definição de struct e criaremos uma instância `Node` chamada `leaf` com o valor `3` e sem filhos, e outra instância chamada `branch` com o valor `5` e `leaf` como um de seus filhos, conforme mostrado na Listagem 15-27.

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let leaf = Rc::new(Node {
        value: 3,
        children: RefCell::new(vec![]),
    });

    let branch = Rc::new(Node {
        value: 5,
        children: RefCell::new(vec![Rc::clone(&leaf)]),
    });
}
```

Listagem 15-27: Criando um nó `leaf` sem filhos e um nó `branch` com `leaf` como um de seus filhos

Clonamos o `Rc<Node>` em `leaf` e o armazenamos em `branch`, o que significa que o `Node` em `leaf` agora tem dois proprietários: `leaf` e `branch`. Podemos ir de `branch` para `leaf` através de `branch.children`, mas não há como ir de `leaf` para `branch`. A razão é que `leaf` não tem referência a `branch` e não sabe que eles estão relacionados. Queremos que `leaf` saiba que `branch` é seu pai. Faremos isso a seguir.
