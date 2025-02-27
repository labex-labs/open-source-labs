# Mostrando datos

JSX te permite poner marcas dentro de JavaScript. Las llaves curvas te permiten "escapar hacia atrás" a JavaScript para que puedas incrustar alguna variable de tu código y mostrarla al usuario. Por ejemplo, esto mostrará `user.name`:

```js
// App.js
const user = {
  name: "Hedy Lamarr"
};
export default function Profile() {
  return (
    <>
      <h1>{user.name}</h1>
    </>
  );
}
```

También puedes "escapar hacia JavaScript" desde los atributos de JSX, pero debes usar llaves curvas en lugar de comillas. Por ejemplo, `className="avatar"` pasa la cadena `"avatar"` como la clase CSS, pero `src={user.imageUrl}` lee el valor de la variable JavaScript `user.imageUrl`, y luego pasa ese valor como el atributo `src`:

```js
// App.js
const user = {
  name: "Hedy Lamarr",
  imageUrl: "https://i.imgur.com/yXOvdOSs.jpg"
};
export default function Profile() {
  return (
    <>
      <h1>{user.name}</h1>
      <img className="avatar" src={user.imageUrl} />
    </>
  );
}
```
