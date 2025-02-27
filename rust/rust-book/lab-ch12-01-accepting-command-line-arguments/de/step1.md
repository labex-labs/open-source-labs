# Akzeptieren von Befehlszeilenargumenten

Lassen Sie uns wie immer mit `cargo new` ein neues Projekt erstellen. Wir werden unser Projekt `minigrep` nennen, um es vom `grep`-Tool zu unterscheiden, das Sie möglicherweise bereits auf Ihrem System haben.

```bash
$ cargo new minigrep
     Created binary (application) `minigrep` project
$ cd minigrep
```

Die erste Aufgabe besteht darin, dass `minigrep` seine zwei Befehlszeilenargumente akzeptiert: den Dateipfad und einen String, nach dem gesucht werden soll. Das heißt, wir möchten unser Programm mit `cargo run` ausführen können, zwei Bindestriche, um anzuzeigen, dass die folgenden Argumente für unser Programm und nicht für `cargo` sind, einen String, nach dem gesucht werden soll, und einen Pfad zu einer Datei, in der gesucht werden soll, wie folgt:

```bash
cargo run -- searchstring example-filename.txt
```

Derzeit kann das von `cargo new` generierte Programm keine Argumente verarbeiten, die wir ihm geben. Einige vorhandene Bibliotheken auf *https://crates.io* können dabei helfen, ein Programm zu schreiben, das Befehlszeilenargumente akzeptiert, aber da Sie gerade dieses Konzept lernen, implementieren wir diese Funktion selbst.
