# Adicionando Estilos

No React, você especifica uma classe CSS com `className`. Funciona da mesma forma que o atributo HTML [class](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/class):

```html
<img className="avatar" />
```

Então você escreve as regras CSS para ela em um arquivo CSS separado:

```css
/* App.css */
.avatar {
  border-radius: 50%;
}
```

O React não prescreve como você adiciona arquivos CSS. No caso mais simples, você adicionará uma tag `<link>` ao seu HTML. Se você usar uma ferramenta de build ou um framework, consulte sua documentação para aprender como adicionar um arquivo CSS ao seu projeto.

```js
// App.js
import "./App.css";
```

Você pode colocar expressões mais complexas dentro das chaves JSX também, por exemplo, [concatenação de strings](https://javascript.info/operators#string-concatenation-with-binary):

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

No exemplo acima, `style={{}}` não é uma sintaxe especial, mas um objeto `{}` regular dentro das chaves JSX `style={ }`. Você pode usar o atributo `style` quando seus estilos dependem de variáveis JavaScript.
