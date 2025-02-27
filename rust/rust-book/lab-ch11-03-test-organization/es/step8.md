# Pruebas de Integración para Crat Binarios

Si nuestro proyecto es un crat binario que solo contiene un archivo `src/main.rs` y no tiene un archivo `src/lib.rs`, no podemos crear pruebas de integración en el directorio `tests` y traer las funciones definidas en el archivo `src/main.rs` al alcance con una declaración `use`. Solo los crates de biblioteca exponen funciones que otros crates pueden usar; los crates binarios están destinados a ser ejecutados por sí mismos.

Esta es una de las razones por las que los proyectos de Rust que proporcionan un binario tienen un archivo `src/main.rs` sencillo que llama a la lógica que reside en el archivo `src/lib.rs`. Utilizando esa estructura, las pruebas de integración _pueden_ probar el crat de biblioteca con `use` para hacer disponible la funcionalidad importante. Si la funcionalidad importante funciona, el pequeño código en el archivo `src/main.rs` también funcionará, y ese pequeño código no necesita ser probado.
