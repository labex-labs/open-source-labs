# Creando Instancias a Partir de Otras Instancias con la Sintaxis de Actualización de Estructura

A menudo es útil crear una nueva instancia de una estructura que incluye la mayoría de los valores de otra instancia, pero cambia algunos. Puedes hacer esto usando la _sintaxis de actualización de estructura_.

Primero, en la Lista 5-6 mostramos cómo crear una nueva instancia de `User` en `user2` regularmente, sin la sintaxis de actualización. Establecemos un nuevo valor para `email` pero de lo contrario usamos los mismos valores de `user1` que creamos en la Lista 5-2.

Nombre del archivo: `src/main.rs`

```rust
fn main() {
    --snip--

    let user2 = User {
        active: user1.active,
        username: user1.username,
        email: String::from("another@example.com"),
        sign_in_count: user1.sign_in_count,
    };
}
```

Lista 5-6: Creando una nueva instancia de `User` usando uno de los valores de `user1`

Usando la sintaxis de actualización de estructura, podemos lograr el mismo efecto con menos código, como se muestra en la Lista 5-7. La sintaxis `..` especifica que los campos restantes no establecidos explícitamente deben tener el mismo valor que los campos de la instancia dada.

Nombre del archivo: `src/main.rs`

```rust
fn main() {
    --snip--


    let user2 = User {
        email: String::from("another@example.com"),
      ..user1
    };
}
```

Lista 5-7: Usando la sintaxis de actualización de estructura para establecer un nuevo valor de `email` para una instancia de `User` pero para usar el resto de los valores de `user1`

El código en la Lista 5-7 también crea una instancia en `user2` que tiene un valor diferente para `email` pero tiene los mismos valores para los campos `username`, `active` y `sign_in_count` de `user1`. El `..user1` debe ir al final para especificar que cualquier campo restante debe obtener sus valores de los campos correspondientes en `user1`, pero podemos elegir especificar valores para tantos campos como queramos en cualquier orden, independientemente del orden de los campos en la definición de la estructura.

Tenga en cuenta que la sintaxis de actualización de estructura usa `=` como una asignación; esto es porque mueve los datos, al igual que vimos en "Variables y Datos Interactuando con Move". En este ejemplo, ya no podemos usar `user1` después de crear `user2` porque la `String` en el campo `username` de `user1` se movió a `user2`. Si hubiéramos dado nuevos valores de `String` a `user2` tanto para `email` como para `username`, y por lo tanto solo hubiéramos usado los valores de `active` y `sign_in_count` de `user1`, entonces `user1` todavía sería válido después de crear `user2`. Tanto `active` como `sign_in_count` son tipos que implementan el trato `Copy`, por lo que se aplicaría el comportamiento que discutimos en "Datos Solo en la Pila: Copy".
