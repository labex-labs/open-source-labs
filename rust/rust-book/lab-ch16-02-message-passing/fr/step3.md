# Envoi de plusieurs valeurs et observation du récepteur en attente

Le code de la Liste 16-8 a compilé et s'est exécuté, mais il n'a pas clairement montré que deux threads distincts communiquaient l'un avec l'autre via le canal. Dans la Liste 16-10, nous avons apporté quelques modifications qui prouveront que le code de la Liste 16-8 s'exécute en parallèle : le thread lancé enverra désormais plusieurs messages et pausera une seconde entre chaque message.

Nom de fichier: `src/main.rs`

```rust
use std::sync::mpsc;
use std::thread;
use std::time::Duration;

fn main() {
    let (tx, rx) = mpsc::channel();

    thread::spawn(move || {
        let vals = vec![
            String::from("hi"),
            String::from("from"),
            String::from("the"),
            String::from("thread"),
        ];

        for val in vals {
            tx.send(val).unwrap();
            thread::sleep(Duration::from_secs(1));
        }
    });

    for received in rx {
        println!("Got: {received}");
    }
}
```

Liste 16-10: Envoi de plusieurs messages et pause entre chacun

Cette fois, le thread lancé a un vecteur de chaînes de caractères que nous voulons envoyer au thread principal. Nous itérons sur eux, envoyant chacun individuellement, et nous mettons en pause entre chaque en appelant la fonction `thread::sleep` avec une valeur `Duration` d'une seconde.

Dans le thread principal, nous n'appelons plus explicitement la fonction `recv` : au lieu de cela, nous traitons `rx` comme un itérateur. Pour chaque valeur reçue, nous l'imprimons. Lorsque le canal est fermé, l'itération se terminera.

Lors de l'exécution du code de la Liste 16-10, vous devriez voir la sortie suivante avec une pause d'une seconde entre chaque ligne :

    Got: hi
    Got: from
    Got: the
    Got: thread

Comme nous n'avons pas de code qui met en pause ou retarde dans la boucle `for` du thread principal, nous pouvons dire que le thread principal est en attente de recevoir des valeurs du thread lancé.
