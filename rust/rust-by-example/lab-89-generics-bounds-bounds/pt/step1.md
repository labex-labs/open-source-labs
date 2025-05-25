# Limites

Ao trabalhar com genéricos, os parâmetros de tipo frequentemente precisam de traits como _limites_ para especificar qual a funcionalidade que um tipo implementa. Por exemplo, o exemplo a seguir utiliza o trait `Display` para impressão, e portanto exige que `T` seja limitado por `Display`; ou seja, `T` _deve_ implementar `Display`.

```rust
// Define uma função `printer` que recebe um tipo genérico `T` que
// deve implementar o trait `Display`.
fn printer<T: Display>(t: T) {
    println!("{}", t);
}
```

A delimitação restringe o genérico a tipos que se ajustam aos limites. Ou seja:

```rust
struct S<T: Display>(T);

// Erro! `Vec<T>` não implementa `Display`. Esta
// especialização falhará.
let s = S(vec![1]);
```

Outro efeito da delimitação é que as instâncias genéricas podem aceder aos [métodos] dos traits especificados nos limites. Por exemplo:

```rust
// Um trait que implementa o marcador de impressão: `{:?}`.
use std::fmt::Debug;

trait HasArea {
    fn area(&self) -> f64;
}

impl HasArea for Rectangle {
    fn area(&self) -> f64 { self.length * self.height }
}

#[derive(Debug)]
struct Rectangle { length: f64, height: f64 }
#[allow(dead_code)]
struct Triangle  { length: f64, height: f64 }

// O genérico `T` deve implementar `Debug`. Independentemente
// do tipo, isto funcionará corretamente.
fn print_debug<T: Debug>(t: &T) {
    println!("{:?}", t);
}

// `T` deve implementar `HasArea`. Qualquer tipo que satisfaça
// o limite pode aceder à função `area` de `HasArea`.
fn area<T: HasArea>(t: &T) -> f64 { t.area() }

fn main() {
    let rectangle = Rectangle { length: 3.0, height: 4.0 };
    let _triangle = Triangle  { length: 3.0, height: 4.0 };

    print_debug(&rectangle);
    println!("Área: {}", area(&rectangle));

    //print_debug(&_triangle);
    //println!("Área: {}", area(&_triangle));
    // ^ TODO: Tente descomentar isto.
    // | Erro: Não implementa `Debug` nem `HasArea`.
}
```

Como nota adicional, as cláusulas `where` também podem ser usadas para aplicar limites em alguns casos para serem mais expressivas.
