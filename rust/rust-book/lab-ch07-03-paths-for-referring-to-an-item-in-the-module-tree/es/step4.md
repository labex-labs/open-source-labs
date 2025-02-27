# Haciendo Públicos Structs y Enums

También podemos usar `pub` para designar structs y enums como públicos, pero hay algunos detalles adicionales en el uso de `pub` con structs y enums. Si usamos `pub` antes de una definición de struct, hacemos el struct público, pero los campos del struct todavía serán privados. Podemos hacer que cada campo sea público o no caso por caso. En la Lista 7-9, hemos definido un struct público `back_of_house::Breakfast` con un campo público `toast` pero un campo privado `seasonal_fruit`. Esto modela el caso en un restaurante donde el cliente puede elegir el tipo de pan que viene con una comida, pero el chef decide qué fruta acompaña la comida según lo que esté de temporada y en stock. La fruta disponible cambia rápidamente, por lo que los clientes no pueden elegir la fruta ni siquiera ver qué fruta recibirán.

Nombre del archivo: `src/lib.rs`

```rust
mod back_of_house {
    pub struct Breakfast {
        pub toast: String,
        seasonal_fruit: String,
    }

    impl Breakfast {
        pub fn summer(toast: &str) -> Breakfast {
            Breakfast {
                toast: String::from(toast),
                seasonal_fruit: String::from("peaches"),
            }
        }
    }
}

pub fn eat_at_restaurant() {
    // Order a breakfast in the summer with Rye toast
    let mut meal = back_of_house::Breakfast::summer("Rye");
    // Change our mind about what bread we'd like
    meal.toast = String::from("Wheat");
    println!("I'd like {} toast please", meal.toast);

    // The next line won't compile if we uncomment it; we're not
    // allowed to see or modify the seasonal fruit that comes
    // with the meal
    // meal.seasonal_fruit = String::from("blueberries");
}
```

Lista 7-9: Un struct con algunos campos públicos y algunos campos privados

Debido a que el campo `toast` en el struct `back_of_house::Breakfast` es público, en `eat_at_restaurant` podemos escribir y leer en el campo `toast` usando notación de punto. Observe que no podemos usar el campo `seasonal_fruit` en `eat_at_restaurant`, porque `seasonal_fruit` es privado. Intente descomentar la línea que modifica el valor del campo `seasonal_fruit` para ver qué error obtiene.

También, observe que debido a que `back_of_house::Breakfast` tiene un campo privado, el struct necesita proporcionar una función asociada pública que construya una instancia de `Breakfast` (la hemos nombrado `summer` aquí). Si `Breakfast` no tuviera tal función, no podríamos crear una instancia de `Breakfast` en `eat_at_restaurant` porque no podríamos establecer el valor del campo privado `seasonal_fruit` en `eat_at_restaurant`.

En contraste, si hacemos un enum público, todas sus variantes entonces son públicas. Solo necesitamos el `pub` antes de la palabra clave `enum`, como se muestra en la Lista 7-10.

Nombre del archivo: `src/lib.rs`

```rust
mod back_of_house {
    pub enum Appetizer {
        Soup,
        Salad,
    }
}

pub fn eat_at_restaurant() {
    let order1 = back_of_house::Appetizer::Soup;
    let order2 = back_of_house::Appetizer::Salad;
}
```

Lista 7-10: Designar un enum como público hace que todas sus variantes sean públicas.

Debido a que hicimos público el enum `Appetizer`, podemos usar las variantes `Soup` y `Salad` en `eat_at_restaurant`.

Los enums no son muy útiles a menos que sus variantes sean públicas; sería molesto tener que anotar todas las variantes de enum con `pub` en cada caso, por lo que el valor predeterminado para las variantes de enum es ser públicas. Los structs a menudo son útiles sin que sus campos sean públicos, por lo que los campos de struct siguen la regla general de que todo es privado por defecto a menos que se anote con `pub`.

Hay una más situación que implica `pub` que no hemos cubierto, y esa es nuestra última característica del sistema de módulos: la palabra clave `use`. Cubriremos `use` por sí sola primero, y luego mostraremos cómo combinar `pub` y `use`.
