# Bucles `for`

## `for` y rango

La construcción `for in` se puede utilizar para iterar a través de un `Iterator`. Una de las maneras más fáciles de crear un iterador es usar la notación de rango `a..b`. Esto produce valores desde `a` (inclusivo) hasta `b` (exclusivo) en pasos de uno.

Escribamos FizzBuzz usando `for` en lugar de `while`.

```rust
fn main() {
    // `n` tomará los valores: 1, 2,..., 100 en cada iteración
    for n in 1..101 {
        if n % 15 == 0 {
            println!("fizzbuzz");
        } else if n % 3 == 0 {
            println!("fizz");
        } else if n % 5 == 0 {
            println!("buzz");
        } else {
            println!("{}", n);
        }
    }
}
```

Alternativamente, `a..=b` se puede utilizar para un rango que es inclusivo en ambos extremos. Lo anterior se puede escribir como:

```rust
fn main() {
    // `n` tomará los valores: 1, 2,..., 100 en cada iteración
    for n in 1..=100 {
        if n % 15 == 0 {
            println!("fizzbuzz");
        } else if n % 3 == 0 {
            println!("fizz");
        } else if n % 5 == 0 {
            println!("buzz");
        } else {
            println!("{}", n);
        }
    }
}
```

## `for` e iteradores

La construcción `for in` es capaz de interactuar con un `Iterator` de varias maneras. Como se discutió en la sección sobre el trato `Iterator`, por defecto el bucle `for` aplicará la función `into_iter` a la colección. Sin embargo, esta no es la única forma de convertir colecciones en iteradores.

`into_iter`, `iter` e `iter_mut` todos manejan la conversión de una colección en un iterador de diferentes maneras, al proporcionar diferentes vistas sobre los datos dentro de la misma.

- `iter` - Esto presta prestado cada elemento de la colección en cada iteración. De esta manera, la colección queda intacta y disponible para reutilizarse después del bucle.

```rust
fn main() {
    let names = vec!["Bob", "Frank", "Ferris"];

    for name in names.iter() {
        match name {
            &"Ferris" => println!("There is a rustacean among us!"),
            // TODO ^ Intenta eliminar el & y coincidir solo con "Ferris"
            _ => println!("Hello {}", name),
        }
    }

    println!("names: {:?}", names);
}
```

- `into_iter` - Esto consume la colección para que en cada iteración se proporcione exactamente los datos. Una vez que la colección ha sido consumida, ya no está disponible para reutilizarse ya que ha sido'movida' dentro del bucle.

```rust
fn main() {
    let names = vec!["Bob", "Frank", "Ferris"];

    for name in names.into_iter() {
        match name {
            "Ferris" => println!("There is a rustacean among us!"),
            _ => println!("Hello {}", name),
        }
    }

    println!("names: {:?}", names);
    // FIXME ^ Comenta esta línea
}
```

- `iter_mut` - Esto presta prestado mutuamente cada elemento de la colección, lo que permite modificar la colección in situ.

```rust
fn main() {
    let mut names = vec!["Bob", "Frank", "Ferris"];

    for name in names.iter_mut() {
        *name = match name {
            &mut "Ferris" => "There is a rustacean among us!",
            _ => "Hello",
        }
    }

    println!("names: {:?}", names);
}
```

En los fragmentos de código anteriores, observe el tipo de rama `match`, que es la diferencia clave en los tipos de iteración. La diferencia en tipo, por supuesto, implica diferentes acciones que pueden ser realizadas.
