# Utiliser un paquet pour obtenir plus de fonctionnalités

Rappelez-vous qu'un paquet est une collection de fichiers de code source Rust. Le projet que nous avons construit est un _paquet binaire_, qui est un exécutable. Le paquet `rand` est un _paquet de bibliothèque_, qui contient du code destiné à être utilisé dans d'autres programmes et ne peut pas être exécuté seul.

La coordination de paquets externes par Cargo est là où Cargo brille vraiment. Avant d'être en mesure d'écrire du code utilisant `rand`, nous devons modifier le fichier `Cargo.toml` pour inclure le paquet `rand` comme dépendance. Ouvrez maintenant ce fichier et ajoutez la ligne suivante en bas, sous l'en-tête de section `[dependencies]` que Cargo a créé pour vous. Assurez-vous de spécifier `rand` exactement comme nous l'avons ici, avec ce numéro de version, sinon les exemples de code de ce tutoriel peuvent ne pas fonctionner :

Nom de fichier : `Cargo.toml`

```tomlrust
[dependencies]
rand = "0.8.5"
```

Dans le fichier `Cargo.toml`, tout ce qui suit un en-tête est partie de cette section qui continue jusqu'à ce qu'une autre section commence. Dans `[dependencies]`, vous dites à Cargo quels paquets externes votre projet dépend et quelles versions de ces paquets vous requérez. Dans ce cas, nous spécifions le paquet `rand` avec le spécificateur de version sémantique `0.8.5`. Cargo comprend la Numérotation de version sémantique (parfois appelée _SemVer_), qui est une norme pour écrire des numéros de version. Le spécificateur `0.8.5` est en fait un raccourci pour `^0.8.5`, ce qui signifie n'importe quelle version qui est au moins 0.8.5 mais inférieure à 0.9.0.

Cargo considère que ces versions ont des API publiques compatibles avec la version 0.8.5, et cette spécification vous assure que vous obtiendrez la dernière version de patch qui compilera toujours avec le code de ce chapitre. Aucune version 0.9.0 ou supérieure n'est garantie d'avoir la même API que celles utilisées dans les exemples suivants.

Maintenant, sans modifier aucun code, construisons le projet, comme indiqué dans la Liste 2-2.

```bash
$ cargo build
    Updating crates.io index
  Downloaded rand v0.8.5
  Downloaded libc v0.2.127
  Downloaded getrandom v0.2.7
  Downloaded cfg-if v1.0.0
  Downloaded ppv-lite86 v0.2.16
  Downloaded rand_chacha v0.3.1
  Downloaded rand_core v0.6.3
   Compiling rand_core v0.6.3
   Compiling libc v0.2.127
   Compiling getrandom v0.2.7
   Compiling cfg-if v1.0.0
   Compiling ppv-lite86 v0.2.16
   Compiling rand_chacha v0.3.1
   Compiling rand v0.8.5
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 2.53s
```

Liste 2-2 : La sortie de l'exécution de `cargo build` après avoir ajouté le paquet `rand` comme dépendance

Vous pouvez voir des numéros de version différents (mais tous seront compatibles avec le code, grâce à SemVer!) et des lignes différentes (en fonction du système d'exploitation), et les lignes peuvent être dans un ordre différent.

Lorsque nous incluons une dépendance externe, Cargo récupère les dernières versions de tout ce dont la dépendance a besoin depuis le _registre_, qui est une copie des données de Crates.io à *https://crates.io*. Crates.io est le lieu où les personnes du monde Rust publient leurs projets Rust open source pour que les autres puissent les utiliser.

Après avoir mis à jour le registre, Cargo vérifie la section `[dependencies]` et télécharge tous les paquets listés qui ne sont pas déjà téléchargés. Dans ce cas, bien que nous ayons seulement listé `rand` comme dépendance, Cargo a également récupéré d'autres paquets dont `rand` dépend pour fonctionner. Après avoir téléchargé les paquets, Rust les compile puis compile le projet avec les dépendances disponibles.

Si vous exécutez immédiatement `cargo build` à nouveau sans apporter de modifications, vous n'obtiendrez aucune sortie autre que la ligne `Finished`. Cargo sait qu'il a déjà téléchargé et compilé les dépendances, et vous n'avez rien changé à propos d'elles dans votre fichier `Cargo.toml`. Cargo sait également que vous n'avez rien changé à propos de votre code, donc il ne le recompile pas non plus. Ayant rien à faire, il quitte simplement.

Si vous ouvrez le fichier `src/main.rs`, apportez une modification triviale, puis enregistrez-le et reconstruisez-le, vous ne verrez que deux lignes de sortie :

```bash
$ cargo build
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 2.53 secs
```

Ces lignes montrent que Cargo ne met à jour la génération que avec votre petite modification au fichier `src/main.rs`. Vos dépendances n'ont pas changé, donc Cargo sait qu'il peut réutiliser ce qu'il a déjà téléchargé et compilé pour celles-ci.
