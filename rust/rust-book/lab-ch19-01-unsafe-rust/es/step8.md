# Implementar un trato inseguro

Podemos usar `unsafe` para implementar un trato inseguro. Un trato es inseguro cuando al menos uno de sus métodos tiene alguna invariante que el compilador no puede verificar. Declaramos que un trato es `inseguro` agregando la palabra clave `unsafe` antes de `trait` y marcando la implementación del trato como `unsafe` también, como se muestra en la Lista 19-11.

    unsafe trait Foo {
        // métodos van aquí
    }

    unsafe impl Foo for i32 {
        // implementaciones de métodos van aquí
    }

Lista 19-11: Definir e implementar un trato inseguro

Al usar `unsafe impl`, estamos prometiendo que cumpliremos con las invariantes que el compilador no puede verificar.

Como ejemplo, recuerde los tratos marcadores `Send` y `Sync` que discutimos en "Concurrencia extensible con los tratos Send y Sync": el compilador implementa estos tratos automáticamente si nuestros tipos están compuestos enteramente de tipos `Send` y `Sync`. Si implementamos un tipo que contiene un tipo que no es `Send` o `Sync`, como punteros crudos, y queremos marcar ese tipo como `Send` o `Sync`, debemos usar `unsafe`. Rust no puede verificar que nuestro tipo cumpla con las garantías de que se puede enviar con seguridad entre hilos o accederse desde múltiples hilos; por lo tanto, necesitamos hacer esas verificaciones manualmente y señalarlo con `unsafe`.
