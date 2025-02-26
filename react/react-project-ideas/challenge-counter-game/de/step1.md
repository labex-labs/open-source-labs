# Zählspiel

Um loszulegen, öffnen Sie den Editor. Sie können die folgenden Dateien in Ihrem Editor sehen.

```txt
├── public
├── src
│   ├── components
│   │  └── HomePage
│   │       ├── HomePage.css
│   │       └── HomePage.js
│   ├── App.js
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

- Bitte vervollständigen Sie diese Herausforderung in der Datei `components/HomePage/HomePage.js`.
- Verwenden Sie den `useState`-Hook, um zwei Zustandsvariablen zu definieren: `count` und `timer`.
- Verwenden Sie den `useEffect`-Hook, um den Timer zu starten, wenn sich die Timer-Zustandsvariable ändert.
- Überprüfen Sie den `timer`-Wert. Wenn er null ist, kehrt die Wirkung frühzeitig zurück und tut nichts.
- Wenn der `timer`-Wert nicht null ist, setzt sie ein Intervall ein, das den `timer`-Wert alle Sekunde um 1 (1000 Millisekunden) verringert.
- Geben Sie eine Bereinigungsmethode zurück, die das Intervall löscht, wenn die Komponente entladen wird oder wenn der Timer-Wert sich ändert.

## Beispiel

Sobald Sie den Code abgeschlossen haben, führen Sie ihn mit dem folgenden Befehl aus:

```bash
npm start
```

Das fertige Ergebnis sieht wie folgt aus:

![Finished counter game demo](../assets/finished.gif)
