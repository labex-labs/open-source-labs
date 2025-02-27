# Correspondance avec des variables nommées

Les variables nommées sont des motifs irréfutables qui correspondent à n'importe quelle valeur, et nous les avons utilisées à de nombreuses reprises dans ce livre. Cependant, il y a une complication lorsqu'on utilise des variables nommées dans des expressions `match`. Étant donné que `match` démarre un nouveau contexte, les variables déclarées en tant que partie d'un motif à l'intérieur de l'expression `match` ombrage les variables du même nom en dehors de la structure `match`, comme c'est le cas pour toutes les variables. Dans la Liste 18-11, nous déclarons une variable nommée `x` avec la valeur `Some(5)` et une variable `y` avec la valeur `10`. Nous créons ensuite une expression `match` sur la valeur `x`. Considérez les motifs dans les branches `match` et l'instruction `println!` à la fin, et essayez de déterminer ce que le code affichera avant d'exécuter ce code ou de continuer à lire.

Nom de fichier : `src/main.rs`

```rust
fn main() {
  1 let x = Some(5);
  2 let y = 10;

    match x {
      3 Some(50) => println!("Got 50"),
      4 Some(y) => println!("Matched, y = {y}"),
      5 _ => println!("Default case, x = {:?}", x),
    }

  6 println!("at the end: x = {:?}, y = {y}", x);
}
```

Liste 18-11 : Une expression `match` avec une branche qui introduit une variable `y` ombragée

Examillons ce qui se passe lorsque l'expression `match` est exécutée. Le motif dans la première branche `match` \[3\] ne correspond pas à la valeur définie de `x` \[1\], donc le code continue.

Le motif dans la deuxième branche `match` \[4\] introduit une nouvelle variable nommée `y` qui correspondra à n'importe quelle valeur à l'intérieur d'une valeur `Some`. Étant donné que nous sommes dans un nouveau contexte à l'intérieur de l'expression `match`, il s'agit d'une nouvelle variable `y`, pas de la variable `y` que nous avons déclarée au début avec la valeur `10` \[2\]. Cette nouvelle liaison `y` correspondra à n'importe quelle valeur à l'intérieur d'un `Some`, ce qui est ce que nous avons dans `x`. Par conséquent, cette nouvelle `y` se lie à la valeur interne du `Some` dans `x`. Cette valeur est `5`, donc l'expression de cette branche est exécutée et affiche `Matched, y = 5`.

Si `x` avait été une valeur `None` au lieu de `Some(5)`, les motifs dans les deux premières branches n'auraient pas correspondu, donc la valeur aurait été associée au tiret de soulignement \[5\]. Nous n'avons pas introduit la variable `x` dans le motif de la branche du tiret de soulignement, donc la `x` dans l'expression est toujours la `x` externe qui n'a pas été ombragée. Dans ce cas hypothétique, le `match` afficherait `Default case, x = None`.

Lorsque l'expression `match` est terminée, son contexte se termine, ainsi que celui de la variable `y` interne. La dernière instruction `println!` \[6\] produit `at the end: x = Some(5), y = 10`.

Pour créer une expression `match` qui compare les valeurs de `x` externe et `y`, plutôt qu'introduire une variable ombragée, nous devrions utiliser une condition de garde `match` à la place. Nous parlerons des gardes `match` dans "Conditions supplémentaires avec les gardes `match`".
