# Hook React useSessionStorage

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Para criar um valor de estado que é persistido no `sessionStorage`, e uma função para atualizá-lo, siga estes passos:

1. Use o hook `useState()` com uma função para inicializar seu valor de forma preguiçosa (lazily).
2. Use um bloco `try...catch` e `Storage.getItem()` para tentar obter o valor do `Window.sessionStorage`. Se nenhum valor for encontrado, use `Storage.setItem()` para armazenar o `defaultValue` e usá-lo como o estado inicial. Se ocorrer um erro, use `defaultValue` como o estado inicial.
3. Defina uma função que irá atualizar a variável de estado com o valor passado e use `Storage.setItem()` para armazená-lo.

Aqui está um exemplo de implementação:

```jsx
const useSessionStorage = (keyName, defaultValue) => {
  const [storedValue, setStoredValue] = React.useState(() => {
    try {
      const value = window.sessionStorage.getItem(keyName);

      if (value) {
        return JSON.parse(value);
      } else {
        window.sessionStorage.setItem(keyName, JSON.stringify(defaultValue));
        return defaultValue;
      }
    } catch (err) {
      return defaultValue;
    }
  });

  const setValue = (newValue) => {
    try {
      window.sessionStorage.setItem(keyName, JSON.stringify(newValue));
    } catch (err) {}
    setStoredValue(newValue);
  };

  return [storedValue, setValue];
};
```

Você pode usar este hook em seu aplicativo assim:

```jsx
const MyApp = () => {
  const [name, setName] = useSessionStorage("name", "John");

  return <input value={name} onChange={(e) => setName(e.target.value)} />;
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
