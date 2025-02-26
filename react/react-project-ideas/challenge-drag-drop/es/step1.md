# Arrastrar y soltar

Para comenzar, abre el editor. Puedes ver los siguientes archivos desde tu editor.

```txt
├── public
├── src
│   ├── App.js
│   ├── App.css
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

- Por favor, completa este desafío en el archivo `App.js`.
- La función `onDragStart` está definida. Es un controlador de eventos para el evento dragstart en una tarjeta de tarea. Establece los datos de transferencia de datos en la propiedad name de la tarea, que se utilizará para identificar la tarea cuando se suelte.
- La función `onDrop` está definida. Es un controlador de eventos para el evento drop en el tablero de tareas. Recupera el nombre de la tarea a partir de los datos de transferencia de datos, actualiza la categoría de la tarea en el estado de tareas según la ubicación de la suelta (cat), y establece el estado de tareas actualizado utilizando setTasks.

## Ejemplo

Una vez que hayas terminado el código, ejecútalo con el siguiente comando:

```bash
npm start
```

El resultado final es el siguiente:

![Drag and drop demo](../assets/finished.gif)
