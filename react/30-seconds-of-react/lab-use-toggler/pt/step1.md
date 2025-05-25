# React useToggler Hook

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Para criar uma variável de estado booleana que pode ser alternada entre seus dois estados, siga estes passos:

1. Use o hook `useState()` para criar a variável de estado `value` e seu setter.
2. Crie uma função que alterna o valor da variável de estado `value` e memorize-a, usando o hook `useCallback()`.
3. Retorne a variável de estado `value` e a função de alternância (toggler) memorizada.

Aqui está um exemplo de implementação:

```jsx
const useToggler = (initialState) => {
  const [value, setValue] = React.useState(initialState);

  const toggleValue = React.useCallback(() => setValue((prev) => !prev), []);

  return [value, toggleValue];
};
```

Você pode então usar este hook em seus componentes, assim:

```jsx
const Switch = () => {
  const [val, toggleVal] = useToggler(false);
  return <button onClick={toggleVal}>{val ? "ON" : "OFF"}</button>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<Switch />);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
