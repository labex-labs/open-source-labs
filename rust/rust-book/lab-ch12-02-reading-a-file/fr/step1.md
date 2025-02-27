# Lecture d'un fichier

Maintenant, nous allons ajouter une fonctionnalité pour lire le fichier spécifié dans l'argument `file_path`. Tout d'abord, nous avons besoin d'un fichier d'échantillonnage pour le tester : nous utiliserons un fichier avec un peu de texte sur plusieurs lignes avec quelques mots répétés. Le Listing 12-3 contient un poème d'Emily Dickinson qui fonctionnera parfaitement! Créez un fichier appelé _poem.txt_ au niveau racine de votre projet et entrez le poème "I'm Nobody! Who are you?".

Nom du fichier : poem.txt

    I'm nobody! Who are you?
    Are you nobody, too?
    Then there's a pair of us - don't tell!
    They'd banish us, you know.

    How dreary to be somebody!
    How public, like a frog
    To tell your name the livelong day
    To an admiring bog!

Listing 12-3 : Un poème d'Emily Dickinson constitue un bon cas de test.

Avec le texte en place, modifiez `src/main.rs` et ajoutez du code pour lire le fichier, comme indiqué dans le Listing 12-4.

Nom du fichier : `src/main.rs`

```rust
use std::env;
1 use std::fs;

fn main() {
    --snip--
    println!("In file {}", file_path);

  2 let contents = fs::read_to_string(file_path)
       .expect("Should have been able to read the file");

  3 println!("With text:\n{contents}");
}
```

Listing 12-4 : Lecture du contenu du fichier spécifié par le second argument

Tout d'abord, nous importons une partie pertinente de la bibliothèque standard avec une instruction `use` : nous avons besoin de `std::fs` pour gérer les fichiers \[1\].

Dans `main`, la nouvelle instruction `fs::read_to_string` prend le `file_path`, ouvre ce fichier et renvoie un `std::io::Result<String>` du contenu du fichier \[2\].

Après cela, nous ajoutons à nouveau une instruction `println!` temporaire qui imprime la valeur de `contents` après la lecture du fichier, afin que nous puissions vérifier que le programme fonctionne pour l'instant \[3\].

Exécutons ce code avec n'importe quelle chaîne de caractères comme premier argument de ligne de commande (car nous n'avons pas encore implémenté la partie de recherche) et le fichier _poem.txt_ comme second argument :

```bash
$ cargo run -- the poem.txt
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep the poem.txt`
Searching for the
In file poem.txt
With text:
I'm nobody! Who are you?
Are you nobody, too?
Then there's a pair of us - don't tell!
They'd banish us, you know.

How dreary to be somebody!
How public, like a frog
To tell your name the livelong day
To an admiring bog!
```

Parfait! Le code a lu puis imprimé le contenu du fichier. Mais le code présente quelques défauts. En ce moment, la fonction `main` a plusieurs responsabilités : généralement, les fonctions sont plus claires et plus faciles à maintenir si chaque fonction n'est responsable que d'une seule idée. L'autre problème est que nous ne gérons pas les erreurs aussi bien que nous le pourrions. Le programme est encore petit, donc ces défauts ne sont pas un gros problème, mais au fur et à mesure que le programme grandit, il sera plus difficile de les corriger proprement. Il est une bonne pratique de commencer à refactoriser tôt lors du développement d'un programme car il est beaucoup plus facile de refactoriser de petites quantités de code. Nous allons le faire ensuite.
