# Creando una Estructura de Datos de Árbol: Un Nodo con Nodos Hijos

Para comenzar, construiremos un árbol con nodos que conocen sobre sus nodos hijos. Crearemos un struct llamado `Node` que contendrá su propio valor `i32` así como referencias a los valores de sus nodos hijos:

Nombre de archivo: `src/main.rs`

```rust
use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug)]
struct Node {
    value: i32,
    children: RefCell<Vec<Rc<Node>>>,
}
```

Queremos que un `Node` posea a sus hijos, y queremos compartir esa propiedad con variables para que podamos acceder directamente a cada `Node` en el árbol. Para hacer esto, definimos los elementos de `Vec<T>` como valores del tipo `Rc<Node>`. También queremos modificar qué nodos son hijos de otro nodo, por lo que tenemos un `RefCell<T>` en `children` alrededor de `Vec<Rc<Node>>`.

A continuación, usaremos nuestra definición de struct y crearemos una instancia de `Node` llamada `leaf` con el valor `3` y sin hijos, y otra instancia llamada `branch` con el valor `5` y `leaf` como uno de sus hijos, como se muestra en la Lista 15-27.

Nombre de archivo: `src/main.rs`

```rust
fn main() {
    let leaf = Rc::new(Node {
        value: 3,
        children: RefCell::new(vec![]),
    });

    let branch = Rc::new(Node {
        value: 5,
        children: RefCell::new(vec![Rc::clone(&leaf)]),
    });
}
```

Lista 15-27: Creando un nodo `leaf` sin hijos y un nodo `branch` con `leaf` como uno de sus hijos

Clonamos el `Rc<Node>` en `leaf` y lo almacenamos en `branch`, lo que significa que el `Node` en `leaf` ahora tiene dos propietarios: `leaf` y `branch`. Podemos llegar de `branch` a `leaf` a través de `branch.children`, pero no hay forma de llegar de `leaf` a `branch`. La razón es que `leaf` no tiene una referencia a `branch` y no sabe que están relacionados. Queremos que `leaf` sepa que `branch` es su padre. Lo haremos a continuación.
