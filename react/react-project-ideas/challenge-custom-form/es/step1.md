# Formulario Personalizado

Para comenzar, abre el editor. Puedes ver los siguientes archivos desde tu editor.

```txt
├── public
├── src
│   ├── components
│   │   └── CustomForm
│   │       ├── CustomForm.css
│   │       └── CustomForm.js
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

- Completa este desafío en el archivo `App.js`.
- Utiliza el hook `useRef` para crear dos objetos de referencia, `usernameRef` y `passwordRef`. Estas referencias se utilizarán para acceder a los valores de los campos de entrada.
- Función `handleLogin`: Esta función se llama cuando se hace clic en el botón "Iniciar sesión". Registra los valores de los campos de entrada de nombre de usuario y contraseña en la consola y muestra una alerta con el nombre de usuario y la contraseña ingresados.
- Función `handleRegister`: Esta función se llama cuando se hace clic en el botón "Registrarse". Registra los valores de los campos de entrada de nombre de usuario y contraseña en la consola.

## Ejemplo

Una vez que hayas terminado el código, ejecútalo con el siguiente comando:

```bash
npm start
```

El resultado final es el siguiente:

![Custom Form Final Result](../assets/finished.gif)
