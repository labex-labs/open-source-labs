# Creating Idiomatic use Paths

Dans la Liste 7-11, vous avez peut-être été curieux de savoir pourquoi nous avons spécifié `use crate::front_of_house::hosting` puis appelé `hosting::add_to_waitlist` dans `eat_at_restaurant`, plutôt que de spécifier le chemin `use` jusqu'à la fonction `add_to_waitlist` pour obtenir le même résultat, comme dans la Liste 7-13.

Nom de fichier : `src/lib.rs`

```rust
mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

use crate::front_of_house::hosting::add_to_waitlist;

pub fn eat_at_restaurant() {
    add_to_waitlist();
}
```

Liste 7-13 : Amener la fonction `add_to_waitlist` dans la portée avec `use`, ce qui n'est pas idiomatique

Bien que les Listes 7-11 et 7-13 accomplissent la même tâche, la Liste 7-11 est la manière idiomatique d'amener une fonction dans la portée avec `use`. Amener le module parent de la fonction dans la portée avec `use` signifie que nous devons spécifier le module parent lorsqu'appelons la fonction. Spécifier le module parent lorsqu'on appelle la fonction montre clairement que la fonction n'est pas définie localement tout en réduisant au minimum la répétition du chemin complet. Le code de la Liste 7-13 est ambigu quant à la définition de `add_to_waitlist`.

D'un autre côté, lorsqu'on amène des structs, des enums et autres éléments avec `use`, il est idiomatique de spécifier le chemin complet. La Liste 7-14 montre la manière idiomatique d'amener la struct `HashMap` de la bibliothèque standard dans la portée d'un crate binaire.

Nom de fichier : `src/main.rs`

```rust
use std::collections::HashMap;

fn main() {
    let mut map = HashMap::new();
    map.insert(1, 2);
}
```

Liste 7-14 : Amener `HashMap` dans la portée d'une manière idiomatique

Il n'y a pas de raison forte derrière cet idiome : c'est simplement la convention qui est apparue, et les gens sont habitués à lire et à écrire du code Rust de cette manière.

L'exception à cet idiome est si nous amenons deux éléments avec le même nom dans la portée avec des instructions `use`, car Rust ne permet pas cela. La Liste 7-15 montre comment amener deux types `Result` dans la portée qui ont le même nom mais des modules parents différents, et comment y faire référence.

Nom de fichier : `src/lib.rs`

```rust
use std::fmt;
use std::io;

fn function1() -> fmt::Result {
    --snip--
}

fn function2() -> io::Result<()> {
    --snip--
}
```

Liste 7-15 : Amener deux types avec le même nom dans la même portée nécessite d'utiliser leurs modules parents.

Comme vous pouvez le voir, en utilisant les modules parents, on distingue les deux types `Result`. Si au lieu de cela nous spécifions `use std::fmt::Result` et `use std::io::Result`, nous aurons deux types `Result` dans la même portée, et Rust ne saura pas lequel nous voulons lorsque nous utilisons `Result`.
