# Tuples

Un tuple est une collection de valeurs de différents types. Les tuples sont construits en utilisant des parenthèses `()`, et chaque tuple lui-même est une valeur avec une signature de type `(T1, T2,...)`, où `T1`, `T2` sont les types de ses membres. Les fonctions peuvent utiliser des tuples pour retourner plusieurs valeurs, car les tuples peuvent contenir un nombre quelconque de valeurs.

```rust
// Les tuples peuvent être utilisés comme arguments de fonction et comme valeurs de retour.
fn reverse(pair: (i32, bool)) -> (bool, i32) {
    // `let` peut être utilisé pour lier les membres d'un tuple à des variables.
    let (int_param, bool_param) = pair;

    (bool_param, int_param)
}

// La structure suivante est pour l'activité.
#[derive(Debug)]
struct Matrix(f32, f32, f32, f32);

fn main() {
    // Un tuple avec une série de différents types.
    let long_tuple = (1u8, 2u16, 3u32, 4u64,
                      -1i8, -2i16, -3i32, -4i64,
                      0.1f32, 0.2f64,
                      'a', true);

    // Les valeurs peuvent être extraites du tuple en utilisant l'indexation de tuple.
    println!("Première valeur du long tuple: {}", long_tuple.0);
    println!("Seconde valeur du long tuple: {}", long_tuple.1);

    // Les tuples peuvent être des membres de tuples.
    let tuple_of_tuples = ((1u8, 2u16, 2u32), (4u64, -1i8), -2i16);

    // Les tuples sont imprimables.
    println!("tuple de tuples: {:?}", tuple_of_tuples);

    // Mais les longs tuples (plus de 12 éléments) ne peuvent pas être imprimés.
    //let too_long_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13);
    //println!("Tuple trop long: {:?}", too_long_tuple);
    // TODO ^ Décochez les 2 lignes ci-dessus pour voir l'erreur du compilateur

    let pair = (1, true);
    println!("Pair est {:?}", pair);

    println!("La paire inversée est {:?}", reverse(pair));

    // Pour créer des tuples à un élément, la virgule est requise pour les distinguer
    // d'un littéral entouré de parenthèses.
    println!("Tuple à un élément: {:?}", (5u32,));
    println!("Juste un entier: {:?}", (5u32));

    // Les tuples peuvent être décomposés pour créer des liaisons.
    let tuple = (1, "hello", 4.5, true);

    let (a, b, c, d) = tuple;
    println!("{:?}, {:?}, {:?}, {:?}", a, b, c, d);

    let matrix = Matrix(1.1, 1.2, 2.1, 2.2);
    println!("{:?}", matrix);
}
```

## Activité

1.  _Récapitulatif_ : Ajoutez le trait `fmt::Display` à la structure `Matrix` dans l'exemple ci-dessus, de sorte que si vous passez de l'impression au format de débogage `{:?}` au format d'affichage `{}`, vous voyez la sortie suivante :

    ```plaintext
    ( 1.1 1.2 )
    ( 2.1 2.2 )
    ```

    Vous pouvez souhaiter vous référer à l'exemple pour l'affichage d'impression.

2.  Ajoutez une fonction `transpose` en utilisant la fonction `reverse` comme modèle, qui accepte une matrice en argument et retourne une matrice dans laquelle deux éléments ont été échangés. Par exemple :

    ```rust
    println!("Matrice:\n{}", matrix);
    println!("Transposée:\n{}", transpose(matrix));
    ```

    Résulte dans la sortie :

    ```plaintext
    Matrice:
    ( 1.1 1.2 )
    ( 2.1 2.2 )
    Transposée:
    ( 1.1 2.1 )
    ( 1.2 2.2 )
    ```
