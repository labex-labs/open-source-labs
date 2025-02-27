# Eliminando una clonación usando un iterador

En la Lista 12-6, agregamos código que tomó una porción de valores de `String` y creó una instancia de la estructura `Config` mediante la indexación en la porción y la clonación de los valores, lo que permite que la estructura `Config` sea dueña de esos valores. En la Lista 13-17, reproducimos la implementación de la función `Config::build` tal como estaba en la Lista 12-23.

Nombre de archivo: `src/lib.rs`

```rust
impl Config {
    pub fn build(
        args: &[String]
    ) -> Result<Config, &'static str> {
        if args.len() < 3 {
            return Err("not enough arguments");
        }

        let query = args[1].clone();
        let file_path = args[2].clone();

        let ignore_case = env::var("IGNORE_CASE").is_ok();

        Ok(Config {
            query,
            file_path,
            ignore_case,
        })
    }
}
```

Lista 13-17: Reproducción de la función `Config::build` de la Lista 12-23

En aquel momento, dijimos que no nos preocupáramos por las llamadas ineficientes a `clone` porque las eliminaremos en el futuro. Bueno, ¡ese momento es ahora!

Necesitamos `clone` aquí porque tenemos una porción con elementos de `String` en el parámetro `args`, pero la función `build` no es dueña de `args`. Para devolver la propiedad de una instancia de `Config`, tuvimos que clonar los valores de los campos `query` y `filename` de `Config` para que la instancia de `Config` pueda ser dueña de sus valores.

Con nuestro nuevo conocimiento sobre iteradores, podemos cambiar la función `build` para tomar la propiedad de un iterador como argumento en lugar de prestar una porción. Usaremos la funcionalidad del iterador en lugar del código que verifica la longitud de la porción e indexa en ubicaciones específicas. Esto clarificará lo que hace la función `Config::build` porque el iterador accederá a los valores.

Una vez que `Config::build` tome la propiedad del iterador y deje de usar operaciones de indexación que presten, podemos mover los valores de `String` desde el iterador a `Config` en lugar de llamar a `clone` y hacer una nueva asignación.
