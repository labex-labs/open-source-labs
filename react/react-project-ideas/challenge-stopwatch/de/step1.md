# Stoppuhr

Um loszulegen, öffnen Sie den Editor. Sie können die folgenden Dateien in Ihrem Editor sehen.

```txt
├── public
├── src
│   ├── components
│   │   ├──common
│   │   ├── stopwatch
│   │   ├── timer
│   │   ├── App.css
│   │   └── App.js
│   ├── index.css
│   └── index.js
├── package-lock.json
└── package.json
```

## Anforderungen

- Um die Projektabhängigkeiten zu installieren, verwenden Sie den folgenden Befehl:

  ```bash
  npm i
  ```

- Bitte vervollständigen Sie diese Herausforderung in der Datei `src/components/timer/Timer.js`.
- Die `onStart`-Funktion wird每秒von der useEffect-Hook aufgerufen.
  - Sie überprüft, ob der Timer auf 0 Stunden, 0 Minuten und 0 Sekunden erreicht hat. Wenn ja, setzt sie isStarted auf false und gibt zurück.
  - Wenn der Timer nicht gestartet ist, gibt sie ohne Änderungen zurück.
  - Wenn der Timer läuft, wird der Timer um 1 Sekunde verringert.
  - Wenn die Minuten oder Sekunden auf 0 gelangen, werden die Stunden, Minuten oder Sekunden entsprechend mithilfe der setTimer-Funktion angepasst.
- Die `onReset`-Funktion wird aufgerufen, wenn die Schaltfläche "Zurücksetzen" angeklickt wird.
  - Sie setzt isStarted auf false und setzt den Timer auf 0 Stunden, 0 Minuten und 0 Sekunden zurück.

## Beispiel

Sobald Sie den Code abgeschlossen haben, führen Sie ihn mit dem folgenden Befehl aus:

```bash
npm start
```

Das fertige Ergebnis sieht wie folgt aus:

![Fertige Stoppuhr-Demonstration](../assets/finished.gif)
