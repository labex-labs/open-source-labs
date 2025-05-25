# Tipos Associados

O uso de "Tipos Associados" melhora a legibilidade geral do código, movendo tipos internos localmente para um tratado como tipos de _saída_. A sintaxe para a definição do `tratado` é a seguinte:

```rust
// `A` e `B` são definidos no tratado através da palavra-chave `type`.
// (Nota: `type` neste contexto é diferente de `type` quando usado para
// aliases).
trait Contains {
    type A;
    type B;

    // Sintaxe atualizada para se referir a esses novos tipos genericamente.
    fn contains(&self, _: &Self::A, _: &Self::B) -> bool;
}
```

Note que as funções que utilizam o `tratado` `Contains` não precisam mais expressar `A` ou `B` em absoluto:

```rust
// Sem usar tipos associados
fn difference<A, B, C>(container: &C) -> i32 where
    C: Contains<A, B> { ... }

// Usando tipos associados
fn difference<C: Contains>(container: &C) -> i32 { ... }
```

Vamos reescrever o exemplo da seção anterior usando tipos associados:

```rust
struct Container(i32, i32);

// Um tratado que verifica se 2 itens estão armazenados dentro do contêiner.
// Também recupera o primeiro ou o último valor.
trait Contains {
    // Defina tipos genéricos aqui que os métodos serão capazes de utilizar.
    type A;
    type B;

    fn contains(&self, _: &Self::A, _: &Self::B) -> bool;
    fn first(&self) -> i32;
    fn last(&self) -> i32;
}

impl Contains for Container {
    // Especifique quais tipos `A` e `B` são. Se o tipo de `entrada`
    // for `Container(i32, i32)`, os tipos de `saída` são determinados
    // como `i32` e `i32`.
    type A = i32;
    type B = i32;

    // `&Self::A` e `&Self::B` também são válidos aqui.
    fn contains(&self, number_1: &i32, number_2: &i32) -> bool {
        (&self.0 == number_1) && (&self.1 == number_2)
    }
    // Pegar o primeiro número.
    fn first(&self) -> i32 { self.0 }

    // Pegar o último número.
    fn last(&self) -> i32 { self.1 }
}

fn difference<C: Contains>(container: &C) -> i32 {
    container.last() - container.first()
}

fn main() {
    let number_1 = 3;
    let number_2 = 10;

    let container = Container(number_1, number_2);

    println!("O contêiner contém {} e {}: {}",
        &number_1, &number_2,
        container.contains(&number_1, &number_2));
    println!("Primeiro número: {}", container.first());
    println!("Último número: {}", container.last());

    println!("A diferença é: {}", difference(&container));
}
```
