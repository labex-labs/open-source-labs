# Desestructuración de enums

Hemos desestructurado enums en este libro (por ejemplo, Lista 6-5), pero aún no hemos discutido explícitamente que el patrón para desestructurar un enum corresponde a la forma en que se define los datos almacenados dentro del enum. Como ejemplo, en la Lista 18-15 usamos el enum `Message` de la Lista 6-2 y escribimos una expresión `match` con patrones que desestructurarán cada valor interno.

Nombre de archivo: `src/main.rs`

```rust
enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
    ChangeColor(i32, i32, i32),
}

fn main() {
  1 let msg = Message::ChangeColor(0, 160, 255);

    match msg {
      2 Message::Quit => {
            println!(
                "La variante Quit no tiene datos para desestructurar."
            );
        }
      3 Message::Move { x, y } => {
            println!(
                "Mover en la dirección x {x}, en la dirección y {y}"
            );
        }
      4 Message::Write(text) => {
            println!("Mensaje de texto: {text}");
        }
      5 Message::ChangeColor(r, g, b) => println!(
            "Cambiar color a rojo {r}, verde {g}, y azul {b}"
        ),
    }
}
```

Lista 18-15: Desestructuración de variantes de enum que contienen diferentes tipos de valores

Este código imprimirá `Cambiar color a rojo 0, verde 160, y azul 255`. Intenta cambiar el valor de `msg` \[1\] para ver el código de los otros brazos en ejecución.

Para las variantes de enum sin ningún dato, como `Message::Quit` \[2\], no podemos desestructurar el valor más allá. Solo podemos coincidir con el valor literal `Message::Quit`, y no hay variables en ese patrón.

Para las variantes de enum similares a structs, como `Message::Move` \[3\], podemos usar un patrón similar al patrón que especificamos para coincidir con structs. Después del nombre de la variante, ponemos llaves y luego listamos los campos con variables para que sepamos descomponer los fragmentos para usarlos en el código de este brazo. Aquí usamos la forma abreviada como lo hicimos en la Lista 18-13.

Para las variantes de enum similares a tuplas, como `Message::Write` que contiene una tupla con un elemento \[4\] y `Message::ChangeColor` que contiene una tupla con tres elementos \[5\], el patrón es similar al patrón que especificamos para coincidir con tuplas. El número de variables en el patrón debe coincidir con el número de elementos en la variante con la que estamos coincidiendo.
