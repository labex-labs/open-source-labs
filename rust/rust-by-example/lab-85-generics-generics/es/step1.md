# Genéricos

Los _genéricos_ son el tema de generalizar tipos y funcionalidades a casos más amplios. Esto es extremadamente útil para reducir la duplicación de código de muchas maneras, pero puede requerir una sintaxis bastante compleja. Es decir, ser genérico requiere tener gran cuidado al especificar sobre qué tipos un tipo genérico se considera realmente válido. El uso más simple y común de los genéricos es para los parámetros de tipo.

Un parámetro de tipo se especifica como genérico mediante el uso de corchetes angulares y letras mayúsculas, y típicamente se representa como `<T>`. En Rust, "genérico" también describe cualquier cosa que acepte uno o más parámetros de tipo genérico `<T>`. Cualquier tipo especificado como parámetro de tipo genérico es genérico, y todo lo demás es concrete (no genérico).

Por ejemplo, definiendo una _función genérica_ llamada `foo` que toma un argumento `T` de cualquier tipo:

```rust
fn foo<T>(arg: T) {... }
```

Debido a que `T` se ha especificado como un parámetro de tipo genérico usando `<T>`, se considera genérico cuando se usa aquí como `(arg: T)`. Esto es así incluso si `T` se ha definido previamente como un `struct`.

Este ejemplo muestra algunos de los aspectos de la sintaxis en acción:

```rust
// Un tipo concrete `A`.
struct A;

// Al definir el tipo `Single`, el primer uso de `A` no está precedido por `<A>`.
// Por lo tanto, `Single` es un tipo concrete, y `A` se define como arriba.
struct Single(A);
//            ^ Aquí está el primer uso de `Single` del tipo `A`.

// Aquí, `<T>` precede al primer uso de `T`, por lo que `SingleGen` es un tipo genérico.
// Debido a que el parámetro de tipo `T` es genérico, podría ser cualquier cosa, incluyendo
// el tipo concrete `A` definido arriba.
struct SingleGen<T>(T);

fn main() {
    // `Single` es concrete y toma explícitamente `A`.
    let _s = Single(A);

    // Crea una variable `_char` del tipo `SingleGen<char>`
    // y dale el valor `SingleGen('a')`.
    // Aquí, `SingleGen` tiene un parámetro de tipo especificado explícitamente.
    let _char: SingleGen<char> = SingleGen('a');

    // `SingleGen` también puede tener un parámetro de tipo especificado implícitamente:
    let _t    = SingleGen(A); // Usa `A` definido arriba.
    let _i32  = SingleGen(6); // Usa `i32`.
    let _char = SingleGen('a'); // Usa `char`.
}
```
