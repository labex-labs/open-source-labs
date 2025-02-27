# Respondiendo a eventos

> El proyecto de React ya se ha proporcionado en la VM. En general, solo necesitas agregar código a `App.js`.

Por favor, utiliza el siguiente comando para instalar las dependencias:

```bash
npm i
```

React te permite agregar manejadores de eventos a tu JSX. Los manejadores de eventos son tus propias funciones que se dispararán en respuesta a interacciones como hacer clic, pasar el cursor por encima, enfocar en los campos de formulario, etc.

Para agregar un manejador de eventos, primero definirás una función y luego [la pasarás como una propiedad](https://react.dev/learn/passing-props-to-a-component) a la etiqueta JSX adecuada. Por ejemplo, aquí hay un botón que todavía no hace nada:

```js
// App.js
export default function Button() {
  return <button>No hago nada</button>;
}
```

Puedes hacer que muestre un mensaje cuando un usuario haga clic siguiendo estos tres pasos:

1. Declara una función llamada `handleClick` dentro de tu componente `Button`.
2. Implementa la lógica dentro de esa función (utiliza `alert` para mostrar el mensaje).
3. Agrega `onClick={handleClick}` a la etiqueta JSX `<button>`.

```js
export default function Button() {
  function handleClick() {
    alert("Me has hecho clic!");
  }

  return <button onClick={handleClick}>Haz clic en mí</button>;
}
```

Definiste la función `handleClick` y luego la pasaste como una propiedad a `<button>`. `handleClick` es un manejador de eventos. Las funciones de manejador de eventos:

Por lo general, se definen dentro de tus componentes.
Tienen nombres que empiezan con `handle`, seguidos del nombre del evento.

Para ejecutar el proyecto, utiliza el siguiente comando. Luego, puedes actualizar la pestaña **Web 8080** para previsualizar la página web.

```bash
npm start
```

Por convención, es común nombrar a los manejadores de eventos como `handle` seguido del nombre del evento. Con frecuencia verás `onClick={handleClick}`, `onMouseEnter={handleMouseEnter}`, etc.

Alternativamente, puedes definir un manejador de eventos en línea en el JSX:

```js
<button onClick={function handleClick() {
  alert('Me has hecho clic!');
}}>
```

O, más concisamente, utilizando una función flecha:

```js
<button onClick={() => {
  alert('Me has hecho clic!');
}}>
```

Todos estos estilos son equivalentes. Los manejadores de eventos en línea son convenientes para funciones cortas.
