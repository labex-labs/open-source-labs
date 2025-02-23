# Tests und Benchmarking

Das Problem, das in dieser Herausforderung gelöst werden soll, ist es, eine einfache Implementierung einer ganzzahligen Minimierungsfunktion namens `IntMin` zu testen und zu benchmarken.

## Anforderungen

- Das `testing`-Paket muss importiert werden.
- Die `IntMin`-Funktion muss zwei ganzzahlige Parameter entgegennehmen und eine Ganzzahl zurückgeben.
- Die `TestIntMinBasic`-Funktion muss die `IntMin`-Funktion für grundlegende Eingabewerte testen.
- Die `TestIntMinTableDriven`-Funktion muss die `IntMin`-Funktion im tabellenbasierten Stil testen.
- Die `BenchmarkIntMin`-Funktion muss die `IntMin`-Funktion benchmarken.

## Beispiel

```sh
# Führen Sie alle Tests im aktuellen Projekt im detaillierten Modus aus.
$ go test -v
== RUN   TestIntMinBasic
--- PASS: TestIntMinBasic (0.00s)
=== RUN   TestIntMinTableDriven
=== RUN   TestIntMinTableDriven/0,1
=== RUN   TestIntMinTableDriven/1,0
=== RUN   TestIntMinTableDriven/2,-2
=== RUN   TestIntMinTableDriven/0,-1
=== RUN   TestIntMinTableDriven/-1,0
--- PASS: TestIntMinTableDriven (0.00s)
    --- PASS: TestIntMinTableDriven/0,1 (0.00s)
    --- PASS: TestIntMinTableDriven/1,0 (0.00s)
    --- PASS: TestIntMinTableDriven/2,-2 (0.00s)
    --- PASS: TestIntMinTableDriven/0,-1 (0.00s)
    --- PASS: TestIntMinTableDriven/-1,0 (0.00s)
PASS
ok  	examples/testing-and-benchmarking	0.023s

# Führen Sie alle Benchmarks im aktuellen Projekt aus. Alle Tests
# werden vor den Benchmarks ausgeführt. Die `bench`-Flag filtriert
# Benchmarkfunktionsnamen mit einer regulären Ausdruck.
$ go test -bench=.
goos: darwin
goarch: arm64
pkg: examples/testing
BenchmarkIntMin-8 1000000000 0.3136 ns/op
PASS
ok  	examples/testing-and-benchmarking	0.351s

```
