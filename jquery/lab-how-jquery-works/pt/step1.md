# Como o jQuery Funciona

> `index.html` já foi fornecido na VM.

Este arquivo será gerado automaticamente durante a inicialização do ambiente. Se não for gerado automaticamente, crie o arquivo e a função conforme mostrado na imagem acima. O código da função é o seguinte:

```html
<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Demo</title>
  </head>
  <body>
    <p>jQuery</p>
    <script src="jquery.min.js"></script>
    <script>
      // Your code goes here.
    </script>
  </body>
</html>
```

O atributo `src` no elemento `<script>` deve apontar para uma cópia do jQuery. Baixe uma cópia do jQuery na página [Downloading jQuery](https://jquery.com/download/) e armazene o arquivo `jquery.min.js` no mesmo diretório do seu arquivo HTML.

> Nota: Ao baixar o jQuery, o nome do arquivo pode conter um número de versão, por exemplo, `jquery-x.y.z.js`. Certifique-se de renomear este arquivo para `jquery.js` ou atualizar o atributo `src` do elemento `<script>` para corresponder ao nome do arquivo.

#### Executando o Código no Document Ready

Para garantir que seu código seja executado após o navegador terminar de carregar o documento, muitos programadores JavaScript envolvem seu código em uma função `onload`:

```js
window.onload = function () {
  alert("welcome");
};
```

Infelizmente, o código não é executado até que todas as imagens terminem de baixar, incluindo anúncios em banner. Para executar o código assim que o documento estiver pronto para ser manipulado, o jQuery tem uma instrução conhecida como [ready event](http://api.jquery.com/ready/):

```js
$(document).ready(function () {
  // Your code here.
});
```

> Nota: A biblioteca jQuery expõe seus métodos e propriedades por meio de duas propriedades do objeto `window` chamadas `jQuery` e `$`. `$` é simplesmente um alias para `jQuery` e é frequentemente empregado porque é mais curto e rápido de escrever.

Por exemplo, dentro do evento ready, você pode adicionar um manipulador de clique ao link:

```js
$(document).ready(function () {
  $("button").click(function () {
    $("p").text("Hello jQuery!");
  });
});
```

Copie o código jQuery acima para o seu arquivo HTML onde diz `// Your code goes here`. Em seguida, salve seu arquivo HTML e recarregue a página de teste no seu navegador.

#### Exemplo Completo

O exemplo a seguir ilustra o código de manipulação de clique discutido acima, incorporado diretamente no `<body>` do HTML. Observe que, na prática, geralmente é melhor colocar seu código em um arquivo JS separado e carregá-lo na página com o atributo `src` de um elemento `<script>`.

```html
<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Demo</title>
  </head>
  <body>
    <button>click me</button>
    <p>Hello World</p>
    <script src="jquery.min.js"></script>
    <script>
      $(document).ready(function () {
        $("button").click(function () {
          $("p").text("Hello jQuery!");
        });
      });
    </script>
  </body>
</html>
```

> Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
