# Utiliser `if` dans une instruction `let`

Comme `if` est une expression, nous pouvons l'utiliser du côté droit d'une instruction `let` pour assigner le résultat à une variable, comme dans la Liste 3-2.

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let condition = true;
    let number = if condition { 5 } else { 6 };

    println!("La valeur de number est : {number}");
}
```

Liste 3-2 : Affecter le résultat d'une expression `if` à une variable

La variable `number` sera liée à une valeur en fonction du résultat de l'expression `if`. Exécutez ce code pour voir ce qui se passe :

```bash
$ cargo run
   Compiling branches v0.1.0 (file:///projets/branches)
    Finished dev [unoptimized + debuginfo] target(s) in 0.30s
     Running `target/debug/branches`
La valeur de number est : 5
```

Rappelez-vous que les blocs de code évaluent à la dernière expression qu'ils contiennent, et les nombres eux-mêmes sont également des expressions. Dans ce cas, la valeur de l'expression `if` entière dépend de quel bloc de code s'exécute. Cela signifie que les valeurs qui ont la possibilité d'être des résultats de chaque branche de l'`if` doivent être du même type ; dans la Liste 3-2, les résultats de la branche `if` et de la branche `else` étaient des entiers `i32`. Si les types ne correspondent pas, comme dans l'exemple suivant, nous obtiendrons une erreur :

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let condition = true;

    let number = if condition { 5 } else { "six" };

    println!("La valeur de number est : {number}");
}
```

Lorsque nous essayons de compiler ce code, nous obtiendrons une erreur. Les branches `if` et `else` ont des types de valeurs incompatibles, et Rust indique exactement où trouver le problème dans le programme :

```bash
$ cargo run
   Compiling branches v0.1.0 (file:///projets/branches)
error[E0308]: `if` et `else` ont des types incompatibles
 --> src/main.rs:4:44
  |
4 |     let number = if condition { 5 } else { "six" };
  |                                 -          ^^^^^ valeur attendue : entier, trouvée `&str`
  |                                 |
  |                                 pour cette raison
```

L'expression dans le bloc `if` évalue à un entier, et l'expression dans le bloc `else` évalue à une chaîne de caractères. Cela ne fonctionnera pas car les variables doivent avoir un seul type, et Rust doit savoir à la compilation quel type est la variable `number`, de manière définitive. Savoir le type de `number` permet au compilateur de vérifier que le type est valide partout où nous utilisons `number`. Rust ne serait pas capable de le faire si le type de `number` était seulement déterminé à l'exécution ; le compilateur serait plus complexe et offrirait moins de garanties sur le code s'il devait suivre plusieurs types hypothétiques pour n'importe quelle variable.
