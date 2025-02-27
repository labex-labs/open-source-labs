# Comprobando resultados con la macro assert!

La macro `assert!`, proporcionada por la biblioteca estándar, es útil cuando quieres asegurarte de que alguna condición en una prueba se evalúa como `true`. Le pasamos a la macro `assert!` un argumento que se evalúa como un booleano. Si el valor es `true`, nada pasa y la prueba pasa. Si el valor es `false`, la macro `assert!` llama a `panic!` para que la prueba falle. Usar la macro `assert!` nos ayuda a comprobar que nuestro código está funcionando de la manera que pretendemos.

En la Lista 5-15, usamos una struct `Rectangle` y un método `can_hold`, que se repiten aquí en la Lista 11-5. Vamos a poner este código en el archivo `src/lib.rs`, luego escribir algunas pruebas para él usando la macro `assert!`.

Nombre de archivo: `src/lib.rs`

```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }
}
```

Lista 11-5: Usando la struct `Rectangle` y su método `can_hold` del Capítulo 5

El método `can_hold` devuelve un booleano, lo que significa que es un caso de uso perfecto para la macro `assert!`. En la Lista 11-6, escribimos una prueba que prueba el método `can_hold` creando una instancia de `Rectangle` que tiene un ancho de 8 y un alto de 7 y asegurándonos de que puede contener otra instancia de `Rectangle` que tiene un ancho de 5 y un alto de 1.

Nombre de archivo: `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
  1 use super::*;

    #[test]
  2 fn larger_can_hold_smaller() {
      3 let larger = Rectangle {
            width: 8,
            height: 7,
        };
        let smaller = Rectangle {
            width: 5,
            height: 1,
        };

      4 assert!(larger.can_hold(&smaller));
    }
}
```

Lista 11-6: Una prueba para `can_hold` que comprueba si un rectángulo más grande puede contener en realidad un rectángulo más pequeño

Tenga en cuenta que hemos agregado una nueva línea dentro del módulo `tests`: `use super::*;` \[1\]. El módulo `tests` es un módulo regular que sigue las reglas de visibilidad habituales que cubrimos en "Rutas para referirse a un elemento en el árbol de módulos". Debido a que el módulo `tests` es un módulo interno, necesitamos traer el código que se está probando en el módulo externo al alcance del módulo interno. Usamos un glob aquí, por lo que cualquier cosa que definamos en el módulo externo está disponible para este módulo `tests`.

Hemos nombrado nuestra prueba `larger_can_hold_smaller` \[2\], y hemos creado las dos instancias de `Rectangle` que necesitamos \[3\]. Luego llamamos a la macro `assert!` y le pasamos el resultado de llamar a `larger.can_hold(&smaller)` \[4\]. Esta expresión debería devolver `true`, por lo que nuestra prueba debería pasar. ¡Vamos a averiguarlo!

    running 1 test
    test tests::larger_can_hold_smaller... ok

    test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

¡Pasa! Vamos a agregar otra prueba, esta vez asegurándonos de que un rectángulo más pequeño no puede contener un rectángulo más grande:

Nombre de archivo: `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn larger_can_hold_smaller() {
        --snip--
    }

    #[test]
    fn smaller_cannot_hold_larger() {
        let larger = Rectangle {
            width: 8,
            height: 7,
        };
        let smaller = Rectangle {
            width: 5,
            height: 1,
        };

        assert!(!smaller.can_hold(&larger));
    }
}
```

Debido a que el resultado correcto de la función `can_hold` en este caso es `false`, necesitamos negar ese resultado antes de pasarlo a la macro `assert!`. Como resultado, nuestra prueba pasará si `can_hold` devuelve `false`:

    running 2 tests
    test tests::larger_can_hold_smaller... ok
    test tests::smaller_cannot_hold_larger... ok

    test result: ok. 2 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

¡Dos pruebas que pasan! Ahora veamos qué pasa con nuestros resultados de prueba cuando introducimos un error en nuestro código. Cambiaremos la implementación del método `can_hold` reemplazando el signo mayor que por un signo menor que cuando compara los anchos:

    --snip--

    impl Rectangle {
        fn can_hold(&self, other: &Rectangle) -> bool {
            self.width < other.width && self.height > other.height
        }
    }

Ejecutar las pruebas ahora produce lo siguiente:

    running 2 tests
    test tests::smaller_cannot_hold_larger... ok
    test tests::larger_can_hold_smaller... FAILED

    failures:

    ---- tests::larger_can_hold_smaller stdout ----
    thread'main' panicked at 'assertion failed:
    larger.can_hold(&smaller)', src/lib.rs:28:9
    note: run with `RUST_BACKTRACE=1` environment variable to display
    a backtrace


    failures:
        tests::larger_can_hold_smaller

    test result: FAILED. 1 passed; 1 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

¡Nuestras pruebas detectaron el error! Debido a que `larger.width` es `8` y `smaller.width` es `5`, la comparación de los anchos en `can_hold` ahora devuelve `false`: 8 no es menor que 5.
