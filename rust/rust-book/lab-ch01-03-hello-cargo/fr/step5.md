# Cargo, une convention

Avec de simples projets, Cargo ne procure pas beaucoup de valeur par rapport à l'utilisation simple de `rustc`, mais sa valeur se révèlera au fur et à mesure que vos programmes deviendront plus complexes. Une fois que les programmes deviennent composés de plusieurs fichiers ou ont besoin d'une dépendance, il est beaucoup plus facile de laisser Cargo coordonner la compilation.

Même si le projet `hello_cargo` est simple, il utilise désormais beaucoup des outils réels que vous utiliserez pour le reste de votre carrière Rust. En fait, pour travailler sur n'importe quel projet existant, vous pouvez utiliser les commandes suivantes pour récupérer le code avec Git, accéder au répertoire de ce projet et compiler :

```bash
git clone example.org/someproject
cd someproject
cargo build
```

Pour en savoir plus sur Cargo, consultez sa documentation sur *https://doc.rust-lang.org/cargo*.
