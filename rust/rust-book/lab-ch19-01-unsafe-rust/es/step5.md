# Crear una abstracción segura sobre código inseguro

El simple hecho de que una función contenga código inseguro no significa que necesitemos marcar toda la función como insegura. De hecho, envolver código inseguro en una función segura es una abstracción común. Como ejemplo, estudiemos la función `split_at_mut` de la biblioteca estándar, que requiere algún código inseguro. Exploraremos cómo podríamos implementarla. Este método seguro está definido en rebanadas mutables: toma una rebanada y la divide en dos, dividiendo la rebanada en el índice dado como argumento. La Lista 19-4 muestra cómo usar `split_at_mut`.

```rust
let mut v = vec![1, 2, 3, 4, 5, 6];

let r = &mut v[..];

let (a, b) = r.split_at_mut(3);

assert_eq!(a, &mut [1, 2, 3]);
assert_eq!(b, &mut [4, 5, 6]);
```

Lista 19-4: Usar la función segura `split_at_mut`

No podemos implementar esta función solo con Rust seguro. Un intento podría ser similar a la Lista 19-5, que no se compilará. Para simplificar, implementaremos `split_at_mut` como una función en lugar de un método y solo para rebanadas de valores `i32` en lugar de un tipo genérico `T`.

```rust
fn split_at_mut(
    values: &mut [i32],
    mid: usize,
) -> (&mut [i32], &mut [i32]) {
    let len = values.len();

    assert!(mid <= len);

    (&mut values[..mid], &mut values[mid..])
}
```

Lista 19-5: Un intento de implementación de `split_at_mut` solo con Rust seguro

Esta función primero obtiene la longitud total de la rebanada. Luego, asegura que el índice dado como parámetro está dentro de la rebanada verificando si es menor o igual a la longitud. La afirmación significa que si pasamos un índice mayor que la longitud para dividir la rebanada, la función se detendrá con un error antes de intentar usar ese índice.

Luego devolvemos dos rebanadas mutables en un par: una desde el principio de la rebanada original hasta el índice `mid` y otra desde `mid` hasta el final de la rebanada.

Cuando intentamos compilar el código de la Lista 19-5, obtendremos un error:

```bash
error[E0499]: cannot borrow `*values` as mutable more than once at a time
 --> src/main.rs:9:31
  |
2 |     values: &mut [i32],
  |             - let's call the lifetime of this reference `'1`
...
9 |     (&mut values[..mid], &mut values[mid..])
  |     --------------------------^^^^^^--------
  |     |     |                   |
  |     |     |                   second mutable borrow occurs here
  |     |     first mutable borrow occurs here
  |     returning this value requires that `*values` is borrowed for `'1`
```

El verificador de préstamos de Rust no puede entender que estamos prestando diferentes partes de la rebanada; solo sabe que estamos prestando de la misma rebanada dos veces. Prestar diferentes partes de una rebanada es fundamentalmente correcto porque las dos rebanadas no se superponen, pero Rust no es lo suficientemente inteligente para saberlo. Cuando sabemos que el código está bien, pero Rust no lo sabe, es hora de recurrir al código inseguro.

La Lista 19-6 muestra cómo usar un bloque `unsafe`, un puntero crudo y algunas llamadas a funciones inseguras para que la implementación de `split_at_mut` funcione.

```rust
use std::slice;

fn split_at_mut(
    values: &mut [i32],
    mid: usize,
) -> (&mut [i32], &mut [i32]) {
  1 let len = values.len();
  2 let ptr = values.as_mut_ptr();

  3 assert!(mid <= len);

  4 unsafe {
        (
          5 slice::from_raw_parts_mut(ptr, mid),
          6 slice::from_raw_parts_mut(ptr.add(mid), len - mid),
        )
    }
}
```

Lista 19-6: Usar código inseguro en la implementación de la función `split_at_mut`

Recuerde de "El tipo de rebanada" que una rebanada es un puntero a algunos datos y la longitud de la rebanada. Usamos el método `len` para obtener la longitud de una rebanada \[1\] y el método `as_mut_ptr` para acceder al puntero crudo de una rebanada \[2\]. En este caso, porque tenemos una rebanada mutable de valores `i32`, `as_mut_ptr` devuelve un puntero crudo con el tipo `*mut i32`, que hemos almacenado en la variable `ptr`.

Mantuvimos la afirmación de que el índice `mid` está dentro de la rebanada \[3\]. Luego llegamos al código inseguro \[4\]: la función `slice::from_raw_parts_mut` toma un puntero crudo y una longitud, y crea una rebanada. La usamos para crear una rebanada que comienza en `ptr` y tiene `mid` elementos de longitud \[5\]. Luego llamamos al método `add` en `ptr` con `mid` como argumento para obtener un puntero crudo que comienza en `mid`, y creamos una rebanada usando ese puntero y el número restante de elementos después de `mid` como la longitud \[6\].

La función `slice::from_raw_parts_mut` es insegura porque toma un puntero crudo y debe confiar en que este puntero es válido. El método `add` en punteros crudos también es inseguro porque debe confiar en que la ubicación de desplazamiento también es un puntero válido. Por lo tanto, tuvimos que poner un bloque `unsafe` alrededor de nuestras llamadas a `slice::from_raw_parts_mut` y `add` para poder llamarlas. Al examinar el código y agregando la afirmación de que `mid` debe ser menor o igual a `len`, podemos decir que todos los punteros crudos usados dentro del bloque `unsafe` serán punteros válidos a datos dentro de la rebanada. Esta es una utilización aceptable y adecuada de `unsafe`.

Tenga en cuenta que no necesitamos marcar la función resultante `split_at_mut` como `unsafe`, y podemos llamar a esta función desde Rust seguro. Hemos creado una abstracción segura para el código inseguro con una implementación de la función que usa código inseguro de manera segura, porque solo crea punteros válidos a partir de los datos a los que tiene acceso esta función.

En contraste, el uso de `slice::from_raw_parts_mut` en la Lista 19-7 probablemente se detendrá con un error cuando se use la rebanada. Este código toma una ubicación de memoria arbitraria y crea una rebanada de 10.000 elementos de longitud.

```rust
use std::slice;

let address = 0x01234usize;
let r = address as *mut i32;

let values: &[i32] = unsafe {
    slice::from_raw_parts_mut(r, 10000)
};
```

Lista 19-7: Crear una rebanada a partir de una ubicación de memoria arbitraria

No tenemos la propiedad de la memoria en esta ubicación arbitraria, y no hay garantía de que la rebanada que crea este código contenga valores `i32` válidos. Intentar usar `values` como si fuera una rebanada válida da como resultado un comportamiento indefinido.
