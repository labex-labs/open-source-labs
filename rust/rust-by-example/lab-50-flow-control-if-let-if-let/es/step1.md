# if let

Para algunos casos de uso, cuando se coinciden enums, `match` es incómodo. Por ejemplo:

```rust
// Hace `optional` del tipo `Option<i32>`
let optional = Some(7);

match optional {
    Some(i) => {
        println!("This is a really long string and `{:?}`", i);
        // ^ Se necesitaron 2 sangrías solo para poder desestructurar
        // `i` de la opción.
    },
    _ => {},
    // ^ Requerido porque `match` es exhaustivo. ¿No parece
    // un espacio desperdiciado?
};
```

`if let` es más limpio para este caso de uso y además permite especificar varias opciones de error:

```rust
fn main() {
    // Todos tienen el tipo `Option<i32>`
    let number = Some(7);
    let letter: Option<i32> = None;
    let emoticon: Option<i32> = None;

    // La construcción `if let` se lee: "si `let` desestructura `number` en
    // `Some(i)`, evalúe el bloque (`{}`).
    if let Some(i) = number {
        println!("Matched {:?}!", i);
    }

    // Si necesita especificar un error, use un else:
    if let Some(i) = letter {
        println!("Matched {:?}!", i);
    } else {
        // La desestructuración falló. Cambie al caso de error.
        println!("Didn't match a number. Let's go with a letter!");
    }

    // Proporcione una condición de error alterada.
    let i_like_letters = false;

    if let Some(i) = emoticon {
        println!("Matched {:?}!", i);
    // La desestructuración falló. Evalúe una condición `else if` para ver si
    // se debe tomar la rama de error alternativa:
    } else if i_like_letters {
        println!("Didn't match a number. Let's go with a letter!");
    } else {
        // La condición se evaluó como falsa. Esta rama es la predeterminada:
        println!("I don't like letters. Let's go with an emoticon :)!");
    }
}
```

Del mismo modo, `if let` se puede utilizar para coincidir con cualquier valor de enum:

```rust
// Nuestro enum de ejemplo
enum Foo {
    Bar,
    Baz,
    Qux(u32)
}

fn main() {
    // Cree variables de ejemplo
    let a = Foo::Bar;
    let b = Foo::Baz;
    let c = Foo::Qux(100);

    // La variable a coincide con Foo::Bar
    if let Foo::Bar = a {
        println!("a is foobar");
    }

    // La variable b no coincide con Foo::Bar
    // Entonces esto no imprimirá nada
    if let Foo::Bar = b {
        println!("b is foobar");
    }

    // La variable c coincide con Foo::Qux que tiene un valor
    // Similar a Some() en el ejemplo anterior
    if let Foo::Qux(value) = c {
        println!("c is {}", value);
    }

    // El enlace también funciona con `if let`
    if let Foo::Qux(value @ 100) = c {
        println!("c is one hundred");
    }
}
```

Otro beneficio es que `if let` nos permite coincidir con variantes de enum no parametrizadas. Esto es cierto incluso en casos donde el enum no implementa o deriva `PartialEq`. En tales casos `if Foo::Bar == a` fallará en la compilación, porque no se pueden igualar instancias del enum, sin embargo `if let` seguirá funcionando.

¿Te gustaría un reto? Corrija el siguiente ejemplo para usar `if let`:

```rust
// Este enum intencionalmente ni implementa ni deriva PartialEq.
// Es por eso que comparar Foo::Bar == a falla a continuación.
enum Foo {Bar}

fn main() {
    let a = Foo::Bar;

    // La variable a coincide con Foo::Bar
    if Foo::Bar == a {
    // ^-- esto causa un error de compilación. Use `if let` en su lugar.
        println!("a is foobar");
    }
}
```
