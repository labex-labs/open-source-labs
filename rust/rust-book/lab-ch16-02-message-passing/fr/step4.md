# Création de plusieurs producteurs en clonant l'émetteur

Plus tôt, nous avons mentionné que `mpsc` était un acronyme pour _multiple producteurs, un consommateur_. Utilisons `mpsc` et étendons le code de la Liste 16-10 pour créer plusieurs threads qui envoient tous des valeurs au même récepteur. Nous pouvons le faire en clonant l'émetteur, comme indiqué dans la Liste 16-11.

Nom de fichier: `src/main.rs`

```rust
--snip--

let (tx, rx) = mpsc::channel();

let tx1 = tx.clone();
thread::spawn(move || {
    let vals = vec![
        String::from("hi"),
        String::from("from"),
        String::from("the"),
        String::from("thread"),
    ];

    for val in vals {
        tx1.send(val).unwrap();
        thread::sleep(Duration::from_secs(1));
    }
});

thread::spawn(move || {
    let vals = vec![
        String::from("more"),
        String::from("messages"),
        String::from("for"),
        String::from("you"),
    ];

    for val in vals {
        tx.send(val).unwrap();
        thread::sleep(Duration::from_secs(1));
    }
});

for received in rx {
    println!("Got: {received}");
}

--snip--
```

Liste 16-11: Envoi de plusieurs messages à partir de plusieurs producteurs

Cette fois, avant de créer le premier thread lancé, nous appelons `clone` sur l'émetteur. Cela nous donnera un nouvel émetteur que nous pouvons passer au premier thread lancé. Nous passons l'émetteur original à un second thread lancé. Cela nous donne deux threads, chacun envoyant des messages différents au même récepteur.

Lorsque vous exécutez le code, votre sortie devrait ressembler à ceci :

    Got: hi
    Got: more
    Got: from
    Got: messages
    Got: for
    Got: the
    Got: thread
    Got: you

Vous pouvez voir les valeurs dans un autre ordre, selon votre système. C'est ce qui rend la concurrence intéressante et difficile. Si vous experimentez avec `thread::sleep`, en lui donnant diverses valeurs dans les différents threads, chaque exécution sera plus non déterministe et créera une sortie différente chaque fois.

Maintenant que nous avons vu comment fonctionnent les canaux, regardons une autre méthode de concurrence.
