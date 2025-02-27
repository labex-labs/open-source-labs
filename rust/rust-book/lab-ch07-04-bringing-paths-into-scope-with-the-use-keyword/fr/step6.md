# Using Nested Paths to Clean Up Large use Lists

Si nous utilisons plusieurs éléments définis dans la même crate ou le même module, énumérer chaque élément sur une ligne distincte peut prendre beaucoup d'espace vertical dans nos fichiers. Par exemple, ces deux instructions `use` que nous avions dans le jeu de devinette de la Liste 2-4 amènent des éléments de `std` dans la portée :

Nom de fichier : `src/main.rs`

```rust
--snip--
use std::cmp::Ordering;
use std::io;
--snip--
```

Au lieu de cela, nous pouvons utiliser des chemins imbriqués pour amener les mêmes éléments dans la portée en une seule ligne. Nous le faisons en spécifiant la partie commune du chemin, suivie de deux points, puis des accolades autour d'une liste des parties du chemin qui diffèrent, comme montré dans la Liste 7-18.

Nom de fichier : `src/main.rs`

```rust
--snip--
use std::{cmp::Ordering, io};
--snip--
```

Liste 7-18 : Spécifier un chemin imbriqué pour amener plusieurs éléments avec le même préfixe dans la portée

Dans des programmes plus grands, amener de nombreux éléments dans la portée à partir de la même crate ou module en utilisant des chemins imbriqués peut réduire considérablement le nombre d'instructions `use` séparées nécessaires!

Nous pouvons utiliser un chemin imbriqué à n'importe quel niveau dans un chemin, ce qui est utile lorsqu'on combine deux instructions `use` qui partagent un sous-chemin. Par exemple, la Liste 7-19 montre deux instructions `use` : l'une qui amène `std::io` dans la portée et l'autre qui amène `std::io::Write` dans la portée.

Nom de fichier : `src/lib.rs`

```rust
use std::io;
use std::io::Write;
```

Liste 7-19 : Deux instructions `use` dont l'une est un sous-chemin de l'autre

La partie commune de ces deux chemins est `std::io`, et c'est le premier chemin complet. Pour fusionner ces deux chemins en une seule instruction `use`, nous pouvons utiliser `self` dans le chemin imbriqué, comme montré dans la Liste 7-20.

Nom de fichier : `src/lib.rs`

```rust
use std::io::{self, Write};
```

Liste 7-20 : Combiner les chemins de la Liste 7-19 en une seule instruction `use`

Cette ligne amène `std::io` et `std::io::Write` dans la portée.
