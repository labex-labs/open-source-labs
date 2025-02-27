# Desestructuración de structs y enums anidados

Hasta ahora, todos nuestros ejemplos han sido para coincidir con structs o enums a un nivel de profundidad, pero la coincidencia también puede funcionar en elementos anidados. Por ejemplo, podemos refactorizar el código de la Lista 18-15 para admitir colores RGB y HSV en el mensaje `ChangeColor`, como se muestra en la Lista 18-16.

Nombre de archivo: `src/main.rs`

```rust
enum Color {
    Rgb(i32, i32, i32),
    Hsv(i32, i32, i32),
}

enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
    ChangeColor(Color),
}

fn main() {
    let msg = Message::ChangeColor(Color::Hsv(0, 160, 255));

    match msg {
        Message::ChangeColor(Color::Rgb(r, g, b)) => println!(
            "Cambiar color a rojo {r}, verde {g}, y azul {b}"
        ),
        Message::ChangeColor(Color::Hsv(h, s, v)) => println!(
            "Cambiar color a matiz {h}, saturación {s}, valor {v}"
        ),
        _ => (),
    }
}
```

Lista 18-16: Coincidencia en enums anidados

El patrón del primer brazo en la expresión `match` coincide con una variante de enum `Message::ChangeColor` que contiene una variante `Color::Rgb`; luego el patrón se enlaza a los tres valores `i32` internos. El patrón del segundo brazo también coincide con una variante de enum `Message::ChangeColor`, pero el enum interno coincide con `Color::Hsv` en lugar. Podemos especificar estas condiciones complejas en una sola expresión `match`, aunque se involucren dos enums.
