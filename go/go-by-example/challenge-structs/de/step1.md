# Structs

In dieser Herausforderung müssen Sie die `newPerson`-Funktion vervollständigen, die eine neue Person-Struktur mit dem angegebenen Namen konstruiert. Der `person`-Strukturtyp hat `name`- und `age`-Felder.

## Anforderungen

- Der `person`-Strukturtyp muss `name`- und `age`-Felder haben.
- Die `newPerson`-Funktion muss eine neue Person-Struktur mit dem angegebenen Namen konstruieren.
- Die `newPerson`-Funktion muss einen Zeiger auf die neu erstellte Person-Struktur zurückgeben.
- Die `main`-Funktion muss folgende ausgeben:
  - Eine neue Struktur mit Namen "Bob" und Alter 20.
  - Eine neue Struktur mit Namen "Alice" und Alter 30.
  - Eine neue Struktur mit Namen "Fred" und Alter 0.
  - Einen Zeiger auf eine neue Struktur mit Namen "Ann" und Alter 40.
  - Eine neue Struktur, die mit der `newPerson`-Funktion konstruiert wurde, mit Namen "Jon" und Alter 42.
  - Das `name`-Feld einer Struktur mit Namen "Sean" und Alter 50.
  - Das `age`-Feld eines Strukturzeigers auf eine Struktur mit Namen "Sean" und Alter 50.
  - Das `age`-Feld eines Strukturzeigers auf eine Struktur mit Namen "Sean" und Alter 50, nachdem das `age`-Feld auf 51 aktualisiert wurde.

## Beispiel

```sh
$ go run structs.go
{Bob 20}
{Alice 30}
{Fred 0}
&{Ann 40}
&{Jon 42}
Sean
50
51
```
