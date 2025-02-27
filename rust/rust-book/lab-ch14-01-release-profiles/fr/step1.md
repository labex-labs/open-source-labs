# Personnaliser les builds avec des profils de publication

En Rust, les _profils de publication_ sont des profils prédéfinis et personnalisables avec différentes configurations qui permettent à un programmeur de mieux contrôler diverses options pour compiler le code. Chaque profil est configuré indépendamment des autres.

Cargo a deux profils principaux : le profil `dev` que Cargo utilise lorsque vous exécutez `cargo build`, et le profil `release` que Cargo utilise lorsque vous exécutez `cargo build --release`. Le profil `dev` est défini avec de bonnes valeurs par défaut pour le développement, et le profil `release` a de bonnes valeurs par défaut pour les builds de publication.

Ces noms de profil peuvent vous être familiers à partir de la sortie de vos builds :

```bash
$ cargo build
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
$ cargo build --release
    Finished release [optimized] target(s) in 0.0s
```

Le `dev` et le `release` sont ces différents profils utilisés par le compilateur.

Cargo a des paramètres par défaut pour chacun des profils qui s'appliquent lorsque vous n'avez pas explicitement ajouté de sections `[profile.*]` dans le fichier `Cargo.toml` du projet. En ajoutant des sections `[profile.*]` pour n'importe quel profil que vous voulez personnaliser, vous substituez n'importe quel sous-ensemble des paramètres par défaut. Par exemple, voici les valeurs par défaut pour le paramètre `opt-level` des profils `dev` et `release` :

Nom de fichier : `Cargo.toml`

```tomltoml
[profile.dev]
opt-level = 0

[profile.release]
opt-level = 3
```

Le paramètre `opt-level` contrôle le nombre d'optimisations que Rust appliquera à votre code, avec une plage de 0 à 3. Appliquer plus d'optimisations prolonge le temps de compilation, donc si vous êtes en développement et que vous compilez souvent votre code, vous voudrez moins d'optimisations pour compiler plus rapidement même si le code résultant exécute plus lentement. La valeur par défaut de `opt-level` pour `dev` est donc `0`. Lorsque vous êtes prêt à publier votre code, il est préférable de consacrer plus de temps à la compilation. Vous ne compilerez qu'une fois en mode release, mais vous exécuterez le programme compilé de nombreuses fois, donc le mode release échange un temps de compilation plus long contre un code qui exécute plus rapidement. C'est pourquoi la valeur par défaut de `opt-level` pour le profil `release` est `3`.

Vous pouvez substituer un paramètre par défaut en ajoutant une valeur différente pour celui-ci dans `Cargo.toml`. Par exemple, si nous voulons utiliser le niveau d'optimisation 1 dans le profil de développement, nous pouvons ajouter ces deux lignes au fichier `Cargo.toml` de notre projet :

Nom de fichier : `Cargo.toml`

```tomltoml
[profile.dev]
opt-level = 1
```

Ce code substitue la valeur par défaut de `0`. Maintenant, lorsque nous exécutons `cargo build`, Cargo utilisera les paramètres par défaut du profil `dev` plus notre personnalisation de `opt-level`. Parce que nous avons défini `opt-level` sur `1`, Cargo appliquera plus d'optimisations que par défaut, mais pas autant qu'en mode release.

Pour obtenir la liste complète des options de configuration et des paramètres par défaut pour chaque profil, consultez la documentation de Cargo à *https://doc.rust-lang.org/cargo/reference/profiles.html*.
