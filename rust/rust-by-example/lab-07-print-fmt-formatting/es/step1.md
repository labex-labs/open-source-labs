# Formateo

Hemos visto que el formateo se especifica a través de una _cadena de formato_:

- `format!("{}", foo)` -> `"3735928559"`
- `format!("0x{:X}", foo)` -> `"0xDEADBEEF"`
- `format!("0o{:o}", foo)` -> `"0o33653337357"`

La misma variable (`foo`) se puede formatear de manera diferente dependiendo del _tipo de argumento_ utilizado: `X` vs `o` vs _no especificado_.

Esta funcionalidad de formateo se implementa a través de traits, y hay un trait para cada tipo de argumento. El trait de formateo más común es `Display`, que maneja los casos en los que el tipo de argumento no se especifica: `{}` por ejemplo.

```rust
use std::fmt::{self, Formatter, Display};

struct City {
    name: &'static str,
    // Latitud
    lat: f32,
    // Longitud
    lon: f32,
}

impl Display for City {
    // `f` es un buffer, y este método debe escribir la cadena formateada en él.
    fn fmt(&self, f: &mut Formatter) -> fmt::Result {
        let lat_c = if self.lat >= 0.0 { 'N' } else { 'S' };
        let lon_c = if self.lon >= 0.0 { 'E' } else { 'W' };

        // `write!` es como `format!`, pero escribirá la cadena formateada
        // en un buffer (el primer argumento).
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
        City { name: "Dublín", lat: 53.347778, lon: -6.259722 },
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
        // Cambie esto a usar {} una vez que haya agregado una implementación
        // para fmt::Display.
        println!("{:?}", color);
    }
}
```

Puede ver una lista completa de los traits de formateo y sus tipos de argumentos en la documentación de `std::fmt`.

## Actividad

Agregue una implementación del trait `fmt::Display` para la estructura `Color` anterior de modo que la salida se muestre como:

```plaintext
RGB (128, 255, 90) 0x80FF5A
RGB (0, 3, 254) 0x0003FE
RGB (0, 0, 0) 0x000000
```

Tres pistas si se atasca:

- La fórmula para calcular un color en el espacio de color RGB es: `RGB = (R*65536)+(G*256)+B, (cuando R es ROJO, G es VERDE y B es AZUL)`. Para más información, consulte el formato y el cálculo del color RGB.
- Es posible que tenga que listar cada color más de una vez.
- Puede rellenar con ceros hasta un ancho de 2 con `:0>2`.
