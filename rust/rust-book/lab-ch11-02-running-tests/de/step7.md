# Auslassen einiger Tests, es sei denn, sie werden speziell angefordert

Manchmal können einige bestimmte Tests sehr zeitaufwendig zu executieren sein, sodass Sie sie möglicherweise während der meisten Ausführungen von `cargo test` ausschließen möchten. Anstatt alle Tests, die Sie tatsächlich ausführen möchten, als Argumente aufzulisten, können Sie stattdessen die zeitaufwendigen Tests mit dem Attribut `ignore` annotieren, um sie auszuschließen, wie hier gezeigt:

Dateiname: `src/lib.rs`

```rust
#[test]
fn it_works() {
    let result = 2 + 2;
    assert_eq!(result, 4);
}

#[test]
#[ignore]
fn expensive_test() {
    // code that takes an hour to run
}
```

Nach `#[test]` fügen wir die Zeile `#[ignore]` zum Test hinzu, den wir ausschließen möchten. Wenn wir jetzt unsere Tests ausführen, wird `it_works` ausgeführt, aber `expensive_test` nicht:

```bash
$ cargo test
   Compiling adder v0.1.0 (file:///projects/adder)
    Finished test [unoptimized + debuginfo] target(s) in 0.60s
     Running unittests src/lib.rs (target/debug/deps/adder-
92948b65e88960b4)

running 2 tests
test expensive_test... ignored
test it_works... ok

test result: ok. 1 passed; 0 failed; 1 ignored; 0 measured; 0
filtered out; finished in 0.00s
```

Die Funktion `expensive_test` wird als `ignored` aufgelistet. Wenn wir nur die ignorierten Tests ausführen möchten, können wir `cargo test -- --ignored` verwenden:

```bash
$ cargo test -- --ignored
    Finished test [unoptimized + debuginfo] target(s) in 0.61s
     Running unittests src/lib.rs (target/debug/deps/adder-
92948b65e88960b4)

running 1 test
test expensive_test... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 1
filtered out; finished in 0.00s
```

Indem Sie steuern, welche Tests ausgeführt werden, können Sie sicherstellen, dass die Ergebnisse von `cargo test` schnell zurückgegeben werden. Wenn Sie an einem Punkt angelangt sind, an dem es Sinn macht, die Ergebnisse der `ignored` Tests zu überprüfen und Sie die Zeit haben, auf die Ergebnisse zu warten, können Sie stattdessen `cargo test -- --ignored` ausführen. Wenn Sie alle Tests ausführen möchten, unabhängig davon, ob sie ignoriert werden oder nicht, können Sie `cargo test -- --include-ignored` ausführen.
