# Zusammenfassung

In dieser Herausforderung haben wir gelernt, wie Mutexe verwendet werden können, um Daten sicher über mehrere Goroutinen hinweg zuzugreifen. Wir haben eine `Container`-Struktur erstellt, um eine Map von Zählern zu speichern, und ein `Mutex` verwendet, um den Zugang zur `counters`-Map zu synchronisieren. Wir haben auch eine `inc`-Methode implementiert, um den benannten Zähler zu erhöhen, und die `sync.WaitGroup`-Struktur verwendet, um auf das Ende der Goroutinen zu warten. Schließlich haben wir die `counters`-Map mit der `fmt.Println`-Funktion ausgegeben.
