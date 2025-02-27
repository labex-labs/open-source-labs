# Données stockées uniquement sur la pile : le trait `Copy`

Il y a encore un détail que nous n'avons pas abordé. Ce code utilisant des entiers - dont une partie était montrée dans la liste 4-2 - fonctionne et est valide :

```rust
let x = 5;
let y = x;

println!("x = {x}, y = {y}");
```

Mais ce code semble contredire ce que nous venons d'apprendre : nous n'avons pas de call à `clone`, mais `x` est toujours valide et n'a pas été déplacé dans `y`.

La raison est que les types tels que les entiers, qui ont une taille connue à la compilation, sont stockés entièrement sur la pile, de sorte que les copies des valeurs réelles sont rapides à effectuer. Cela signifie qu'il n'y a pas de raison pour laquelle nous voudrions empêcher `x` d'être valide après la création de la variable `y`. En d'autres termes, il n'y a pas de différence entre une copie profonde et une copie superficielle ici, donc appeler `clone` ne ferait rien de différent de la copie superficielle habituelle, et nous pouvons l'omettre.

Rust a une annotation spéciale appelée le trait `Copy` que nous pouvons ajouter à des types stockés sur la pile, comme les entiers (nous en parlerons plus en détail au chapitre 10). Si un type implémente le trait `Copy`, les variables qui l'utilisent ne sont pas déplacées, mais plutôt copiées de manière triviale, ce qui les rend encore valides après leur attribution à une autre variable.

Rust ne nous permettra pas d'ajouter l'annotation `Copy` à un type si le type, ou l'un de ses composants, a implémenté le trait `Drop`. Si le type a besoin de quelque chose de spécial lorsqu'une valeur sort de portée et que nous ajoutons l'annotation `Copy` à ce type, nous obtiendrons une erreur de compilation. Pour en savoir plus sur la manière d'ajouter l'annotation `Copy` à votre type pour implémenter le trait, consultez "Traits dérivables".

Alors, quels types implémentent le trait `Copy`? Vous pouvez vérifier la documentation pour le type donné pour être sûr, mais comme règle générale, tout groupe de valeurs scalaires simples peut implémenter `Copy`, et rien qui nécessite une allocation ou qui est une forme de ressource ne peut implémenter `Copy`. Voici quelques-uns des types qui implémentent `Copy` :

- Tous les types entiers, tels que `u32`.
- Le type booléen, `bool`, avec les valeurs `true` et `false`.
- Tous les types à virgule flottante, tels que `f64`.
- Le type caractère, `char`.
- Les tuples, s'ils ne contiennent que des types qui implémentent également `Copy`. Par exemple, `(i32, i32)` implémente `Copy`, mais `(i32, String)` ne l'implémente pas.
