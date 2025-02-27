# Publication sur crates.io

Maintenant que vous avez créé un compte, enregistré votre jeton API, choisi un nom pour votre boîte à outils (crate) et spécifié les métadonnées requises, vous êtes prêt à publier ! Publier une boîte à outils télécharge une version spécifique sur *https://crates.io* pour qu'autrui puisse l'utiliser.

Faites attention, car une publication est _permanente_. La version ne peut jamais être écrasée et le code ne peut pas être supprimé. Un des principaux objectifs de Crates.io est d'agir comme un archive permanente de code afin que les builds de tous les projets qui dépendent de boîtes à outils de *https://crates.io* continuent de fonctionner. Autoriser la suppression de versions rendrait impossible de réaliser cet objectif. Cependant, il n'y a pas de limite au nombre de versions de boîtes à outils que vous pouvez publier.

Exécutez à nouveau la commande `cargo publish`. Elle devrait réussir maintenant :

```bash
$ cargo publish
    Updating crates.io index
   Packaging guessing_game v0.1.0 (file:///projects/guessing_game)
   Verifying guessing_game v0.1.0 (file:///projects/guessing_game)
   Compiling guessing_game v0.1.0
(file:///projects/guessing_game/target/package/guessing_game-0.1.0)
    Finished dev [unoptimized + debuginfo] target(s) in 0.19s
   Uploading guessing_game v0.1.0 (file:///projects/guessing_game)
```

Félicitations ! Vous avez désormais partagé votre code avec la communauté Rust et n'importe qui peut facilement ajouter votre boîte à outils comme dépendance de leur projet.
