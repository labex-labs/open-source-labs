# Usando métodos del trato Iterator en lugar de indexación

A continuación, corregiremos el cuerpo de `Config::build`. Debido a que `args` implementa el trato `Iterator`, sabemos que podemos llamar al método `next` en él. La Lista 13-20 actualiza el código de la Lista 12-23 para usar el método `next`.

Nombre de archivo: `src/lib.rs`

```rust
impl Config {
    pub fn build(
        mut args: impl Iterator<Item = String>,
    ) -> Result<Config, &'static str> {
        args.next();

        let query = match args.next() {
            Some(arg) => arg,
            None => return Err("Didn't get a query string"),
        };

        let file_path = match args.next() {
            Some(arg) => arg,
            None => return Err("Didn't get a file path"),
        };

        let ignore_case = env::var("IGNORE_CASE").is_ok();

        Ok(Config {
            query,
            file_path,
            ignore_case,
        })
    }
}
```

Lista 13-20: Cambiando el cuerpo de `Config::build` para usar métodos de iterador

Recuerde que el primer valor en el valor devuelto de `env::args` es el nombre del programa. Queremos ignorarlo y pasar al siguiente valor, por lo que primero llamamos a `next` y no hacemos nada con el valor devuelto. Luego llamamos a `next` para obtener el valor que queremos poner en el campo `query` de `Config`. Si `next` devuelve `Some`, usamos una `match` para extraer el valor. Si devuelve `None`, significa que no se dieron suficientes argumentos y retornamos temprano con un valor `Err`. Hacemos lo mismo para el valor `filename`.
