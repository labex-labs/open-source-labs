# Providing New Names with the as Keyword

Il existe une autre solution au problème d'amener deux types de même nom dans la même portée avec `use` : après le chemin, nous pouvons spécifier `as` et un nouveau nom local, ou _alias_, pour le type. La Liste 7-16 montre une autre manière d'écrire le code de la Liste 7-15 en renommant l'un des deux types `Result` à l'aide de `as`.

Nom de fichier : `src/lib.rs`

```rust
use std::fmt::Result;
use std::io::Result as IoResult;

fn function1() -> Result {
    --snip--
}

fn function2() -> IoResult<()> {
    --snip--
}
```

Liste 7-16 : Renommer un type lorsqu'il est amené dans la portée avec le mot-clé `as`

Dans la deuxième instruction `use`, nous avons choisi le nouveau nom `IoResult` pour le type `std::io::Result`, qui ne rentrera pas en conflit avec le `Result` de `std::fmt` que nous avons également amené dans la portée. Les Listes 7-15 et 7-16 sont considérées comme idiomatiques, donc le choix est laissé à vous!
