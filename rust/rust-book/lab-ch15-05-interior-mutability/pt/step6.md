# Permitindo Múltiplos Proprietários de Dados Mutáveis com Rc`<T>` e RefCell`<T>`

Uma forma comum de usar `RefCell<T>` é em combinação com `Rc<T>`. Lembre-se que `Rc<T>` permite que você tenha múltiplos proprietários de alguns dados, mas ele só dá acesso imutável a esses dados. Se você tiver um `Rc<T>` que contém um `RefCell<T>`, você pode obter um valor que pode ter múltiplos proprietários _e_ que você pode mutar!

Por exemplo, lembre-se do exemplo de lista cons na Listagem 15-18, onde usamos `Rc<T>` para permitir que múltiplas listas compartilhassem a propriedade de outra lista. Como `Rc<T>` contém apenas valores imutáveis, não podemos alterar nenhum dos valores na lista depois de criá-los. Vamos adicionar `RefCell<T>` por sua capacidade de alterar os valores nas listas. A Listagem 15-24 mostra que, usando um `RefCell<T>` na definição `Cons`, podemos modificar o valor armazenado em todas as listas.

Nome do arquivo: `src/main.rs`

```rust
#[derive(Debug)]
enum List {
    Cons(Rc<RefCell<i32>>, Rc<List>),
    Nil,
}

use crate::List::{Cons, Nil};
use std::cell::RefCell;
use std::rc::Rc;

fn main() {
  1 let value = Rc::new(RefCell::new(5));

  2 let a = Rc::new(Cons(Rc::clone(&value), Rc::new(Nil)));

    let b = Cons(Rc::new(RefCell::new(3)), Rc::clone(&a));
    let c = Cons(Rc::new(RefCell::new(4)), Rc::clone(&a));

  3 *value.borrow_mut() += 10;

    println!("a after = {:?}", a);
    println!("b after = {:?}", b);
    println!("c after = {:?}", c);
}
```

Listagem 15-24: Usando `Rc<RefCell<i32>>` para criar uma `List` que podemos mutar

Criamos um valor que é uma instância de `Rc<RefCell<i32>>` e o armazenamos em uma variável chamada `value` \[1] para que possamos acessá-lo diretamente mais tarde. Em seguida, criamos uma `List` em `a` com uma variante `Cons` que contém `value` \[2]. Precisamos clonar `value` para que tanto `a` quanto `value` tenham a propriedade do valor interno `5`, em vez de transferir a propriedade de `value` para `a` ou fazer com que `a` empreste de `value`.

Envolvemos a lista `a` em um `Rc<T>` para que, quando criarmos as listas `b` e `c`, ambas possam se referir a `a`, que é o que fizemos na Listagem 15-18.

Depois de criarmos as listas em `a`, `b` e `c`, queremos adicionar 10 ao valor em `value` \[3]. Fazemos isso chamando `borrow_mut` em `value`, que usa o recurso de desreferenciação automática que discutimos em "Onde está o operador ->?" para desreferenciar o `Rc<T>` para o valor interno `RefCell<T>`. O método `borrow_mut` retorna um ponteiro inteligente `RefMut<T>`, e usamos o operador de desreferenciação nele e alteramos o valor interno.

Quando imprimimos `a`, `b` e `c`, podemos ver que todos eles têm o valor modificado de `15` em vez de `5`:

    a after = Cons(RefCell { value: 15 }, Nil)
    b after = Cons(RefCell { value: 3 }, Cons(RefCell { value: 15 }, Nil))
    c after = Cons(RefCell { value: 4 }, Cons(RefCell { value: 15 }, Nil))

Essa técnica é muito legal! Usando `RefCell<T>`, temos um valor `List` externamente imutável. Mas podemos usar os métodos em `RefCell<T>` que fornecem acesso à sua mutabilidade interior para que possamos modificar nossos dados quando precisarmos. As verificações em tempo de execução das regras de empréstimo nos protegem de condições de corrida de dados, e às vezes vale a pena trocar um pouco de velocidade por essa flexibilidade em nossas estruturas de dados. Observe que `RefCell<T>` não funciona para código multithread! `Mutex<T>` é a versão thread-safe de `RefCell<T>`, e discutiremos `Mutex<T>` no Capítulo 16.
