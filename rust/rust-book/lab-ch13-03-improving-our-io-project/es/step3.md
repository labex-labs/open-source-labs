# Usando directamente el iterador devuelto

Abra el archivo `src/main.rs` de su proyecto de E/S, que debería verse así:

Nombre de archivo: `src/main.rs`

```rust
fn main() {
    let args: Vec<String> = env::args().collect();

    let config = Config::build(&args).unwrap_or_else(|err| {
        eprintln!("Problem parsing arguments: {err}");
        process::exit(1);
    });

    --snip--
}
```

Primero, cambiaremos el comienzo de la función `main` que teníamos en la Lista 12-24 al código de la Lista 13-18, que esta vez utiliza un iterador. Esto no se compilará hasta que actualicemos `Config::build` también.

Nombre de archivo: `src/main.rs`

```rust
fn main() {
    let config =
        Config::build(env::args()).unwrap_or_else(|err| {
            eprintln!("Problem parsing arguments: {err}");
            process::exit(1);
        });

    --snip--
}
```

Lista 13-18: Pasando el valor devuelto de `env::args` a `Config::build`

La función `env::args` devuelve un iterador ¡Qué sorpresa! En lugar de recopilar los valores del iterador en un vector y luego pasar una porción a `Config::build`, ahora estamos pasando la propiedad del iterador devuelto por `env::args` a `Config::build` directamente.

A continuación, necesitamos actualizar la definición de `Config::build`. En el archivo `src/lib.rs` de su proyecto de E/S, cambiemos la firma de `Config::build` para que se vea como en la Lista 13-19. Esto todavía no se compilará, porque necesitamos actualizar el cuerpo de la función.

Nombre de archivo: `src/lib.rs`

```rust
impl Config {
    pub fn build(
        mut args: impl Iterator<Item = String>,
    ) -> Result<Config, &'static str> {
        --snip--
```

Lista 13-19: Actualizando la firma de `Config::build` para esperar un iterador

La documentación de la biblioteca estándar para la función `env::args` muestra que el tipo del iterador que devuelve es `std::env::Args`, y ese tipo implementa el trato `Iterator` y devuelve valores de `String`.

Hemos actualizado la firma de la función `Config::build` para que el parámetro `args` tenga un tipo genérico con los límites de trato `impl Iterator<Item = String>` en lugar de `&[String]`. Este uso de la sintaxis `impl Trait` que discutimos en "Tratos como parámetros" significa que `args` puede ser cualquier tipo que implemente el tipo `Iterator` y devuelva elementos de `String`.

Debido a que estamos tomando la propiedad de `args` y vamos a mutar `args` iterando sobre él, podemos agregar la palabra clave `mut` en la especificación del parámetro `args` para que sea mutable.
