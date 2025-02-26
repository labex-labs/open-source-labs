# Portafolio personal

Para comenzar, abre el editor. Puedes ver los siguientes archivos desde tu editor.

```txt
├── public
├── src
│   ├── components
│   ├── App.css
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

- Por favor, completa este desafío en el archivo `src/App.js`.
- La función `toggleVisible` está definida para comprobar la posición de desplazamiento y actualizar el estado showBackToTopBtn en consecuencia.
- El hook `useEffect` se utiliza para agregar un controlador de eventos al evento de desplazamiento de la ventana, que desencadena la función toggleVisible.
- La función `scrollToTop` está definida para desplazar la ventana hacia la parte superior cuando se hace clic en el botón de volver arriba.

## Ejemplo

Una vez que hayas terminado el código, ejecútalo con el siguiente comando:

```bash
npm start
```

El resultado final es el siguiente:

![Finished project demo](../assets/finished.gif)
