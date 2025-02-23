# Prozesse ausführen

Das Problem besteht darin, den aktuellen Go-Prozess durch einen anderen Prozess, wie beispielsweise einen Nicht-Go-Prozess, zu ersetzen.

## Anforderungen

- Go-Programmiersprache
- Grundkenntnisse der Go-`exec`-Funktion
- Vertrautheit mit Umgebungsvariablen

## Beispiel

```sh
# Wenn wir unser Programm ausführen, wird es durch `ls` ersetzt.
$ go run execing-processes.go
gesamt 16
drwxr-xr-x 4 mark 136B Okt 3 16:29.
drwxr-xr-x 91 mark 3,0K Okt 3 12:50..
-rw-r--r-- 1 mark 1,3K Okt 3 16:28 execing-processes.go

# Beachten Sie, dass Go keine klassische Unix-`fork`-Funktion bietet.
# Normalerweise ist dies jedoch kein Problem, da das Starten von Goroutinen,
# das Erzeugen von Prozessen und das Ausführen von Prozessen die meisten
# Anwendungsfälle für `fork` abdecken.
```
