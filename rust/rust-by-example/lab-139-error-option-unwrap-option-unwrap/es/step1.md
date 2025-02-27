# `Option` & `unwrap`

En el último ejemplo, mostramos que podemos causar el fallo del programa a voluntad. Le dijimos a nuestro programa que `panic`ara si bebíamos un limonada azucarada. Pero ¿y si esperamos _alguna_ bebida pero no recibimos ninguna? Ese caso sería igual de malo, por lo que debe ser manejado.

Podríamos probar esto contra la cadena nula (`""`), como lo hacemos con una limonada. Dado que estamos usando Rust, en lugar de eso, hagamos que el compilador señale los casos en los que no hay bebida.

Un `enum` llamado `Option<T>` en la librería `std` se utiliza cuando la ausencia es una posibilidad. Se manifiesta como una de dos "opciones":

- `Some(T)`: Se encontró un elemento de tipo `T`
- `None`: No se encontró ningún elemento

Estos casos pueden ser manejados explícitamente a través de `match` o implícitamente con `unwrap`. El manejo implícito devolverá el elemento interno o causará un `panic`.

Tenga en cuenta que es posible personalizar manualmente el `panic` con `expect`, pero `unwrap` de lo contrario nos deja con una salida menos significativa que el manejo explícito. En el siguiente ejemplo, el manejo explícito produce un resultado más controlado mientras que mantiene la opción de `panic` si se desea.

```rust
// El adulto ha visto todo, y puede manejar cualquier bebida bien.
// Todas las bebidas se manejan explícitamente usando `match`.
fn give_adult(drink: Option<&str>) {
    // Especifique un curso de acción para cada caso.
    match drink {
        Some("lemonade") => println!("Yuck! Too sugary."),
        Some(inner)   => println!("{}? How nice.", inner),
        None          => println!("No drink? Oh well."),
    }
}

// Otros `panic`arán antes de beber bebidas azucaradas.
// Todas las bebidas se manejan implícitamente usando `unwrap`.
fn drink(drink: Option<&str>) {
    // `unwrap` devuelve un `panic` cuando recibe un `None`.
    let inside = drink.unwrap();
    if inside == "lemonade" { panic!("AAAaaaaa!!!!"); }

    println!("I love {}s!!!!!", inside);
}

fn main() {
    let water  = Some("water");
    let lemonade = Some("lemonade");
    let void  = None;

    give_adult(water);
    give_adult(lemonade);
    give_adult(void);

    let coffee = Some("coffee");
    let nothing = None;

    drink(coffee);
    drink(nothing);
}
```
