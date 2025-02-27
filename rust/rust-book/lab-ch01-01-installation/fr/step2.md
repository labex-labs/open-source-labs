# Installation de rustup sur Linux ou macOS

Si vous utilisez Linux ou macOS, ouvrez un terminal et entrez la commande suivante :

```bash
curl --proto '=https' --tlsv1.3 https://sh.rustup.rs -sSf | sh
```

La commande télécharge un script et lance l'installation de l'outil `rustup`, qui installe la dernière version stable de Rust. Vous pouvez être invité à saisir votre mot de passe. Si l'installation est réussie, la ligne suivante apparaîtra :

```rust
Rust is installed now. Great!
```

Vous aurez également besoin d'un _lienqueur_, qui est un programme que Rust utilise pour joindre ses sorties compilées en un seul fichier. Il est probable que vous en avez déjà un. Si vous rencontrez des erreurs de lienqueur, vous devriez installer un compilateur C, qui inclura généralement un lienqueur. Un compilateur C est également utile car certains paquets Rust courants dépendent de code C et auront besoin d'un compilateur C.

Les utilisateurs de Linux devraient généralement installer GCC ou Clang, selon les instructions de leur distribution. Par exemple, si vous utilisez Ubuntu, vous pouvez installer le paquet `build-essential`.
