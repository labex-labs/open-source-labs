# Visualizando Mudanças em `strong_count` e `weak_count`

Vamos analisar como os valores `strong_count` e `weak_count` das instâncias `Rc<Node>` mudam, criando um novo escopo interno e movendo a criação de `branch` para dentro desse escopo. Ao fazer isso, podemos ver o que acontece quando `branch` é criado e, em seguida, descartado quando sai do escopo. As modificações são mostradas na Listagem 15-29.

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let leaf = Rc::new(Node {
        value: 3,
        parent: RefCell::new(Weak::new()),
        children: RefCell::new(vec![]),
    });

  1 println!(
        "leaf strong = {}, weak = {}",
        Rc::strong_count(&leaf),
        Rc::weak_count(&leaf),
    );

  2 {
        let branch = Rc::new(Node {
            value: 5,
            parent: RefCell::new(Weak::new()),
            children: RefCell::new(vec![Rc::clone(&leaf)]),
        });

        *leaf.parent.borrow_mut() = Rc::downgrade(&branch);

      3 println!(
            "branch strong = {}, weak = {}",
            Rc::strong_count(&branch),
            Rc::weak_count(&branch),
        );

      4 println!(
            "leaf strong = {}, weak = {}",
            Rc::strong_count(&leaf),
            Rc::weak_count(&leaf),
        );
  5 }

  6 println!(
        "leaf parent = {:?}",
        leaf.parent.borrow().upgrade()
    );
  7 println!(
        "leaf strong = {}, weak = {}",
        Rc::strong_count(&leaf),
        Rc::weak_count(&leaf),
    );
}
```

Listagem 15-29: Criando `branch` em um escopo interno e examinando as contagens de referência fortes e fracas

Depois que `leaf` é criado, seu `Rc<Node>` tem uma contagem forte de 1 e uma contagem fraca de 0 \[1]. No escopo interno \[2], criamos `branch` e o associamos a `leaf`, momento em que, quando imprimimos as contagens \[3], o `Rc<Node>` em `branch` terá uma contagem forte de 1 e uma contagem fraca de 1 (para `leaf.parent` apontando para `branch` com um `Weak<Node>`). Quando imprimimos as contagens em `leaf` \[4], veremos que ele terá uma contagem forte de 2 porque `branch` agora tem um clone do `Rc<Node>` de `leaf` armazenado em `branch.children`, mas ainda terá uma contagem fraca de 0.

Quando o escopo interno termina \[5], `branch` sai do escopo e a contagem forte do `Rc<Node>` diminui para 0, então seu `Node` é descartado. A contagem fraca de 1 de `leaf.parent` não tem influência sobre se o `Node` é descartado ou não, então não temos nenhum vazamento de memória!

Se tentarmos acessar o pai de `leaf` após o final do escopo, obteremos `None` novamente \[6]. No final do programa \[7], o `Rc<Node>` em `leaf` tem uma contagem forte de 1 e uma contagem fraca de 0 porque a variável `leaf` agora é a única referência ao `Rc<Node>` novamente.

Toda a lógica que gerencia as contagens e a queda de valores é integrada em `Rc<T>` e `Weak<T>` e suas implementações do trait `Drop`. Ao especificar que a relação de um filho para seu pai deve ser uma referência `Weak<T>` na definição de `Node`, você pode ter nós pais apontando para nós filhos e vice-versa sem criar um ciclo de referência e vazamentos de memória.
