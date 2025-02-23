# Kanalsynchronisierung

Das Problem, das in dieser Aufgabe gelöst werden soll, ist es, eine Goroutine zu erstellen, die eine bestimmte Arbeit ausführt und eine andere Goroutine benachrichtigt, wenn diese Arbeit mit Hilfe eines Kanals abgeschlossen ist.

## Anforderungen

Um diese Aufgabe zu lösen, müssen Sie Folgendes tun:

- Erstellen Sie eine Funktion namens `worker`, die einen Kanal vom Typ `bool` als Parameter annimmt.
- Innerhalb der Funktion `worker` führen Sie eine bestimmte Arbeit aus und senden dann einen Wert an den Kanal, um anzuzeigen, dass die Arbeit abgeschlossen ist.
- In der `main`-Funktion erstellen Sie einen Kanal vom Typ `bool` mit einer Puffergröße von 1.
- Starten Sie eine Goroutine, die die `worker`-Funktion aufruft und den Kanal als Parameter übergibt.
- Blockieren Sie die `main`-Funktion, bis ein Wert vom Kanal empfangen wird.

## Beispiel

```sh
$ go run channel-synchronization.go
working...done

# Wenn Sie die Zeile `<- done` aus diesem Programm entfernen,
# würde das Programm vor dem Start der `worker`-Funktion
# beenden.
```
