# Visibilidad de los structs

Los structs tienen un nivel adicional de visibilidad en sus campos. La visibilidad por defecto es privada y se puede anular con el modificador `pub`. Esta visibilidad solo es importante cuando se accede a un struct desde fuera del módulo donde se define y tiene como objetivo ocultar información (encapsulación).

```rust
mod my {
    // Un struct público con un campo público de tipo genérico `T`
    pub struct OpenBox<T> {
        pub contents: T,
    }

    // Un struct público con un campo privado de tipo genérico `T`
    pub struct ClosedBox<T> {
        contents: T,
    }

    impl<T> ClosedBox<T> {
        // Un método constructor público
        pub fn new(contents: T) -> ClosedBox<T> {
            ClosedBox {
                contents: contents,
            }
        }
    }
}

fn main() {
    // Los structs públicos con campos públicos se pueden construir como de costumbre
    let open_box = my::OpenBox { contents: "información pública" };

    // y sus campos se pueden acceder normalmente.
    println!("La caja abierta contiene: {}", open_box.contents);

    // Los structs públicos con campos privados no se pueden construir usando los nombres de campo.
    // Error! `ClosedBox` tiene campos privados
    //let closed_box = my::ClosedBox { contents: "información clasificada" };
    // TODO ^ Intenta descomentar esta línea

    // Sin embargo, los structs con campos privados se pueden crear usando
    // constructores públicos
    let _closed_box = my::ClosedBox::new("información clasificada");

    // y los campos privados de un struct público no se pueden acceder.
    // Error! El campo `contents` es privado
    //println!("La caja cerrada contiene: {}", _closed_box.contents);
    // TODO ^ Intenta descomentar esta línea
}
```
