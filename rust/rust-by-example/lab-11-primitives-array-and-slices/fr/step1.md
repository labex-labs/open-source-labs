# Tableaux et tranches

Un tableau est une collection d'objets du même type `T`, stockés en mémoire contiguë. Les tableaux sont créés en utilisant des crochets `[]`, et leur longueur, qui est connue à la compilation, fait partie de leur signature de type `[T; longueur]`.

Les tranches sont similaires aux tableaux, mais leur longueur n'est pas connue à la compilation. Au lieu de cela, une tranche est un objet à deux mots ; le premier mot est un pointeur vers les données, le second mot est la longueur de la tranche. La taille de mot est la même que usize, déterminée par l'architecture du processeur, par exemple 64 bits sur un x86-64. Les tranches peuvent être utilisées pour emprunter une section d'un tableau et ont la signature de type `&[T]`.

```rust
use std::mem;

// Cette fonction emprunte une tranche.
fn analyze_slice(slice: &[i32]) {
    println!("Premier élément de la tranche: {}", slice[0]);
    println!("La tranche a {} éléments", slice.len());
}

fn main() {
    // Tableau de taille fixe (la signature de type est superflue).
    let xs: [i32; 5] = [1, 2, 3, 4, 5];

    // Tous les éléments peuvent être initialisés avec la même valeur.
    let ys: [i32; 500] = [0; 500];

    // L'indexation commence à 0.
    println!("Premier élément du tableau: {}", xs[0]);
    println!("Second élément du tableau: {}", xs[1]);

    // `len` renvoie le nombre d'éléments dans le tableau.
    println!("Nombre d'éléments dans le tableau: {}", xs.len());

    // Les tableaux sont alloués sur la pile.
    println!("Le tableau occupe {} octets", mem::size_of_val(&xs));

    // Les tableaux peuvent être automatiquement empruntés sous forme de tranches.
    println!("Emprunte le tableau entier sous forme de tranche.");
    analyze_slice(&xs);

    // Les tranches peuvent pointer vers une section d'un tableau.
    // Elles sont de la forme [index_de_début..index_de_fin].
    // `index_de_début` est la première position dans la tranche.
    // `index_de_fin` est un indice supérieur à la dernière position dans la tranche.
    println!("Emprunte une section du tableau sous forme de tranche.");
    analyze_slice(&ys[1..4]);

    // Exemple de tranche vide `&[]`:
    let empty_array: [u32; 0] = [];
    assert_eq!(&empty_array, &[]);
    assert_eq!(&empty_array, &[][..]); // Même chose mais plus verbeux

    // Les tableaux peuvent être accessibles de manière sécurisée en utilisant `.get`, qui renvoie un
    // `Option`. Cela peut être utilisé comme indiqué ci-dessous, ou avec
    // `.expect()` si vous souhaitez que le programme quitte avec un message agréable
    // au lieu de continuer de manière tranquille.
    for i in 0..xs.len() + 1 { // Oups, un élément de trop!
        match xs.get(i) {
            Some(xval) => println!("{}: {}", i, xval),
            None => println!("Ralentis! {} est trop loin!", i),
        }
    }

    // L'indexation en dehors des limites du tableau provoque une erreur de compilation.
    //println!("{}", xs[5]);
    // L'indexation en dehors des limites de la tranche provoque une erreur à l'exécution.
    //println!("{}", xs[..][5]);
}
```
