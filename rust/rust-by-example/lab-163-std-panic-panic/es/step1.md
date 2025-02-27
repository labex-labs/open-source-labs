# `panic!`

La macro `panic!` se puede utilizar para generar un error y comenzar a deshacerse de su pila. Mientras se deshace, la ejecución del programa se encargará de liberar todos los recursos _propios_ del hilo llamando al destructor de todos sus objetos.

Dado que estamos trabajando con programas de un solo hilo, `panic!` hará que el programa informe el mensaje de error y salga.

```rust
// Re-implementación de la división entera (/)
fn division(dividendo: i32, divisor: i32) -> i32 {
    if divisor == 0 {
        // La división por cero desencadena un error
        panic!("división por cero");
    } else {
        dividendo / divisor
    }
}

// La tarea `main`
fn main() {
    // Entero asignado en el montón
    let _x = Box::new(0i32);

    // Esta operación desencadenará un error en la tarea
    division(3, 0);

    println!("Este punto no se alcanzará!");

    // `_x` debería ser destruido en este punto
}
```

Veamos que `panic!` no produce fugas de memoria.

```{=html}
<!-- REUSE-IgnoreStart -->
```

```{=html}
<!-- Evita que REUSE analice el enunciado de derechos de autor en el código de muestra -->
```

```shell
$ rustc panic.rs && valgrind./panic
==4401== Memcheck, un detector de errores de memoria
==4401== Copyright (C) 2002-2013, y bajo licencia GNU GPL, por Julian Seward et al.
==4401== Usando Valgrind-3.10.0.SVN y LibVEX; vuelva a ejecutar con -h para información de derechos de autor
==4401== Comando:./panic
==4401==
hilo '<main>' se desató con 'división por cero', panic.rs:5
==4401==
==4401== RESUMEN DEL MONTÓN:
==4401==     en uso al finalizar: 0 bytes en 0 bloques
==4401==   uso total del montón: 18 asignaciones, 18 liberaciones, 1,648 bytes asignados
==4401==
==4401== Todos los bloques de montón se liberaron -- no es posible tener fugas
==4401==
==4401== Para ver los recuentos de errores detectados y suprimidos, vuelva a ejecutar con: -v
==4401== RESUMEN DE ERRORES: 0 errores de 0 contextos (suprimidos: 0 de 0)
```

```{=html}
<!-- REUSE-IgnoreEnd -->
```
