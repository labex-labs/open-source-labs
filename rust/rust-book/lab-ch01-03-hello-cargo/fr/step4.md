# Compilation pour la version de production

Lorsque votre projet est finalement prêt à être publié, vous pouvez utiliser `cargo build --release` pour le compiler avec des optimisations.

```bash
cargo build --release
```

Cette commande créera un exécutable dans `target/release` au lieu de `target/debug`. Les optimisations font en sorte que votre code Rust s'exécute plus rapidement, mais les activer augmente le temps nécessaire pour compiler votre programme. C'est pourquoi il existe deux profils différents : l'un pour le développement, lorsque vous voulez reconstruire rapidement et souvent, et l'autre pour la construction du programme final que vous donnerez à un utilisateur qui ne sera pas reconstruit plusieurs fois et qui devra s'exécuter le plus rapidement possible. Si vous effectuez des tests de performance de votre code, assurez-vous d'exécuter `cargo build --release` et de faire des tests de performance avec l'exécutable dans `target/release`.
