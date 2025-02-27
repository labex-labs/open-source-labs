# Analyse anatomique d'un programme Rust

Examnons de plus près ce programme "Bonjour, le monde!". Voici la première partie du puzzle :

```rust
fn main() {

}
```

Ces lignes définissent une fonction nommée `main`. La fonction `main` est spéciale : elle est toujours le premier code qui s'exécute dans tout programme Rust exécutable. Ici, la première ligne déclare une fonction nommée `main` qui n'a pas de paramètres et ne renvoie rien. S'il y avait des paramètres, ils se trouveraient entre les parenthèses `()`.

Le corps de la fonction est entouré de `{}`. Rust exige des accolades autour de tous les corps de fonction. Il est bon de placer l'accolade ouvrante sur la même ligne que la déclaration de la fonction, en laissant un espace entre les deux.

> Note : Si vous voulez adhérer à un style standard dans tous les projets Rust, vous pouvez utiliser un outil de formatage automatique appelé `rustfmt` pour formater votre code dans un style particulier (plus de détails sur `rustfmt` dans l'annexe D). L'équipe Rust a inclus cet outil dans la distribution standard de Rust, tout comme `rustc`, donc il devrait déjà être installé sur votre ordinateur!

Le corps de la fonction `main` contient le code suivant :

```rust
    println!("Bonjour, le monde!");
```

Cette ligne effectue tout le travail dans ce petit programme : elle imprime du texte à l'écran. Il y a quatre détails importants à noter ici.

Premièrement, le style Rust est d'indenter avec quatre espaces, pas une tabulation.

Deuxièmement, `println!` appelle une macro Rust. Si elle avait appelé une fonction à la place, elle serait écrite `println` (sans le `!`). Nous aborderons les macros Rust en détail au chapitre 19. Pour l'instant, vous n'avez qu'à savoir que l'utilisation d'un `!` signifie que vous appelez une macro plutôt qu'une fonction normale et que les macros ne suivent pas toujours les mêmes règles que les fonctions.

Troisièmement, vous voyez la chaîne de caractères `"Bonjour, le monde!"`. Nous passons cette chaîne en tant qu'argument à `println!`, et la chaîne est imprimée à l'écran.

Quatrièmement, nous terminons la ligne avec un point-virgule (`;`), qui indique que cette expression est terminée et que la suivante est prête à commencer. La plupart des lignes de code Rust se terminent par un point-virgule.
