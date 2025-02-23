# Zusammenfassung

In diesem Lab haben wir gelernt, wie das Paket `sync/atomic` in Go verwendet wird, um den Zustand zu verwalten, indem ein Zähler mit mehreren Goroutinen erhöht wird. Die Funktion `AddUint64` wurde verwendet, um den Zähler atomar zu erhöhen, und eine WaitGroup wurde verwendet, um auf alle Goroutinen zu warten, bis sie ihre Arbeit beendet haben.
