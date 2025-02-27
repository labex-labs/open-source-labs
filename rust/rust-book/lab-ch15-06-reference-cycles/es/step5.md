# Agregando una Referencia de un Hijo a su Padre

Para que el nodo hijo sea consciente de su padre, necesitamos agregar un campo `parent` a la definición de nuestro struct `Node`. El problema está en decidir cuál debe ser el tipo de `parent`. Sabemos que no puede contener un `Rc<T>` porque eso crearía un ciclo de referencia con `leaf.parent` apuntando a `branch` y `branch.children` apuntando a `leaf`, lo que haría que sus valores de `strong_count` nunca fueran 0.

Pensando en las relaciones de otra manera, un nodo padre debe poseer a sus hijos: si se elimina un nodo padre, sus nodos hijos también deben eliminarse. Sin embargo, un hijo no debe poseer a su padre: si eliminamos un nodo hijo, el padre debe seguir existiendo. ¡Este es un caso para referencias débiles!

Entonces, en lugar de `Rc<T>`, haremos que el tipo de `parent` utilice `Weak<T>`, específicamente un `RefCell<Weak<Node>>`. Ahora la definición de nuestro struct `Node` se ve así:

Nombre de archivo: `src/main.rs`

```rust
use std::cell::RefCell;
use std::rc::{Rc, Weak};

#[derive(Debug)]
struct Node {
    value: i32,
    parent: RefCell<Weak<Node>>,
    children: RefCell<Vec<Rc<Node>>>,
}
```

Un nodo será capaz de referirse a su nodo padre pero no posee a su padre. En la Lista 15-28, actualizamos `main` para usar esta nueva definición para que el nodo `leaf` tenga una forma de referirse a su padre, `branch`.

Nombre de archivo: `src/main.rs`

```rust
fn main() {
    let leaf = Rc::new(Node {
        value: 3,
      1 parent: RefCell::new(Weak::new()),
        children: RefCell::new(vec![]),
    });

  2 println!(
        "leaf parent = {:?}",
        leaf.parent.borrow().upgrade()
    );

    let branch = Rc::new(Node {
        value: 5,
      3 parent: RefCell::new(Weak::new()),
        children: RefCell::new(vec![Rc::clone(&leaf)]),
    });

  4 *leaf.parent.borrow_mut() = Rc::downgrade(&branch);

  5 println!(
        "leaf parent = {:?}",
        leaf.parent.borrow().upgrade()
    );
}
```

Lista 15-28: Un nodo `leaf` con una referencia débil a su nodo padre, `branch`

Crear el nodo `leaf` se parece a la Lista 15-27 con la excepción del campo `parent`: `leaf` comienza sin un padre, por lo que creamos una nueva instancia de referencia `Weak<Node>` vacía \[1\].

En este punto, cuando intentamos obtener una referencia al padre de `leaf` usando el método `upgrade`, obtenemos un valor `None`. Vemos esto en la salida de la primera declaración `println!` \[2\]:

```rust
leaf parent = None
```

Cuando creamos el nodo `branch`, también tendrá una nueva referencia `Weak<Node>` en el campo `parent` \[3\] porque `branch` no tiene un nodo padre. Todavía tenemos `leaf` como uno de los hijos de `branch`. Una vez que tenemos la instancia `Node` en `branch`, podemos modificar `leaf` para darle una referencia `Weak<Node>` a su padre \[4\]. Usamos el método `borrow_mut` en el `RefCell<Weak<Node>>` en el campo `parent` de `leaf`, y luego usamos la función `Rc::downgrade` para crear una referencia `Weak<Node>` a `branch` a partir del `Rc<Node>` en `branch`.

Cuando imprimimos el padre de `leaf` nuevamente \[5\], esta vez obtendremos una variante `Some` que contiene `branch`: ahora `leaf` puede acceder a su padre. Cuando imprimimos `leaf`, también evitamos el ciclo que eventualmente terminó en un desbordamiento de pila como tuvimos en la Lista 15-26; las referencias `Weak<Node>` se imprimen como `(Weak)`:

    leaf parent = Some(Node { value: 5, parent: RefCell { value: (Weak) },
    children: RefCell { value: [Node { value: 3, parent: RefCell { value: (Weak) },
    children: RefCell { value: [] } }] } })

La ausencia de una salida infinita indica que este código no creó un ciclo de referencia. También podemos saberlo al ver los valores que obtenemos al llamar a `Rc::strong_count` y `Rc::weak_count`.
