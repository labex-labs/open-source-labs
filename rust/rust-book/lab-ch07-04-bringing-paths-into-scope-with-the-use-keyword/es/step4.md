# Re-exportar nombres con pub use

Cuando traemos un nombre al alcance con la palabra clave `use`, el nombre disponible en el nuevo alcance es privado. Para permitir que el código que llama a nuestro código haga referencia a ese nombre como si hubiera sido definido en el alcance de ese código, podemos combinar `pub` y `use`. Esta técnica se llama _re-exportación_ porque estamos trayendo un elemento al alcance pero también haciéndolo disponible para que otros lo traigan a su alcance.

La Lista 7-17 muestra el código de la Lista 7-11 con `use` en el módulo raíz cambiado a `pub use`.

Nombre del archivo: `src/lib.rs`

```rust
mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

pub use crate::front_of_house::hosting;

pub fn eat_at_restaurant() {
    hosting::add_to_waitlist();
}
```

Lista 7-17: Hacer un nombre disponible para que cualquier código lo use desde un nuevo alcance con `pub use`

Antes de este cambio, el código externo tendría que llamar a la función `add_to_waitlist` usando la ruta `restaurant::front_of_house::hosting::add_to_waitlist()`. Ahora que este `pub use` ha re-exportado el módulo `hosting` desde el módulo raíz, el código externo puede usar la ruta `restaurant::hosting::add_to_waitlist()` en su lugar.

La re-exportación es útil cuando la estructura interna de su código es diferente de cómo los programadores que llaman a su código pensarían sobre el dominio. Por ejemplo, en esta metáfora del restaurante, las personas que administran el restaurante piensan en "frente de casa" y "trasera de casa". Pero los clientes que visitan un restaurante probablemente no pensarían en las partes del restaurante en esos términos. Con `pub use`, podemos escribir nuestro código con una estructura pero exponer una estructura diferente. Hacer esto hace que nuestra biblioteca esté bien organizada para los programadores que trabajan en la biblioteca y los programadores que llaman a la biblioteca. Veremos otro ejemplo de `pub use` y cómo afecta a la documentación de su crat en "Exporting a Convenient Public API with pub use".
