# Mettre en version obsolète des versions sur Crates.io avec cargo yank

Bien que vous ne puissiez pas supprimer les versions antérieures d'une boîte à outils (crate), vous pouvez empêcher tout projet futur d'ajouter ces versions comme nouvelle dépendance. Cela est utile lorsqu'une version d'une boîte à outils est cassée pour une raison ou une autre. Dans de telles situations, Cargo prend en charge le retrait d'une version d'une boîte à outils.

Retirer une version empêche les nouveaux projets de dépendre de cette version tout en permettant à tous les projets existants qui en dépendent de continuer. Essentiellement, un retrait signifie que tous les projets avec un fichier _Cargo.lock_ ne se casseront pas et que tous les futurs fichiers _Cargo.lock_ générés n'utiliseront pas la version retirée.

Pour retirer une version d'une boîte à outils, dans le répertoire de la boîte à outils que vous avez publiée précédemment, exécutez `cargo yank` et spécifiez quelle version vous voulez retirer. Par exemple, si nous avons publié une boîte à outils nommée `guessing_game` version 1.0.1 et que nous voulons la retirer, dans le répertoire du projet `guessing_game` nous exécuterions :

```bash
$ cargo yank --vers 1.0.1
Updating crates.io index
Yank guessing_game@1.0.1
```

En ajoutant `--undo` à la commande, vous pouvez également annuler un retrait et autoriser les projets à recommencer à dépendre d'une version :

```bash
$ cargo yank --vers 1.0.1 --undo
Updating crates.io index
Unyank guessing_game@1.0.1
```

Un retrait _ne supprime pas_ de code. Il ne peut pas, par exemple, supprimer des secrets accidentellement téléchargés. Si cela se produit, vous devez réinitialiser immédiatement ces secrets.
