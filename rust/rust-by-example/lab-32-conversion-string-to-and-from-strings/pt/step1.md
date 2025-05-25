# Conversão para e de Strings

## Conversão para String

Converter qualquer tipo para uma `String` é tão simples quanto implementar o traço [`ToString`] para o tipo. Em vez de fazê-lo diretamente, você deve implementar o traço `fmt::Display`, que automaticamente fornece [`ToString`] e também permite a impressão do tipo, como discutido na seção sobre `print!`.

```rust
use std::fmt;

struct Circle {
    radius: i32
}

impl fmt::Display for Circle {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "Círculo de raio {}", self.radius)
    }
}

fn main() {
    let circle = Circle { radius: 6 };
    println!("{}", circle.to_string());
}
```

## Analisando uma String

Um dos tipos mais comuns para converter uma string em um número. A abordagem idiomática para isso é usar a função [`parse`] e, ou, organizar a inferência de tipo, ou especificar o tipo para análise usando a sintaxe 'turbofish'. Ambas as alternativas são mostradas no exemplo a seguir.

Isso converterá a string no tipo especificado, desde que o traço [`FromStr`] seja implementado para esse tipo. Isso é implementado para numerosos tipos dentro da biblioteca padrão. Para obter essa funcionalidade em um tipo definido pelo usuário, basta implementar o traço [`FromStr`] para esse tipo.

```rust
fn main() {
    let parsed: i32 = "5".parse().unwrap();
    let turbo_parsed = "10".parse::<i32>().unwrap();

    let sum = parsed + turbo_parsed;
    println!("Soma: {:?}", sum);
}
```
