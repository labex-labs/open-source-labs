# Juego de Contador

Para comenzar, abre el editor. Puedes ver los siguientes archivos desde tu editor.

```txt
├── public
├── src
│   ├── components
│   │  └── HomePage
│   │       ├── HomePage.css
│   │       └── HomePage.js
│   ├── App.js
│   ├── index.css
│   └── index.js
├── package-lock.json
└── package.json
```

## Requisitos

- Para instalar las dependencias del proyecto, utiliza el siguiente comando:

  ```bash
  npm i
  ```

- Completa este desafío en el archivo `components/HomePage/HomePage.js`.
- Utiliza el hook `useState` para definir dos variables de estado: `count` y `timer`.
- Utiliza el hook `useEffect` para iniciar el temporizador cuando la variable de estado del temporizador cambia.
- Verifica el valor de `timer`. Si es cero, el efecto se detiene temprano y no hace nada.
- Si el valor de `timer` no es cero, establece un intervalo que decremente el valor de `timer` en 1 cada segundo (1000 milisegundos).
- Devuelve una función de limpieza que elimine el intervalo cuando el componente se desmonta o cuando el valor del temporizador cambia.

## Ejemplo

Una vez que hayas terminado el código, ejecútalo con el siguiente comando:

```bash
npm start
```

El resultado final es el siguiente:

![Finished counter game demo](../assets/finished.gif)
