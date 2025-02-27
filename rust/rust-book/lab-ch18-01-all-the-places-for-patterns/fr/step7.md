# Function Parameters

Les paramètres de fonction peuvent également être des motifs. Le code du listing 18-6, qui déclare une fonction nommée `foo` qui prend un paramètre nommé `x` de type `i32`, devrait désormais vous paraître familier.

```rust
fn foo(x: i32) {
    // code goes here
}
```

Listing 18-6: A function signature using patterns in the parameters

La partie `x` est un motif! Comme nous l'avons fait avec `let`, nous pouvons comparer un tuple dans les arguments d'une fonction avec le motif. Le listing 18-7 sépare les valeurs d'un tuple lorsqu'on le passe à une fonction.

Nom de fichier : `src/main.rs`

```rust
fn print_coordinates(&(x, y): &(i32, i32)) {
    println!("Current location: ({x}, {y})");
}

fn main() {
    let point = (3, 5);
    print_coordinates(&point);
}
```

Listing 18-7: A function with parameters that destructure a tuple

Ce code imprime `Current location: (3, 5)`. Les valeurs `&(3, 5)` correspondent au motif `&(x, y)`, donc `x` est la valeur `3` et `y` est la valeur `5`.

Nous pouvons également utiliser des motifs dans les listes de paramètres de closures de la même manière que dans les listes de paramètres de fonctions car les closures sont similaires aux fonctions, comme discuté au chapitre 13.

À ce stade, vous avez vu plusieurs façons d'utiliser des motifs, mais les motifs ne fonctionnent pas de la même manière dans tous les endroits où nous pouvons les utiliser. Dans certains endroits, les motifs doivent être irréfutables ; dans d'autres circonstances, ils peuvent être réfutable. Nous allons discuter de ces deux concepts ensuite.
