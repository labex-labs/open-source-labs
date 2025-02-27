# Ausführen einzelner Tests

Wir können den Namen einer beliebigen Testfunktion an `cargo test` übergeben, um nur diesen Test auszuführen:

```bash
$ cargo test one_hundred
   Compiling adder v0.1.0 (file:///projects/adder)
    Finished test [unoptimized + debuginfo] target(s) in 0.69s
     Running unittests src/lib.rs (target/debug/deps/adder-
92948b65e88960b4)

running 1 test
test tests::one_hundred... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 2
filtered out; finished in 0.00s
```

Nur der Test mit dem Namen `one_hundred` wurde ausgeführt; die anderen beiden Tests stimmten nicht mit diesem Namen überein. Die Testausgabe lässt uns dadurch wissen, dass wir weitere Tests hatten, die nicht ausgeführt wurden, indem am Ende `2 filtered out` angezeigt wird.

Wir können nicht auf diese Weise die Namen mehrerer Tests angeben; nur der erste Wert, der an `cargo test` gegeben wird, wird verwendet. Es gibt jedoch einen Weg, mehrere Tests auszuführen.
