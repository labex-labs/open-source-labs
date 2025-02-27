# Capturando el Entorno con Closures

Primero examinaremos cómo podemos usar closures para capturar valores del entorno en el que se definen para su uso posterior. Aquí está el escenario: de vez en cuando, nuestra empresa de camisetas regala una camiseta exclusiva y limitada a alguien en nuestra lista de correo como promoción. Las personas en la lista de correo pueden opcionalmente agregar su color favorito a su perfil. Si la persona elegida para una camiseta gratis tiene su color favorito definido, obtiene la camiseta de ese color. Si la persona no ha especificado un color favorito, obtiene el color que la empresa tiene en mayor cantidad en este momento.

Hay muchas maneras de implementar esto. Para este ejemplo, vamos a usar un enum llamado `ShirtColor` que tiene las variantes `Red` y `Blue` (limitando el número de colores disponibles por simplicidad). Representamos el inventario de la empresa con una struct `Inventory` que tiene un campo llamado `shirts` que contiene un `Vec<ShirtColor>` que representa los colores de camisetas actualmente en stock. El método `giveaway` definido en `Inventory` obtiene la preferencia opcional de color de camiseta del ganador de la camiseta gratis y devuelve el color de la camiseta que la persona recibirá. Esta configuración se muestra en la Lista 13-1.

Nombre de archivo: `src/main.rs`

```rust
#[derive(Debug, PartialEq, Copy, Clone)]
enum ShirtColor {
    Red,
    Blue,
}

struct Inventory {
    shirts: Vec<ShirtColor>,
}

impl Inventory {
    fn giveaway(
        &self,
        user_preference: Option<ShirtColor>,
    ) -> ShirtColor {
      1 user_preference.unwrap_or_else(|| self.most_stocked())
    }

    fn most_stocked(&self) -> ShirtColor {
        let mut num_red = 0;
        let mut num_blue = 0;

        for color in &self.shirts {
            match color {
                ShirtColor::Red => num_red += 1,
                ShirtColor::Blue => num_blue += 1,
            }
        }
        if num_red > num_blue {
            ShirtColor::Red
        } else {
            ShirtColor::Blue
        }
    }
}

fn main() {
    let store = Inventory {
      2 shirts: vec![
            ShirtColor::Blue,
            ShirtColor::Red,
            ShirtColor::Blue,
        ],
    };

    let user_pref1 = Some(ShirtColor::Red);
  3 let giveaway1 = store.giveaway(user_pref1);
    println!(
        "The user with preference {:?} gets {:?}",
        user_pref1, giveaway1
    );

    let user_pref2 = None;
  4 let giveaway2 = store.giveaway(user_pref2);
    println!(
        "The user with preference {:?} gets {:?}",
        user_pref2, giveaway2
    );
}
```

Lista 13-1: Situación de regalo de camisetas de la empresa

La `store` definida en `main` tiene dos camisetas azules y una roja restantes para distribuir en esta promoción limitada \[2\]. Llamamos al método `giveaway` para un usuario con preferencia por una camiseta roja \[3\] y un usuario sin ninguna preferencia \[4\].

Una vez más, este código podría implementarse de muchas maneras, y aquí, para centrarse en los closures, hemos adherido a conceptos que ya has aprendido, excepto el cuerpo del método `giveaway` que utiliza un closure. En el método `giveaway`, obtenemos la preferencia del usuario como un parámetro de tipo `Option<ShirtColor>` y llamamos al método `unwrap_or_else` en `user_preference` \[1\]. El método `unwrap_or_else` en `Option<T>` está definido por la biblioteca estándar. Toma un argumento: un closure sin ningún argumento que devuelve un valor `T` (el mismo tipo almacenado en la variante `Some` de `Option<T>`, en este caso `ShirtColor`). Si `Option<T>` es la variante `Some`, `unwrap_or_else` devuelve el valor dentro de `Some`. Si `Option<T>` es la variante `None`, `unwrap_or_else` llama al closure y devuelve el valor devuelto por el closure.

Especificamos la expresión de closure `|| self.most_stocked()` como argumento para `unwrap_or_else`. Este es un closure que no toma parámetros por sí mismo (si el closure tuviera parámetros, aparecerían entre los dos tubos verticales). El cuerpo del closure llama a `self.most_stocked()`. Estamos definiendo el closure aquí, y la implementación de `unwrap_or_else` evaluará el closure más tarde si es necesario.

Ejecutar este código imprime lo siguiente:

```rust
The user with preference Some(Red) gets Red
The user with preference None gets Blue
```

Un aspecto interesante aquí es que hemos pasado un closure que llama a `self.most_stocked()` en la instancia actual de `Inventory`. La biblioteca estándar no necesita saber nada sobre los tipos `Inventory` o `ShirtColor` que definimos, ni sobre la lógica que queremos usar en este escenario. El closure captura una referencia inmutable a la instancia `self` de `Inventory` y la pasa con el código que especificamos al método `unwrap_or_else`. Las funciones, por otro lado, no pueden capturar su entorno de esta manera.
