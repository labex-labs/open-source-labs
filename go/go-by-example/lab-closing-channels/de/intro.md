# Einführung

In Golang kann das Schließen eines Kanals verwendet werden, um die Fertigstellung an die Empfänger des Kanals zu kommunizieren. In diesem Lab wird gezeigt, wie ein Kanal verwendet wird, um Arbeit, die von der `main()`-Goroutine an eine Arbeits-Goroutine zu erledigen, zu kommunizieren, und wie der Kanal geschlossen wird, wenn es keine weiteren Aufgaben für die Arbeiter gibt.
