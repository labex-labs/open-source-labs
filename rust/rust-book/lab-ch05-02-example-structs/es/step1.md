# Un Programa de Ejemplo que Utiliza Estructuras

Para entender cuándo podríamos querer utilizar estructuras, escribamos un programa que calcule el área de un rectángulo. Empezaremos utilizando variables individuales y luego refactorizaremos el programa hasta que lo estemos haciendo con estructuras en lugar de eso.

Vamos a crear un nuevo proyecto binario con Cargo llamado _rectángulos_ que tomará el ancho y el alto de un rectángulo especificado en píxeles y calculará el área del rectángulo. La Lista 5-8 muestra un programa corto con una forma de hacer exactamente eso en el `src/main.rs` de nuestro proyecto.

Nombre del archivo: `src/main.rs`

```rust
fn main() {
    let width1 = 30;
    let height1 = 50;

    println!(
        "El área del rectángulo es {} píxeles cuadrados.",
        area(width1, height1)
    );
}

fn area(width: u32, height: u32) -> u32 {
    width * height
}
```

Lista 5-8: Calculando el área de un rectángulo especificado por variables separadas de ancho y alto

Ahora, ejecuta este programa usando `cargo run`:

```rust
El área del rectángulo es 1500 píxeles cuadrados.
```

Este código logra calcular el área del rectángulo llamando a la función `area` con cada dimensión, pero podemos hacer más para que este código sea claro y legible.

El problema con este código es evidente en la firma de `area`:

```rust
fn area(width: u32, height: u32) -> u32 {
```

La función `area` está supuesta para calcular el área de un rectángulo, pero la función que escribimos tiene dos parámetros y no está claro en ningún lugar de nuestro programa que los parámetros estén relacionados. Sería más legible y más manejable agrupar el ancho y el alto juntos. Ya hemos discutido una forma en que podríamos hacerlo en "El Tipo Tupla": usando tuplas.
