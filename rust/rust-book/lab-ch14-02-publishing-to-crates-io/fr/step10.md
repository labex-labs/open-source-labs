# Publication d'une nouvelle version d'une boîte à outils existante

Lorsque vous avez apporté des modifications à votre boîte à outils et que vous êtes prêt à publier une nouvelle version, vous modifiez la valeur `version` spécifiée dans votre fichier `Cargo.toml` et republiez. Utilisez les règles de numérotation des versions sémantiques à *http://semver.org* pour décider quelle est la prochaine version appropriée en fonction des types de modifications que vous avez effectuées. Ensuite, exécutez `cargo publish` pour télécharger la nouvelle version.
