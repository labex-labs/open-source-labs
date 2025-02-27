# Utiliser la communication par messages pour transférer des données entre des threads

Une approche de concurrence sécurisée de plus en plus populaire est la _communication par messages_, où les threads ou les acteurs communiquent en s'envoyant des messages contenant des données. Voici l'idée sous forme d'un slogan de la documentation du langage Go à *https://golang.org/doc/effective_go.html#concurrency*: "Ne communiquez pas en partageant la mémoire; au contraire, partagez la mémoire en communiquant."

Pour réaliser une concurrence de communication de messages, la bibliothèque standard de Rust fournit une implémentation de _canaux_. Un canal est un concept de programmation général par lequel des données sont envoyées d'un thread à un autre.

Vous pouvez imaginer un canal en programmation comme un canal directionnel d'eau, comme un ruisseau ou une rivière. Si vous mettez quelque chose comme un canard en caoutchouc dans une rivière, il ira en aval jusqu'à la fin de l'eauway.

Un canal a deux parties: un émetteur et un récepteur. La partie émettrice est l'emplacement en amont où vous mettez le canard en caoutchouc dans la rivière, et la partie réceptrice est où le canard en caoutchouc finit en aval. Une partie de votre code appelle des méthodes sur l'émetteur avec les données que vous voulez envoyer, et une autre partie vérifie l'extrémité de réception pour les messages arrivant. Un canal est dit _fermé_ si l'une ou l'autre des parties émettrice ou réceptrice est supprimée.

Ici, nous allons travailler jusqu'à un programme qui a un thread pour générer des valeurs et les envoyer à travers un canal, et un autre thread qui recevra les valeurs et les imprimera. Nous enverrons des valeurs simples entre les threads en utilisant un canal pour illustrer la fonctionnalité. Une fois que vous serez familier avec la technique, vous pourriez utiliser des canaux pour tous les threads qui ont besoin de communiquer entre eux, comme un système de chat ou un système où de nombreux threads exécutent des parties d'un calcul et envoient les parties à un thread qui agrège les résultats.

Tout d'abord, dans la Liste 16-6, nous allons créer un canal mais ne rien faire avec. Notez que cela ne compilera pas encore car Rust ne peut pas savoir quel type de valeurs nous voulons envoyer sur le canal.

Nom de fichier: `src/main.rs`

```rust
use std::sync::mpsc;

fn main() {
    let (tx, rx) = mpsc::channel();
}
```

Liste 16-6: Création d'un canal et attribution des deux parties à `tx` et `rx`

Nous créons un nouveau canal en utilisant la fonction `mpsc::channel`; `mpsc` signifie _multiple producteurs, un consommateur_. En bref, la manière dont la bibliothèque standard de Rust implémente les canaux signifie qu'un canal peut avoir plusieurs _extrémités d'envoi_ qui produisent des valeurs mais seulement une _extrémité de réception_ qui consomme ces valeurs. Imaginez plusieurs ruisseaux qui convergent dans une grande rivière: tout ce qui est envoyé dans l'un des ruisseaux finira dans une seule rivière à la fin. Nous commencerons avec un seul producteur pour l'instant, mais nous ajouterons plusieurs producteurs lorsque cet exemple fonctionnera.

La fonction `mpsc::channel` renvoie un tuple, dont le premier élément est l'extrémité d'envoi - l'émetteur - et le second élément est l'extrémité de réception - le récepteur. Les abréviations `tx` et `rx` sont traditionnellement utilisées dans de nombreux domaines pour _émetteur_ et _récepteur_ respectivement, donc nous nommons nos variables ainsi pour indiquer chaque extrémité. Nous utilisons une instruction `let` avec un motif qui décompose les tuples; nous discuterons de l'utilisation des motifs dans les instructions `let` et de la décomposition au Chapitre 18. Pour l'instant, sachez que l'utilisation d'une instruction `let` de cette manière est une approche pratique pour extraire les parties du tuple renvoyé par `mpsc::channel`.

Déplaçons l'extrémité d'envoi dans un thread lancé et lui faisons envoyer une chaîne de caractères de sorte que le thread lancé communique avec le thread principal, comme indiqué dans la Liste 16-7. C'est comme mettre un canard en caoutchouc dans la rivière en amont ou envoyer un message de chat d'un thread à un autre.

Nom de fichier: `src/main.rs`

```rust
use std::sync::mpsc;
use std::thread;

fn main() {
    let (tx, rx) = mpsc::channel();

    thread::spawn(move || {
        let val = String::from("hi");
        tx.send(val).unwrap();
    });
}
```

Liste 16-7: Déplacement de `tx` dans un thread lancé et envoi de `"hi"`

Encore une fois, nous utilisons `thread::spawn` pour créer un nouveau thread puis `move` pour déplacer `tx` dans la fermeture afin que le thread lancé possède `tx`. Le thread lancé doit posséder l'émetteur pour être capable d'envoyer des messages à travers le canal.

L'émetteur a une méthode `send` qui prend la valeur que nous voulons envoyer. La méthode `send` renvoie un type `Result<T, E>`, donc si le récepteur a déjà été supprimé et qu'il n'y a nulle part où envoyer une valeur, l'opération d'envoi renverra une erreur. Dans cet exemple, nous appelons `unwrap` pour générer une panique en cas d'erreur. Mais dans une application réelle, nous la gérerions correctement: revenez au Chapitre 9 pour réviser les stratégies de gestion appropriée des erreurs.

Dans la Liste 16-8, nous allons obtenir la valeur du récepteur dans le thread principal. C'est comme récupérer le canard en caoutchouc dans l'eau à la fin de la rivière ou recevoir un message de chat.

Nom de fichier: `src/main.rs`

```rust
use std::sync::mpsc;
use std::thread;

fn main() {
    let (tx, rx) = mpsc::channel();

    thread::spawn(move || {
        let val = String::from("hi");
        tx.send(val).unwrap();
    });

    let received = rx.recv().unwrap();
    println!("Got: {received}");
}
```

Liste 16-8: Réception de la valeur `"hi"` dans le thread principal et l'impression

Le récepteur a deux méthodes utiles: `recv` et `try_recv`. Nous utilisons `recv`, abréviation de _recevoir_, qui bloquera l'exécution du thread principal et attendra jusqu'à ce qu'une valeur soit envoyée à travers le canal. Une fois qu'une valeur est envoyée, `recv` la renverra dans un `Result<T, E>`. Lorsque l'émetteur se ferme, `recv` renverra une erreur pour signaler qu'aucune valeur ne viendra plus.

La méthode `try_recv` ne bloque pas, mais renverra immédiatement un `Result<T, E>`: une valeur `Ok` contenant un message s'il y en a un disponible et une valeur `Err` s'il n'y a pas de messages cette fois-ci. L'utilisation de `try_recv` est utile si ce thread a d'autres travaux à faire en attendant les messages: nous pourrions écrire une boucle qui appelle `try_recv` de temps en temps, traite un message s'il y en a un disponible et sinon effectue d'autres travaux pendant un certain temps jusqu'à vérifier à nouveau.

Nous avons utilisé `recv` dans cet exemple pour la simplicité; nous n'avons pas d'autres travaux pour le thread principal à faire autre que d'attendre les messages, donc bloquer le thread principal est approprié.

Lorsque nous exécutons le code de la Liste 16-8, nous verrons la valeur imprimée à partir du thread principal:

```rust
Got: hi
```

Parfait!
