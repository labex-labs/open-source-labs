# Permitiendo Varios Propietarios de Datos Mutables con Rc`<T>`{=html} y RefCell`<T>`{=html}

Una forma común de usar `RefCell<T>` es en combinación con `Rc<T>`. Recuerda que `Rc<T>` te permite tener múltiples propietarios de algunos datos, pero solo te da acceso inmutable a esos datos. Si tienes un `Rc<T>` que contiene un `RefCell<T>`, puedes obtener un valor que puede tener múltiples propietarios _y_ que puedes mutar.

Por ejemplo, recuerda el ejemplo de la lista en la Lista 15-18 donde usamos `Rc<T>` para permitir que múltiples listas compartan la propiedad de otra lista. Debido a que `Rc<T>` solo contiene valores inmutables, una vez que los hemos creado no podemos cambiar ninguno de los valores de la lista. Vamos a agregar `RefCell<T>` por su capacidad para cambiar los valores en las listas. La Lista 15-24 muestra que al usar un `RefCell<T>` en la definición de `Cons`, podemos modificar el valor almacenado en todas las listas.

Nombre de archivo: `src/main.rs`

```rust
#[derive(Debug)]
enum List {
    Cons(Rc<RefCell<i32>>, Rc<List>),
    Nil,
}

use crate::List::{Cons, Nil};
use std::cell::RefCell;
use std::rc::Rc;

fn main() {
  1 let value = Rc::new(RefCell::new(5));

  2 let a = Rc::new(Cons(Rc::clone(&value), Rc::new(Nil)));

    let b = Cons(Rc::new(RefCell::new(3)), Rc::clone(&a));
    let c = Cons(Rc::new(RefCell::new(4)), Rc::clone(&a));

  3 *value.borrow_mut() += 10;

    println!("a after = {:?}", a);
    println!("b after = {:?}", b);
    println!("c after = {:?}", c);
}
```

Lista 15-24: Usando `Rc<RefCell<i32>>` para crear una `List` que podemos mutar

Creamos un valor que es una instancia de `Rc<RefCell<i32>>` y lo almacenamos en una variable llamada `value` \[1\] para poder acceder a él directamente más adelante. Luego creamos una `List` en `a` con una variante `Cons` que contiene `value` \[2\]. Necesitamos clonar `value` para que tanto `a` como `value` tengan la propiedad del valor interno `5` en lugar de transferir la propiedad de `value` a `a` o que `a` preste de `value`.

Envuelve la lista `a` en un `Rc<T>` para que cuando creemos las listas `b` y `c`, ambas puedan hacer referencia a `a`, como hicimos en la Lista 15-18.

Después de haber creado las listas en `a`, `b` y `c`, queremos sumar 10 al valor en `value` \[3\]. Hacemos esto llamando a `borrow_mut` en `value`, que utiliza la característica de desreferenciación automática que discutimos en "¿Dónde está el operador -\>?" para desreferenciar el `Rc<T>` al valor interno `RefCell<T>`. El método `borrow_mut` devuelve un apuntador inteligente `RefMut<T>`, y usamos el operador de desreferenciación en él y cambiamos el valor interno.

Cuando imprimimos `a`, `b` y `c`, podemos ver que todos tienen el valor modificado de `15` en lugar de `5`:

    a after = Cons(RefCell { value: 15 }, Nil)
    b after = Cons(RefCell { value: 3 }, Cons(RefCell { value: 15 }, Nil))
    c after = Cons(RefCell { value: 4 }, Cons(RefCell { value: 15 }, Nil))

Esta técnica es bastante ingeniosa. Al usar `RefCell<T>`, tenemos un valor `List` inmutable en apariencia. Pero podemos usar los métodos en `RefCell<T>` que proporcionan acceso a su mutabilidad interior para que podamos modificar nuestros datos cuando sea necesario. Las comprobaciones en tiempo de ejecución de las reglas de préstamo nos protegen de las carreras de datos, y a veces vale la pena intercambiar un poco de velocidad por esta flexibilidad en nuestras estructuras de datos. Tenga en cuenta que `RefCell<T>` no funciona para el código de varios subprocesos. `Mutex<T>` es la versión segura para subprocesos de `RefCell<T>`, y discutiremos `Mutex<T>` en el Capítulo 16.
