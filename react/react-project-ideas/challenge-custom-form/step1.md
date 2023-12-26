# Custom Form

To get started, open the editor. You can see the following files from your editor.

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

## Requirements

- To install the project dependencies, use the following command:

  ```bash
  npm i
  ```

- Please complete this challenge in the `App.js` file.
- Use the `useRef` hook to create two ref objects, `usernameRef` and `passwordRef`. These refs will be used to access the values of the input fields.
- `handleLogin` function: This function is called when the "Login" button is clicked. It logs the values of the username and password input fields to the console and displays an alert with the entered username and password.
- `handleRegister` function: This function is called when the "Register" button is clicked. It logs the values of the username and password input fields to the console.

## Example

Once you have completed the code, run it with the following command: 

```bash
npm start
```

The finished result is as follows:

![finished](./assets/finished.gif)
