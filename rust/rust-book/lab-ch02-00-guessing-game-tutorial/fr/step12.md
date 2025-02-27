# Mettre à jour un paquet pour obtenir une nouvelle version

Lorsque vous _voulez_ mettre à jour un paquet, Cargo fournit la commande `update`, qui ignorera le fichier _Cargo.lock_ et déterminera toutes les dernières versions qui répondent à vos spécifications dans `Cargo.toml`. Cargo écrira ensuite ces versions dans le fichier _Cargo.lock_. Sinon, par défaut, Cargo ne cherchera que les versions supérieures à 0.8.5 et inférieures à 0.9.0. Si le paquet `rand` a publié les deux nouvelles versions 0.8.6 et 0.9.0, vous verriez ceci si vous exécutiez `cargo update` :

```bash
$ cargo update
Updating crates.io index
Updating rand v0.8.5 - > v0.8.6
```

Cargo ignore la version 0.9.0. À ce stade, vous remarqueriez également un changement dans votre fichier _Cargo.lock_ indiquant que la version du paquet `rand` que vous utilisez maintenant est 0.8.6. Pour utiliser la version 0.9.0 de `rand` ou n'importe quelle version dans la série 0.9.\_x\_, vous devriez mettre à jour le fichier `Cargo.toml` pour qu'il ressemble à ceci :

```rust
[dependencies]
rand = "0.9.0"
```

La prochaine fois que vous exécuterez `cargo build`, Cargo mettra à jour le registre des paquets disponibles et réévaluera vos exigences en `rand` selon la nouvelle version que vous avez spécifiée.

Il y a beaucoup plus à dire sur Cargo et son écosystème, que nous aborderons au Chapitre 14, mais pour l'instant, voilà tout ce que vous avez besoin de savoir. Cargo facilite grandement la réutilisation de bibliothèques, de sorte que les Rustaceans sont capables d'écrire de plus petits projets assemblés à partir de plusieurs packages.
