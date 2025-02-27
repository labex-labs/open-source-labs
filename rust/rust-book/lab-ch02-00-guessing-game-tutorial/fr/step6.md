# Handling Potential Failure with Result

Nous travaillons toujours sur cette ligne de code. Nous discutons maintenant d'une troisième ligne de texte, mais notez qu'il s'agit toujours d'une seule ligne logique de code. La partie suivante est cette méthode :

```rust
.expect("Failed to read line");
```

Nous aurions pu écrire ce code comme ceci :

```rust
io::stdin().read_line(&mut guess).expect("Failed to read line");
```

Cependant, une longue ligne est difficile à lire, il est donc préférable de la diviser. Il est souvent sage d'introduire un retour à la ligne et d'autres espaces pour aider à découper les longues lignes lorsque vous appelez une méthode avec la syntaxe `.method_name()`. Maintenant, discutons de ce que fait cette ligne.

Comme mentionné précédemment, `read_line` met tout ce que l'utilisateur entre dans la chaîne que nous lui passons, mais elle renvoie également une valeur de type `Result`. `Result` est une _énumération_, souvent appelée _enum_, qui est un type qui peut être dans l'un de plusieurs états possibles. Nous appelons chaque état possible une _variante_.

Le chapitre 6 couvrira les enums en détail. Le but de ces types `Result` est de coder des informations de gestion d'erreurs.

Les variantes de `Result` sont `Ok` et `Err`. La variante `Ok` indique que l'opération a réussi, et à l'intérieur de `Ok` se trouve la valeur générée avec succès. La variante `Err` signifie que l'opération a échoué, et `Err` contient des informations sur la manière dont ou pourquoi l'opération a échoué.

Les valeurs du type `Result`, comme les valeurs de tout type, ont des méthodes définies sur elles. Une instance de `Result` a une méthode `expect` que vous pouvez appeler. Si cette instance de `Result` est une valeur `Err`, `expect` fera planter le programme et affichera le message que vous avez passé en argument à `expect`. Si la méthode `read_line` renvoie une `Err`, cela serait probablement le résultat d'une erreur provenant du système d'exploitation sous-jacent. Si cette instance de `Result` est une valeur `Ok`, `expect` prendra la valeur de retour que `Ok` contient et vous renverra juste cette valeur pour que vous puissiez l'utiliser. Dans ce cas, cette valeur est le nombre d'octets de l'entrée de l'utilisateur.

Si vous n'appelez pas `expect`, le programme compilera, mais vous obtiendrez un avertissement :

```bash
$ cargo build
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
warning: unused `Result` that must be used
  --> src/main.rs:10:5
   |
10 |     io::stdin().read_line(&mut guess);
   |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   |
   = note: `#[warn(unused_must_use)]` on by default
   = note: this `Result` may be an `Err` variant, which should be handled

warning: `guessing_game` (bin "guessing_game") generated 1 warning
    Finished dev [unoptimized + debuginfo] target(s) in 0.59s
```

Rust avertit que vous n'avez pas utilisé la valeur `Result` renvoyée par `read_line`, indiquant que le programme n'a pas géré une erreur possible.

La bonne manière de supprimer l'avertissement est d'écrire réellement du code de gestion d'erreurs, mais dans notre cas, nous voulons simplement faire planter ce programme lorsqu'un problème se produit, donc nous pouvons utiliser `expect`. Vous apprendrez à récupérer des erreurs au chapitre 9.
