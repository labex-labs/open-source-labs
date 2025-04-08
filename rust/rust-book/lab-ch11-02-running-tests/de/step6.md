# Filtern, um mehrere Tests auszuführen

Wir können einen Teil des Testnamens angeben, und jeder Test, dessen Name diesem Wert entspricht, wird ausgeführt. Beispielsweise können wir die beiden Tests, deren Namen `add` enthalten, ausführen, indem wir `cargo test add` ausführen:

```bash

```

Dieser Befehl führte alle Tests mit `add` im Namen aus und filterte den Test namens `one_hundred` aus. Beachten Sie auch, dass das Modul, in dem ein Test erscheint, Teil des Testnamens wird, sodass wir alle Tests in einem Modul ausführen können, indem wir nach dem Modulnamen filtern.
