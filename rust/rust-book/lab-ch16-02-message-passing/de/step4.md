# Erstellen mehrerer Produzenten durch Klonen des Senders

Früher haben wir erwähnt, dass `mpsc` die Abkürzung für _multiple producer, single consumer_ ist. Lassen Sie uns `mpsc` in Aktion setzen und den Code in Listing 16-10 erweitern, um mehrere Threads zu erstellen, die alle Werte an den gleichen Empfänger senden. Wir können dies tun, indem wir den Sender klonen, wie in Listing 16-11 gezeigt.

Dateiname: `src/main.rs`

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

Listing 16-11: Senden mehrerer Nachrichten von mehreren Produzenten

Diesmal rufen wir vor dem Erstellen des ersten erzeugten Threads `clone` auf dem Sender auf. Dies gibt uns einen neuen Sender, den wir an den ersten erzeugten Thread übergeben können. Wir übergeben den ursprünglichen Sender an einen zweiten erzeugten Thread. Dadurch erhalten wir zwei Threads, die jeweils unterschiedliche Nachrichten an den einen Empfänger senden.

Wenn Sie den Code ausführen, sollte Ihre Ausgabe ungefähr so aussehen:

    Got: hi
    Got: more
    Got: from
    Got: messages
    Got: for
    Got: the
    Got: thread
    Got: you

Je nach Ihrem System können Sie die Werte in einer anderen Reihenfolge sehen. Dies macht die Konkurrenz sowohl interessant als auch schwierig. Wenn Sie mit `thread::sleep` experimentieren und ihm verschiedene Werte in den verschiedenen Threads geben, wird jede Ausführung noch unsicherer und erzeugt jedes Mal eine andere Ausgabe.

Jetzt, nachdem wir gesehen haben, wie Kanäle funktionieren, betrachten wir eine andere Methode der Konkurrenz.
