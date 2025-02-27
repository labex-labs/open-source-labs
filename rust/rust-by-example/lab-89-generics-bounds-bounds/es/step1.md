# Límites

Al trabajar con genéricos, los parámetros de tipo a menudo deben usar traits como _límites_ para especificar qué funcionalidad implementa un tipo. Por ejemplo, el siguiente ejemplo utiliza el trait `Display` para imprimir y por lo tanto requiere que `T` esté limitado por `Display`; es decir, `T` _debe_ implementar `Display`.

```rust
// Define una función `printer` que toma un tipo genérico `T` que
// debe implementar el trait `Display`.
fn printer<T: Display>(t: T) {
    println!("{}", t);
}
```

Establecer límites restringe el genérico a tipos que cumplen con los límites. Es decir:

```rust
struct S<T: Display>(T);

// Error! `Vec<T>` no implementa `Display`. Esta
// especialización fallará.
let s = S(vec![1]);
```

Otro efecto de establecer límites es que se permite a las instancias genéricas acceder a los \[métodos\] de los traits especificados en los límites. Por ejemplo:

```rust
// Un trait que implementa el marcador de impresión: `{:?}`.
use std::fmt::Debug;

trait HasArea {
    fn area(&self) -> f64;
}

impl HasArea for Rectangle {
    fn area(&self) -> f64 { self.length * self.height }
}

#[derive(Debug)]
struct Rectangle { length: f64, height: f64 }
#[allow(dead_code)]
struct Triangle  { length: f64, height: f64 }

// El genérico `T` debe implementar `Debug`. Independientemente
// del tipo, esto funcionará correctamente.
fn print_debug<T: Debug>(t: &T) {
    println!("{:?}", t);
}

// `T` debe implementar `HasArea`. Cualquier tipo que cumpla
// con el límite puede acceder a la función `area` de `HasArea`.
fn area<T: HasArea>(t: &T) -> f64 { t.area() }

fn main() {
    let rectangle = Rectangle { length: 3.0, height: 4.0 };
    let _triangle = Triangle  { length: 3.0, height: 4.0 };

    print_debug(&rectangle);
    println!("Area: {}", area(&rectangle));

    //print_debug(&_triangle);
    //println!("Area: {}", area(&_triangle));
    // ^ TODO: Intentar descomentar estos.
    // | Error: No implementa ni `Debug` ni `HasArea`.
}
```

Como nota adicional, en algunos casos también se pueden usar cláusulas `where` para aplicar límites y ser más expresivos.
