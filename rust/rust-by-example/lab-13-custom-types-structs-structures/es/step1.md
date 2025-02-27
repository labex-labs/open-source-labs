# Estructuras

Hay tres tipos de estructuras ("structs") que se pueden crear utilizando la palabra clave `struct`:

- Structs de tupla, que son, básicamente, tuplas con nombre.
- Los structs clásicos de C
- Structs unitarios, que no tienen campos y son útiles para genéricos.

```rust
// Un atributo para ocultar advertencias de código no utilizado.
#![allow(dead_code)]

#[derive(Debug)]
struct Person {
    name: String,
    age: u8,
}

// Un struct unitario
struct Unit;

// Un struct de tupla
struct Pair(i32, f32);

// Un struct con dos campos
struct Point {
    x: f32,
    y: f32,
}

// Los structs se pueden reutilizar como campos de otro struct
struct Rectangle {
    // Un rectángulo se puede especificar por donde están las esquinas superior izquierda e inferior derecha
    // en el espacio.
    top_left: Point,
    bottom_right: Point,
}

fn main() {
    // Crear struct con sintaxis abreviada de inicialización de campos
    let name = String::from("Peter");
    let age = 27;
    let peter = Person { name, age };

    // Imprimir struct de depuración
    println!("{:?}", peter);

    // Instanciar un `Point`
    let point: Point = Point { x: 10.3, y: 0.4 };

    // Acceder a los campos del punto
    println!("coordenadas del punto: ({}, {})", point.x, point.y);

    // Hacer un nuevo punto utilizando la sintaxis de actualización de struct para utilizar los campos de nuestro
    // otro punto
    let bottom_right = Point { x: 5.2,..point };

    // `bottom_right.y` será el mismo que `point.y` porque utilizamos ese campo
    // de `point`
    println!("segundo punto: ({}, {})", bottom_right.x, bottom_right.y);

    // Desestructurar el punto utilizando una vinculación `let`
    let Point { x: left_edge, y: top_edge } = point;

    let _rectangle = Rectangle {
        // La instanciación de struct es una expresión también
        top_left: Point { x: left_edge, y: top_edge },
        bottom_right: bottom_right,
    };

    // Instanciar un struct unitario
    let _unit = Unit;

    // Instanciar un struct de tupla
    let pair = Pair(1, 0.1);

    // Acceder a los campos de un struct de tupla
    println!("pair contiene {:?} y {:?}", pair.0, pair.1);

    // Desestructurar un struct de tupla
    let Pair(integer, decimal) = pair;

    println!("pair contiene {:?} y {:?}", integer, decimal);
}
```

## Actividad

1.  Agregar una función `rect_area` que calcule el área de un `Rectangle` (intenta utilizar desestructuración anidada).
2.  Agregar una función `square` que tome un `Point` y un `f32` como argumentos, y devuelva un `Rectangle` con su esquina superior izquierda en el punto, y un ancho y altura correspondientes al `f32`.
