# Embed-Anweisung

Ihre Aufgabe ist es, den gegebenen Code zu modifizieren, um Dateien und Ordner in die Go-Binärdatei zu integrieren und deren Inhalt auszugeben.

## Anforderungen

- Sie müssen das `embed`-Paket verwenden, um Dateien und Ordner zu integrieren.
- Sie müssen die `string`- und `[]byte`-Typen verwenden, um den Inhalt der integrierten Dateien zu speichern.
- Sie müssen den `embed.FS`-Typ verwenden, um mehrere Dateien oder Ordner mit Platzhaltern zu integrieren.
- Sie müssen den Inhalt der integrierten Dateien ausgeben.

## Beispiel

```sh
# Verwenden Sie diese Befehle, um das Beispiel auszuführen.
# (Hinweis: Aufgrund der Einschränkungen auf dem Go-Playground
# kann dieses Beispiel nur auf Ihrem lokalen Computer ausgeführt werden.)
$ mkdir -p folder
$ echo "hello go" > folder/single_file.txt
$ echo "123" > folder/file1.hash
$ echo "456" > folder/file2.hash

$ go run embed-directive.go
hello go
hello go
123
456
```
