# Usando Hooks

> El proyecto de React ya se ha proporcionado en la VM. En general, solo necesitas agregar código a `App.js`.

Por favor, utiliza el siguiente comando para instalar las dependencias:

```bash
npm i
```

Las funciones que empiezan con `use` se llaman Hooks. `useState` es un Hook integrado proporcionado por React. Puedes encontrar otros Hooks integrados en la referencia de la API. También puedes escribir tus propios Hooks combinando los existentes.

Los Hooks son más restrictivos que otras funciones. Solo puedes llamar a Hooks en la parte superior de tus componentes (o otros Hooks). Si quieres usar `useState` en una condición o un bucle, extrae un nuevo componente y ponlo allí.

En el ejemplo anterior, cada `MyButton` tenía su propio `count` independiente, y cuando se clicaba cada botón, solo cambiaba el `count` del botón que se había clicado:

![No usando hooks](../assets/1.png)

Sin embargo, a menudo necesitarás que los componentes compartan datos y se actualicen siempre juntos.

Para que ambos componentes `MyButton` muestren el mismo `count` y se actualicen juntos, debes mover el estado de los botones individuales "hacia arriba" hasta el componente más cercano que los contenga a todos.

En este ejemplo, es `MyApp`:

![Usando hooks](../assets/2.png)

Ahora, cuando haces clic en cualquiera de los botones, el `count` en `MyApp` cambiará, lo que cambiará ambos `count` en `MyButton`. Aquí está cómo puedes expresarlo en código.

Primero, mueve el estado hacia arriba desde `MyButton` hasta `MyApp`:

```js
// App.js
export default function MyApp() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return (
    <div>
      <h1>Contadores que se actualizan por separado</h1>
      <MyButton />
      <MyButton />
    </div>
  );
}

function MyButton() {
  //... estamos moviendo código de aquí...
}
```

Luego, pasa el estado hacia abajo desde `MyApp` hasta cada `MyButton`, junto con el manejador de clic compartido. Puedes pasar información a `MyButton` usando las llaves de JSX, al igual que lo hiciste anteriormente con etiquetas integradas como `<img>`:

```js
export default function MyApp() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return (
    <div>
      <h1>Contadores que se actualizan juntos</h1>
      <MyButton count={count} onClick={handleClick} />
      <MyButton count={count} onClick={handleClick} />
    </div>
  );
}
```

La información que pasas de esta manera se llama props. Ahora el componente `MyApp` contiene el estado `count` y el manejador de eventos `handleClick`, y los pasa a ambos botones como props.

Finalmente, cambia `MyButton` para leer las props que has pasado de su componente padre:

```js
function MyButton({ count, onClick }) {
  return <button onClick={onClick}>Clicked {count} times</button>;
}
```

Cuando haces clic en el botón, se activa el manejador `onClick`. La prop `onClick` de cada botón se estableció en la función `handleClick` dentro de `MyApp`, por lo que el código dentro de ella se ejecuta. Ese código llama a `setCount(count + 1)`, incrementando la variable de estado `count`. El nuevo valor de `count` se pasa como una prop a cada botón, por lo que todos muestran el nuevo valor. Esto se llama "subir el estado". Al mover el estado hacia arriba, lo has compartido entre componentes.

```js
import { useState } from "react";

export default function MyApp() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return (
    <div>
      <h1>Contadores que se actualizan juntos</h1>
      <MyButton count={count} onClick={handleClick} />
      <MyButton count={count} onClick={handleClick} />
    </div>
  );
}

function MyButton({ count, onClick }) {
  return <button onClick={onClick}>Clicked {count} times</button>;
}
```

Para ejecutar el proyecto, utiliza el siguiente comando. Luego, puedes actualizar la pestaña **Web 8080** para previsualizar la página web.

```bash
npm start
```
