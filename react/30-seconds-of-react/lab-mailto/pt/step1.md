# Email Link

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Esta função cria um link que, quando clicado, abre o cliente de e-mail do usuário e preenche um novo e-mail com o assunto e o conteúdo do corpo especificados. O link é formatado usando o protocolo `mailto:`.

Para usar a função, forneça uma prop `email` com o endereço de e-mail do destinatário e, opcionalmente, forneça as props `subject` e `body` para preencher o e-mail com o conteúdo inicial. Essas props são codificadas com segurança usando `encodeURIComponent` antes de serem adicionadas à URL do link.

O link é renderizado com os `children` fornecidos como seu conteúdo.

```jsx
const Mailto = ({ email, subject = "", body = "", children }) => {
  const params =
    subject || body
      ? `?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(
          body
        )}`
      : "";

  return <a href={`mailto:${email}${params}`}>{children}</a>;
};
```

Exemplo de uso:

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Mailto email="foo@bar.baz" subject="Hello & Welcome" body="Hello world!">
    Mail me!
  </Mailto>
);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
