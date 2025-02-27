# Concise Control Flow with if let

La syntaxe `if let` vous permet de combiner `if` et `let` d'une manière moins verbeuse pour traiter les valeurs qui correspondent à un motif tout en ignorant le reste. Considérez le programme de la Liste 6-6 qui effectue une correspondance sur une valeur `Option<u8>` dans la variable `config_max`, mais ne veut exécuter le code que si la valeur est la variante `Some`.

```rust
let config_max = Some(3u8);
match config_max {
    Some(max) => println!("The maximum is configured to be {max}"),
    _ => (),
}
```

Liste 6-6 : Une `match` qui ne s'intéresse qu'à l'exécution du code lorsque la valeur est `Some`

Si la valeur est `Some`, nous affichons la valeur dans la variante `Some` en liant la valeur à la variable `max` dans le motif. Nous ne voulons rien faire avec la valeur `None`. Pour satisfaire l'expression `match`, nous devons ajouter `_ => ()` après avoir traité une seule variante, ce qui est un code de gabarit ennuyeux à ajouter.

Au lieu de cela, nous pourrions écrire cela d'une manière plus courte en utilisant `if let`. Le code suivant se comporte de la même manière que la `match` de la Liste 6-6 :

```rust
let config_max = Some(3u8);
if let Some(max) = config_max {
    println!("The maximum is configured to be {max}");
}
```

La syntaxe `if let` prend un motif et une expression séparées par un signe égal. Elle fonctionne de la même manière qu'une `match`, où l'expression est donnée à la `match` et le motif est son premier bras. Dans ce cas, le motif est `Some(max)`, et `max` est lié à la valeur à l'intérieur de `Some`. Nous pouvons ensuite utiliser `max` dans le corps du bloc `if let` de la même manière que nous avons utilisé `max` dans le bras `match` correspondant. Le code dans le bloc `if let` n'est pas exécuté si la valeur ne correspond pas au motif.

Utiliser `if let` signifie moins de frappe, moins d'indentation et moins de code de gabarit. Cependant, vous perdez la vérification exhaustive que la `match` impose. Le choix entre `match` et `if let` dépend de ce que vous faites dans votre situation particulière et si gagner en concision est un compromis approprié pour perdre la vérification exhaustive.

En d'autres termes, vous pouvez considérer `if let` comme du sucre syntaxique pour une `match` qui exécute du code lorsque la valeur correspond à un motif et ignore ensuite toutes les autres valeurs.

Nous pouvons inclure un `else` avec un `if let`. Le bloc de code associé à l'`else` est le même que le bloc de code qui serait associé au cas `_` dans l'expression `match` qui est équivalente à l'`if let` et à l'`else`. Rappelez-vous la définition de l'énumération `Coin` dans la Liste 6-4, où la variante `Quarter` contenait également une valeur `UsState`. Si nous voulions compter toutes les pièces qui ne sont pas des quarters tout en annonçant l'état des quarters, nous pourrions le faire avec une expression `match`, comme ceci :

```rust
let mut count = 0;
match coin {
    Coin::Quarter(state) => println!("State quarter from {:?}!", state),
    _ => count += 1,
}
```

Ou nous pourrions utiliser une expression `if let` et `else`, comme ceci :

```rust
let mut count = 0;
if let Coin::Quarter(state) = coin {
    println!("State quarter from {:?}!", state);
} else {
    count += 1;
}
```

Si vous avez une situation dans laquelle la logique de votre programme est trop verbeuse pour être exprimée à l'aide d'une `match`, rappelez-vous que `if let` est également dans votre boîte à outils Rust.
