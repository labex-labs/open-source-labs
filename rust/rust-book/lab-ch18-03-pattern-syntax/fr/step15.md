# Parties restantes d'une valeur avec..

Avec des valeurs qui ont de nombreuses parties, nous pouvons utiliser la syntaxe `..` pour utiliser des parties spécifiques et ignorer le reste, évitant ainsi d'avoir à énumérer des underscores pour chaque valeur ignorée. Le motif `..` ignore toutes les parties d'une valeur que nous n'avons pas explicitement correspondues dans le reste du motif. Dans la Liste 18-23, nous avons une structure `Point` qui stocke une coordonnée dans l'espace tridimensionnel. Dans l'expression `match`, nous voulons opérer uniquement sur la coordonnée `x` et ignorer les valeurs dans les champs `y` et `z`.

Nom de fichier : `src/main.rs`

```rust
struct Point {
    x: i32,
    y: i32,
    z: i32,
}

let origin = Point { x: 0, y: 0, z: 0 };

match origin {
    Point { x,.. } => println!("x is {x}"),
}
```

Liste 18-23 : Ignorer tous les champs d'un `Point` sauf `x` en utilisant `..`

Nous listons la valeur `x` puis nous incluons simplement le motif `..`. Cela est plus rapide que d'avoir à énumérer `y: _` et `z: _`, en particulier lorsque nous travaillons avec des structs qui ont de nombreux champs dans des situations où seulement un ou deux champs sont pertinents.

La syntaxe `..` s'étendra à autant de valeurs qu'il en faut. La Liste 18-24 montre comment utiliser `..` avec un tuple.

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let numbers = (2, 4, 8, 16, 32);

    match numbers {
        (first,.., last) => {
            println!("Some numbers: {first}, {last}");
        }
    }
}
```

Liste 18-24 : Correspondre uniquement aux premières et dernières valeurs d'un tuple et ignorer toutes les autres valeurs

Dans ce code, les premières et dernières valeurs sont correspondues avec `first` et `last`. Le `..` correspondra et ignorera tout le reste.

Cependant, l'utilisation de `..` doit être sans ambiguïté. Si il n'est pas clair quelles valeurs sont destinées à être correspondues et lesquelles doivent être ignorées, Rust nous donnera une erreur. La Liste 18-25 montre un exemple d'utilisation ambiguë de `..`, donc elle ne se compilera pas.

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let numbers = (2, 4, 8, 16, 32);

    match numbers {
        (.., second,..) => {
            println!("Some numbers: {second}");
        },
    }
}
```

Liste 18-25 : Tentative d'utilisation ambiguë de `..`

Lorsque nous compilons cet exemple, nous obtenons cette erreur :

```bash
error: `..` can only be used once per tuple pattern
 --> src/main.rs:5:22
  |
5 |         (.., second,..) => {
  |          --          ^^ can only be used once per tuple pattern
  |          |
  |          previously used here
```

Il est impossible pour Rust de déterminer combien de valeurs dans le tuple doivent être ignorées avant de correspondre une valeur avec `second` et puis combien de valeurs supplémentaires doivent être ignorées ensuite. Ce code pourrait signifier que nous voulons ignorer `2`, lier `second` à `4` et puis ignorer `8`, `16` et `32` ; ou que nous voulons ignorer `2` et `4`, lier `second` à `8` et puis ignorer `16` et `32` ; etc. Le nom de variable `second` n'a rien de spécial pour Rust, donc nous obtenons une erreur du compilateur car utiliser `..` en deux endroits comme ceci est ambigu.
