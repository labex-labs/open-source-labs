# La compilation et l'exécution sont des étapes distinctes

Vous venez d'exécuter un programme nouvellement créé, donc examinons chaque étape du processus.

Avant d'exécuter un programme Rust, vous devez le compiler à l'aide du compilateur Rust en entrant la commande `rustc` et en lui passant le nom de votre fichier source, comme ceci :

```bash
rustc main.rs
```

Si vous avez une expérience avec C ou C++, vous remarquerez que cela est similaire à `gcc` ou `clang`. Après une compilation réussie, Rust produit un exécutable binaire.

Sur Linux, macOS et PowerShell sur Windows, vous pouvez voir l'exécutable en entrant la commande `ls` dans votre terminal :

```bash
$ ls
main main.rs
```

À partir d'ici, vous exécutez le fichier `main`, comme ceci :

```bash
./main
```

Si votre `main.rs` est votre programme "Bonjour, le monde!", cette ligne imprime `Bonjour, le monde!` dans votre terminal.

Si vous êtes plus familier avec un langage dynamique, tel que Ruby, Python ou JavaScript, vous n'êtes peut-être pas habitué à compiler et à exécuter un programme en tant qu'étapes distinctes. Rust est un langage _compilé en amont_, ce qui signifie que vous pouvez compiler un programme et donner l'exécutable à quelqu'un d'autre, et qu'ils peuvent l'exécuter même s'ils n'ont pas Rust installé. Si vous donnez à quelqu'un un fichier `.rb`, `.py` ou `.js`, ils doivent avoir une implémentation de Ruby, Python ou JavaScript installée (respectivement). Mais dans ces langages, vous n'avez besoin que d'une seule commande pour compiler et exécuter votre programme. Tout est un compromis dans la conception des langages.

Seulement compiler avec `rustc` est suffisant pour les programmes simples, mais à mesure que votre projet grandit, vous voudrez gérer toutes les options et faciliter la partage de votre code. Ensuite, nous allons vous présenter l'outil Cargo, qui vous aidera à écrire des programmes Rust pour le monde réel.
