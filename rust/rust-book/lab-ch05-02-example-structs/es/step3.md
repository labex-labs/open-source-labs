# Refactorización con Estructuras: Agregando Más Significado

Usamos estructuras para agregar significado al etiquetar los datos. Podemos transformar la tupla que estamos usando en una estructura con un nombre para todo y nombres para las partes, como se muestra en la Lista 5-10.

Nombre del archivo: `src/main.rs`

```rust
1 struct Rectangle {
  2 width: u32,
    height: u32,
}

fn main() {
  3 let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

    println!(
        "El área del rectángulo es {} píxeles cuadrados.",
        area(&rect1)
    );
}

4 fn area(rectangle: &Rectangle) -> u32 {
  5 rectangle.width * rectangle.height
}
```

Lista 5-10: Definiendo una estructura `Rectangle`

Aquí, hemos definido una estructura y la hemos nombrado `Rectangle` \[1\]. Dentro de las llaves, definimos los campos como `width` y `height`, ambos de tipo `u32` \[2\]. Luego, en `main`, creamos una instancia particular de `Rectangle` que tiene un ancho de `30` y un alto de `50` \[3\].

Nuestra función `area` ahora está definida con un parámetro, que hemos nombrado `rectangle`, cuyo tipo es un préstamo inmutable de una instancia de la estructura `Rectangle` \[4\]. Como se mencionó en el Capítulo 4, queremos prestar la estructura en lugar de tomar posesión de ella. De esta manera, `main` conserva su posesión y puede continuar usando `rect1`, que es la razón por la que usamos el `&` en la firma de la función y donde llamamos a la función.

La función `area` accede a los campos `width` y `height` de la instancia de `Rectangle` \[5\] (tenga en cuenta que acceder a los campos de una instancia de estructura prestada no mueve los valores de los campos, que es por lo que a menudo se ven préstamos de estructuras). Nuestra firma de función para `area` ahora dice exactamente lo que queremos decir: calcular el área de `Rectangle`, usando sus campos `width` y `height`. Esto transmite que el ancho y el alto están relacionados entre sí, y le da nombres descriptivos a los valores en lugar de usar los valores de índice de tupla de `0` y `1`. Esto es una victoria para la claridad.
