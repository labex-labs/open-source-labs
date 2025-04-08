# Ausführen einzelner Tests

Wir können den Namen einer beliebigen Testfunktion an `cargo test` übergeben, um nur diesen Test auszuführen:

```bash

```

Nur der Test mit dem Namen `one_hundred` wurde ausgeführt; die anderen beiden Tests stimmten nicht mit diesem Namen überein. Die Testausgabe lässt uns dadurch wissen, dass wir weitere Tests hatten, die nicht ausgeführt wurden, indem am Ende `2 filtered out` angezeigt wird.

Wir können nicht auf diese Weise die Namen mehrerer Tests angeben; nur der erste Wert, der an `cargo test` gegeben wird, wird verwendet. Es gibt jedoch einen Weg, mehrere Tests auszuführen.
