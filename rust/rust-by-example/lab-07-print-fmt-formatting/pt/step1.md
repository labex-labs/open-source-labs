# Formatação

Vimos que a formatação é especificada por meio de uma _format string_:

- `format!("{}", foo)` -\> `"3735928559"`
- `format!("0x{:X}", foo)` -\> `"0xDEADBEEF"`
- `format!("0o{:o}", foo)` -\> `"0o33653337357"`

A mesma variável (`foo`) pode ser formatada de maneira diferente, dependendo do _tipo de argumento_ usado: `X` vs `o` vs _não especificado_.

Esta funcionalidade de formatação é implementada por meio de _traits_, e há uma _trait_ para cada tipo de argumento. A _trait_ de formatação mais comum é `Display`, que lida com casos em que o tipo de argumento é deixado não especificado: `{}` por exemplo.

```rust
use std::fmt::{self, Formatter, Display};

struct City {
    name: &'static str,
    // Latitude
    lat: f32,
    // Longitude
    lon: f32,
}

impl Display for City {
    // `f` is a buffer, and this method must write the formatted string into it.
    fn fmt(&self, f: &mut Formatter) -> fmt::Result {
        let lat_c = if self.lat >= 0.0 { 'N' } else { 'S' };
        let lon_c = if self.lon >= 0.0 { 'E' } else { 'W' };

        // `write!` is like `format!`, but it will write the formatted string
        // into a buffer (the first argument).
        write!(f, "{}: {:.3}°{} {:.3}°{}",
               self.name, self.lat.abs(), lat_c, self.lon.abs(), lon_c)
    }
}

#[derive(Debug)]
struct Color {
    red: u8,
    green: u8,
    blue: u8,
}

fn main() {
    for city in [
        City { name: "Dublin", lat: 53.347778, lon: -6.259722 },
        City { name: "Oslo", lat: 59.95, lon: 10.75 },
        City { name: "Vancouver", lat: 49.25, lon: -123.1 },
    ] {
        println!("{}", city);
    }
    for color in [
        Color { red: 128, green: 255, blue: 90 },
        Color { red: 0, green: 3, blue: 254 },
        Color { red: 0, green: 0, blue: 0 },
    ] {
        // Switch this to use {} once you've added an implementation
        // for fmt::Display.
        println!("{:?}", color);
    }
}
```

Você pode ver uma lista completa de _traits_ de formatação e seus tipos de argumento na documentação `std::fmt`.

## Atividade

Adicione uma implementação da _trait_ `fmt::Display` para a _struct_ `Color` acima, para que a saída seja exibida como:

```plaintext
RGB (128, 255, 90) 0x80FF5A
RGB (0, 3, 254) 0x0003FE
RGB (0, 0, 0) 0x000000
```

Três dicas se você ficar preso:

- A fórmula para calcular uma cor no espaço de cores RGB é: `RGB = (R*65536)+(G*256)+B , (when R is RED, G is GREEN and B is BLUE)`. Para mais informações, consulte RGB color format & calculation.
- Você pode precisar listar cada cor mais de uma vez.
- Você pode preencher com zeros para uma largura de 2 com `:0>2`.
