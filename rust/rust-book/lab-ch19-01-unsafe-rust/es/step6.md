# Usar funciones extern para llamar a código externo

A veces, su código de Rust puede necesitar interactuar con código escrito en otro lenguaje. Para esto, Rust tiene la palabra clave `extern` que facilita la creación y uso de una _Interfaz de Funciones Externas_ _(FFI)_, que es una forma en que un lenguaje de programación define funciones y permite que otro lenguaje de programación (exterior) llame a esas funciones.

La Lista 19-8 demuestra cómo establecer una integración con la función `abs` de la biblioteca estándar de C. Las funciones declaradas dentro de bloques `extern` siempre son inseguras para llamar desde código de Rust. La razón es que otros lenguajes no aplican las reglas y garantías de Rust, y Rust no puede comprobarlas, por lo que la responsabilidad recae en el programador para garantizar la seguridad.

Nombre del archivo: `src/main.rs`

```rust
extern "C" {
    fn abs(input: i32) -> i32;
}

fn main() {
    unsafe {
        println!(
            "Valor absoluto de -3 según C: {}",
            abs(-3)
        );
    }
}
```

Lista 19-8: Declarar y llamar a una función `extern` definida en otro lenguaje

Dentro del bloque `extern "C"`, listamos los nombres y firmas de las funciones externas de otro lenguaje que queremos llamar. La parte `"C"` define qué _Interfaz Binaria de Aplicación_ _(ABI)_ utiliza la función externa: el ABI define cómo llamar a la función a nivel de ensamblador. El ABI `"C"` es el más común y sigue el ABI del lenguaje de programación C.

> **Llamar a funciones de Rust desde otros lenguajes**
>
> También podemos usar `extern` para crear una interfaz que permita que otros lenguajes llamen a funciones de Rust. En lugar de crear un bloque `extern` completo, agregamos la palabra clave `extern` y especificamos el ABI a utilizar justo antes de la palabra clave `fn` para la función relevante. También necesitamos agregar una anotación `#[no_mangle]` para decirle al compilador de Rust que no desordene el nombre de esta función. _Desordenar el nombre_ es cuando un compilador cambia el nombre que le hemos dado a una función a un nombre diferente que contiene más información para que otras partes del proceso de compilación la consuman, pero es menos legible para humanos. Cada compilador de lenguaje de programación desordena los nombres ligeramente de manera diferente, por lo que para que una función de Rust sea nombrada por otros lenguajes, debemos deshabilitar el desordenamiento de nombres del compilador de Rust.
>
> En el siguiente ejemplo, hacemos que la función `call_from_c` sea accesible desde código de C, después de que se compile a una biblioteca compartida y se enlace desde C:
>
>     #[no_mangle]
>     pub extern "C" fn call_from_c() {
>         println!("¡Acabo de llamar a una función de Rust desde C!");
>     }
>
> Este uso de `extern` no requiere `unsafe`.
