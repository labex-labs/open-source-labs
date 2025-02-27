# Stile hinzufügen

In React geben Sie eine CSS-Klasse mit `className` an. Es funktioniert genauso wie das HTML-[class](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/class)-Attribut:

```html
<img className="avatar" />
```

Dann schreiben Sie die CSS-Regeln dafür in einer separaten CSS-Datei:

```css
/* App.css */
.avatar {
  border-radius: 50%;
}
```

React gibt keine Vorgaben darüber vor, wie Sie CSS-Dateien hinzufügen. Im einfachsten Fall fügen Sie ein `<link>`-Tag zu Ihrer HTML hinzu. Wenn Sie ein Build-Tool oder ein Framework verwenden, konsultieren Sie dessen Dokumentation, um zu erfahren, wie Sie einer CSS-Datei zu Ihrem Projekt hinzufügen.

```js
// App.js
import "./App.css";
```

Sie können auch komplexere Ausdrücke in die geschweiften Klammern von JSX einfügen, z. B. [Stringverkettung](https://javascript.info/operators#string-concatenation-with-binary):

```js
// App.js
const user = {
  name: "Hedy Lamarr",
  imageUrl: "https://i.imgur.com/yXOvdOSs.jpg",
  imageSize: 90
};

export default function Profile() {
  return (
    <>
      <h1>{user.name}</h1>
      <img
        className="avatar"
        src={user.imageUrl}
        alt={"Photo of " + user.name}
        style={{
          width: user.imageSize,
          height: user.imageSize
        }}
      />
    </>
  );
}
```

Im obigen Beispiel ist `style={{}}` keine spezielle Syntax, sondern ein reguläres `{}`-Objekt innerhalb der geschweiften Klammern von `style={ }` in JSX. Sie können das `style`-Attribut verwenden, wenn Ihre Stile von JavaScript-Variablen abhängen.
