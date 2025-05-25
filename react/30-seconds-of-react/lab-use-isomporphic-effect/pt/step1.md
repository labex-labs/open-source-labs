# React useIsomporphicEffect Hook

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Para garantir o uso adequado de `useEffect()` no servidor e `useLayoutEffect()` no cliente, você pode usar `typeof` para verificar se o objeto `Window` está definido. Se estiver, retorne `useLayoutEffect()`, caso contrário, retorne `useEffect()`. Aqui está um exemplo de como implementar isso:

```jsx
const useIsomorphicEffect =
  typeof window !== "undefined" ? React.useLayoutEffect : React.useEffect;
```

Então, em seu código, você pode usar `useIsomorphicEffect()` como mostrado neste exemplo:

```jsx
const MyApp = () => {
  useIsomorphicEffect(() => {
    window.console.log("Hello");
  }, []);

  return null;
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Isso registrará 'Hello' no console quando o componente for montado e funcionará corretamente tanto no servidor quanto no cliente.

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
