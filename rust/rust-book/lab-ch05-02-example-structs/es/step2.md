# Refactorización con Tuplas

La Lista 5-9 muestra otra versión de nuestro programa que utiliza tuplas.

Nombre del archivo: `src/main.rs`

```rust
fn main() {
    let rect1 = (30, 50);

    println!(
        "El área del rectángulo es {} píxeles cuadrados.",
      1 area(rect1)
    );
}

fn area(dimensions: (u32, u32)) -> u32 {
  2 dimensions.0 * dimensions.1
}
```

Lista 5-9: Especificando el ancho y el alto del rectángulo con una tupla

De un modo, este programa es mejor. Las tuplas nos permiten agregar un poco de estructura y ahora estamos pasando solo un argumento \[1\]. Pero de otro modo, esta versión es menos clara: las tuplas no nombran sus elementos, por lo que tenemos que acceder por índice a las partes de la tupla \[2\], lo que hace que nuestro cálculo sea menos obvio.

Intercambiar el ancho y el alto no importaría para el cálculo del área, pero si queremos dibujar el rectángulo en la pantalla, sí importaría! Tendríamos que recordar que `width` es el índice de la tupla `0` y `height` es el índice de la tupla `1`. Esto sería aún más difícil de entender y recordar para alguien más si tuviera que usar nuestro código. Debido a que no hemos transmitido el significado de nuestros datos en nuestro código, ahora es más fácil introducir errores.
