# Anotaciones de lifetimes en definiciones de métodos

Cuando implementamos métodos en un struct con lifetimes, usamos la misma sintaxis que la de los parámetros de tipo genéricos mostrada en la Lista 10-11. Donde declaramos y usamos los parámetros de lifetime depende de si están relacionados con los campos del struct o con los parámetros y valores de retorno del método.

Los nombres de lifetime para los campos del struct siempre deben declararse después de la palabra clave `impl` y luego usarse después del nombre del struct porque esos lifetimes son parte del tipo del struct.

En las firmas de métodos dentro del bloque `impl`, las referencias pueden estar ligadas al lifetime de las referencias en los campos del struct, o pueden ser independientes. Además, las reglas de elisión de lifetimes a menudo hacen que no sea necesario anotar los lifetimes en las firmas de métodos. Veamos algunos ejemplos usando el struct llamado `ImportantExcerpt` que definimos en la Lista 10-24.

Primero usaremos un método llamado `level` cuyo único parámetro es una referencia a `self` y cuyo valor de retorno es un `i32`, que no es una referencia a nada:

```rust
impl<'a> ImportantExcerpt<'a> {
    fn level(&self) -> i32 {
        3
    }
}
```

La declaración del parámetro de lifetime después de `impl` y su uso después del nombre del tipo es obligatoria, pero no estamos obligados a anotar el lifetime de la referencia a `self` debido a la primera regla de elisión.

Aquí hay un ejemplo donde se aplica la tercera regla de elisión de lifetimes:

```rust
impl<'a> ImportantExcerpt<'a> {
    fn announce_and_return_part(&self, announcement: &str) -> &str {
        println!("Attention please: {announcement}");
        self.part
    }
}
```

Hay dos lifetimes de entrada, por lo que Rust aplica la primera regla de elisión de lifetimes y le da a `&self` y `announcement` sus propios lifetimes. Luego, porque uno de los parámetros es `&self`, el tipo de retorno obtiene el lifetime de `&self`, y todos los lifetimes han sido contabilizados.
