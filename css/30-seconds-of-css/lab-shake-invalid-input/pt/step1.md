# Shake em Entrada Inválida

`index.html` e `style.css` já foram fornecidos na VM.

Para criar uma animação de "shake" (tremor) quando houver uma entrada inválida, siga estes passos:

1.  Use o atributo `pattern` para definir uma expressão regular que especifica a entrada permitida. Por exemplo, use `[A-Za-z]*` para permitir apenas letras.
2.  Defina uma animação de "shake" usando `@keyframes`. Defina a propriedade `margin-left` para mover a entrada para a esquerda e para a direita.
3.  Use a pseudo-classe `:invalid` para aplicar a animação de "shake" à entrada.
4.  Opcionalmente, adicione uma `box-shadow` vermelha à entrada para indicar o erro.

Aqui está um exemplo de trecho de código:

```html
<input type="text" placeholder="Letters only" pattern="[A-Za-z]*" />
```

```css
@keyframes shake {
  0% {
    margin-left: 0rem;
  }
  25% {
    margin-left: 0.5rem;
  }
  75% {
    margin-left: -0.5rem;
  }
  100% {
    margin-left: 0rem;
  }
}

input:invalid {
  animation: shake 0.2s ease-in-out 0s 2;
  box-shadow: 0 0 0.6rem #ff0000;
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
