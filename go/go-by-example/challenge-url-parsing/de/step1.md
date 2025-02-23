# URL-Analyse

Die Herausforderung besteht darin, eine Beispiel-URL zu analysieren, die ein Schema, Authentifizierungsinformationen, Host, Port, Pfad, Abfrageparameter und Abfragefragment enthält. Die analysierte URL sollte verwendet werden, um die einzelnen Komponenten der URL zu extrahieren.

## Anforderungen

- Die Pakete `url` und `net` sollten importiert werden.
- Die Beispiel-URL sollte analysiert und auf Fehler überprüft werden.
- Das Schema, die Authentifizierungsinformationen, der Host, der Port, der Pfad, die Abfrageparameter und das Abfragefragment sollten aus der analysierten URL extrahiert werden.
- Die Funktion `SplitHostPort` sollte verwendet werden, um den Hostnamen und den Port aus dem Feld `Host` zu extrahieren.
- Die Funktion `ParseQuery` sollte verwendet werden, um die Abfrageparameter in eine Map zu analysieren.

## Beispiel

```sh
# Wenn wir unser URL-Analyse-Programm ausführen, werden alle
# verschiedenen Teile angezeigt, die wir extrahiert haben.
$ go run url-parsing.go
postgres
user:pass
user
pass
host.com:5432
host.com
5432
/path
f
k=v
map[k:[v]]
v

```
