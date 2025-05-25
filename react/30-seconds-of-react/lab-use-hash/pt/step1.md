# React useHash Hook

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Este código rastreia e atualiza o valor hash da localização do navegador. Para usá-lo, siga estes passos:

1. Use o hook `useState()` para obter preguiçosamente a propriedade `hash` do objeto `Location`.
2. Use o hook `useCallback()` para criar um manipulador que atualiza o estado `hash` quando o evento `'hashchange'` é disparado.
3. Use o hook `useEffect()` para adicionar um listener para o evento `'hashchange'` ao montar e limpá-lo ao desmontar.
4. Use o hook `useCallback()` para criar uma função que atualiza a propriedade `hash` do objeto `Location` com o valor fornecido.
5. Em seu componente, chame `useHash()` para obter o valor `hash` atual e uma função `updateHash()` para alterá-lo.
6. Use a função `updateHash()` para alterar o valor `hash`.
7. Renderize o valor `hash` atual em um componente.
8. Crie um campo de entrada que permita ao usuário alterar o valor `hash`.

Aqui está o código:

```jsx
const useHash = () => {
  const [hash, setHash] = React.useState(() => window.location.hash);

  const hashChangeHandler = React.useCallback(() => {
    setHash(window.location.hash);
  }, []);

  React.useEffect(() => {
    window.addEventListener("hashchange", hashChangeHandler);
    return () => {
      window.removeEventListener("hashchange", hashChangeHandler);
    };
  }, []);

  const updateHash = React.useCallback(
    (newHash) => {
      if (newHash !== hash) window.location.hash = newHash;
    },
    [hash]
  );

  return [hash, updateHash];
};

const MyApp = () => {
  const [hash, setHash] = useHash();

  React.useEffect(() => {
    setHash("#list");
  }, []);

  return (
    <>
      <p>Current hash value: {hash}</p>
      <p>Edit hash: </p>
      <input value={hash} onChange={(e) => setHash(e.target.value)} />
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
