# Visualizando los Cambios en strong_count y weak_count

Veamos cómo cambian los valores de `strong_count` y `weak_count` de las instancias `Rc<Node>` creando un nuevo ámbito interno y moviendo la creación de `branch` a ese ámbito. Al hacerlo, podemos ver qué pasa cuando se crea `branch` y luego se elimina cuando sale del ámbito. Las modificaciones se muestran en la Lista 15-29.

Nombre de archivo: `src/main.rs`

```rust
fn main() {
    let leaf = Rc::new(Node {
        value: 3,
        parent: RefCell::new(Weak::new()),
        children: RefCell::new(vec![]),
    });

  1 println!(
        "leaf strong = {}, weak = {}",
        Rc::strong_count(&leaf),
        Rc::weak_count(&leaf),
    );

  2 {
        let branch = Rc::new(Node {
            value: 5,
            parent: RefCell::new(Weak::new()),
            children: RefCell::new(vec![Rc::clone(&leaf)]),
        });

        *leaf.parent.borrow_mut() = Rc::downgrade(&branch);

      3 println!(
            "branch strong = {}, weak = {}",
            Rc::strong_count(&branch),
            Rc::weak_count(&branch),
        );

      4 println!(
            "leaf strong = {}, weak = {}",
            Rc::strong_count(&leaf),
            Rc::weak_count(&leaf),
        );
  5 }

  6 println!(
        "leaf parent = {:?}",
        leaf.parent.borrow().upgrade()
    );
  7 println!(
        "leaf strong = {}, weak = {}",
        Rc::strong_count(&leaf),
        Rc::weak_count(&leaf),
    );
}
```

Lista 15-29: Creando `branch` en un ámbito interno y examinando los recuentos de referencias fuertes y débiles

Después de crear `leaf`, su `Rc<Node>` tiene un recuento fuerte de 1 y un recuento débil de 0 \[1\]. En el ámbito interno \[2\], creamos `branch` y lo asociamos con `leaf`, momento en el que al imprimir los recuentos \[3\], el `Rc<Node>` en `branch` tendrá un recuento fuerte de 1 y un recuento débil de 1 (por `leaf.parent` apuntando a `branch` con un `Weak<Node>`). Cuando imprimimos los recuentos en `leaf` \[4\], veremos que tendrá un recuento fuerte de 2 porque `branch` ahora tiene una copia del `Rc<Node>` de `leaf` almacenado en `branch.children`, pero todavía tendrá un recuento débil de 0.

Cuando finaliza el ámbito interno \[5\], `branch` sale del ámbito y el recuento fuerte del `Rc<Node>` disminuye a 0, por lo que su `Node` se elimina. El recuento débil de 1 de `leaf.parent` no tiene nada que ver con si se elimina o no `Node`, por lo que no tenemos fugas de memoria.

Si intentamos acceder al padre de `leaf` después del final del ámbito, obtendremos `None` nuevamente \[6\]. Al final del programa \[7\], el `Rc<Node>` en `leaf` tiene un recuento fuerte de 1 y un recuento débil de 0 porque la variable `leaf` ahora es la única referencia al `Rc<Node>` nuevamente.

Toda la lógica que gestiona los recuentos y la eliminación de valores está integrada en `Rc<T>` y `Weak<T>` y sus implementaciones del trato `Drop`. Al especificar que la relación de un hijo a su padre debe ser una referencia `Weak<T>` en la definición de `Node`, puedes tener nodos padres que apunten a nodos hijos y viceversa sin crear un ciclo de referencia y fugas de memoria.
