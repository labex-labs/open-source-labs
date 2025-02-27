# Compilation et exécution d'un projet Cargo

Maintenant, examinons ce qui est différent lorsque nous compilons et exécutons le programme "Hello, world!" avec Cargo! Depuis votre répertoire `hello_cargo`, compilez votre projet en tapant la commande suivante :

```bash
$ cargo build
   Compiling hello_cargo v0.1.0 (file:///projects/hello_cargo)
    Finished dev [unoptimized + debuginfo] target(s) in 2.85 secs
```

Cette commande crée un fichier exécutable dans `target/debug/hello_cargo` plutôt que dans votre répertoire actuel. Parce que la compilation par défaut est une compilation de débogage, Cargo place le binaire dans un répertoire nommé `debug`. Vous pouvez exécuter l'exécutable avec cette commande :

```bash
$./target/debug/hello_cargo
Hello, world!
```

Si tout se passe bien, `Hello, world!` devrait s'afficher dans le terminal. L'exécution de `cargo build` pour la première fois entraîne également la création d'un nouveau fichier au niveau supérieur : _Cargo.lock_. Ce fichier suit les versions exactes des dépendances de votre projet. Ce projet n'a pas de dépendances, donc le fichier est un peu sparse. Vous n'aurez jamais besoin de modifier manuellement ce fichier ; Cargo gère son contenu pour vous.

Nous venons de compiler un projet avec `cargo build` et de l'exécuter avec `./target/debug/hello_cargo`, mais nous pouvons également utiliser `cargo run` pour compiler le code puis exécuter l'exécutable résultant en une seule commande :

```bash
$ cargo run
    Finished dev [unoptimized + debuginfo] target(s) in 0.0 secs
     Running `target/debug/hello_cargo`
Hello, world!
```

Utiliser `cargo run` est plus pratique que de devoir se souvenir d'exécuter `cargo build` puis d'utiliser le chemin complet vers le binaire, donc la plupart des développeurs utilisent `cargo run`.

Remarquez que cette fois-ci, nous n'avons pas vu de sortie indiquant que Cargo compilait `hello_cargo`. Cargo a déterminé que les fichiers n'avaient pas été modifiés, donc il n'a pas reconstruit mais a simplement exécuté le binaire. Si vous aviez modifié votre code source, Cargo aurait reconstruit le projet avant de l'exécuter, et vous auriez vu cette sortie :

```bash
$ cargo run
   Compiling hello_cargo v0.1.0 (file:///projects/hello_cargo)
    Finished dev [unoptimized + debuginfo] target(s) in 0.33 secs
     Running `target/debug/hello_cargo`
Hello, world!
```

Cargo fournit également une commande appelée `cargo check`. Cette commande vérifie rapidement votre code pour vous assurer qu'il se compile mais ne produit pas d'exécutable :

```bash
$ cargo check
   Checking hello_cargo v0.1.0 (file:///projects/hello_cargo)
    Finished dev [unoptimized + debuginfo] target(s) in 0.32 secs
```

Pourquoi ne voudriez-vous pas un exécutable? Souvent, `cargo check` est beaucoup plus rapide que `cargo build` car elle saute l'étape de production d'un exécutable. Si vous vérifiez constamment votre travail pendant que vous écrivez le code, utiliser `cargo check` accélérera le processus de vérification si votre projet se compile toujours! En conséquence, de nombreux Rustaceans exécutent `cargo check` régulièrement pendant qu'ils écrivent leur programme pour s'assurer qu'il se compile. Ensuite, ils exécutent `cargo build` lorsqu'ils sont prêts à utiliser l'exécutable.

Récapitulons ce que nous avons appris jusqu'à présent sur Cargo :

- Nous pouvons créer un projet en utilisant `cargo new`.
- Nous pouvons compiler un projet en utilisant `cargo build`.
- Nous pouvons compiler et exécuter un projet en une seule étape en utilisant `cargo run`.
- Nous pouvons compiler un projet sans produire un binaire pour vérifier les erreurs en utilisant `cargo check`.
- Au lieu de sauvegarder le résultat de la compilation dans le même répertoire que notre code, Cargo le stocke dans le répertoire `target/debug`.

Un avantage supplémentaire d'utiliser Cargo est que les commandes sont les mêmes peu importe le système d'exploitation sur lequel vous travaillez. Ainsi, à partir de maintenant, nous ne fournirons plus d'instructions spécifiques pour Linux et macOS par rapport à Windows.
