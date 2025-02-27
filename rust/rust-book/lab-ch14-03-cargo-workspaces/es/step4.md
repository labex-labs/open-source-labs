# Dependiendo de un paquete externo en un espacio de trabajo

Tenga en cuenta que el espacio de trabajo tiene solo un archivo _Cargo.lock_ en el nivel superior, en lugar de tener un _Cargo.lock_ en el directorio de cada crate. Esto garantiza que todos los crates estén usando la misma versión de todas las dependencias. Si agregamos el paquete `rand` a los archivos _adder/Cargo.toml_ y _add_one/Cargo.toml_, Cargo resolverá ambos a una versión de `rand` y registrará eso en el único _Cargo.lock_. Hacer que todos los crates en el espacio de trabajo usen las mismas dependencias significa que los crates siempre serán compatibles entre sí. Agreguemos el crate `rand` a la sección `[dependencies]` en el archivo _add_one/Cargo.toml_ para que podamos usar el crate `rand` en el crate `add_one`:

Nombre del archivo: `add_one/Cargo.toml`

```tomlrust
[dependencies]
rand = "0.8.5"
```

Ahora podemos agregar `use rand;` al archivo `add_one/src/lib.rs`, y compilar todo el espacio de trabajo ejecutando `cargo build` en el directorio `add` traerá y compilará el crate `rand`. Obtendremos una advertencia porque no estamos referenciando el `rand` que trajimos al ámbito:

```bash
$ cargo build
    Actualizando el índice de crates.io
  Descargado rand v0.8.5
   --snip--
   Compilando rand v0.8.5
   Compilando add_one v0.1.0 (file:///projects/add/add_one)
   Compilando adder v0.1.0 (file:///projects/add/adder)
    Compilación finalizada [no optimizada + información de depuración] en 10.18s
```

El _Cargo.lock_ de nivel superior ahora contiene información sobre la dependencia de `add_one` en `rand`. Sin embargo, aunque `rand` se use en algún lugar del espacio de trabajo, no podemos usarlo en otros crates del espacio de trabajo a menos que lo agreguemos a sus archivos `Cargo.toml` también. Por ejemplo, si agregamos `use rand;` al archivo `adder/src/main.rs` para el paquete `adder`, obtendremos un error:

```bash
$ cargo build
   --snip--
   Compilando adder v0.1.0 (file:///projects/add/adder)
error[E0432]: import no resuelto `rand`
 --> adder/src/main.rs:2:5
  |
2 | use rand;
  |     ^^^^ no hay crate externo `rand`
```

Para solucionar esto, edite el archivo `Cargo.toml` para el paquete `adder` e indique que `rand` es una dependencia para él también. Compilar el paquete `adder` agregará `rand` a la lista de dependencias de `adder` en _Cargo.lock_, pero no se descargarán copias adicionales de `rand`. Cargo ha garantizado que cada crate en cada paquete en el espacio de trabajo que use el paquete `rand` usará la misma versión, ahorrándonos espacio y asegurando que los crates en el espacio de trabajo serán compatibles entre sí.
