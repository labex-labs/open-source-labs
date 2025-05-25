# Retornando Traits com `dyn`

O compilador Rust precisa saber quanto espaço o tipo de retorno de cada função requer. Isso significa que todas as suas funções precisam retornar um tipo concreto. Diferente de outras linguagens, se você tem uma trait como `Animal`, você não pode escrever uma função que retorna `Animal`, porque suas diferentes implementações precisarão de diferentes quantidades de memória.

No entanto, existe uma solução fácil. Em vez de retornar um objeto trait diretamente, nossas funções retornam um `Box` que _contém_ algum `Animal`. Um `box` é apenas uma referência a alguma memória no heap. Como uma referência tem um tamanho estaticamente conhecido, e o compilador pode garantir que ela aponta para um `Animal` alocado no heap, podemos retornar uma trait da nossa função!

Rust tenta ser o mais explícito possível sempre que aloca memória no heap. Então, se sua função retorna um ponteiro-para-trait-no-heap dessa forma, você precisa escrever o tipo de retorno com a palavra-chave `dyn`, por exemplo, `Box<dyn Animal>`.

```rust
struct Sheep {}
struct Cow {}

trait Animal {
    // Instance method signature
    fn noise(&self) -> &'static str;
}

// Implement the `Animal` trait for `Sheep`.
impl Animal for Sheep {
    fn noise(&self) -> &'static str {
        "baaaaah!"
    }
}

// Implement the `Animal` trait for `Cow`.
impl Animal for Cow {
    fn noise(&self) -> &'static str {
        "moooooo!"
    }
}

// Returns some struct that implements Animal, but we don't know which one at compile time.
fn random_animal(random_number: f64) -> Box<dyn Animal> {
    if random_number < 0.5 {
        Box::new(Sheep {})
    } else {
        Box::new(Cow {})
    }
}

fn main() {
    let random_number = 0.234;
    let animal = random_animal(random_number);
    println!("You've randomly chosen an animal, and it says {}", animal.noise());
}
```
