# Depuración

Todos los tipos que deseen utilizar las características de formato `std::fmt` requieren una implementación para ser imprimibles. Las implementaciones automáticas solo se proporcionan para tipos como los de la biblioteca `std`. Todos los demás _deben_ ser implementados manualmente de alguna manera.

La característica `fmt::Debug` hace esto muy sencillo. _Todos_ los tipos pueden `derivar` (crear automáticamente) la implementación de `fmt::Debug`. Esto no es cierto para `fmt::Display`, que debe ser implementado manualmente.

```rust
// Esta estructura no se puede imprimir con `fmt::Display` ni
// con `fmt::Debug`.
struct UnPrintable(i32);

// El atributo `derive` crea automáticamente la implementación
// necesaria para hacer que esta `struct` sea imprimible con `fmt::Debug`.
#[derive(Debug)]
struct DebugPrintable(i32);
```

Todos los tipos de la biblioteca `std` también son automáticamente imprimibles con `{:?}`:

```rust
// Derive la implementación de `fmt::Debug` para `Structure`. `Structure`
// es una estructura que contiene un solo `i32`.
#[derive(Debug)]
struct Structure(i32);

// Coloca una `Structure` dentro de la estructura `Deep`. Haz que sea imprimible
// también.
#[derive(Debug)]
struct Deep(Structure);

fn main() {
    // Imprimir con `{:?}` es similar a con `{}`.
    println!("{:?} meses en un año.", 12);
    println!("{1:?} {0:?} es el {actor:?} nombre.",
             "Slater",
             "Christian",
             actor="actor's");

    // `Structure` es imprimible!
    println!("Ahora {:?} se imprimirá!", Structure(3));

    // El problema con `derive` es que no hay control sobre cómo
    // se ven los resultados. ¿Qué pasa si quiero que esto solo muestre un `7`?
    println!("Ahora {:?} se imprimirá!", Deep(Structure(7)));
}
```

Entonces `fmt::Debug` definitivamente hace que esto sea imprimible pero sacrifica algo de elegancia. Rust también proporciona "impresión bonita" con `{:#?}`.

```rust
#[derive(Debug)]
struct Person<'a> {
    name: &'a str,
    age: u8
}

fn main() {
    let name = "Peter";
    let age = 27;
    let peter = Person { name, age };

    // Impresión bonita
    println!("{:#?}", peter);
}
```

Uno puede implementar manualmente `fmt::Display` para controlar la representación.
