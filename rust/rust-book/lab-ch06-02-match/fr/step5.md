# Modèles génériques et le placeholder `_`

En utilisant les enums, nous pouvons également prendre des actions spécifiques pour quelques valeurs particulières, mais pour toutes les autres valeurs, prendre une action par défaut. Imaginez que nous implémentons un jeu où, si vous obtenez un 3 lors d'un lancer de dé, votre joueur ne bouge pas, mais reçoit au contraire un nouveau chapeau élégant. Si vous obtenez un 7, votre joueur perd un chapeau élégant. Pour toutes les autres valeurs, votre joueur avance de ce nombre d'espaces sur le plateau de jeu. Voici un `match` qui implémente cette logique, avec le résultat du lancer de dé codé en dur plutôt qu'une valeur aléatoire, et toute autre logique représentée par des fonctions sans corps car leur implémentation réelle est hors du champ d'application de cet exemple :

```rust
let dice_roll = 9;
match dice_roll {
    3 => add_fancy_hat(),
    7 => remove_fancy_hat(),
  1 other => move_player(other),
}

fn add_fancy_hat() {}
fn remove_fancy_hat() {}
fn move_player(num_spaces: u8) {}
```

Pour les deux premières branches, les modèles sont les valeurs littérales `3` et `7`. Pour la dernière branche qui couvre toutes les autres valeurs possibles, le modèle est la variable que nous avons choisi de nommer `other` \[1\]. Le code qui s'exécute pour la branche `other` utilise la variable en la passant à la fonction `move_player`.

Ce code compile, même si nous n'avons pas listé toutes les valeurs possibles qu'un `u8` peut avoir, car le dernier modèle correspondra à toutes les valeurs qui ne sont pas spécifiquement listées. Ce modèle générique répond à la condition que le `match` doit être exhaustif. Notez que nous devons placer la branche générique en dernier car les modèles sont évalués dans l'ordre. Si nous plaçons la branche générique plus tôt, les autres branches ne s'exécuteraient jamais, donc Rust nous avertira si nous ajoutons des branches après une branche générique!

Rust dispose également d'un modèle que nous pouvons utiliser lorsque nous voulons un modèle générique mais ne voulons pas _utiliser_ la valeur dans le modèle générique : `_` est un modèle spécial qui correspond à n'importe quelle valeur et ne se lie pas à cette valeur. Cela indique à Rust que nous n'allons pas utiliser la valeur, donc Rust ne nous avertira pas au sujet d'une variable inutilisée.

Modifions les règles du jeu : maintenant, si vous obtenez n'importe quoi d'autre qu'un 3 ou un 7, vous devez relancer le dé. Nous n'avons plus besoin d'utiliser la valeur générique, donc nous pouvons modifier notre code pour utiliser `_` au lieu de la variable nommée `other` :

```rust
let dice_roll = 9;
match dice_roll {
    3 => add_fancy_hat(),
    7 => remove_fancy_hat(),
    _ => reroll(),
}

fn add_fancy_hat() {}
fn remove_fancy_hat() {}
fn reroll() {}
```

Cet exemple répond également à la condition d'exhaustivité car nous ignorons explicitement toutes les autres valeurs dans la dernière branche ; nous n'avons rien oublié.

Enfin, modifions les règles du jeu une dernière fois de sorte que rien d'autre ne se passe pendant votre tour si vous obtenez n'importe quoi d'autre qu'un 3 ou un 7. Nous pouvons l'exprimer en utilisant la valeur unitaire (le type de tuple vide que nous avons mentionné dans "Le type tuple") comme code qui accompagne la branche `_` :

```rust
let dice_roll = 9;
match dice_roll {
    3 => add_fancy_hat(),
    7 => remove_fancy_hat(),
    _ => (),
}

fn add_fancy_hat() {}
fn remove_fancy_hat() {}
```

Ici, nous disons explicitement à Rust que nous n'allons pas utiliser n'importe quelle autre valeur qui ne correspond pas à un modèle dans une branche précédente, et que nous ne voulons pas exécuter de code dans ce cas.

Il y a plus à savoir sur les modèles et la correspondance que nous aborderons au chapitre 18. Pour l'instant, nous allons passer à la syntaxe `if let`, qui peut être utile dans des situations où l'expression `match` est un peu verbeuse.
