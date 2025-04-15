# La anatomía de una función de prueba

En su forma más simple, una prueba en Rust es una función que está anotada con el atributo `test`. Los atributos son metadatos sobre piezas de código de Rust; un ejemplo es el atributo `derive` que usamos con structs en el Capítulo 5. Para convertir una función en una función de prueba, agrega `#[test]` en la línea antes de `fn`. Cuando ejecutas tus pruebas con el comando `cargo test`, Rust construye un binario ejecutor de pruebas que ejecuta las funciones anotadas y reporta si cada función de prueba pasa o falla.

Cada vez que creamos un nuevo proyecto de biblioteca con Cargo, se genera automáticamente un módulo de pruebas con una función de prueba en él. Este módulo te da una plantilla para escribir tus pruebas para que no tengas que buscar la estructura y la sintaxis exactas cada vez que empiezas un nuevo proyecto. ¡Puedes agregar tantas funciones de prueba adicionales y tantos módulos de prueba como desees!

Vamos a explorar algunos aspectos de cómo funcionan las pruebas experimentando con la prueba de plantilla antes de probar realmente cualquier código. Luego escribiremos algunas pruebas del mundo real que llamen a algún código que hayamos escrito y aseguremos que su comportamiento sea correcto.

Vamos a crear un nuevo proyecto de biblioteca llamado `adder` que sumará dos números:

```bash
$ cargo new adder --lib
Created library $(adder) project
$ cd adder
```

El contenido del archivo `src/lib.rs` en tu biblioteca `adder` debería verse como en la Lista 11-1.

Nombre de archivo: `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
  1 #[test]
    fn it_works() {
        let result = 2 + 2;
      2 assert_eq!(result, 4);
    }
}
```

Lista 11-1: El módulo y la función de prueba generados automáticamente por `cargo new`

Por ahora, ignoremos las dos primeras líneas y centrémonos en la función. Observe la anotación `#[test]` \[1\]: este atributo indica que esta es una función de prueba, por lo que el ejecutor de pruebas sabe tratar esta función como una prueba. También podríamos tener funciones no de prueba en el módulo `tests` para ayudar a configurar escenarios comunes o realizar operaciones comunes, por lo que siempre necesitamos indicar cuáles funciones son pruebas.

El cuerpo del ejemplo de función utiliza la macro `assert_eq!` \[2\] para asegurar que `result`, que contiene el resultado de sumar 2 y 2, es igual a 4. Esta afirmación sirve como un ejemplo del formato para una prueba típica. Vamos a ejecutarlo para ver que esta prueba pasa.

El comando `cargo test` ejecuta todas las pruebas en nuestro proyecto, como se muestra en la Lista 11-2.

```bash
[object Object]
```

Lista 11-2: La salida de la ejecución de la prueba generada automáticamente

Cargo compiló y ejecutó la prueba. Vemos la línea `running 1 test` \[1\]. La siguiente línea muestra el nombre de la función de prueba generada, llamada `it_works`, y que el resultado de ejecutar esa prueba es `ok` \[2\]. El resumen general `test result: ok.` \[3\] significa que todas las pruebas pasaron, y la parte que dice `1 passed; 0 failed` suma el número de pruebas que pasaron o fallaron.

Es posible marcar una prueba como ignorada para que no se ejecute en una instancia particular; lo cubriremos en "Ignorando algunas pruebas a menos que se solicite específicamente". Debido a que no lo hemos hecho aquí, el resumen muestra `0 ignored`. También podemos pasar un argumento al comando `cargo test` para ejecutar solo las pruebas cuyo nombre coincida con una cadena; esto se llama _filtrado_ y lo cubriremos en "Ejecutando un subconjunto de pruebas por nombre". Aquí no hemos filtrado las pruebas que se están ejecutando, por lo que el final del resumen muestra `0 filtered out`.

La estadística `0 measured` es para las pruebas de rendimiento que miden el rendimiento. Las pruebas de rendimiento, a la fecha de redacción de este documento, solo están disponibles en Rust nocturno. Consulte la documentación sobre las pruebas de rendimiento en *https://doc.rust-lang.org/unstable-book/library-features/test.html* para obtener más información.

La siguiente parte de la salida de la prueba que comienza en `Doc-tests adder` \[4\] es para los resultados de cualquier prueba de documentación. Todavía no tenemos ninguna prueba de documentación, pero Rust puede compilar cualquier ejemplo de código que aparezca en nuestra documentación de API. ¡Esta característica ayuda a mantener tus documentos y tu código actualizados! Discutiremos cómo escribir pruebas de documentación en "Comentarios de documentación como pruebas". Por ahora, ignoraremos la salida `Doc-tests`.

Vamos a empezar a personalizar la prueba a nuestras propias necesidades. Primero, cambia el nombre de la función `it_works` a un nombre diferente, como `exploration`, así:

Nombre de archivo: `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    #[test]
    fn exploration() {
        let result = 2 + 2;
        assert_eq!(result, 4);
    }
}
```

Luego ejecuta `cargo test` nuevamente. La salida ahora muestra `exploration` en lugar de `it_works`:

    running 1 test
    test tests::exploration... ok

    test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

Ahora agregaremos otra prueba, pero esta vez haremos una prueba que falle. Las pruebas fallan cuando algo en la función de prueba se desborda. Cada prueba se ejecuta en un nuevo hilo, y cuando el hilo principal ve que un hilo de prueba ha muerto, la prueba se marca como fallida. En el Capítulo 9, hablamos de que la forma más simple de desbordarse es llamar a la macro `panic!`. Ingresa la nueva prueba como una función llamada `another`, para que tu archivo `src/lib.rs` se vea como la Lista 11-3.

Nombre de archivo: `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    #[test]
    fn exploration() {
        assert_eq!(2 + 2, 4);
    }

    #[test]
    fn another() {
        panic!("Make this test fail");
    }
}
```

Lista 11-3: Agregando una segunda prueba que fallará porque llamamos a la macro `panic!`

Ejecute las pruebas nuevamente usando `cargo test`. La salida debería verse como en la Lista 11-4, que muestra que nuestra prueba `exploration` pasó y `another` falló.

    running 2 tests
    test tests::exploration... ok
    1 test tests::another... FAILED

    2 failures:

    ---- tests::another stdout ----
    thread'main' panicked at 'Make this test fail', src/lib.rs:10:9
    note: run with `RUST_BACKTRACE=1` environment variable to display
    a backtrace

    3 failures:
        tests::another

    4 test result: FAILED. 1 passed; 1 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

    error: test failed, to rerun pass '--lib'

Lista 11-4: Resultados de la prueba cuando una prueba pasa y una prueba falla

En lugar de `ok`, la línea `test tests::another` muestra `FAILED` \[1\]. Dos secciones nuevas aparecen entre los resultados individuales y el resumen: la primera \[2\] muestra la razón detallada de cada fallo de prueba. En este caso, obtenemos los detalles de que `another` falló porque se `desbordó en 'Make this test fail'` en la línea 10 del archivo `src/lib.rs`. La siguiente sección \[3\] lista solo los nombres de todas las pruebas que fallan, lo que es útil cuando hay muchas pruebas y mucha salida detallada de pruebas que fallan. Podemos usar el nombre de una prueba que falla para ejecutar solo esa prueba para depurarla más fácilmente; hablaremos más sobre maneras de ejecutar pruebas en "Controlar cómo se ejecutan las pruebas".

La línea de resumen se muestra al final \[4\]: en general, nuestro resultado de prueba es `FAILED`. Tuvimos una prueba que pasó y una prueba que falló.

Ahora que has visto cómo se ven los resultados de la prueba en diferentes escenarios, echemos un vistazo a algunas macros diferentes de `panic!` que son útiles en las pruebas.
