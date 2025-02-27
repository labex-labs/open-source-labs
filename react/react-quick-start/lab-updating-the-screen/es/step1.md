# Actualización de la pantalla

> El proyecto de React ya se ha proporcionado en la máquina virtual. En general, solo es necesario agregar código a `App.js`.

Utilice el siguiente comando para instalar las dependencias:

```bash
npm i
```

Con frecuencia, desearás que tu componente "recuerde" alguna información y la muestre. Por ejemplo, quizás desees contar el número de veces que se hace clic en un botón. Para hacer esto, agregue estado a su componente.

Primero, importe `useState` de React:

```js
import { useState } from "react";
```

Ahora puede declarar una variable de estado dentro de su componente:

```js
function MyButton() {
  const [count, setCount] = useState(0);
  //...
```

Obtendrás dos cosas de `useState`: el estado actual (`count`), y la función que te permite actualizarlo (`setCount`). Puedes darles cualquier nombre, pero la convención es escribir `[algo, setAlgo]`.

La primera vez que se muestra el botón, `count` será `0` porque se pasó 0 a `useState()`. Cuando desees cambiar el estado, llame a `setCount()` y pase el nuevo valor a ella. Hacer clic en este botón incrementará el contador:

```js
function MyButton() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return <button onClick={handleClick}>Clicked {count} times</button>;
}
```

React llamará nuevamente a tu función de componente. Esta vez, `count` será `1`. Luego será `2`. Y así sucesivamente.

Si renderizas el mismo componente varias veces, cada uno tendrá su propio estado. Haz clic en cada botón por separado:

```js
// App.js
import { useState } from "react";

export default function MyApp() {
  return (
    <div>
      <h1>Counters that update separately</h1>
      <MyButton />
      <MyButton />
    </div>
  );
}

function MyButton() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return <button onClick={handleClick}>Clicked {count} times</button>;
}
```

Observa cómo cada botón "recuerda" su propio estado `count` y no afecta a otros botones.

Para ejecutar el proyecto, use el siguiente comando. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.

```bash
npm start
```
