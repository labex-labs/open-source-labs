# Clonar un Rc`<T>`{=html} aumenta el recuento de referencias

Modifiquemos nuestro ejemplo funcional de la Lista 15-18 para ver cómo cambian los recuentos de referencias a medida que creamos y eliminamos referencias al `Rc<List>` en `a`.

En la Lista 15-19, modificaremos `main` para que tenga un ámbito interno alrededor de la lista `c`; luego podemos ver cómo cambia el recuento de referencias cuando `c` sale del ámbito.

Nombre de archivo: `src/main.rs`

```rust
--snip--

fn main() {
    let a = Rc::new(Cons(5, Rc::new(Cons(10, Rc::new(Nil)))));
    println!(
        "count after creating a = {}",
        Rc::strong_count(&a)
    );
    let b = Cons(3, Rc::clone(&a));
    println!(
        "count after creating b = {}",
        Rc::strong_count(&a)
    );
    {
        let c = Cons(4, Rc::clone(&a));
        println!(
            "count after creating c = {}",
            Rc::strong_count(&a)
        );
    }
    println!(
        "count after c goes out of scope = {}",
        Rc::strong_count(&a)
    );
}
```

Lista 15-19: Imprimiendo el recuento de referencias

En cada punto del programa en el que el recuento de referencias cambia, imprimimos el recuento de referencias, que obtenemos llamando a la función `Rc::strong_count`. Esta función se llama `strong_count` en lugar de `count` porque el tipo `Rc<T>` también tiene un `weak_count`; veremos para qué se utiliza `weak_count` en "Evitando ciclos de referencias usando Weak`<T>`{=html}".

Este código imprime lo siguiente:

    count after creating a = 1
    count after creating b = 2
    count after creating c = 3
    count after c goes out of scope = 2

Podemos ver que el `Rc<List>` en `a` tiene un recuento de referencias inicial de 1; luego, cada vez que llamamos a `clone`, el recuento aumenta en 1. Cuando `c` sale del ámbito, el recuento disminuye en 1. No tenemos que llamar a una función para disminuir el recuento de referencias como tenemos que llamar a `Rc::clone` para aumentar el recuento de referencias: la implementación del trato `Drop` disminuye el recuento de referencias automáticamente cuando un valor `Rc<T>` sale del ámbito.

Lo que no podemos ver en este ejemplo es que cuando `b` y luego `a` salen del ámbito al final de `main`, el recuento es entonces 0, y el `Rc<List>` se limpia completamente. Usar `Rc<T>` permite que un solo valor tenga múltiples propietarios, y el recuento garantiza que el valor siga siendo válido mientras exista cualquiera de los propietarios.

A través de referencias inmutables, `Rc<T>` te permite compartir datos entre múltiples partes de tu programa solo para lectura. Si `Rc<T>` te permitiera tener también múltiples referencias mutables, es posible que violaras una de las reglas de préstamo discutidas en el Capítulo 4: múltiples préstamos mutables al mismo lugar pueden causar conflictos de datos e inconsistencias. Pero poder mutar los datos es muy útil! En la siguiente sección, discutiremos el patrón de mutabilidad interior y el tipo `RefCell<T>` que puedes usar en combinación con un `Rc<T>` para trabajar con esta restricción de inmutabilidad.
