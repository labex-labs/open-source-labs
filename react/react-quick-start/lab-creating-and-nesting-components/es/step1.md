# Creación y anidamiento de componentes

> El proyecto de React ya se ha proporcionado en la máquina virtual. En general, solo es necesario agregar código a `App.js`.

Utilice el siguiente comando para instalar las dependencias:

```bash
npm i
```

Las aplicaciones de React están hechas de componentes. Un componente es una parte de la IU (interfaz de usuario) que tiene su propia lógica y apariencia. Un componente puede ser tan pequeño como un botón, o tan grande como una página completa.

Los componentes de React son funciones de JavaScript que devuelven marcado:

```js
// App.js
function MyButton() {
  return <button>Soy un botón</button>;
}
```

Ahora que has declarado `MyButton`, puedes anidarlo en otro componente:

```js
// App.js
export default function MyApp() {
  return (
    <div>
      <h1>Bienvenido a mi aplicación</h1>
      <MyButton />
    </div>
  );
}
```

Observa que `<MyButton />` empieza con una letra mayúscula. Así es como sabes que es un componente de React. Los nombres de los componentes de React siempre deben comenzar con una letra mayúscula, mientras que las etiquetas HTML deben ser en minúsculas.

Las palabras clave `export default` especifican el componente principal en el archivo. Si no estás familiarizado con algún fragmento de sintaxis de JavaScript, [MDN](https://developer.mozilla.org/en-US/docs/web/javascript/reference/statements/export) y [javascript.info](https://javascript.info/import-export) tienen excelentes referencias.

Para ejecutar el proyecto, utiliza el siguiente comando. Luego, puedes actualizar la pestaña **Web 8080** para previsualizar la página web.

```bash
npm start
```
