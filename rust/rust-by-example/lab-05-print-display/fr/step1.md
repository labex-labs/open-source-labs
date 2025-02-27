# Affichage

`fmt::Debug` ne semble pas très compact et propre, il est donc souvent avantageux de personnaliser l'apparence de la sortie. Cela se fait en implémentant manuellement `fmt::Display`, qui utilise le marqueur d'impression `{}`. L'implémentation ressemble à ceci :

```rust
// Importez (via `use`) le module `fmt` pour le rendre disponible.
use std::fmt;

// Définissez une structure pour laquelle `fmt::Display` sera implémenté.
// Il s'agit d'une structure tuple nommée `Structure` qui contient un `i32`.
struct Structure(i32);

// Pour utiliser le marqueur `{}`, le trait `fmt::Display` doit être
// implémenté manuellement pour le type.
impl fmt::Display for Structure {
    // Ce trait nécessite `fmt` avec cette signature exacte.
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        // Écrivez strictement le premier élément dans le flux de sortie
        // fourni : `f`. Retourne `fmt::Result` qui indique si l'opération
        // a réussi ou échoué. Notez que `write!` utilise une syntaxe
        // très similaire à `println!`.
        write!(f, "{}", self.0)
    }
}
```

`fmt::Display` peut être plus propre que `fmt::Debug`, mais cela pose un problème pour la bibliothèque `std`. Comment les types ambigus devraient-ils être affichés? Par exemple, si la bibliothèque `std` avait implémenté un seul style pour tous les `Vec<T>`, quel style devrait-il être? Serait-ce l'un de ces deux?

- `Vec<path>` : `/:/etc:/home/username:/bin` (séparé par `:`)
- `Vec<number>` : `1,2,3` (séparé par `,`)

Non, car il n'y a pas de style idéal pour tous les types et la bibliothèque `std` ne prétend pas dicter un style. `fmt::Display` n'est pas implémenté pour `Vec<T>` ou pour tout autre conteneur générique. `fmt::Debug` doit donc être utilisé pour ces cas génériques.

Cela n'est cependant pas un problème car pour tout nouveau type de _conteneur_ qui n'est _pas_ générique, `fmt::Display` peut être implémenté.

```rust
use std::fmt; // Importez `fmt`

// Une structure contenant deux nombres. `Debug` sera dérivé pour que les
// résultats puissent être comparés avec `Display`.
#[derive(Debug)]
struct MinMax(i64, i64);

// Implémentez `Display` pour `MinMax`.
impl fmt::Display for MinMax {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        // Utilisez `self.number` pour vous référer à chaque point de
        // données positionnel.
        write!(f, "({}, {})", self.0, self.1)
    }
}

// Définissez une structure où les champs sont nommables pour la
// comparaison.
#[derive(Debug)]
struct Point2D {
    x: f64,
    y: f64,
}

// De même, implémentez `Display` pour `Point2D`.
impl fmt::Display for Point2D {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        // Personnalisez pour que seulement `x` et `y` soient indiqués.
        write!(f, "x: {}, y: {}", self.x, self.y)
    }
}

fn main() {
    let minmax = MinMax(0, 14);

    println!("Comparez les structures :");
    println!("Affichage : {}", minmax);
    println!("Debug : {:?}", minmax);

    let big_range =   MinMax(-300, 300);
    let small_range = MinMax(-3, 3);

    println!("La plage large est {big} et la plage petite est {small}",
             small = small_range,
             big = big_range);

    let point = Point2D { x: 3.3, y: 7.2 };

    println!("Comparez les points :");
    println!("Affichage : {}", point);
    println!("Debug : {:?}", point);

    // Erreur. `Debug` et `Display` ont été implémentés, mais `{:b}`
    // nécessite l'implémentation de `fmt::Binary`. Cela ne fonctionnera
    // pas.
    // println!("Quel est l'aspect de Point2D en binaire : {:b}?", point);
}
```

Donc, `fmt::Display` a été implémenté mais `fmt::Binary` n'a pas, et donc ne peut pas être utilisé. `std::fmt` a de nombreux tels `traits` et chacun nécessite son propre implémentation. Cela est détaillé plus en détail dans `std::fmt`.

## Activité

Après avoir vérifié la sortie de l'exemple ci-dessus, utilisez la structure `Point2D` comme guide pour ajouter une structure `Complex` à l'exemple. Lorsqu'elle est affichée de la même manière, la sortie devrait être :

```txt
Affichage : 3.3 + 7.2i
Debug : Complex { real: 3.3, imag: 7.2 }
```
