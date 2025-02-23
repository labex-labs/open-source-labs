# Base64-Kodierung

Sie müssen ein Golang-Programm schreiben, das einen gegebenen String mit der standardmäßigen und der URL-kompatiblen Base64-Kodierung codiert und decodiert.

## Anforderungen

- Das Programm sollte das `encoding/base64`-Paket mit dem Namen `b64` importieren, statt des Standardnamens `base64`.
- Das Programm sollte den gegebenen String mit der standardmäßigen und der URL-kompatiblen Base64-Kodierung codieren.
- Das Programm sollte den codierten String mit der standardmäßigen und der URL-kompatiblen Base64-Dekodierung decodieren.
- Das Programm sollte die codierten und decodierten Strings in die Konsole ausgeben.

## Beispiel

```sh
# Der String codiert sich mit den standardmäßigen und
# URL-basierten Base64-Codern zu leicht unterschiedlichen Werten
# (Endung `+` vs `-`), aber beide decodieren zu dem ursprünglichen String wie gewünscht.
$ go run base64-encoding.go
YWJjMTIzIT8kKiYoKSctPUB+
abc123!?$*&()'-=@~

YWJjMTIzIT8kKiYoKSctPUB-
abc123!?$*&()'-=@~

```
