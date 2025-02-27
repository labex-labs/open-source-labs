# Déconstruction de structs

La Liste 18-12 montre une struct `Point` avec deux champs, `x` et `y`, que nous pouvons séparer à l'aide d'un motif avec une instruction `let`.

Nom de fichier : `src/main.rs`

```rust
struct Point {
    x: i32,
    y: i32,
}

fn main() {
    let p = Point { x: 0, y: 7 };

    let Point { x: a, y: b } = p;
    assert_eq!(0, a);
    assert_eq!(7, b);
}
```

Liste 18-12 : Déconstruction des champs d'une struct en variables séparées

Ce code crée les variables `a` et `b` qui correspondent aux valeurs des champs `x` et `y` de la struct `p`. Cet exemple montre que les noms des variables dans le motif n'ont pas besoin de correspondre aux noms des champs de la struct. Cependant, il est courant de faire correspondre les noms des variables aux noms des champs pour faciliter la mémoire de savoir quelles variables proviennent de quels champs. En raison de cette utilisation courante, et parce que l'écriture `let Point { x: x, y: y } = p;` contient beaucoup de duplication, Rust a une forme abrégée pour les motifs qui correspondent aux champs de struct : vous n'avez qu'à lister le nom du champ de struct, et les variables créées à partir du motif auront les mêmes noms. La Liste 18-13 se comporte de la même manière que le code de la Liste 18-12, mais les variables créées dans le motif `let` sont `x` et `y` au lieu de `a` et `b`.

Nom de fichier : `src/main.rs`

```rust
struct Point {
    x: i32,
    y: i32,
}

fn main() {
    let p = Point { x: 0, y: 7 };

    let Point { x, y } = p;
    assert_eq!(0, x);
    assert_eq!(7, y);
}
```

Liste 18-13 : Déconstruction des champs de struct en utilisant la forme abrégée des champs de struct

Ce code crée les variables `x` et `y` qui correspondent aux champs `x` et `y` de la variable `p`. Le résultat est que les variables `x` et `y` contiennent les valeurs de la struct `p`.

Nous pouvons également déconstruire avec des valeurs littérales en tant que partie du motif de struct plutôt que de créer des variables pour tous les champs. Cela nous permet de tester certains des champs pour des valeurs particulières tout en créant des variables pour déconstruire les autres champs.

Dans la Liste 18-14, nous avons une expression `match` qui sépare les valeurs `Point` en trois cas : les points qui se trouvent directement sur l'axe `x` (ce qui est vrai lorsque `y = 0`), sur l'axe `y` (`x = 0`), ou sur aucun des deux axes.

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let p = Point { x: 0, y: 7 };

    match p {
        Point { x, y: 0 } => println!("On the x axis at {x}"),
        Point { x: 0, y } => println!("On the y axis at {y}"),
        Point { x, y } => {
            println!("On neither axis: ({x}, {y})");
        }
    }
}
```

Liste 18-14 : Déconstruction et correspondance de valeurs littérales dans un motif

Le premier bras correspondra à tout point qui se trouve sur l'axe `x` en spécifiant que le champ `y` correspond si sa valeur correspond au littéral `0`. Le motif crée toujours une variable `x` que nous pouvons utiliser dans le code de ce bras.

De manière similaire, le second bras correspond à tout point sur l'axe `y` en spécifiant que le champ `x` correspond si sa valeur est `0` et crée une variable `y` pour la valeur du champ `y`. Le troisième bras ne spécifie aucun littéral, donc il correspond à tout autre `Point` et crée des variables pour les deux champs `x` et `y`.

Dans cet exemple, la valeur `p` correspond au second bras en raison de `x` qui contient un `0`, donc ce code imprimera `On the y axis at 7`.

Rappelez-vous qu'une expression `match` arrête de vérifier les bras une fois qu'elle a trouvé le premier motif correspondant, donc même si `Point { x: 0, y: 0}` est sur l'axe `x` et l'axe `y`, ce code n'imprimera que `On the x axis at 0`.
