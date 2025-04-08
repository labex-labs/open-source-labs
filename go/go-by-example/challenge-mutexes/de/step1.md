# Mutexe

Das Problem, das in dieser Herausforderung gelöst werden soll, besteht darin, einen benannten Zähler in einer Schleife mithilfe mehrerer Goroutinen zu erhöhen und sicherzustellen, dass der Zugang zum Zähler synchronisiert ist.

## Anforderungen

- Verwenden Sie eine `Container`-Struktur, um eine Map von Zählern zu speichern.
- Verwenden Sie ein `Mutex`, um den Zugang zur `counters`-Map zu synchronisieren.
- Die `Container`-Struktur sollte eine `inc`-Methode haben, die einen `name`-String als Parameter nimmt und den entsprechenden Zähler in der `counters`-Map erhöht.
- Die `inc`-Methode sollte den Mutex vor dem Zugriff auf die `counters`-Map sperren und ihn am Ende der Funktion mit einem `defer`-Statement entsperren.
- Verwenden Sie die `sync.WaitGroup`-Struktur, um auf das Ende der Goroutinen zu warten.
- Verwenden Sie die `fmt.Println`-Funktion, um die `counters`-Map auszugeben.

## Beispiel

```sh
# Wenn das Programm ausgeführt wird, werden die Zähler
# wie erwartet aktualisiert.

# Als Nächstes betrachten wir die Implementierung dieser
# selben Zustandsverwaltungstask, indem wir nur Goroutinen
# und Kanäle verwenden.
```
