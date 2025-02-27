# Dans les définitions de méthodes

Nous pouvons implémenter des méthodes sur des structs et des enums (comme nous l'avons fait au Chapitre 5) et utiliser des types génériques dans leurs définitions également. La Liste 10-9 montre la struct `Point<T>` que nous avons définie dans la Liste 10-6 avec une méthode nommée `x` implémentée sur elle.

Nom de fichier : `src/main.rs`

```rust
struct Point<T> {
    x: T,
    y: T,
}

impl<T> Point<T> {
    fn x(&self) -> &T {
        &self.x
    }
}

fn main() {
    let p = Point { x: 5, y: 10 };

    println!("p.x = {}", p.x());
}
```

Liste 10-9 : Implémentation d'une méthode nommée `x` sur la struct `Point<T>` qui retournera une référence au champ `x` du type `T`

Ici, nous avons défini une méthode nommée `x` sur `Point<T>` qui retourne une référence aux données dans le champ `x`.

Notez que nous devons déclarer `T` juste après `impl` afin que nous puissions utiliser `T` pour spécifier que nous implémentons des méthodes sur le type `Point<T>`. En déclarant `T` comme un type générique après `impl`, Rust peut identifier que le type entre crochets dans `Point` est un type générique plutôt qu'un type concret. Nous aurions pu choisir un nom différent pour ce paramètre générique que le paramètre générique déclaré dans la définition de la struct, mais utiliser le même nom est la convention. Les méthodes écrites à l'intérieur d'un `impl` qui déclare le type générique seront définies sur n'importe quelle instance du type, peu importe quel type concret se substitue finalement au type générique.

Nous pouvons également spécifier des contraintes sur les types génériques lors de la définition de méthodes sur le type. Par exemple, nous pourrions implémenter des méthodes uniquement sur des instances de `Point<f32>` plutôt que sur des instances de `Point<T>` avec n'importe quel type générique. Dans la Liste 10-10, nous utilisons le type concret `f32`, ce qui signifie que nous ne déclarons aucun type après `impl`.

Nom de fichier : `src/main.rs`

```rust
impl Point<f32> {
    fn distance_from_origin(&self) -> f32 {
        (self.x.powi(2) + self.y.powi(2)).sqrt()
    }
}
```

Liste 10-10 : Un bloc `impl` qui ne s'applique qu'à une struct avec un type concret particulier pour le paramètre de type générique `T`

Ce code signifie que le type `Point<f32>` aura une méthode `distance_from_origin` ; les autres instances de `Point<T>` où `T` n'est pas du type `f32` n'auront pas cette méthode définie. La méthode mesure à quelle distance notre point se trouve du point aux coordonnées (0.0, 0.0) et utilise des opérations mathématiques qui ne sont disponibles que pour les types à virgule flottante.

Les paramètres de type générique dans une définition de struct ne sont pas toujours les mêmes que ceux que vous utilisez dans les signatures de méthodes de cette même struct. La Liste 10-11 utilise les types génériques `X1` et `Y1` pour la struct `Point` et `X2` `Y2` pour la signature de la méthode `mixup` pour rendre l'exemple plus clair. La méthode crée une nouvelle instance de `Point` avec la valeur de `x` de la `Point` `self` (du type `X1`) et la valeur de `y` de la `Point` passée en argument (du type `Y2`).

Nom de fichier : `src/main.rs`

```rust
struct Point<X1, Y1> {
    x: X1,
    y: Y1,
}

1 impl<X1, Y1> Point<X1, Y1> {
  2 fn mixup<X2, Y2>(
        self,
        other: Point<X2, Y2>,
    ) -> Point<X1, Y2> {
        Point {
            x: self.x,
            y: other.y,
        }
    }
}

fn main() {
  3 let p1 = Point { x: 5, y: 10.4 };
  4 let p2 = Point { x: "Hello", y: 'c' };

  5 let p3 = p1.mixup(p2);

  6 println!("p3.x = {}, p3.y = {}", p3.x, p3.y);
}
```

Liste 10-11 : Une méthode qui utilise des types génériques différents de sa définition de struct

Dans `main`, nous avons défini une `Point` qui a un `i32` pour `x` (avec la valeur `5`) et un `f64` pour `y` (avec la valeur `10.4` \[3\]). La variable `p2` est une struct `Point` qui a une tranche de chaîne de caractères pour `x` (avec la valeur `"Hello"`) et un `char` pour `y` (avec la valeur `c` \[4\]). Appeler `mixup` sur `p1` avec l'argument `p2` nous donne `p3` \[5\], qui aura un `i32` pour `x` car `x` vient de `p1`. La variable `p3` aura un `char` pour `y` car `y` vient de `p2`. L'appel à la macro `println!` \[6\] affichera `p3.x = 5, p3.y = c`.

Le but de cet exemple est de démontrer une situation dans laquelle certains paramètres génériques sont déclarés avec `impl` et certains sont déclarés avec la définition de la méthode. Ici, les paramètres génériques `X1` et `Y1` sont déclarés après `impl` \[1\] car ils sont liés à la définition de la struct. Les paramètres génériques `X2` et `Y2` sont déclarés après `fn mixup` \[2\] car ils ne sont pertinents que pour la méthode.
