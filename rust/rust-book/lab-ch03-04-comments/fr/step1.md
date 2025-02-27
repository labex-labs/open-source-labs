# Commentaires

Tous les programmeurs s'efforcent de rendre leur code facile à comprendre, mais parfois des explications supplémentaires sont nécessaires. Dans ces cas, les programmeurs laissent des _commentaires_ dans leur code source que le compilateur ignorera, mais qui peuvent s'avérer utiles pour les personnes qui lisent le code source.

Voici un commentaire simple :

```rust
// hello, world
```

En Rust, le style de commentaire idoine commence un commentaire avec deux barres obliques, et le commentaire se poursuit jusqu'à la fin de la ligne. Pour les commentaires qui s'étendent sur plusieurs lignes, vous devrez inclure `//` sur chaque ligne, comme ceci :

    // Donc, nous faisons quelque chose de compliqué ici, assez long pour que nous ayons besoin
    // de plusieurs lignes de commentaires pour le faire! Phew! Espérons que ce commentaire
    // expliquera ce qui se passe.

Les commentaires peuvent également être placés à la fin des lignes contenant du code :

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let lucky_number = 7; // Je sens que j'ai de la chance aujourd'hui
}
```

Mais vous verrez plus souvent qu'ils sont utilisés dans ce format, avec le commentaire sur une ligne séparée au-dessus du code qu'il annote :

Nom de fichier : `src/main.rs`

```rust
fn main() {
    // Je sens que j'ai de la chance aujourd'hui
    let lucky_number = 7;
}
```

Rust a également un autre type de commentaire, les commentaires de documentation, que nous aborderons dans "Publier une boîte à outils sur Crates.io".
