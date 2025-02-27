# Box, pila y montón

Todos los valores en Rust se asignan en pila por defecto. Los valores se pueden "empaquetar" (asignar en el montón) creando un `Box<T>`. Una caja es un puntero inteligente a un valor de tipo `T` asignado en el montón. Cuando una caja sale del ámbito, se llama a su destructor, el objeto interno se destruye y se libera la memoria en el montón.

Los valores empaquetados se pueden desreferenciar utilizando el operador `*`; esto quita un nivel de indirección.

```rust
use std::mem;

#[allow(dead_code)]
#[derive(Debug, Clone, Copy)]
struct Point {
    x: f64,
    y: f64,
}

// Un Rectángulo se puede especificar por donde están sus esquinas superior izquierda e inferior derecha
// en el espacio
#[allow(dead_code)]
struct Rectangle {
    top_left: Point,
    bottom_right: Point,
}

fn origin() -> Point {
    Point { x: 0.0, y: 0.0 }
}

fn boxed_origin() -> Box<Point> {
    // Asigna este punto en el montón y devuelve un puntero a él
    Box::new(Point { x: 0.0, y: 0.0 })
}

fn main() {
    // (todas las anotaciones de tipo son superfluas)
    // Variables asignadas en pila
    let point: Point = origin();
    let rectangle: Rectangle = Rectangle {
        top_left: origin(),
        bottom_right: Point { x: 3.0, y: -4.0 }
    };

    // Rectángulo asignado en el montón
    let boxed_rectangle: Box<Rectangle> = Box::new(Rectangle {
        top_left: origin(),
        bottom_right: Point { x: 3.0, y: -4.0 },
    });

    // La salida de funciones se puede empaquetar
    let boxed_point: Box<Point> = Box::new(origin());

    // Doble indirección
    let box_in_a_box: Box<Box<Point>> = Box::new(boxed_origin());

    println!("Point ocupa {} bytes en la pila",
             mem::size_of_val(&point));
    println!("Rectangle ocupa {} bytes en la pila",
             mem::size_of_val(&rectangle));

    // Tamaño de la caja == tamaño del puntero
    println!("Boxed point ocupa {} bytes en la pila",
             mem::size_of_val(&boxed_point));
    println!("Boxed rectangle ocupa {} bytes en la pila",
             mem::size_of_val(&boxed_rectangle));
    println!("Boxed box ocupa {} bytes en la pila",
             mem::size_of_val(&box_in_a_box));

    // Copia los datos contenidos en `boxed_point` en `unboxed_point`
    let unboxed_point: Point = *boxed_point;
    println!("Unboxed point ocupa {} bytes en la pila",
             mem::size_of_val(&unboxed_point));
}
```
