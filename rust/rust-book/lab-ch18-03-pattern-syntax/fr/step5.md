# Correspondance de plages de valeurs avec..=

La syntaxe `..=` nous permet de correspondre à une plage de valeurs inclusive. Dans le code suivant, lorsqu'un motif correspond à l'une des valeurs dans la plage donnée, cette branche sera exécutée :

Nom de fichier : `src/main.rs`

```rust
let x = 5;

match x {
    1..=5 => println!("one through five"),
    _ => println!("something else"),
}
```

Si `x` est `1`, `2`, `3`, `4` ou `5`, la première branche correspondra. Cette syntaxe est plus pratique pour plusieurs valeurs de correspondance que d'utiliser l'opérateur `|` pour exprimer la même idée ; si nous utilisions `|`, nous devrions spécifier `1 | 2 | 3 | 4 | 5`. Spécifier une plage est beaucoup plus court, surtout si nous voulons correspondre, disons, n'importe quel nombre entre 1 et 1 000!

Le compilateur vérifie que la plage n'est pas vide à la compilation, et puisque les seuls types pour lesquels Rust peut dire si une plage est vide ou non sont `char` et les valeurs numériques, les plages ne sont autorisées que avec des valeurs numériques ou `char`.

Voici un exemple utilisant des plages de valeurs de `char` :

Nom de fichier : `src/main.rs`

```rust
let x = 'c';

match x {
    'a'..='j' => println!("early ASCII letter"),
    'k'..='z' => println!("late ASCII letter"),
    _ => println!("something else"),
}
```

Rust peut dire que `'c'` est dans la plage du premier motif et affiche `early ASCII letter`.
