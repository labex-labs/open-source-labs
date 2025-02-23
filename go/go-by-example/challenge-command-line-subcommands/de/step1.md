# Befehlszeilenunterbefehle

Es wird ein Programm erstellt, das zwei Unterbefehle unterstützt, `foo` und `bar`, jeder mit seiner eigenen Flaggegruppe. Der `foo`-Unterbefehl sollte zwei Flags haben, `enable` und `name`, während der `bar`-Unterbefehl ein Flag `level` haben sollte.

## Anforderungen

- Das Programm sollte das `flag`-Paket verwenden, um Flags zu definieren und zu analysieren.
- Der `foo`-Unterbefehl sollte zwei Flags haben, `enable` und `name`, beide vom Typ string.
- Der `bar`-Unterbefehl sollte ein Flag `level` vom Typ int haben.
- Das Programm sollte eine Fehlermeldung ausgeben, wenn ein ungültiger Unterbefehl angegeben wird.
- Das Programm sollte die Werte der Flags für den aufgerufenen Unterbefehl ausgeben.

## Beispiel

```sh
$ go build command-line-subcommands.go

# Rufen Sie zunächst den foo-Unterbefehl auf.
$./command-line-subcommands foo -enable -name=joe a1 a2
Unterbefehl 'foo'
enable: true
name: joe
tail: [a1 a2]

# Versuchen Sie jetzt bar.
$./command-line-subcommands bar -level 8 a1
Unterbefehl 'bar'
level: 8
tail: [a1]

# Aber bar akzeptiert die Flags von foo nicht.
$./command-line-subcommands bar -enable a1
Flag angegeben, aber nicht definiert: -enable
Verwendung von bar:
-level int
level

# Als Nächstes betrachten wir Umgebungsvariablen, eine weitere häufige
# Möglichkeit, Programme zu parametrisieren.
```
