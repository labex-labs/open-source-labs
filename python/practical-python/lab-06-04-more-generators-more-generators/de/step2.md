# Warum Generatoren?

- Viele Probleme lassen sich in Bezug auf die Iteration viel deutlicher ausdrücken.
  - Schleifen über eine Sammlung von Elementen und Ausführung einer bestimmten Art von Operation (Suchen, Ersetzen, Modifizieren usw.).
  - Prozessierleitungen können auf eine Vielzahl von Datenverarbeitungsproblemen angewendet werden.
- Bessere Arbeitsspeicher-Effizienz.
  - Erzeugen nur Werte, wenn sie benötigt werden.
  - Im Gegensatz zur Konstruktion riesiger Listen.
  - Kann auf Streaming-Daten operieren
- Generatoren ermutigen zur Code-Wiederverwendung
  - Trennt die _Iteration_ vom Code, der die Iteration verwendet
  - Sie können einen Toolbox von interessanten Iterationsfunktionen erstellen und _mischen und kombinieren_.
