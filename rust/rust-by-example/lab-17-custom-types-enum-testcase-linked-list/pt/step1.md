# Caso de Teste: Lista Encadeada

Uma forma comum de implementar uma lista encadeada é através de `enums`:

```rust
use crate::List::*;

enum List {
    // Cons: Estrutura de tupla que encapsula um elemento e um ponteiro para o próximo nó
    Cons(u32, Box<List>),
    // Nil: Um nó que indica o fim da lista encadeada
    Nil,
}

// Métodos podem ser anexados a um enum
impl List {
    // Criar uma lista vazia
    fn new() -> List {
        // `Nil` tem tipo `List`
        Nil
    }

    // Consumir uma lista e retornar a mesma lista com um novo elemento no início
    fn prepend(self, elem: u32) -> List {
        // `Cons` também tem tipo List
        Cons(elem, Box::new(self))
    }

    // Retornar o comprimento da lista
    fn len(&self) -> u32 {
        // `self` precisa ser correspondido, porque o comportamento deste método
        // depende da variante de `self`
        // `self` tem tipo `&List`, e `*self` tem tipo `List`, corresponder a um tipo concreto `T` é preferido a corresponder a uma referência `&T`
        // após Rust 2018 você pode usar self aqui e tail (sem ref) abaixo também,
        // rust inferirá &s e ref tail.
        // Veja https://doc.rust-lang.org/edition-guide/rust-2018/ownership-and-lifetimes/default-match-bindings.html
        match *self {
            // Não é possível assumir a propriedade do tail, porque `self` é emprestado;
            // em vez disso, pegue uma referência ao tail
            Cons(_, ref tail) => 1 + tail.len(),
            // Caso base: uma lista vazia tem comprimento zero
            Nil => 0
        }
    }

    // Retornar a representação da lista como uma string (alocada em heap)
    fn stringify(&self) -> String {
        match *self {
            Cons(head, ref tail) => {
                // `format!` é semelhante a `print!`, mas retorna uma string alocada em heap em vez de imprimir na consola
                format!("{}, {}", head, tail.stringify())
            },
            Nil => {
                format!("Nil")
            },
        }
    }
}

fn main() {
    // Criar uma lista encadeada vazia
    let mut list = List::new();

    // Adicionar alguns elementos
    list = list.prepend(1);
    list = list.prepend(2);
    list = list.prepend(3);

    // Mostrar o estado final da lista
    println!("A lista encadeada tem o comprimento: {}", list.len());
    println!("{}", list.stringify());
}
```
