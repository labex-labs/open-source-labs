# Exponiendo Rutas con la Palabra Clave pub

Volvamos al error de la Lista 7-4 que nos dijo que el módulo `hosting` es privado. Queremos que la función `eat_at_restaurant` en el módulo padre tenga acceso a la función `add_to_waitlist` en el módulo hijo, por lo que marcamos el módulo `hosting` con la palabra clave `pub`, como se muestra en la Lista 7-5.

Nombre del archivo: `src/lib.rs`

```rust
mod front_of_house {
    pub mod hosting {
        fn add_to_waitlist() {}
    }
}

--snip--
```

Lista 7-5: Declarando el módulo `hosting` como `pub` para usarlo desde `eat_at_restaurant`

Lamentablemente, el código de la Lista 7-5 todavía genera errores del compilador, como se muestra en la Lista 7-6.

```bash
$ cargo build
   Compiling restaurant v0.1.0 (file:///projects/restaurant)
error[E0603]: function `add_to_waitlist` is private
 --> src/lib.rs:9:37
  |
9 |     crate::front_of_house::hosting::add_to_waitlist();
  |                                     ^^^^^^^^^^^^^^^ private function
  |
note: the function `add_to_waitlist` is defined here
 --> src/lib.rs:3:9
  |
3 |         fn add_to_waitlist() {}
  |         ^^^^^^^^^^^^^^^^^^^^

error[E0603]: function `add_to_waitlist` is private
  --> src/lib.rs:12:30
   |
12 |     front_of_house::hosting::add_to_waitlist();
   |                              ^^^^^^^^^^^^^^^ private function
   |
note: the function `add_to_waitlist` is defined here
  --> src/lib.rs:3:9
   |
3  |         fn add_to_waitlist() {}
   |         ^^^^^^^^^^^^^^^^^^^^
```

Lista 7-6: Errores del compilador al compilar el código de la Lista 7-5

¿Qué pasó? Agregar la palabra clave `pub` delante de `mod hosting` hace que el módulo sea público. Con este cambio, si podemos acceder a `front_of_house`, podemos acceder a `hosting`. Pero los _contenidos_ de `hosting` siguen siendo privados; hacer el módulo público no hace que sus contenidos sean públicos. La palabra clave `pub` en un módulo solo permite que el código en sus módulos ancestros se refiera a él, no acceda a su código interno. Debido a que los módulos son contenedores, no hay mucho que podamos hacer solo haciendo el módulo público; necesitamos ir más allá y elegir hacer público uno o más de los elementos dentro del módulo también.

Los errores de la Lista 7-6 dicen que la función `add_to_waitlist` es privada. Las reglas de privacidad se aplican a structs, enums, funciones, métodos y módulos.

Vamos a hacer también pública la función `add_to_waitlist` agregando la palabra clave `pub` antes de su definición, como en la Lista 7-7.

Nombre del archivo: `src/lib.rs`

```rust
mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

--snip--
```

Lista 7-7: Agregando la palabra clave `pub` a `mod hosting` y `fn add_to_waitlist` nos permite llamar a la función desde `eat_at_restaurant`.

Ahora el código se compilará! Para ver por qué agregar la palabra clave `pub` nos permite usar estas rutas en `add_to_waitlist` con respecto a las reglas de privacidad, veamos las rutas absolutas y relativas.

En la ruta absoluta, comenzamos con `crate`, la raíz del árbol de módulos de nuestro crat. El módulo `front_of_house` está definido en la raíz del crat. Si bien `front_of_house` no es público, dado que la función `eat_at_restaurant` está definida en el mismo módulo que `front_of_house` (es decir, `eat_at_restaurant` y `front_of_house` son hermanos), podemos referirnos a `front_of_house` desde `eat_at_restaurant`. A continuación está el módulo `hosting` marcado con `pub`. Podemos acceder al módulo padre de `hosting`, por lo que podemos acceder a `hosting`. Finalmente, la función `add_to_waitlist` está marcada con `pub` y podemos acceder a su módulo padre, por lo que esta llamada a función funciona!

En la ruta relativa, la lógica es la misma que la ruta absoluta excepto en el primer paso: en lugar de comenzar desde la raíz del crat, la ruta comienza desde `front_of_house`. El módulo `front_of_house` está definido dentro del mismo módulo que `eat_at_restaurant`, por lo que la ruta relativa que comienza desde el módulo en el que está definida `eat_at_restaurant` funciona. Luego, dado que `hosting` y `add_to_waitlist` están marcados con `pub`, el resto de la ruta funciona, y esta llamada a función es válida!

Si planeas compartir tu crat de biblioteca para que otros proyectos puedan usar tu código, tu API pública es tu contrato con los usuarios de tu crat que determina cómo pueden interactuar con tu código. Hay muchas consideraciones al gestionar los cambios en tu API pública para que sea más fácil para las personas depender de tu crat. Estas consideraciones están fuera del alcance de este libro; si estás interesado en este tema, consulta las Guías de API de Rust en *https://rust-lang.github.io/api-guidelines*.

> **Mejores Prácticas para Paquetes con un Binario y una Biblioteca**
>
> Mencionamos que un paquete puede contener tanto una raíz de crat binario `src/main.rs` como una raíz de crat de biblioteca `src/lib.rs`, y ambos crates tendrán el nombre del paquete por defecto. Típicamente, los paquetes con este patrón de contener tanto una biblioteca como un crat binario tendrán solo suficiente código en el crat binario para iniciar un ejecutable que llame a código con el crat de biblioteca. Esto permite que otros proyectos beneficien de la mayor funcionalidad que el paquete ofrece porque el código del crat de biblioteca se puede compartir.
>
> El árbol de módulos debe definirse en `src/lib.rs`. Luego, cualquier elemento público se puede usar en el crat binario comenzando las rutas con el nombre del paquete. El crat binario se convierte en un usuario del crat de biblioteca al igual que un crat completamente externo usaría el crat de biblioteca: solo puede usar la API pública. Esto te ayuda a diseñar una buena API; no solo eres el autor, también eres un cliente!
>
> En el Capítulo 12, demostraremos esta práctica de organización con un programa de línea de comandos que contendrá tanto un crat binario como un crat de biblioteca.
