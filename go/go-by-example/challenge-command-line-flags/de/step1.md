# Befehlszeilenflags

Implementieren Sie ein Golang-Programm, das Befehlszeilenflags analysiert und die analysierten Optionen sowie alle nachfolgenden Positionsargumente ausgibt. Das Programm sollte die folgenden Flags unterstützen:

- `word`: Ein String-Flag mit einem Standardwert von `"foo"`.
- `numb`: Ein Integer-Flag mit einem Standardwert von `42`.
- `fork`: Ein boolescher Flag mit einem Standardwert von `false`.
- `svar`: Ein String-Flag, das eine vorhandene Variable verwendet, die an anderer Stelle im Programm deklariert wurde.

## Anforderungen

- Das Programm sollte das `flag`-Paket verwenden, um Befehlszeilenflags zu analysieren.
- Das Programm sollte die analysierten Optionen und alle nachfolgenden Positionsargumente ausgeben.
- Das Programm sollte die Flags `word`, `numb`, `fork` und `svar` wie oben beschrieben unterstützen.

## Beispiel

```sh
# Um das Befehlszeilenflags-Programm zu testen, ist es
# am besten, es zuerst zu kompilieren und dann die
# resultierende Binärdatei direkt auszuführen.
$ go build command-line-flags.go

# Testen Sie das kompilierte Programm, indem Sie zuerst
# allen Flags Werte zuweisen.
$./command-line-flags -word=opt -numb=7 -fork -svar=flag
word: opt
numb: 7
fork: true
svar: flag
tail: []

# Beachten Sie, dass die Flags automatisch ihre
# Standardwerte annehmen, wenn Sie sie weglassen.
$./command-line-flags -word=opt
word: opt
numb: 42
fork: false
svar: bar
tail: []

# Nachfolgende Positionsargumente können nach allen
# Flags angegeben werden.
$./command-line-flags -word=opt a1 a2 a3
word: opt
...
tail: [a1 a2 a3]

# Beachten Sie, dass das `flag`-Paket erfordert, dass
# alle Flags vor den Positionsargumenten erscheinen
# (ansonsten werden die Flags als Positionsargumente
# interpretiert).
$./command-line-flags -word=opt a1 a2 a3 -numb=7
word: opt
numb: 42
fork: false
svar: bar
tail: [a1 a2 a3 -numb=7]

# Verwenden Sie die Flags `-h` oder `--help`, um automatisch
# generierte Hilfetexte für das Befehlszeilenprogramm zu erhalten.
$./command-line-flags -h
Usage of./command-line-flags:
-fork=false: a bool
-numb=42: an int
-svar="bar": a string var
-word="foo": a string

# Wenn Sie ein Flag angeben, das nicht im `flag`-Paket
# definiert ist, wird das Programm eine Fehlermeldung
# ausgeben und den Hilfetext erneut anzeigen.
$./command-line-flags -wat
flag provided but not defined: -wat
Usage of./command-line-flags:
...
```
