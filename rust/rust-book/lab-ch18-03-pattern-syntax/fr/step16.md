# Conditions supplémentaires avec des gardes de correspondance

Une **garde de correspondance** est une condition `if` supplémentaire, spécifiée après le motif dans un bras de `match`, qui doit également correspondre pour que ce bras soit choisi. Les gardes de correspondance sont utiles pour exprimer des idées plus complexes que ne le permet un motif seul.

La condition peut utiliser les variables créées dans le motif. La Liste 18-26 montre un `match` où le premier bras a le motif `Some(x)` et également une garde de correspondance `if x % 2 == 0` (qui sera `true` si le nombre est pair).

Nom de fichier : `src/main.rs`

```rust
let num = Some(4);

match num {
    Some(x) if x % 2 == 0 => println!("The number {x} is even"),
    Some(x) => println!("The number {x} is odd"),
    None => (),
}
```

Liste 18-26 : Ajout d'une garde de correspondance à un motif

Cet exemple imprimera `The number 4 is even`. Lorsque `num` est comparé au motif dans le premier bras, il correspond car `Some(4)` correspond à `Some(x)`. Ensuite, la garde de correspondance vérifie si le reste de la division de `x` par 2 est égal à 0, et puisque c'est le cas, le premier bras est sélectionné.

Si `num` avait été `Some(5)` au lieu de `Some(4)`, la garde de correspondance dans le premier bras serait restée `false` car le reste de la division de 5 par 2 est 1, ce qui n'est pas égal à 0. Rust passerait alors au second bras, qui correspondrait car le second bras n'a pas de garde de correspondance et correspond donc à n'importe quelle variante `Some`.

Il n'est pas possible d'exprimer la condition `if x % 2 == 0` à l'intérieur d'un motif, donc la garde de correspondance nous permet d'exprimer cette logique. Le désavantage de cette expressivité supplémentaire est que le compilateur n'essaie pas de vérifier l'exhaustivité lorsqu'il y a des expressions de garde de correspondance.

Dans la Liste 18-11, nous avons mentionné que nous pouvions utiliser des gardes de correspondance pour résoudre notre problème d'ombrage de motif. Rappelez-vous que nous avons créé une nouvelle variable à l'intérieur du motif dans l'expression `match` au lieu d'utiliser la variable en dehors du `match`. Cette nouvelle variable signifiait que nous ne pouvions pas tester la valeur de la variable externe. La Liste 18-27 montre comment nous pouvons utiliser une garde de correspondance pour résoudre ce problème.

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let x = Some(5);
    let y = 10;

    match x {
        Some(50) => println!("Got 50"),
        Some(n) if n == y => println!("Matched, n = {n}"),
        _ => println!("Default case, x = {:?}", x),
    }

    println!("at the end: x = {:?}, y = {y}", x);
}
```

Liste 18-27 : Utilisation d'une garde de correspondance pour tester l'égalité avec une variable externe

Ce code imprimera maintenant `Default case, x = Some(5)`. Le motif dans le second bras de correspondance n'introduit pas une nouvelle variable `y` qui ombrerait la variable externe `y`, ce qui signifie que nous pouvons utiliser la variable externe `y` dans la garde de correspondance. Au lieu de spécifier le motif comme `Some(y)`, qui aurait ombré la variable externe `y`, nous spécifions `Some(n)`. Cela crée une nouvelle variable `n` qui n'ombre rien car il n'y a pas de variable `n` en dehors du `match`.

La garde de correspondance `if n == y` n'est pas un motif et ne introduit donc pas de nouvelles variables. Cette `y` est bien la variable externe `y` plutôt qu'une nouvelle `y` ombrée, et nous pouvons chercher une valeur qui a la même valeur que la variable externe `y` en comparant `n` à `y`.

Vous pouvez également utiliser l'opérateur **ou** `|` dans une garde de correspondance pour spécifier plusieurs motifs ; la condition de la garde de correspondance s'appliquera à tous les motifs. La Liste 18-28 montre la précédence lorsqu'on combine un motif qui utilise `|` avec une garde de correspondance. La partie importante de cet exemple est que la garde de correspondance `if y` s'applique à `4`, `5` et `6`, même si cela peut sembler que `if y` ne s'applique qu'à `6`.

Nom de fichier : `src/main.rs`

```rust
let x = 4;
let y = false;

match x {
    4 | 5 | 6 if y => println!("yes"),
    _ => println!("no"),
}
```

Liste 18-28 : Combinaison de plusieurs motifs avec une garde de correspondance

La condition de correspondance indique que le bras ne correspond que si la valeur de `x` est égale à `4`, `5` ou `6` et si `y` est `true`. Lorsque ce code s'exécute, le motif du premier bras correspond car `x` est `4`, mais la garde de correspondance `if y` est `false`, donc le premier bras n'est pas choisi. Le code passe au second bras, qui correspond effectivement, et ce programme imprimera `no`. La raison est que la condition `if` s'applique au motif entier `4 | 5 | 6`, pas seulement à la dernière valeur `6`. En d'autres termes, la précédence d'une garde de correspondance par rapport à un motif se comporte comme ceci :

```rust
(4 | 5 | 6) if y =>...
```

plutôt que comme ceci :

```rust
4 | 5 | (6 if y) =>...
```

Après avoir exécuté le code, le comportement de précédence est évident : si la garde de correspondance était appliquée seulement à la valeur finale de la liste de valeurs spécifiée à l'aide de l'opérateur `|`, le bras aurait correspondu et le programme aurait imprimé `yes`.
