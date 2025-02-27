# Le type tuple

Un _tuple_ est une manière générale de regrouper un certain nombre de valeurs de différents types en un seul type composé. Les tuples ont une longueur fixe : une fois déclarés, ils ne peuvent pas grandir ou rétrécir en taille.

Nous créons un tuple en écrivant une liste séparée par des virgules de valeurs entre parenthèses. Chaque position dans le tuple a un type, et les types des différentes valeurs dans le tuple n'ont pas besoin d'être les mêmes. Nous avons ajouté des annotations de type optionnelles dans cet exemple :

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let tup: (i32, f64, u8) = (500, 6.4, 1);
}
```

La variable `tup` est liée à l'ensemble du tuple car un tuple est considéré comme un seul élément composé. Pour extraire les valeurs individuelles d'un tuple, nous pouvons utiliser la correspondance de motifs pour décomposer une valeur de tuple, comme ceci :

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let tup = (500, 6.4, 1);

    let (x, y, z) = tup;

    println!("La valeur de y est : {y}");
}
```

Ce programme crée d'abord un tuple et le lie à la variable `tup`. Il utilise ensuite un motif avec `let` pour prendre `tup` et le transformer en trois variables distinctes, `x`, `y` et `z`. Cela s'appelle _décomposition_ car il brise le tuple unique en trois parties. Enfin, le programme imprime la valeur de `y`, qui est `6,4`.

Nous pouvons également accéder directement à un élément de tuple en utilisant un point (`.`) suivi de l'index de la valeur que nous souhaitons accéder. Par exemple :

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let x: (i32, f64, u8) = (500, 6.4, 1);

    let five_hundred = x.0;

    let six_point_four = x.1;

    let one = x.2;
}
```

Ce programme crée le tuple `x` puis accède à chaque élément du tuple en utilisant leurs indices respectifs. Comme dans la plupart des langages de programmation, le premier index dans un tuple est 0.

Le tuple sans aucune valeur a un nom spécial, _unité_. Cette valeur et son type correspondant sont tous deux écrits `()` et représentent une valeur vide ou un type de retour vide. Les expressions renvoient implicitement la valeur d'unité si elles ne renvoient pas d'autre valeur.
