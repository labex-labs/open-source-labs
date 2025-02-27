# RAII

Las variables en Rust hacen más que solo almacenar datos en la pila: también _poseen_ recursos, por ejemplo, `Box<T>` posee memoria en el montón. Rust fuerza el RAII (Resource Acquisition Is Initialization), por lo que siempre que un objeto sale del ámbito, se llama a su destructor y se liberan los recursos que posee.

Este comportamiento protege contra los errores de _fuga de recursos_, ¡así que nunca tendrás que liberar manualmente la memoria ni preocuparte por fugas de memoria nuevamente! Aquí hay un rápido demostración:

```rust
// raii.rs
fn create_box() {
    // Asignar un entero en el montón
    let _box1 = Box::new(3i32);

    // `_box1` se destruye aquí, y la memoria se libera
}

fn main() {
    // Asignar un entero en el montón
    let _box2 = Box::new(5i32);

    // Un ámbito anidado:
    {
        // Asignar un entero en el montón
        let _box3 = Box::new(4i32);

        // `_box3` se destruye aquí, y la memoria se libera
    }

    // Crear muchos boxes solo por diversión
    // No es necesario liberar manualmente la memoria!
    for _ in 0u32..1_000 {
        create_box();
    }

    // `_box2` se destruye aquí, y la memoria se libera
}
```

Por supuesto, podemos comprobar doblemente errores de memoria usando `valgrind`:

```{=html}
<!-- REUSE-IgnoreStart -->
```

```{=html}
<!-- Prevent REUSE from parsing the copyright statement in the sample code -->
```

```shell
$ rustc raii.rs && valgrind./raii
==26873== Memcheck, a memory error detector
==26873== Copyright (C) 2002-2013, and GNU GPL'd, by Julian Seward et al.
==26873== Using Valgrind-3.9.0 and LibVEX; rerun with -h for copyright info
==26873== Command:./raii
==26873==
==26873==
==26873== HEAP SUMMARY:
==26873==     in use at exit: 0 bytes in 0 blocks
==26873==   total heap usage: 1,013 allocs, 1,013 frees, 8,696 bytes allocated
==26873==
==26873== All heap blocks were freed -- no leaks are possible
==26873==
==26873== For counts of detected and suppressed errors, rerun with: -v
==26873== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 2 from 2)
```

```{=html}
<!-- REUSE-IgnoreEnd -->
```

¡No hay fugas aquí!

## Destructor

La noción de destructor en Rust se proporciona a través del trato \[`Drop`\]. El destructor se llama cuando el recurso sale del ámbito. No es necesario implementar este trato para cada tipo, solo impleméntelo para su tipo si requiere su propia lógica de destructor.

Ejecute el siguiente ejemplo para ver cómo funciona el trato \[`Drop`\]. Cuando la variable en la función `main` sale del ámbito, se invocará el destructor personalizado.

```rust
struct ToDrop;

impl Drop for ToDrop {
    fn drop(&mut self) {
        println!("ToDrop está siendo eliminado");
    }
}

fn main() {
    let x = ToDrop;
    println!("Creado un ToDrop!");
}
```
