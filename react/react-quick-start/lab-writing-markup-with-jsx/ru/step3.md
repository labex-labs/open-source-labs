# Добавление стилей

В React вы указываете CSS-класс с помощью `className`. Это работает так же, как атрибут [class](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/class) в HTML:

```html
<img className="avatar" />
```

Затем вы пишете CSS-правила для него в отдельном CSS-файле:

```css
/* App.css */
.avatar {
  border-radius: 50%;
}
```

React не规定дает, как добавлять CSS-файлы. В простейшем случае вы добавите тег `<link>` в свой HTML. Если вы используете инструмент сборки или фреймворк, обратитесь к его документации, чтобы узнать, как добавить CSS-файл в ваш проект.

```js
// App.js
import "./App.css";
```

Вы также можете поместить более сложные выражения внутри фигурных скобок JSX, например, [конкатенацию строк](https://javascript.info/operators#string-concatenation-with-binary):

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

В приведенном выше примере `style={{}}` не является специальным синтаксисом, а обычным объектом `{}` внутри фигурных скобок `style={ }` JSX. Вы можете использовать атрибут `style`, когда ваши стили зависят от переменных JavaScript.
