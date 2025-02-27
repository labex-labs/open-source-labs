# Filtern, um mehrere Tests auszuführen

Wir können einen Teil des Testnamens angeben, und jeder Test, dessen Name diesem Wert entspricht, wird ausgeführt. Beispielsweise können wir die beiden Tests, deren Namen `add` enthalten, ausführen, indem wir `cargo test add` ausführen:

```bash
$ cargo test add
   Compiling adder v0.1.0 (file:///projects/adder)
    Finished test [unoptimized + debuginfo] target(s) in 0.61s
     Running unittests src/lib.rs (target/debug/deps/adder-
92948b65e88960b4)

running 2 tests
test tests::add_three_and_two... ok
test tests::add_two_and_two... ok

test result: ok. 2 passed; 0 failed; 0 ignored; 0 measured; 1
filtered out; finished in 0.00s
```

Dieser Befehl führte alle Tests mit `add` im Namen aus und filterte den Test namens `one_hundred` aus. Beachten Sie auch, dass das Modul, in dem ein Test erscheint, Teil des Testnamens wird, sodass wir alle Tests in einem Modul ausführen können, indem wir nach dem Modulnamen filtern.
