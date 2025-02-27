# Compilando y ejecutando un proyecto con Cargo

Ahora veamos qué es lo diferente cuando compilamos y ejecutamos el programa "Hello, world!" con Cargo. Desde tu directorio `hello_cargo`, compila tu proyecto ingresando el siguiente comando:

```bash
$ cargo build
   Compilando hello_cargo v0.1.0 (file:///projects/hello_cargo)
    Terminada la compilación en modo desarrollo [no optimizada + información de depuración] de los target(s) en 2.85 segundos
```

Este comando crea un archivo ejecutable en `target/debug/hello_cargo` en lugar de en tu directorio actual. Debido a que la compilación predeterminada es una compilación de depuración, Cargo coloca el binario en un directorio llamado `debug`. Puedes ejecutar el ejecutable con este comando:

```bash
$./target/debug/hello_cargo
Hello, world!
```

Si todo sale bien, `Hello, world!` debería imprimirse en la terminal. Ejecutar `cargo build` por primera vez también hace que Cargo cree un nuevo archivo en el nivel superior: _Cargo.lock_. Este archivo lleva un registro de las versiones exactas de las dependencias en tu proyecto. Este proyecto no tiene dependencias, por lo que el archivo es un poco esparso. Nunca tendrás que cambiar este archivo manualmente; Cargo se encarga de su contenido para ti.

Acabamos de compilar un proyecto con `cargo build` y lo ejecutamos con `./target/debug/hello_cargo`, pero también podemos usar `cargo run` para compilar el código y luego ejecutar el ejecutable resultante todo en un solo comando:

```bash
$ cargo run
    Terminada la compilación en modo desarrollo [no optimizada + información de depuración] de los target(s) en 0.0 segundos
     Ejecutando `target/debug/hello_cargo`
Hello, world!
```

Usar `cargo run` es más conveniente que tener que recordar ejecutar `cargo build` y luego usar la ruta completa al binario, por lo que la mayoría de los desarrolladores usan `cargo run`.

Observa que esta vez no vimos salida que indique que Cargo estaba compilando `hello_cargo`. Cargo se dio cuenta de que los archivos no habían cambiado, por lo que no los recompiló sino que simplemente ejecutó el binario. Si hubieras modificado tu código fuente, Cargo habría recompilado el proyecto antes de ejecutarlo, y habrías visto esta salida:

```bash
$ cargo run
   Compilando hello_cargo v0.1.0 (file:///projects/hello_cargo)
    Terminada la compilación en modo desarrollo [no optimizada + información de depuración] de los target(s) en 0.33 segundos
     Ejecutando `target/debug/hello_cargo`
Hello, world!
```

Cargo también proporciona un comando llamado `cargo check`. Este comando revisa rápidamente tu código para asegurarse de que se compile pero no produce un ejecutable:

```bash
$ cargo check
   Revisando hello_cargo v0.1.0 (file:///projects/hello_cargo)
    Terminada la compilación en modo desarrollo [no optimizada + información de depuración] de los target(s) en 0.32 segundos
```

¿Por qué no querrías un ejecutable? A menudo, `cargo check` es mucho más rápido que `cargo build` porque salta el paso de producir un ejecutable. Si estás revisando constantemente tu trabajo mientras escribes el código, usar `cargo check` acelerará el proceso de saber si tu proyecto todavía se compila. Por lo tanto, muchos rustianos ejecutan `cargo check` periódicamente mientras escriben su programa para asegurarse de que se compile. Luego ejecutan `cargo build` cuando están listos para usar el ejecutable.

Repasemos lo que hemos aprendido hasta ahora sobre Cargo:

- Podemos crear un proyecto usando `cargo new`.
- Podemos compilar un proyecto usando `cargo build`.
- Podemos compilar y ejecutar un proyecto en un solo paso usando `cargo run`.
- Podemos compilar un proyecto sin producir un binario para revisar errores usando `cargo check`.
- En lugar de guardar el resultado de la compilación en el mismo directorio que nuestro código, Cargo lo almacena en el directorio `target/debug`.

Una ventaja adicional de usar Cargo es que los comandos son los mismos independientemente del sistema operativo en el que estés trabajando. Entonces, en este punto, ya no proporcionaremos instrucciones específicas para Linux y macOS en comparación con Windows.
