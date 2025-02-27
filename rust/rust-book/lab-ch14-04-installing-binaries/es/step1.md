# Instalación de Binarios con cargo install

El comando `cargo install` te permite instalar y usar cajas binarias localmente. Esto no pretende reemplazar los paquetes del sistema; se supone que es una forma conveniente para los desarrolladores de Rust de instalar herramientas que otros han compartido en *https://crates.io*. Tenga en cuenta que solo puede instalar paquetes que tienen objetivos binarios. Un _objetivo binario_ es el programa ejecutable que se crea si la caja tiene un archivo `src/main.rs` o otro archivo especificado como binario, en contraste con un objetivo de biblioteca que no es ejecutable por sí solo pero es adecuado para incluirse en otros programas. Por lo general, las cajas tienen información en el archivo _README_ sobre si una caja es una biblioteca, tiene un objetivo binario o ambos.

Todos los binarios instalados con `cargo install` se almacenan en la carpeta `bin` de la raíz de instalación. Si instaló Rust usando `rustup.rs` y no tiene ninguna configuración personalizada, este directorio será \_$HOME/.cargo/bin_. Asegúrese de que este directorio esté en su `$PATH`para poder ejecutar los programas que ha instalado con`cargo install`.

Por ejemplo, en el Capítulo 12 mencionamos que hay una implementación de Rust de la herramienta `grep` llamada `ripgrep` para buscar archivos. Para instalar `ripgrep`, podemos ejecutar lo siguiente:

```bash
$ cargo install ripgrep
    Updating crates.io index
  Downloaded ripgrep v13.0.0
  Downloaded 1 crate (243.3 KB) in 0.88s
  Installing ripgrep v13.0.0
   --snip--
   Compiling ripgrep v13.0.0
    Finished release [optimized + debuginfo] target(s) in 3m 10s
  Installing ~/.cargo/bin/rg
   Installed package `ripgrep v13.0.0` (executable `rg`)
```

La penúltima línea de la salida muestra la ubicación y el nombre del binario instalado, que en el caso de `ripgrep` es `rg`. Siempre y cuando el directorio de instalación esté en su `$PATH`, como se mencionó anteriormente, luego puede ejecutar `rg --help` y comenzar a usar una herramienta más rápida y más Rustica para buscar archivos.
