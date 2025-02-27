# Compilar y ejecutar son pasos separados

Acabas de ejecutar un programa recién creado, así que examinemos cada paso del proceso.

Antes de ejecutar un programa Rust, debes compilarlo usando el compilador de Rust escribiendo el comando `rustc` y pasándole el nombre de tu archivo fuente, como esto:

```bash
rustc main.rs
```

Si tienes un conocimiento previo de C o C++, notarás que esto es similar a `gcc` o `clang`. Después de compilar con éxito, Rust produce un ejecutable binario.

En Linux, macOS y PowerShell en Windows, puedes ver el ejecutable escribiendo el comando `ls` en tu shell:

```bash
$ ls
main main.rs
```

A partir de aquí, ejecutas el archivo `main`, como esto:

```bash
./main
```

Si tu `main.rs` es tu programa "¡Hola, mundo!", esta línea imprimirá `¡Hola, mundo!` en tu terminal.

Si estás más familiarizado con un lenguaje dinámico, como Ruby, Python o JavaScript, es posible que no estés acostumbrado a compilar y ejecutar un programa como pasos separados. Rust es un lenguaje _compilado anticipadamente_, lo que significa que puedes compilar un programa y dar el ejecutable a alguien más, y ellos pueden ejecutarlo incluso sin tener Rust instalado. Si le das a alguien un archivo `.rb`, `.py` o `.js`, ellos necesitan tener instalada una implementación de Ruby, Python o JavaScript (respectivamente). Pero en esos lenguajes, solo necesitas un comando para compilar y ejecutar tu programa. Todo es un trato en el diseño de los lenguajes.

Simplemente compilar con `rustc` es suficiente para programas simples, pero a medida que tu proyecto crece, querrás manejar todas las opciones y facilitar la compartición de tu código. A continuación, te presentaremos la herramienta Cargo, que te ayudará a escribir programas Rust del mundo real.
