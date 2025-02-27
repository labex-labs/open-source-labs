# Métodos que Consumen el Iterador

El trait `Iterator` tiene una serie de métodos diferentes con implementaciones predeterminadas proporcionadas por la biblioteca estándar; puedes conocer estos métodos consultando la documentación de la API de la biblioteca estándar para el trait `Iterator`. Algunos de estos métodos llaman al método `next` en su definición, razón por la cual se te requiere implementar el método `next` al implementar el trait `Iterator`.

Los métodos que llaman a `next` se denominan _adaptadores consumidores_ porque llamarlos agota el iterador. Un ejemplo es el método `sum`, que toma posesión del iterador y itera a través de los elementos llamando repetidamente a `next`, consumiendo así el iterador. A medida que itera, suma cada elemento a un total acumulado y devuelve el total cuando la iteración ha finalizado. La Lista 13-13 tiene una prueba que ilustra el uso del método `sum`.

Nombre de archivo: `src/lib.rs`

```rust
#[test]
fn iterator_sum() {
    let v1 = vec![1, 2, 3];

    let v1_iter = v1.iter();

    let total: i32 = v1_iter.sum();

    assert_eq!(total, 6);
}
```

Lista 13-13: Llamada al método `sum` para obtener el total de todos los elementos en el iterador

No podemos utilizar `v1_iter` después de la llamada a `sum` porque `sum` toma posesión del iterador en el que se la llama.
