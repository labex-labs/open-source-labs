# Enums (Enumerações)

A palavra-chave `enum` permite a criação de um tipo que pode ser um de alguns variantes diferentes. Qualquer variante que seja válida como um `struct` também é válida em um `enum`.

```rust
// Crie um `enum` para classificar um evento web. Note como ambos
// nomes e informações de tipo juntos especificam a variante:
// `PageLoad != PageUnload` e `KeyPress(char) != Paste(String)`.
// Cada um é diferente e independente.
enum WebEvent {
    // Uma variante `enum` pode ser `unit-like`,
    PageLoad,
    PageUnload,
    // como tuple structs,
    KeyPress(char),
    Paste(String),
    // ou estruturas c-like.
    Click { x: i64, y: i64 },
}

// Uma função que recebe um enum `WebEvent` como argumento e
// não retorna nada.
fn inspect(event: WebEvent) {
    match event {
        WebEvent::PageLoad => println!("página carregada"),
        WebEvent::PageUnload => println!("página descarregada"),
        // Destructure `c` de dentro da variante `enum`.
        WebEvent::KeyPress(c) => println!("pressionado '{}'.", c),
        WebEvent::Paste(s) => println!("colado \"{}\".", s),
        // Destructure `Click` em `x` e `y`.
        WebEvent::Click { x, y } => {
            println!("clicado em x={}, y={}.", x, y);
        },
    }
}

fn main() {
    let pressed = WebEvent::KeyPress('x');
    // `to_owned()` cria uma `String` própria a partir de uma fatia de string.
    let pasted  = WebEvent::Paste("my text".to_owned());
    let click   = WebEvent::Click { x: 20, y: 80 };
    let load    = WebEvent::PageLoad;
    let unload  = WebEvent::PageUnload;

    inspect(pressed);
    inspect(pasted);
    inspect(click);
    inspect(load);
    inspect(unload);
}
```

## Type aliases (Alias de Tipos)

Se você usar um type alias, pode referenciar cada variante de enum através de seu alias. Isso pode ser útil se o nome do enum for muito longo ou muito genérico, e você quiser renomeá-lo.

```rust
enum VeryVerboseEnumOfThingsToDoWithNumbers {
    Add,
    Subtract,
}

// Cria um type alias
type Operations = VeryVerboseEnumOfThingsToDoWithNumbers;

fn main() {
    // Podemos referenciar cada variante através de seu alias, não seu nome longo e inconveniente.
    let x = Operations::Add;
}
```

O lugar mais comum onde você verá isso é em blocos `impl` usando o alias `Self`.

```rust
enum VeryVerboseEnumOfThingsToDoWithNumbers {
    Add,
    Subtract,
}

impl VeryVerboseEnumOfThingsToDoWithNumbers {
    fn run(&self, x: i32, y: i32) -> i32 {
        match self {
            Self::Add => x + y,
            Self::Subtract => x - y,
        }
    }
}
```

Para saber mais sobre enums e type aliases, você pode ler o relatório de estabilização de quando esse recurso foi estabilizado no Rust.
