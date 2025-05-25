# Criando um Ciclo de Referência

Vamos analisar como um ciclo de referência pode acontecer e como evitá-lo, começando com a definição do enum `List` e um método `tail` na Listagem 15-25.

Nome do arquivo: `src/main.rs`

```rust
use crate::List::{Cons, Nil};
use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug)]
enum List {
  1 Cons(i32, RefCell<Rc<List>>),
    Nil,
}

impl List {
  2 fn tail(&self) -> Option<&RefCell<Rc<List>>> {
        match self {
            Cons(_, item) => Some(item),
            Nil => None,
        }
    }
}
```

Listagem 15-25: Uma definição de lista cons que contém um `RefCell<T>` para que possamos modificar o que uma variante `Cons` está referenciando

Estamos usando outra variação da definição `List` da Listagem 15-5. O segundo elemento na variante `Cons` agora é `RefCell<Rc<List>>` \[1], o que significa que, em vez de ter a capacidade de modificar o valor `i32` como fizemos na Listagem 15-24, queremos modificar o valor `List` que uma variante `Cons` está apontando. Também estamos adicionando um método `tail` \[2] para facilitar o acesso ao segundo item se tivermos uma variante `Cons`.

Na Listagem 15-26, estamos adicionando uma função `main` que usa as definições na Listagem 15-25. Este código cria uma lista em `a` e uma lista em `b` que aponta para a lista em `a`. Em seguida, ele modifica a lista em `a` para apontar para `b`, criando um ciclo de referência. Existem instruções `println!` ao longo do caminho para mostrar quais são as contagens de referência em vários pontos neste processo.

Nome do arquivo: `src/main.rs`

```rust
fn main() {
  1 let a = Rc::new(Cons(5, RefCell::new(Rc::new(Nil))));

    println!("a initial rc count = {}", Rc::strong_count(&a));
    println!("a next item = {:?}", a.tail());

  2 let b = Rc::new(Cons(10, RefCell::new(Rc::clone(&a))));

    println!(
        "a rc count after b creation = {}",
        Rc::strong_count(&a)
    );
    println!("b initial rc count = {}", Rc::strong_count(&b));
    println!("b next item = {:?}", b.tail());

  3 if let Some(link) = a.tail() {
      4 *link.borrow_mut() = Rc::clone(&b);
    }

    println!(
        "b rc count after changing a = {}",
        Rc::strong_count(&b)
    );
    println!(
        "a rc count after changing a = {}",
        Rc::strong_count(&a)
    );

    // Uncomment the next line to see that we have a cycle;
    // it will overflow the stack
    // println!("a next item = {:?}", a.tail());
}
```

Listagem 15-26: Criando um ciclo de referência de dois valores `List` apontando um para o outro

Criamos uma instância `Rc<List>` contendo um valor `List` na variável `a` com uma lista inicial de `5, Nil` \[1]. Em seguida, criamos uma instância `Rc<List>` contendo outro valor `List` na variável `b` que contém o valor `10` e aponta para a lista em `a` \[2].

Modificamos `a` para que aponte para `b` em vez de `Nil`, criando um ciclo. Fazemos isso usando o método `tail` para obter uma referência ao `RefCell<Rc<List>>` em `a`, que colocamos na variável `link` \[3]. Em seguida, usamos o método `borrow_mut` no `RefCell<Rc<List>>` para alterar o valor interno de um `Rc<List>` que contém um valor `Nil` para o `Rc<List>` em `b` \[4].

Quando executamos este código, mantendo o último `println!` comentado por enquanto, obteremos esta saída:

    a initial rc count = 1
    a next item = Some(RefCell { value: Nil })
    a rc count after b creation = 2
    b initial rc count = 1
    b next item = Some(RefCell { value: Cons(5, RefCell { value: Nil }) })
    b rc count after changing a = 2
    a rc count after changing a = 2

A contagem de referência das instâncias `Rc<List>` em `a` e `b` é 2 depois que alteramos a lista em `a` para apontar para `b`. No final de `main`, o Rust descarta a variável `b`, o que diminui a contagem de referência da instância `b` `Rc<List>` de 2 para 1. A memória que `Rc<List>` tem no heap não será descartada neste ponto porque sua contagem de referência é 1, não 0. Então o Rust descarta `a`, o que também diminui a contagem de referência da instância `a` `Rc<List>` de 2 para 1. A memória desta instância também não pode ser descartada, porque a outra instância `Rc<List>` ainda se refere a ela. A memória alocada para a lista permanecerá não coletada para sempre. Para visualizar este ciclo de referência, criamos um diagrama na Figura 15-4.

Figura 15-4: Um ciclo de referência de listas `a` e `b` apontando um para o outro

Se você descomentar o último `println!` e executar o programa, o Rust tentará imprimir este ciclo com `a` apontando para `b` apontando para `a` e assim por diante até que ele transborde a pilha.

Comparado a um programa do mundo real, as consequências de criar um ciclo de referência neste exemplo não são muito graves: logo após criarmos o ciclo de referência, o programa termina. No entanto, se um programa mais complexo alocasse muita memória em um ciclo e a mantivesse por um longo tempo, o programa usaria mais memória do que o necessário e poderia sobrecarregar o sistema, fazendo com que ele ficasse sem memória disponível.

Criar ciclos de referência não é fácil, mas também não é impossível. Se você tiver valores `RefCell<T>` que contenham valores `Rc<T>` ou combinações aninhadas semelhantes de tipos com mutabilidade interna e contagem de referência, você deve garantir que não crie ciclos; você não pode confiar no Rust para detectá-los. Criar um ciclo de referência seria um bug lógico em seu programa que você deve usar testes automatizados, revisões de código e outras práticas de desenvolvimento de software para minimizar.

Outra solução para evitar ciclos de referência é reorganizar suas estruturas de dados para que algumas referências expressem propriedade e algumas referências não. Como resultado, você pode ter ciclos compostos por algumas relações de propriedade e algumas relações de não propriedade, e apenas as relações de propriedade afetam se um valor pode ou não ser descartado. Na Listagem 15-25, sempre queremos que as variantes `Cons` possuam sua lista, então reorganizar a estrutura de dados não é possível. Vamos analisar um exemplo usando gráficos compostos por nós pai e nós filho para ver quando as relações de não propriedade são uma maneira apropriada de evitar ciclos de referência.
