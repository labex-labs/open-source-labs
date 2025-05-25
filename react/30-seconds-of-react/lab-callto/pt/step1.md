# Link de Telefone Chamável

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Para criar um link que liga para um número de telefone, use o componente `Callto`. Este componente cria um elemento `<a>` com um atributo `href` apropriado. Para renderizar o link, especifique o número de telefone usando a prop `phone` e o texto do link usando a prop `children`.

```jsx
const Callto = ({ phone, children }) => {
  return <a href={`tel:${phone}`}>{children}</a>;
};
```

Para usar o componente `Callto`, chame o método `ReactDOM.render()` e passe o elemento `Callto` com as props `phone` e `children` definidas.

```jsx
ReactDOM.render(
  <Callto phone="+302101234567">Ligue para mim!</Callto>,
  document.getElementById("root")
);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
