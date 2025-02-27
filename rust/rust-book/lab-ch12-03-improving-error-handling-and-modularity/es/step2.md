# Separación de Preocupaciones para Proyectos Binarios

El problema organizacional de asignar la responsabilidad de múltiples tareas a la función `main` es común a muchos proyectos binarios. Como resultado, la comunidad de Rust ha desarrollado pautas para dividir las preocupaciones separadas de un programa binario cuando `main` comienza a crecer. Este proceso tiene los siguientes pasos:

- Divida su programa en un archivo `main.rs` y un archivo `lib.rs` y mueva la lógica de su programa a `lib.rs`.
- Mientras su lógica de análisis de línea de comandos sea pequeña, puede permanecer en `main.rs`.
- Cuando la lógica de análisis de línea de comandos comienza a volverse complicada, extáyala de `main.rs` y muevala a `lib.rs`.

Las responsabilidades que permanecen en la función `main` después de este proceso deben limitarse a lo siguiente:

- Llamar a la lógica de análisis de línea de comandos con los valores de argumento
- Configurar cualquier otra configuración
- Llamar a una función `run` en `lib.rs`
- Manejar el error si `run` devuelve un error

Este patrón se trata de separar preocupaciones: `main.rs` se encarga de ejecutar el programa y `lib.rs` se encarga de toda la lógica de la tarea en cuestión. Debido a que no se puede probar directamente la función `main`, esta estructura le permite probar toda la lógica de su programa al moverla a funciones en `lib.rs`. El código que queda en `main.rs` será lo suficientemente pequeño como para verificar su corrección leyéndolo. Vamos a rehacer nuestro programa siguiendo este proceso.
