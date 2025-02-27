# Ámbito y Sombreado

Los enlaces de variables tienen un ámbito y están restringidos a existir dentro de un _bloque_. Un bloque es una colección de declaraciones encerradas entre llaves `{}`.

```rust
fn main() {
    // Este enlace existe dentro de la función main
    let long_lived_binding = 1;

    // Este es un bloque y tiene un ámbito más pequeño que la función main
    {
        // Este enlace solo existe dentro de este bloque
        let short_lived_binding = 2;

        println!("interno corto: {}", short_lived_binding);
    }
    // Fin del bloque

    // Error! `short_lived_binding` no existe en este ámbito
    println!("externo corto: {}", short_lived_binding);
    // FIXME ^ Comenta esta línea

    println!("externo largo: {}", long_lived_binding);
}
```

Además, el sombreado de variables está permitido.

```rust
fn main() {
    let shadowed_binding = 1;

    {
        println!("antes de ser sombreado: {}", shadowed_binding);

        // Este enlace *sombra* el externo
        let shadowed_binding = "abc";

        println!("sombreado en el bloque interno: {}", shadowed_binding);
    }
    println!("fuera del bloque interno: {}", shadowed_binding);

    // Este enlace *sombra* el enlace anterior
    let shadowed_binding = 2;
    println!("sombreado en el bloque externo: {}", shadowed_binding);
}
```
