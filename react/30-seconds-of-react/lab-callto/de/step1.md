# Aufrufbarer Telefonlink

> In der VM wurden bereits `index.html` und `script.js` bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Um einen Link zu erstellen, der eine Telefonnummer anruft, verwenden Sie die Komponente `Callto`. Diese Komponente erstellt ein `<a>`-Element mit einem passenden `href`-Attribut. Um den Link zu rendern, geben Sie die Telefonnummer über die Eigenschaft `phone` und den Linktext über die Eigenschaft `children` an.

```jsx
const Callto = ({ phone, children }) => {
  return <a href={`tel:${phone}`}>{children}</a>;
};
```

Um die `Callto`-Komponente zu verwenden, rufen Sie die Methode `ReactDOM.render()` auf und übergeben das `Callto`-Element mit den festgelegten Eigenschaften `phone` und `children`.

```jsx
ReactDOM.render(
  <Callto phone="+302101234567">Call me!</Callto>,
  document.getElementById("root")
);
```

Klicken Sie bitte in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
