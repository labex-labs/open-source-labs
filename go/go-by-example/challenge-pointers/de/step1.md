# Zeiger

Das Problem besteht darin, zu verstehen, wie Zeiger im Gegensatz zu Werten mit zwei Funktionen funktionieren: `zeroval` und `zeroptr`. `zeroval` hat einen `int`-Parameter, sodass Argumente per Wert an sie übergeben werden. `zeroval` erhält eine Kopie von `ival`, die von der im aufrufenden Funktionsunterschiedlich ist. Im Gegensatz dazu hat `zeroptr` einen `*int`-Parameter, was bedeutet, dass es einen Zeiger auf einen `int` akzeptiert. Der Code `*iptr` im Funktionskörper dereferenziert dann den Zeiger von seiner Speicheradresse auf den aktuellen Wert an dieser Adresse. Das Zuweisen eines Werts an einen dereferenzierten Zeiger ändert den Wert an der referenzierten Adresse.

## Anforderungen

- Sie sollten über ein grundlegendes Verständnis von Golang verfügen.
- Sie sollten wissen, wie man in Golang Funktionen definiert und verwendet.
- Sie sollten wissen, wie man in Golang Zeiger verwendet.

## Beispiel

```sh
# `zeroval` ändert das `i` in `main` nicht, aber
# `zeroptr` tut es, weil es eine Referenz auf
# die Speicheradresse für diese Variable hat.
$ go run pointers.go
initial: 1
zeroval: 1
zeroptr: 0
pointer: 0x42131100
```
