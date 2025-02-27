# El Trait Iterator y el Método next

Todos los iteradores implementan un trait llamado `Iterator` que está definido en la biblioteca estándar. La definición del trait se ve así:

```rust
pub trait Iterator {
    type Item;

    fn next(&mut self) -> Option<Self::Item>;

    // métodos con implementaciones predeterminadas omitidas
}
```

Observa que esta definición utiliza un nuevo sintaxis: `type Item` y `Self::Item`, que están definiendo un _tipo asociado_ con este trait. Hablaremos de los tipos asociados en profundidad en el Capítulo 19. Por ahora, todo lo que necesitas saber es que este código dice que implementar el trait `Iterator` requiere que también defina un tipo `Item`, y este tipo `Item` se utiliza en el tipo de retorno del método `next`. En otras palabras, el tipo `Item` será el tipo devuelto por el iterador.

El trait `Iterator` solo requiere que los implementadores definan un método: el método `next`, que devuelve un elemento del iterador a la vez, envuelto en `Some`, y, cuando la iteración ha terminado, devuelve `None`.

Podemos llamar al método `next` en los iteradores directamente; la Lista 13-12 demuestra qué valores se devuelven de llamadas repetidas a `next` en el iterador creado a partir del vector.

Nombre de archivo: `src/lib.rs`

```rust
#[test]
fn iterator_demonstration() {
    let v1 = vec![1, 2, 3];

    let mut v1_iter = v1.iter();

    assert_eq!(v1_iter.next(), Some(&1));
    assert_eq!(v1_iter.next(), Some(&2));
    assert_eq!(v1_iter.next(), Some(&3));
    assert_eq!(v1_iter.next(), None);
}
```

Lista 13-12: Llamada al método `next` en un iterador

Observa que tuvimos que hacer `v1_iter` mutable: llamar al método `next` en un iterador cambia el estado interno que el iterador utiliza para llevar un registro de dónde se encuentra en la secuencia. En otras palabras, este código _consume_, o agota, el iterador. Cada llamada a `next` consume un elemento del iterador. No tuvimos que hacer `v1_iter` mutable cuando usamos un bucle `for` porque el bucle tomó posesión de `v1_iter` y lo hizo mutable en secreto.

También observa que los valores que obtenemos de las llamadas a `next` son referencias inmutables a los valores en el vector. El método `iter` produce un iterador sobre referencias inmutables. Si queremos crear un iterador que tome posesión de `v1` y devuelva valores con posesión, podemos llamar a `into_iter` en lugar de `iter`. Del mismo modo, si queremos iterar sobre referencias mutables, podemos llamar a `iter_mut` en lugar de `iter`.
