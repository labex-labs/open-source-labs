# Dans les définitions de structs

Nous pouvons également définir des structs pour utiliser un paramètre de type générique dans un ou plusieurs champs en utilisant la syntaxe `< >`. La Liste 10-6 définit une struct `Point<T>` pour stocker les valeurs des coordonnées `x` et `y` de n'importe quel type.

Nom de fichier : `src/main.rs`

```rust
1 struct Point<T> {
  2 x: T,
  3 y: T,
}

fn main() {
    let integer = Point { x: 5, y: 10 };
    let float = Point { x: 1.0, y: 4.0 };
}
```

Liste 10-6 : Une struct `Point<T>` qui stocke les valeurs `x` et `y` du type `T`

La syntaxe pour utiliser des génériques dans les définitions de structs est similaire à celle utilisée dans les définitions de fonctions. Tout d'abord, nous déclarons le nom du paramètre de type entre crochets angulaires juste après le nom de la struct \[1\]. Ensuite, nous utilisons le type générique dans la définition de la struct où nous spécifierions normalement des types de données concrètes \[23\].

Notez que parce que nous avons utilisé seulement un type générique pour définir `Point<T>`, cette définition indique que la struct `Point<T>` est générique sur un certain type `T`, et les champs `x` et `y` sont _tous deux_ de ce même type, quel que soit ce type. Si nous créons une instance d'un `Point<T>` qui a des valeurs de types différents, comme dans la Liste 10-7, notre code ne compilera pas.

Nom de fichier : `src/main.rs`

```rust
struct Point<T> {
    x: T,
    y: T,
}

fn main() {
    let wont_work = Point { x: 5, y: 4.0 };
}
```

Liste 10-7 : Les champs `x` et `y` doivent être du même type car les deux ont le même type de données générique `T`.

Dans cet exemple, lorsque nous assignons la valeur entière `5` à `x`, nous informons le compilateur que le type générique `T` sera un entier pour cette instance de `Point<T>`. Ensuite, lorsque nous spécifions `4.0` pour `y`, que nous avons défini pour avoir le même type que `x`, nous obtiendrons une erreur de mismatch de type comme celle-ci :

```bash
error[E0308]: mismatched types
 --> src/main.rs:7:38
  |
7 |     let wont_work = Point { x: 5, y: 4.0 };
  |                                      ^^^ expected integer, found floating-
point number
```

Pour définir une struct `Point` où `x` et `y` sont tous deux des génériques mais peuvent avoir des types différents, nous pouvons utiliser plusieurs paramètres de type générique. Par exemple, dans la Liste 10-8, nous modifions la définition de `Point` pour qu'elle soit générique sur les types `T` et `U` où `x` est du type `T` et `y` est du type `U`.

Nom de fichier : `src/main.rs`

```rust
struct Point<T, U> {
    x: T,
    y: U,
}

fn main() {
    let both_integer = Point { x: 5, y: 10 };
    let both_float = Point { x: 1.0, y: 4.0 };
    let integer_and_float = Point { x: 5, y: 4.0 };
}
```

Liste 10-8 : Un `Point<T, U>` générique sur deux types de sorte que `x` et `y` puissent être des valeurs de types différents

Maintenant, toutes les instances de `Point` montrées sont autorisées! Vous pouvez utiliser autant de paramètres de type générique dans une définition que vous le souhaitez, mais en utiliser plus d'un ou deux rend votre code difficile à lire. Si vous constatez que vous avez besoin de nombreux types génériques dans votre code, cela pourrait indiquer que votre code a besoin d'être restructuré en parties plus petites.
