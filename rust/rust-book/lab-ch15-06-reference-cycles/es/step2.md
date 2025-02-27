# Creando un Ciclo de Referencia

Veamos cómo podría ocurrir un ciclo de referencia y cómo evitarlo, comenzando con la definición del enum `List` y un método `tail` en la Lista 15-25.

Nombre de archivo: `src/main.rs`

```rust
use crate::List::{Cons, Nil};
use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug)]
enum List {
  1 Cons(i32, RefCell<Rc<List>>),
    Nil,
}

impl List {
  2 fn tail(&self) -> Option<&RefCell<Rc<List>>> {
        match self {
            Cons(_, item) => Some(item),
            Nil => None,
        }
    }
}
```

Lista 15-25: Definición de una lista cons que contiene un `RefCell<T>` para que podamos modificar a qué se refiere una variante `Cons`

Estamos usando otra variación de la definición de `List` de la Lista 15-5. El segundo elemento en la variante `Cons` ahora es `RefCell<Rc<List>>` \[1\], lo que significa que en lugar de tener la capacidad de modificar el valor `i32` como hicimos en la Lista 15-24, queremos modificar el valor de `List` al que apunta una variante `Cons`. También estamos agregando un método `tail` \[2\] para que sea conveniente acceder al segundo elemento si tenemos una variante `Cons`.

En la Lista 15-26, estamos agregando una función `main` que utiliza las definiciones de la Lista 15-25. Este código crea una lista en `a` y una lista en `b` que apunta a la lista en `a`. Luego modifica la lista en `a` para que apunte a `b`, creando un ciclo de referencia. Hay declaraciones `println!` a lo largo del camino para mostrar cuáles son los recuentos de referencias en varios puntos de este proceso.

Nombre de archivo: `src/main.rs`

```rust
fn main() {
  1 let a = Rc::new(Cons(5, RefCell::new(Rc::new(Nil))));

    println!("a initial rc count = {}", Rc::strong_count(&a));
    println!("a next item = {:?}", a.tail());

  2 let b = Rc::new(Cons(10, RefCell::new(Rc::clone(&a))));

    println!(
        "a rc count after b creation = {}",
        Rc::strong_count(&a)
    );
    println!("b initial rc count = {}", Rc::strong_count(&b));
    println!("b next item = {:?}", b.tail());

  3 if let Some(link) = a.tail() {
      4 *link.borrow_mut() = Rc::clone(&b);
    }

    println!(
        "b rc count after changing a = {}",
        Rc::strong_count(&b)
    );
    println!(
        "a rc count after changing a = {}",
        Rc::strong_count(&a)
    );

    // Descomenta la siguiente línea para ver que tenemos un ciclo;
    // desbordará la pila
    // println!("a next item = {:?}", a.tail());
}
```

Lista 15-26: Creando un ciclo de referencia de dos valores `List` que se apuntan mutuamente

Creamos una instancia `Rc<List>` que contiene un valor de `List` en la variable `a` con una lista inicial de `5, Nil` \[1\]. Luego creamos una instancia `Rc<List>` que contiene otro valor de `List` en la variable `b` que contiene el valor `10` y apunta a la lista en `a` \[2\].

Modificamos `a` para que apunte a `b` en lugar de `Nil`, creando un ciclo. Hacemos eso usando el método `tail` para obtener una referencia al `RefCell<Rc<List>>` en `a`, que ponemos en la variable `link` \[3\]. Luego usamos el método `borrow_mut` en el `RefCell<Rc<List>>` para cambiar el valor interno de un `Rc<List>` que contiene un valor `Nil` al `Rc<List>` en `b` \[4\].

Cuando ejecutamos este código, manteniendo la última declaración `println!` comentada por el momento, obtendremos esta salida:

    a initial rc count = 1
    a next item = Some(RefCell { value: Nil })
    a rc count after b creation = 2
    b initial rc count = 1
    b next item = Some(RefCell { value: Cons(5, RefCell { value: Nil }) })
    b rc count after changing a = 2
    a rc count after changing a = 2

El recuento de referencias de las instancias `Rc<List>` en tanto `a` como `b` es 2 después de cambiar la lista en `a` para que apunte a `b`. Al final de `main`, Rust elimina la variable `b`, lo que reduce el recuento de referencias de la instancia `Rc<List>` de `b` de 2 a 1. La memoria que tiene `Rc<List>` en el montón no se eliminará en este punto porque su recuento de referencias es 1, no 0. Luego Rust elimina `a`, lo que también reduce el recuento de referencias de la instancia `Rc<List>` de `a` de 2 a 1. La memoria de esta instancia tampoco se puede eliminar, porque la otra instancia `Rc<List>` todavía la referencia. La memoria asignada a la lista permanecerá sin recopilar para siempre. Para visualizar este ciclo de referencia, hemos creado un diagrama en la Figura 15-4.

Figura 15-4: Un ciclo de referencia de listas `a` y `b` que se apuntan mutuamente

Si descomentas la última declaración `println!` y ejecutas el programa, Rust intentará imprimir este ciclo con `a` apuntando a `b` apuntando a `a` y así sucesivamente hasta que desborde la pila.

En comparación con un programa del mundo real, las consecuencias de crear un ciclo de referencia en este ejemplo no son muy graves: justo después de crear el ciclo de referencia, el programa termina. Sin embargo, si un programa más complejo asignara mucha memoria en un ciclo y la mantuviera durante mucho tiempo, el programa usaría más memoria de la necesaria y podría abrumar el sistema, causando que se agote la memoria disponible.

Crear ciclos de referencia no es fácil de hacer, pero tampoco es imposible. Si tienes valores `RefCell<T>` que contienen valores `Rc<T>` o combinaciones anidadas similares de tipos con mutabilidad interior y conteo de referencias, debes asegurarte de no crear ciclos; no puedes confiar en que Rust los capture. Crear un ciclo de referencia sería un error lógico en tu programa que debes minimizar utilizando pruebas automatizadas, revisiones de código y otras prácticas de desarrollo de software.

Otra solución para evitar los ciclos de referencia es reorganizar tus estructuras de datos de modo que algunas referencias expresen propiedad y otras no. Como resultado, puedes tener ciclos formados por algunas relaciones de propiedad y algunas relaciones no de propiedad, y solo las relaciones de propiedad afectan a si un valor puede ser eliminado. En la Lista 15-25, siempre queremos que las variantes `Cons` posean su lista, por lo que no es posible reorganizar la estructura de datos. Veamos un ejemplo usando gráficos compuestos por nodos padre y nodos hijo para ver cuándo las relaciones no de propiedad son una forma adecuada de prevenir ciclos de referencia.
