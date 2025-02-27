# Canaux et transfert de propriété

Les règles de propriété jouent un rôle crucial dans l'envoi de messages car elles vous aident à écrire du code concurrent sécurisé. Prévenir les erreurs en programmation concurrente est l'avantage de penser à la propriété tout au long de vos programmes Rust. Faisons une expérience pour montrer comment les canaux et la propriété fonctionnent ensemble pour prévenir les problèmes : nous allons essayer d'utiliser une valeur `val` dans le thread lancé _après_ l'avoir envoyée à travers le canal. Essayez de compiler le code de la Liste 16-9 pour voir pourquoi ce code n'est pas autorisé.

Nom de fichier: `src/main.rs`

```rust
use std::sync::mpsc;
use std::thread;

fn main() {
    let (tx, rx) = mpsc::channel();

    thread::spawn(move || {
        let val = String::from("hi");
        tx.send(val).unwrap();
        println!("val is {val}");
    });

    let received = rx.recv().unwrap();
    println!("Got: {received}");
}
```

Liste 16-9: Tentative d'utilisation de `val` après l'avoir envoyée à travers le canal

Ici, nous essayons d'imprimer `val` après l'avoir envoyée à travers le canal via `tx.send`. Autoriser cela serait une mauvaise idée : une fois que la valeur a été envoyée à un autre thread, ce thread pourrait la modifier ou la supprimer avant que nous n'essayions à nouveau d'utiliser la valeur. Potentiellement, les modifications de l'autre thread pourraient entraîner des erreurs ou des résultats inattendus en raison de données inconsistantes ou inexistantes. Cependant, Rust nous donne une erreur si nous essayons de compiler le code de la Liste 16-9 :

```bash
error[E0382]: emprunt d'une valeur déplacée: `val`
  --> src/main.rs:10:31
   |
8  |         let val = String::from("hi");
   |             --- déplacement car `val` est de type `String`, qui ne
définit pas le trait `Copy`
9  |         tx.send(val).unwrap();
   |                 --- valeur déplacée ici
10 |         println!("val is {val}");
   |                           ^^^ valeur empruntée ici après déplacement
```

Notre erreur de concurrence a entraîné une erreur de compilation. La fonction `send` prend la propriété de son paramètre, et lorsque la valeur est déplacée, le récepteur en prend la propriété. Cela empêche de l'utiliser accidentellement une fois de plus après l'avoir envoyée ; le système de propriété vérifie que tout est correct.
