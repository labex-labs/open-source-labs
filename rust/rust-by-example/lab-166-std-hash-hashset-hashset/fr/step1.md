# HashSet

Considérez un `HashSet` comme un `HashMap` où nous ne nous intéressons qu'aux clés (`HashSet<T>` est, en réalité, simplement un wrapper autour de `HashMap<T, ()>`).

"Pourquoi faire ça?" vous demandez. "Je pourrais tout simplement stocker les clés dans un `Vec`."

La caractéristique unique d'un `HashSet` est qu'il est garanti de ne pas avoir d'éléments dupliqués. C'est le contrat que toute collection d'ensemble remplit. `HashSet` n'est qu'une implémentation. (voir également : `BTreeSet`)

Si vous insérez une valeur qui est déjà présente dans le `HashSet` (c'est-à-dire que la nouvelle valeur est égale à l'existante et qu'elles ont toutes les deux le même hachage), alors la nouvelle valeur remplacera l'ancienne.

Cela est très pratique lorsque vous ne voulez jamais avoir plus d'un exemplaire de quelque chose, ou lorsque vous voulez savoir si vous avez déjà quelque chose.

Mais les ensembles peuvent faire bien plus que ça.

Les ensembles ont 4 opérations principales (tous les appels suivants renvoient un itérateur) :

- `union` : obtenir tous les éléments uniques des deux ensembles.

- `difference` : obtenir tous les éléments qui sont dans le premier ensemble mais pas dans le second.

- `intersection` : obtenir tous les éléments qui ne sont que dans _les deux_ ensembles.

- `symmetric_difference` : obtenir tous les éléments qui sont dans un ensemble ou dans l'autre, mais _pas_ dans les deux.

Essayez toutes ces opérations dans l'exemple suivant :

```rust
use std::collections::HashSet;

fn main() {
    let mut a: HashSet<i32> = vec![1i32, 2, 3].into_iter().collect();
    let mut b: HashSet<i32> = vec![2i32, 3, 4].into_iter().collect();

    assert!(a.insert(4));
    assert!(a.contains(&4));

    // `HashSet::insert()` renvoie false si
    // une valeur était déjà présente.
    assert!(b.insert(4), "Value 4 is already in set B!");
    // FIXME ^ Commenter cette ligne

    b.insert(5);

    // Si le type d'élément d'une collection implémente `Debug`,
    // alors la collection implémente `Debug`.
    // Elle imprime généralement ses éléments au format `[elem1, elem2,...]`
    println!("A: {:?}", a);
    println!("B: {:?}", b);

    // Affiche [1, 2, 3, 4, 5] dans un ordre arbitraire
    println!("Union: {:?}", a.union(&b).collect::<Vec<&i32>>());

    // Cela devrait afficher [1]
    println!("Difference: {:?}", a.difference(&b).collect::<Vec<&i32>>());

    // Affiche [2, 3, 4] dans un ordre arbitraire.
    println!("Intersection: {:?}", a.intersection(&b).collect::<Vec<&i32>>());

    // Affiche [1, 5]
    println!("Symmetric Difference: {:?}",
             a.symmetric_difference(&b).collect::<Vec<&i32>>());
}
```

(Les exemples sont adaptés de la documentation.)
