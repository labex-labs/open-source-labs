# Splitting Code into a Library Crate

Notre projet `minigrep` va bien pour l'instant! Maintenant, nous allons diviser le fichier `src/main.rs` et déplacer du code dans le fichier `src/lib.rs`. Ainsi, nous pourrons tester le code et avoir un fichier `src/main.rs` avec moins de responsabilités.

Déplaçons tout le code qui n'est pas dans la fonction `main` de `src/main.rs` vers `src/lib.rs` :

- La définition de la fonction `run`
- Les instructions `use` pertinentes
- La définition de `Config`
- La définition de la fonction `Config::build`

Le contenu de `src/lib.rs` devrait avoir les signatures montrées dans le Listing 12-13 (nous avons omis le corps des fonctions pour la brièveté). Notez que cela ne compilera pas jusqu'à ce que nous modifions `src/main.rs` dans le Listing 12-14.

Nom du fichier : `src/lib.rs`

```rust
use std::error::Error;
use std::fs;

pub struct Config {
    pub query: String,
    pub file_path: String,
}

impl Config {
    pub fn build(
        args: &[String],
    ) -> Result<Config, &'static str> {
        --snip--
    }
}

pub fn run(config: Config) -> Result<(), Box<dyn Error>> {
    --snip--
}
```

Listing 12-13 : Décalage de `Config` et `run` dans `src/lib.rs`

Nous avons largement utilisé le mot clé `pub` : sur `Config`, sur ses champs et sa méthode `build`, et sur la fonction `run`. Maintenant, nous avons une boîte à outils de bibliothèque qui a une API publique que nous pouvons tester!

Maintenant, nous devons amener le code que nous avons déplacé vers `src/lib.rs` dans la portée de la boîte à outils binaire dans `src/main.rs`, comme montré dans le Listing 12-14.

Nom du fichier : `src/main.rs`

```rust
use std::env;
use std::process;

use minigrep::Config;

fn main() {
    --snip--
    if let Err(e) = minigrep::run(config) {
        --snip--
    }
}
```

Listing 12-14 : Utilisation de la boîte à outils de bibliothèque `minigrep` dans `src/main.rs`

Nous ajoutons une ligne `use minigrep::Config` pour amener le type `Config` de la boîte à outils de bibliothèque dans la portée de la boîte à outils binaire, et nous préfixons la fonction `run` avec le nom de notre boîte à outils. Maintenant, toutes les fonctionnalités devraient être connectées et devraient fonctionner. Exécutez le programme avec `cargo run` et assurez-vous que tout fonctionne correctement.

Phew! C'était beaucoup de travail, mais nous nous sommes préparés à la réussite pour l'avenir. Maintenant, il est beaucoup plus facile de gérer les erreurs, et nous avons rendu le code plus modulaire. Presque tout notre travail sera désormais effectué dans `src/lib.rs`.

Prenons avantage de cette nouvelle modularité en faisant quelque chose qui aurait été difficile avec l'ancien code mais est facile avec le nouveau code : écrivons quelques tests!
