# Strukturembedding

Erstellen Sie eine Struktur namens `container`, die eine Struktur namens `base` einbetten. Die `base`-Struktur sollte ein Feld namens `num` vom Typ `int` und eine Methode namens `describe()` haben, die einen String zurückgibt. Die `container`-Struktur sollte ein Feld namens `str` vom Typ `string` haben. Die `container`-Struktur sollte auf das `num`-Feld und die `describe()`-Methode der `base`-Struktur zugreifen können.

## Anforderungen

- Die `base`-Struktur sollte ein Feld namens `num` vom Typ `int` haben.
- Die `base`-Struktur sollte eine Methode namens `describe()` haben, die einen String zurückgibt.
- Die `container`-Struktur sollte ein Feld namens `str` vom Typ `string` haben.
- Die `container`-Struktur sollte die `base`-Struktur einbetten.
- Die `container`-Struktur sollte auf das `num`-Feld und die `describe()`-Methode der `base`-Struktur zugreifen können.

## Beispiel

```sh
$ go run struct-embedding.go
co={num: 1, str: some name}
auch num: 1
beschreiben: base mit num=1
Beschreiber: base mit num=1
```
