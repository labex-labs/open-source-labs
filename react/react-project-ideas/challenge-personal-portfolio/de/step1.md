# Persönliches Portfolio

Um zu beginnen, öffnen Sie den Editor. Sie können die folgenden Dateien in Ihrem Editor sehen.

```txt
├── public
├── src
│   ├── components
│   ├── App.css
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

- Bitte vervollständigen Sie diese Herausforderung in der Datei `src/App.js`.
- Die Funktion `toggleVisible` ist definiert, um die Scrollposition zu überprüfen und den Zustand `showBackToTopBtn` entsprechend zu aktualisieren.
- Der Hook `useEffect` wird verwendet, um einen Event-Listener für das Scrollereignis des Fensters hinzuzufügen, das die Funktion `toggleVisible` auslöst.
- Die Funktion `scrollToTop` ist definiert, um das Fenster zum oberen Rand zu scrollen, wenn auf die Rück-zu-oben-Schaltfläche geklickt wird.

## Beispiel

Sobald Sie den Code abgeschlossen haben, führen Sie ihn mit dem folgenden Befehl aus:

```bash
npm start
```

Das fertige Ergebnis sieht wie folgt aus:

![Finished project demo](../assets/finished.gif)
