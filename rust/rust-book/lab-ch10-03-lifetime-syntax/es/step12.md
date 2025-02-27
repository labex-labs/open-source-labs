# Parámetros de tipo genéricos, límites de trato y lifetimes juntos

Echemos un vistazo breve a la sintaxis de especificar parámetros de tipo genéricos, límites de trato y lifetimes todos en una sola función.

```rust
use std::fmt::Display;

fn longest_with_an_announcement<'a, T>(
    x: &'a str,
    y: &'a str,
    ann: T,
) -> &'a str
where
    T: Display,
{
    println!("Announcement! {ann}");
    if x.len() > y.len() {
        x
    } else {
        y
    }
}
```

Esta es la función `longest` de la Lista 10-21 que devuelve la cadena más larga de dos trozos de cadena. Pero ahora tiene un parámetro extra llamado `ann` del tipo genérico `T`, que puede ser rellenado por cualquier tipo que implemente el trato `Display` como se especifica en la cláusula `where`. Este parámetro extra se imprimirá usando `{}`, por lo que el límite de trato `Display` es necesario. Debido a que los lifetimes son un tipo de genérico, las declaraciones del parámetro de lifetime `'a` y del parámetro de tipo genérico `T` van en la misma lista dentro de los corchetes angulares después del nombre de la función.
