# Hello, Cargo

Cargo est le système de construction et le gestionnaire de packages de Rust. La plupart des Rustaceens utilisent cet outil pour gérer leurs projets Rust car Cargo gère de nombreuses tâches pour vous, telles que la construction de votre code, le téléchargement des bibliothèques dont votre code dépend et la construction de ces bibliothèques. (Nous appelons les bibliothèques dont votre code a besoin _dépendances_.)

Les programmes Rust les plus simples, comme celui que nous avons écrit jusqu'à présent, n'ont pas de dépendances. Si nous avions construit le projet "Hello, world!" avec Cargo, il n'utiliserait que la partie de Cargo qui gère la construction de votre code. Lorsque vous écrivez des programmes Rust plus complexes, vous ajouterez des dépendances, et si vous commencez un projet en utilisant Cargo, ajouter des dépendances sera beaucoup plus facile.

Parce que la vaste majorité des projets Rust utilisent Cargo, le reste de ce livre suppose que vous utilisez également Cargo. Cargo est installé avec Rust si vous avez utilisé les installateurs officiels discutés dans "Installation". Si vous avez installé Rust par d'autres moyens, vérifiez si Cargo est installé en tapant la commande suivante dans votre terminal :

```bash
cargo --version
```

Si vous voyez un numéro de version, vous l'avez! Si vous voyez une erreur, telle que `command not found`, consultez la documentation de votre méthode d'installation pour déterminer comment installer Cargo séparément.
