# Hello, Cargo

Cargo es el sistema de compilación y administrador de paquetes de Rust. La mayoría de los rustianos utilizan esta herramienta para administrar sus proyectos de Rust porque Cargo se encarga de muchas tareas para ti, como compilar tu código, descargar las bibliotecas en las que tu código depende y compilar esas bibliotecas. (Llamamos _dependencias_ a las bibliotecas que necesita tu código.)

Los programas de Rust más simples, como el que hemos escrito hasta ahora, no tienen ninguna dependencia. Si hubiéramos compilado el proyecto "Hello, world!" con Cargo, solo usaría la parte de Cargo que se encarga de compilar tu código. A medida que escribas programas de Rust más complejos, agregará dependencias, y si empiezas un proyecto usando Cargo, agregarlas será mucho más fácil de hacer.

Debido a que la gran mayoría de los proyectos de Rust usan Cargo, el resto de este libro asume que también estás usando Cargo. Cargo viene instalado con Rust si usaste los instaladores oficiales discutidos en "Instalación". Si instalaste Rust de alguna otra manera, verifica si Cargo está instalado ingresando lo siguiente en tu terminal:

```bash
cargo --version
```

Si ves un número de versión, ¡lo tienes! Si ves un error, como `command not found`, consulta la documentación de tu método de instalación para determinar cómo instalar Cargo por separado.
