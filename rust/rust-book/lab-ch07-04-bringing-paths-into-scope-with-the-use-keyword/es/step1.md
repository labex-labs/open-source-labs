# Traer rutas al alcance con la palabra clave use

Tener que escribir las rutas para llamar a funciones puede resultar incómodo y repetitivo. En la Lista 7-7, ya sea que hayamos elegido la ruta absoluta o relativa a la función `add_to_waitlist`, cada vez que queríamos llamar a `add_to_waitlist` también teníamos que especificar `front_of_house` y `hosting`. Afortunadamente, existe una forma de simplificar este proceso: podemos crear un atajo a una ruta una vez con la palabra clave `use`, y luego utilizar el nombre más corto en cualquier otro lugar del ámbito.

En la Lista 7-11, traemos el módulo `crate::front_of_house::hosting` al ámbito de la función `eat_at_restaurant` para que solo tengamos que especificar `hosting::add_to_waitlist` para llamar a la función `add_to_waitlist` en `eat_at_restaurant`.

Nombre del archivo: `src/lib.rs`

```rust
mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

use crate::front_of_house::hosting;

pub fn eat_at_restaurant() {
    hosting::add_to_waitlist();
}
```

Lista 7-11: Traer un módulo al alcance con `use`

Agregar `use` y una ruta en un ámbito es similar a crear un enlace simbólico en el sistema de archivos. Al agregar `use crate::front_of_house::hosting` en la raíz del crat, `hosting` ahora es un nombre válido en ese ámbito, al igual que si el módulo `hosting` hubiera sido definido en la raíz del crat. Las rutas traídas al alcance con `use` también verifican la privacidad, al igual que cualquier otra ruta.

Tenga en cuenta que `use` solo crea el atajo para el ámbito particular en el que se produce el `use`. La Lista 7-12 mueve la función `eat_at_restaurant` a un nuevo módulo hijo llamado `customer`, que luego es un ámbito diferente al de la declaración `use`, por lo que el cuerpo de la función no se compilará.

Nombre del archivo: `src/lib.rs`

```rust
mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

use crate::front_of_house::hosting;

mod customer {
    pub fn eat_at_restaurant() {
        hosting::add_to_waitlist();
    }
}
```

Lista 7-12: Una declaración `use` solo se aplica en el ámbito en el que se encuentra.

El error del compilador muestra que el atajo ya no es aplicable dentro del módulo `customer`:

```bash
error[E0433]: failed to resolve: use of undeclared crate or module `hosting`
  --> src/lib.rs:11:9
   |
11 |         hosting::add_to_waitlist();
   |         ^^^^^^^ use of undeclared crate or module `hosting`

warning: unused import: `crate::front_of_house::hosting`
 --> src/lib.rs:7:5
  |
7 | use crate::front_of_house::hosting;
  |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  |
  = note: `#[warn(unused_imports)]` on by default
```

Tenga en cuenta que también hay una advertencia de que el `use` ya no se utiliza en su ámbito. Para solucionar este problema, mueva el `use` dentro del módulo `customer` también, o haga referencia al atajo en el módulo padre con `super::hosting` dentro del módulo hijo `customer`.
