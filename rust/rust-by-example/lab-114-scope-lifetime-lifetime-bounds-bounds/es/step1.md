# Límites

Al igual que los tipos genéricos pueden estar limitados, los períodos de vida (que son genéricos por sí mismos) también utilizan límites. El carácter `:` tiene un significado ligeramente diferente aquí, pero `+` es el mismo. Observe cómo se lee lo siguiente:

1.  `T: 'a`: _Todas_ las referencias en `T` deben tener un período de vida mayor que el período de vida `'a`.
2.  `T: Trait + 'a`: El tipo `T` debe implementar el rasgo `Trait` y _todas_ las referencias en `T` deben tener un período de vida mayor que `'a`.

El ejemplo siguiente muestra la sintaxis anterior en acción utilizada después de la palabra clave `where`:

```rust
use std::fmt::Debug; // Trait con el que se limita.

#[derive(Debug)]
struct Ref<'a, T: 'a>(&'a T);
// `Ref` contiene una referencia a un tipo genérico `T` que tiene
// un período de vida desconocido `'a`. `T` está limitado de modo que cualquier
// *referencia* en `T` debe tener un período de vida mayor que `'a`. Además, el período de vida
// de `Ref` no puede exceder `'a`.

// Una función genérica que imprime utilizando el rasgo `Debug`.
fn print<T>(t: T) where
    T: Debug {
    println!("`print`: t es {:?}", t);
}

// Aquí se toma una referencia a `T` donde `T` implementa
// `Debug` y todas las *referencias* en `T` tienen un período de vida mayor que `'a`. Además,
// `'a` debe tener un período de vida mayor que la función.
fn print_ref<'a, T>(t: &'a T) where
    T: Debug + 'a {
    println!("`print_ref`: t es {:?}", t);
}

fn main() {
    let x = 7;
    let ref_x = Ref(&x);

    print_ref(&ref_x);
    print(ref_x);
}
```
