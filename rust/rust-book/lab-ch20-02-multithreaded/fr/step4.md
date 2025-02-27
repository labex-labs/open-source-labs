# Spawning a Thread for Each Request

Tout d'abord, explorons à quoi pourrait ressembler notre code s'il créait un nouveau thread pour chaque connexion. Comme mentionné précédemment, ce n'est pas notre plan final en raison des problèmes liés à la génération potentiellement illimitée de threads, mais c'est un point de départ pour obtenir tout d'abord un serveur multithreadé fonctionnel. Ensuite, nous ajouterons le thread pool en tant qu'amélioration, et il sera plus facile de comparer les deux solutions.

Le Listing 20-11 montre les modifications à apporter à `main` pour lancer un nouveau thread pour traiter chaque flux dans la boucle `for`.

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let listener = TcpListener::bind("127.0.0.1:7878").unwrap();

    for stream in listener.incoming() {
        let stream = stream.unwrap();

        thread::spawn(|| {
            handle_connection(stream);
        });
    }
}
```

Listing 20-11 : Lancement d'un nouveau thread pour chaque flux

Comme vous l'avez appris au Chapitre 16, `thread::spawn` créera un nouveau thread puis exécutera le code dans la closure dans le nouveau thread. Si vous exécutez ce code et chargez _/sleep_ dans votre navigateur, puis _/_ dans deux autres onglets de navigateur, vous verrez effectivement que les requêtes à _/_ n'ont pas à attendre que _/sleep_ soit terminée. Cependant, comme nous l'avons mentionné, cela finira par surcharger le système car vous créeriez de nouveaux threads sans limite.
