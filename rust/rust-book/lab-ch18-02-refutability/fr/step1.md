# Refutabilité : La possibilité qu'un motif ne corresponde pas

Les motifs se présentent sous deux formes : réfutables et irréfutables. Les motifs qui correspondent à n'importe quelle valeur possible passée sont _irréfutables_. Un exemple serait `x` dans l'énoncé `let x = 5;` car `x` correspond à tout et ne peut donc pas échouer à correspondre. Les motifs qui peuvent échouer à correspondre pour certaines valeurs possibles sont _réfutables_. Un exemple serait `Some(x)` dans l'expression `if let Some(x) = a_value` car si la valeur dans la variable `a_value` est `None` plutôt que `Some`, le motif `Some(x)` ne correspondra pas.

Les paramètres de fonction, les instructions `let` et les boucles `for` ne peuvent accepter que des motifs irréfutables car le programme ne peut rien faire de significatif lorsque les valeurs ne correspondent pas. Les expressions `if let` et `while let` acceptent des motifs réfutables et irréfutables, mais le compilateur avertit contre les motifs irréfutables car, par définition, ils sont destinés à gérer les échecs possibles : la fonctionnalité d'une condition est dans sa capacité à se comporter différemment selon le succès ou l'échec.

En général, vous n'avez pas à vous soucier de la distinction entre les motifs réfutables et irréfutables ; cependant, vous devez être familier du concept de réfutabilité pour pouvoir répondre lorsqu'il apparaît dans un message d'erreur. Dans ces cas, vous devrez modifier soit le motif, soit la construction dans laquelle vous utilisez le motif, selon le comportement souhaité du code.

Regardons un exemple de ce qui se passe lorsque nous essayons d'utiliser un motif réfuté où Rust exige un motif irréfuté et vice versa. La liste 18-8 montre une instruction `let`, mais pour le motif, nous avons spécifié `Some(x)`, un motif réfuté. Comme vous le devriez imaginer, ce code ne compilera pas.

```rust
let Some(x) = some_option_value;
```

Liste 18-8 : Tentative d'utilisation d'un motif réfuté avec `let`

Si `some_option_value` était une valeur `None`, elle ne correspondrait pas au motif `Some(x)`, ce qui signifie que le motif est réfuté. Cependant, l'instruction `let` ne peut accepter que des motifs irréfutables car il n'y a rien de valide que le code puisse faire avec une valeur `None`. Au moment de la compilation, Rust signalera qu'il y a eu une erreur car nous avons essayé d'utiliser un motif réfuté où un motif irréfuté était requis :

```bash
error[E0005]: refutable pattern in local binding: `None` not covered
   --> src/main.rs:3:9
    |
3   |     let Some(x) = some_option_value;
    |         ^^^^^^^ pattern `None` not covered
    |
    = note: `let` bindings require an "irrefutable pattern", like a `struct` or
an `enum` with only one variant
    = note: for more information, visit
https://doc.rust-lang.org/book/ch18-02-refutability.html
    = note: the matched value is of type `Option<i32>`
help: you might want to use `if let` to ignore the variant that isn't matched
    |
3   |     let x = if let Some(x) = some_option_value { x } else { todo!() };
    |     ++++++++++                                 ++++++++++++++++++++++
```

Comme nous n'avons pas couvert (et ne pouvions pas couvrir!) toutes les valeurs valides avec le motif `Some(x)`, Rust produit légitimement une erreur de compilation.

Si nous avons un motif réfuté où un motif irréfuté est nécessaire, nous pouvons le corriger en changeant le code qui utilise le motif : au lieu d'utiliser `let`, nous pouvons utiliser `if let`. Ensuite, si le motif ne correspond pas, le code saute simplement le code entre les accolades, lui donnant ainsi un moyen de continuer correctement. La liste 18-9 montre comment corriger le code de la liste 18-8.

    if let Some(x) = some_option_value {
        println!("{x}");
    }

Liste 18-9 : Utilisation de `if let` et d'un bloc avec des motifs réfutés au lieu de `let`

Nous avons trouvé une solution! Ce code est parfaitement valide, bien que cela signifie que nous ne pouvons pas utiliser un motif irréfuté sans recevoir une erreur. Si nous donnons à `if let` un motif qui correspondra toujours, tel que `x`, comme montré dans la liste 18-10, le compilateur donnera un avertissement.

    if let x = 5 {
        println!("{x}");
    };

Liste 18-10 : Tentative d'utilisation d'un motif irréfuté avec `if let`

Rust signale qu'il n'a pas de sens d'utiliser `if let` avec un motif irréfuté :

    warning: irrefutable `if let` pattern
     --> src/main.rs:2:8
      |
    2 |     if let x = 5 {
      |        ^^^^^^^^^
      |
      = note: `#[warn(irrefutable_let_patterns)]` on by default
      = note: this pattern will always match, so the `if let` is
    useless
      = help: consider replacing the `if let` with a `let`

Pour cette raison, les branches de correspondance doivent utiliser des motifs réfutés, sauf pour la dernière branche, qui devrait correspondre à toutes les valeurs restantes avec un motif irréfuté. Rust nous permet d'utiliser un motif irréfuté dans une correspondance avec une seule branche, mais cette syntaxe n'est pas particulièrement utile et pourrait être remplacée par une instruction `let` plus simple.

Maintenant que vous savez où utiliser les motifs et la différence entre les motifs réfutés et irréfutés, couvrons toute la syntaxe que nous pouvons utiliser pour créer des motifs.
