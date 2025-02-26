# Benutzerdefiniertes Formular

Um loszulegen, öffnen Sie den Editor. Sie können die folgenden Dateien in Ihrem Editor sehen.

```txt
├── public
├── src
│   ├── components
│   │   └── CustomForm
│   │       ├── CustomForm.css
│   │       └── CustomForm.js
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

- Bitte vervollständigen Sie diese Herausforderung in der Datei `App.js`.
- Verwenden Sie den `useRef`-Hook, um zwei Ref-Objekte, `usernameRef` und `passwordRef`, zu erstellen. Diese Refs werden verwendet, um die Werte der Eingabefelder zuzugreifen.
- `handleLogin`-Funktion: Diese Funktion wird aufgerufen, wenn der "Login"-Button geklickt wird. Sie protokolliert die Werte der Benutzernamen- und Passwort-Eingabefelder in die Konsole und zeigt eine Meldung mit dem eingegebenen Benutzernamen und Passwort an.
- `handleRegister`-Funktion: Diese Funktion wird aufgerufen, wenn der "Register"-Button geklickt wird. Sie protokolliert die Werte der Benutzernamen- und Passwort-Eingabefelder in die Konsole.

## Beispiel

Wenn Sie den Code abgeschlossen haben, führen Sie ihn mit dem folgenden Befehl aus:

```bash
npm start
```

Das fertige Ergebnis sieht wie folgt aus:

![Custom Form Final Result](../assets/finished.gif)
