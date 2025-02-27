# Un valor entero con \_

Hemos usado el guion bajo como un patrón comodín que coincidirá con cualquier valor pero no se enlazará al valor. Esto es especialmente útil como el último brazo en una expresión `match`, pero también podemos usarlo en cualquier patrón, incluyendo parámetros de función, como se muestra en la Lista 18-17.

Nombre de archivo: `src/main.rs`

```rust
fn foo(_: i32, y: i32) {
    println!("Este código solo usa el parámetro y: {y}");
}

fn main() {
    foo(3, 4);
}
```

Lista 18-17: Usando `_` en una firma de función

Este código ignorará completamente el valor `3` pasado como primer argumento y imprimirá `Este código solo usa el parámetro y: 4`.

En la mayoría de los casos, cuando ya no necesitas un parámetro de función en particular, cambiarías la firma para que no incluya el parámetro no utilizado. Ignorar un parámetro de función puede ser especialmente útil en casos donde, por ejemplo, estás implementando un trato y necesitas una cierta firma de tipo, pero el cuerpo de la función en tu implementación no necesita uno de los parámetros. Entonces evitas recibir una advertencia del compilador sobre parámetros de función no utilizados, como ocurriría si usaras un nombre en lugar de eso.
