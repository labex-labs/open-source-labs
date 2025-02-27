# HashSet

Considere un `HashSet` como un `HashMap` donde solo nos importan las claves (`HashSet<T>` es, en realidad, solo un envoltorio alrededor de `HashMap<T, ()>`).

"¿Cuál es el objetivo de eso?" preguntas. "Podría simplemente almacenar las claves en un `Vec`".

La característica única de un `HashSet` es que está garantizado de no tener elementos duplicados. Ese es el contrato que cumple cualquier colección de conjuntos. `HashSet` es solo una implementación. (ver también: `BTreeSet`)

Si inserta un valor que ya está presente en el `HashSet` (es decir, el nuevo valor es igual al existente y ambos tienen el mismo hash), entonces el nuevo valor reemplazará al antiguo.

Esto es genial cuando nunca quieres más de uno de algo, o cuando quieres saber si ya tienes algo.

Pero los conjuntos pueden hacer más que eso.

Los conjuntos tienen 4 operaciones principales (todas las siguientes llamadas devuelven un iterador):

- `union`: obtenga todos los elementos únicos de ambos conjuntos.

- `diferencia`: obtenga todos los elementos que están en el primer conjunto pero no en el segundo.

- `intersección`: obtenga todos los elementos que solo están en _ambos_ conjuntos.

- `diferencia simétrica`: obtenga todos los elementos que están en un conjunto o en el otro, pero _no_ en ambos.

Pruebe todas estas en el siguiente ejemplo:

```rust
use std::collections::HashSet;

fn main() {
    let mut a: HashSet<i32> = vec![1i32, 2, 3].into_iter().collect();
    let mut b: HashSet<i32> = vec![2i32, 3, 4].into_iter().collect();

    assert!(a.insert(4));
    assert!(a.contains(&4));

    // `HashSet::insert()` devuelve false si
    // ya había un valor presente.
    assert!(b.insert(4), "Value 4 is already in set B!");
    // FIXME ^ Comment out this line

    b.insert(5);

    // Si el tipo de elemento de una colección implementa `Debug`,
    // entonces la colección implementa `Debug`.
    // Normalmente imprime sus elementos en el formato `[elem1, elem2,...]`
    println!("A: {:?}", a);
    println!("B: {:?}", b);

    // Imprime [1, 2, 3, 4, 5] en cualquier orden
    println!("Union: {:?}", a.union(&b).collect::<Vec<&i32>>());

    // Esto debería imprimir [1]
    println!("Difference: {:?}", a.difference(&b).collect::<Vec<&i32>>());

    // Imprime [2, 3, 4] en cualquier orden.
    println!("Intersection: {:?}", a.intersection(&b).collect::<Vec<&i32>>());

    // Imprime [1, 5]
    println!("Symmetric Difference: {:?}",
             a.symmetric_difference(&b).collect::<Vec<&i32>>());
}
```

(Ejemplos adaptados de la documentación.)
