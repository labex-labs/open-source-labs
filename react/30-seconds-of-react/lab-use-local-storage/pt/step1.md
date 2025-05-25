# Hook `useLocalStorage` em React

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Esta função cria um valor que é salvo no `localStorage` e uma função para modificá-lo. Veja como funciona:

1. Para criar o valor, use o hook `useState()` com uma função para inicializá-lo de forma preguiçosa (lazily).
2. Para recuperar o valor salvo do `localStorage`, use um bloco `try...catch` e `Storage.getItem()`. Se não houver valor salvo, use `Storage.setItem()` para armazenar o `defaultValue` e usá-lo como o estado inicial. Se houver um erro, use `defaultValue`.
3. Defina uma função que atualiza a variável de estado com o valor passado e usa `Storage.setItem()` para salvá-lo.

Aqui está o código:

```jsx
const useLocalStorage = (keyName, defaultValue) => {
  const [storedValue, setStoredValue] = React.useState(() => {
    try {
      const value = window.localStorage.getItem(keyName);

      if (value) {
        return JSON.parse(value);
      } else {
        window.localStorage.setItem(keyName, JSON.stringify(defaultValue));
        return defaultValue;
      }
    } catch (err) {
      return defaultValue;
    }
  });

  const setValue = (newValue) => {
    try {
      window.localStorage.setItem(keyName, JSON.stringify(newValue));
    } catch (err) {}
    setStoredValue(newValue);
  };

  return [storedValue, setValue];
};
```

Você pode usar esta função em seu aplicativo assim:

```jsx
const MyApp = () => {
  const [name, setName] = useLocalStorage("name", "John");

  return <input value={name} onChange={(e) => setName(e.target.value)} />;
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
