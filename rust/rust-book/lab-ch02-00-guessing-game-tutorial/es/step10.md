# Usando un crado para obtener más funcionalidad

Recuerda que un crado es una colección de archivos de código fuente de Rust. El proyecto que hemos estado construyendo es un _crado binario_, que es un ejecutable. El crado `rand` es un _crado de biblioteca_, que contiene código que está destinado a ser utilizado en otros programas y no puede ejecutarse por sí solo.

La coordinación de crados externos de Cargo es donde Cargo realmente se destaca. Antes de que podamos escribir código que use `rand`, necesitamos modificar el archivo `Cargo.toml` para incluir el crado `rand` como una dependencia. Abre ese archivo ahora y agrega la siguiente línea al final, debajo de la cabecera de la sección `[dependencies]` que Cargo creó para ti. Asegúrate de especificar `rand` exactamente como lo tenemos aquí, con este número de versión, o los ejemplos de código de este tutorial es posible que no funcionen:

Nombre del archivo: `Cargo.toml`

```tomlrust
[dependencies]
rand = "0.8.5"
```

En el archivo `Cargo.toml`, todo lo que sigue a una cabecera es parte de esa sección que continúa hasta que comienza otra sección. En `[dependencies]` le dices a Cargo cuales son los crados externos en los que depende tu proyecto y cuales versiones de esos crados requieres. En este caso, especificamos el crado `rand` con el especificador de versión semántica `0.8.5`. Cargo entiende la Versionamiento Semántico (a veces llamado _SemVer_), que es un estándar para escribir números de versión. El especificador `0.8.5` es en realidad un atajo para `^0.8.5`, lo que significa cualquier versión que sea al menos 0.8.5 pero menor que 0.9.0.

Cargo considera que estas versiones tienen una API pública compatible con la versión 0.8.5, y esta especificación asegura que obtendrás la última versión de parche que todavía se compilará con el código de este capítulo. No se garantiza que cualquier versión 0.9.0 o mayor tenga la misma API que la que usan los siguientes ejemplos.

Ahora, sin cambiar ningún código, construyamos el proyecto, como se muestra en la Lista 2-2.

```bash
$ cargo build
    Updating crates.io index
  Downloaded rand v0.8.5
  Downloaded libc v0.2.127
  Downloaded getrandom v0.2.7
  Downloaded cfg-if v1.0.0
  Downloaded ppv-lite86 v0.2.16
  Downloaded rand_chacha v0.3.1
  Downloaded rand_core v0.6.3
   Compiling rand_core v0.6.3
   Compiling libc v0.2.127
   Compiling getrandom v0.2.7
   Compiling cfg-if v1.0.0
   Compiling ppv-lite86 v0.2.16
   Compiling rand_chacha v0.3.1
   Compiling rand v0.8.5
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 2.53s
```

Lista 2-2: La salida de ejecutar `cargo build` después de agregar el crado `rand` como una dependencia

Es posible que veas números de versión diferentes (pero todos serán compatibles con el código, gracias a SemVer!) y líneas diferentes (dependiendo del sistema operativo), y las líneas pueden estar en un orden diferente.

Cuando incluimos una dependencia externa, Cargo obtiene las últimas versiones de todo lo que necesita esa dependencia desde el _registro_, que es una copia de los datos de Crates.io en *https://crates.io*. Crates.io es donde las personas en el ecosistema de Rust publican sus proyectos de Rust de código abierto para que otros los usen.

Después de actualizar el registro, Cargo revisa la sección `[dependencies]` y descarga cualquier crado que se liste y que no haya sido descargado ya. En este caso, aunque solo listamos `rand` como una dependencia, Cargo también capturó otros crates en los que `rand` depende para funcionar. Después de descargar los crates, Rust los compila y luego compila el proyecto con las dependencias disponibles.

Si ejecutas inmediatamente `cargo build` nuevamente sin hacer ningún cambio, no recibirás ninguna salida aparte de la línea `Finished`. Cargo sabe que ya ha descargado y compilado las dependencias, y no has cambiado nada sobre ellas en tu archivo `Cargo.toml`. Cargo también sabe que no has cambiado nada en tu código, por lo que tampoco lo recompila. Sin nada que hacer, simplemente sale.

Si abres el archivo `src/main.rs`, haces un cambio trivial, luego lo guardas y lo vuelves a compilar, solo verás dos líneas de salida:

```bash
$ cargo build
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 2.53 secs
```

Estas líneas muestran que Cargo solo actualiza la compilación con tu pequeño cambio en el archivo `src/main.rs`. Tus dependencias no han cambiado, por lo que Cargo sabe que puede reutilizar lo que ya ha descargado y compilado para esas.
