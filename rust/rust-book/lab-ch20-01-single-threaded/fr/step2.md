# Écouter la connexion TCP

Notre serveur web doit écouter une connexion TCP, c'est donc la première partie sur laquelle nous allons travailler. La bibliothèque standard propose un module `std::net` qui nous permet de le faire. Créons un nouveau projet de la manière habituelle :

```bash
$ cargo new hello
     Créé un projet binaire (application) `hello`
$ cd hello
```

Maintenant, entrez le code de la Liste 20-1 dans `src/main.rs` pour commencer. Ce code écoutera l'adresse locale `127.0.0.1:7878` pour les flux TCP entrants. Lorsqu'il reçoit un flux entrant, il imprimera `Connection established!`.

Nom du fichier : `src/main.rs`

```rust
use std::net::TcpListener;

fn main() {
  1 let listener = TcpListener::bind("127.0.0.1:7878").unwrap();

  2 for stream in listener.incoming() {
      3 let stream = stream.unwrap();

      4 println!("Connection established!");
    }
}
```

Liste 20-1 : Écoute des flux entrants et impression d'un message lorsqu'un flux est reçu

En utilisant `TcpListener`, nous pouvons écouter les connexions TCP à l'adresse `127.0.0.1:7878` \[1\]. Dans l'adresse, la partie avant le deux-points est une adresse IP représentant votre ordinateur (c'est la même sur chaque ordinateur et ne représente pas spécifiquement l'ordinateur des auteurs), et `7878` est le port. Nous avons choisi ce port pour deux raisons : HTTP n'est normalement pas accepté sur ce port, de sorte que notre serveur est peu susceptible de entrer en conflit avec tout autre serveur web que vous pourriez avoir exécuté sur votre machine, et 7878 est _rust_ tapé sur un téléphone.

La fonction `bind` dans ce scénario fonctionne comme la fonction `new` en ce sens qu'elle retournera une nouvelle instance de `TcpListener`. La fonction est appelée `bind` car, en réseau, se connecter à un port pour l'écouter est connu sous le nom de "liaison à un port".

La fonction `bind` retourne un `Result<T, E>`, ce qui indique qu'il est possible que la liaison échoue. Par exemple, se connecter au port 80 nécessite des privilèges d'administrateur (les non-administrateurs ne peuvent écouter que sur des ports supérieurs à 1023), de sorte que si nous essayions de nous connecter au port 80 sans être administrateur, la liaison ne fonctionnerait pas. La liaison ne fonctionnerait pas non plus, par exemple, si nous exécutions deux instances de notre programme et avions donc deux programmes écoutant le même port. Comme nous écrivons un serveur de base uniquement à des fins d'apprentissage, nous n'aurons pas à nous soucier de gérer ce genre d'erreurs ; au lieu de cela, nous utilisons `unwrap` pour arrêter le programme si des erreurs se produisent.

La méthode `incoming` sur `TcpListener` retourne un itérateur qui nous donne une séquence de flux \[2\] (plus précisément, des flux de type `TcpStream`). Un seul _flux_ représente une connexion ouverte entre le client et le serveur. Une _connexion_ est le nom donné au processus complet de demande et de réponse dans lequel un client se connecte au serveur, le serveur génère une réponse et le serveur ferme la connexion. Ainsi, nous allons lire le `TcpStream` pour voir ce que le client a envoyé et puis écrire notre réponse dans le flux pour renvoyer des données au client. Dans l'ensemble, cette boucle `for` traitera chaque connexion tour à tour et produira une série de flux pour nous à traiter.

Pour l'instant, notre traitement du flux consiste à appeler `unwrap` pour terminer notre programme si le flux présente des erreurs \[3\] ; s'il n'y a pas d'erreurs, le programme imprime un message \[4\]. Nous ajouterons plus de fonctionnalités pour le cas de réussite dans la prochaine liste. La raison pour laquelle nous pouvons recevoir des erreurs de la méthode `incoming` lorsqu'un client se connecte au serveur est que nous n'itérons pas réellement sur les connexions. Au lieu de cela, nous itérons sur les _tentatives de connexion_. La connexion peut ne pas réussir pour un certain nombre de raisons, dont de nombreuses sont spécifiques au système d'exploitation. Par exemple, de nombreux systèmes d'exploitation ont une limite au nombre de connexions ouvertes simultanées qu'ils peuvent prendre en charge ; de nouvelles tentatives de connexion au-delà de ce nombre produiront une erreur jusqu'à ce que certaines des connexions ouvertes soient fermées.

Essayons d'exécuter ce code! Appelez `cargo run` dans le terminal puis chargez _127.0.0.1:7878_ dans un navigateur web. Le navigateur devrait afficher un message d'erreur comme "Connection reset" car le serveur ne renvoie actuellement aucune donnée. Mais lorsque vous regardez votre terminal, vous devriez voir plusieurs messages qui ont été imprimés lorsque le navigateur s'est connecté au serveur!

         Exécution de `target/debug/hello`
    Connection established!
    Connection established!
    Connection established!

Parfois, vous verrez plusieurs messages imprimés pour une seule demande de navigateur ; la raison peut être que le navigateur effectue une demande pour la page ainsi qu'une demande pour d'autres ressources, comme l'icône _favicon.ico_ qui apparaît dans l'onglet du navigateur.

Il se peut également que le navigateur essaie de se connecter au serveur plusieurs fois car le serveur ne répond pas avec de données. Lorsque `stream` sort de portée et est supprimé à la fin de la boucle, la connexion est fermée en tant que partie de la mise en œuvre de `drop`. Les navigateurs traitent parfois les connexions fermées en réessayant, car le problème peut être temporaire. Le facteur important est que nous avons obtenu avec succès un contrôle sur une connexion TCP!

N'oubliez pas d'arrêter le programme en appuyant sur ctrl-C lorsque vous avez fini d'exécuter une version particulière du code. Ensuite, redémarrez le programme en invoquant la commande `cargo run` après avoir effectué chaque ensemble de modifications de code pour vous assurer que vous exécutez le code le plus récent.
