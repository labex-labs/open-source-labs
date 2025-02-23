# SHA256-Hashes

Gegeben einen String, berechne seinen SHA256-Hash.

## Anforderungen

- Das Programm sollte das Paket `crypto/sha256` und `fmt` importieren.
- Das Programm sollte die Funktion `sha256.New()` verwenden, um einen neuen Hash zu erstellen.
- Das Programm sollte die `Write`-Funktion verwenden, um die Bytes des Strings in den Hash zu schreiben.
- Das Programm sollte die `Sum`-Funktion verwenden, um das endgültige Hash-Ergebnis als Byte-Slice zu erhalten.
- Das Programm sollte den ursprünglichen String und das Hash-Ergebnis im hexadezimalen Format ausgeben.

## Beispiel

```sh
# Wenn man das Programm ausführt, berechnet es den Hash und gibt ihn
# im menschenlesbaren hexadezimalen Format aus.
$ go run sha256-hashes.go
sha256 diesen String
1af1dfa857bf1d8814fe1af8983c18080019922e557f15a8a...

# Man kann andere Hashes mit einem ähnlichen Muster wie
# dem oben gezeigten berechnen. Beispielsweise um SHA512-Hashes
# zu berechnen, importiert man `crypto/sha512` und verwendet
# `sha512.New()`.

# Beachten Sie, dass Sie, wenn Sie kryptografisch sichere Hashes benötigen,
# gründlich recherchieren sollten
# [Hash-Stärke](https://en.wikipedia.org/wiki/Cryptographic_hash_function)!
```
