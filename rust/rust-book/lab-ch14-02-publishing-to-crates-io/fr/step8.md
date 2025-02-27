# Ajout de métadonnées à une nouvelle boîte à outils (crate)

Disons que vous avez une boîte à outils que vous souhaitez publier. Avant de publier, vous devrez ajouter certaines métadonnées dans la section `[package]` du fichier `Cargo.toml` de la boîte à outils.

Votre boîte à outils devra avoir un nom unique. Lorsque vous travaillez sur une boîte à outils localement, vous pouvez nommer la boîte à outils comme vous le souhaitez. Cependant, les noms de boîtes à outils sur *https://crates.io* sont attribués selon le principe "premier arrivé, premier servi". Une fois un nom de boîte à outils pris, personne d'autre ne peut publier une boîte à outils avec ce nom. Avant d'essayer de publier une boîte à outils, recherchez le nom que vous voulez utiliser. Si le nom a déjà été utilisé, vous devrez trouver un autre nom et éditer le champ `name` dans le fichier `Cargo.toml` sous la section `[package]` pour utiliser le nouveau nom pour la publication, comme ceci :

Nom du fichier : `Cargo.toml`

```tomlrust
[package]
name = "guessing_game"
```

Même si vous avez choisi un nom unique, lorsque vous exécutez `cargo publish` pour publier la boîte à outils à ce stade, vous obtiendrez un avertissement puis une erreur :

```bash
$ cargo publish
    Updating crates.io index
warning: manifest has no description, license, license-file, documentation,
homepage or repository.
See https://doc.rust-lang.org/cargo/reference/manifest.html#package-metadata
for more info.
--snip--
error: failed to publish to registry at https://crates.io

Caused by:
  the remote server responded with an error: missing or empty metadata fields:
description, license. Please see https://doc.rust-
lang.org/cargo/reference/manifest.html for how to upload metadata
```

Cela résulte en une erreur car vous manquez d'informations cruciales : une description et une licence sont requises pour que les gens sachent ce que fait votre boîte à outils et sous quelles conditions ils peuvent l'utiliser. Dans `Cargo.toml`, ajoutez une description d'une ou deux phrases, car elle apparaîtra avec votre boîte à outils dans les résultats de recherche. Pour le champ `license`, vous devez donner une _valeur d'identifiant de licence_. Le Software Package Data Exchange (SPDX) de The Linux Foundation à *http://spdx.org/licenses* liste les identifiants que vous pouvez utiliser pour cette valeur. Par exemple, pour spécifier que vous avez licencié votre boîte à outils sous la licence MIT, ajoutez l'identifiant `MIT` :

Nom du fichier : `Cargo.toml`

```toml
[package]
name = "guessing_game"
license = "MIT"
```

Si vous voulez utiliser une licence qui n'apparaît pas dans le SPDX, vous devrez placer le texte de cette licence dans un fichier, inclure le fichier dans votre projet, puis utiliser `license-file` pour spécifier le nom de ce fichier au lieu d'utiliser la clé `license`.

La présentation des licences appropriées pour votre projet est en dehors des limites de ce livre. De nombreuses personnes dans la communauté Rust licencient leurs projets de la même manière que Rust en utilisant une double licence `MIT OU Apache-2.0`. Cette pratique montre également que vous pouvez également spécifier plusieurs identifiants de licence séparés par `OU` pour avoir plusieurs licences pour votre projet.

Avec un nom unique, la version, votre description et une licence ajoutées, le fichier `Cargo.toml` d'un projet prêt à être publié pourrait ressembler à ceci :

Nom du fichier : `Cargo.toml`

```toml
[package]
name = "guessing_game"
version = "0.1.0"
edition = "2021"
description = "Un jeu amusant où vous devinez le nombre que
l'ordinateur a choisi."
license = "MIT OR Apache-2.0"

[dependencies]
```

La documentation de Cargo à *https://doc.rust-lang.org/cargo* décrit d'autres métadonnées que vous pouvez spécifier pour vous assurer que les autres peuvent découvrir et utiliser votre boîte à outils plus facilement.
