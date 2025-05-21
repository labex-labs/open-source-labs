# Criando a Estrutura HTML

Agora que entendemos nossos arquivos de projeto, vamos criar a estrutura HTML para o nosso padrão quadriculado.

1. Abra o arquivo `index.html` no editor novamente.

2. Precisamos adicionar um elemento container para o nosso padrão quadriculado. Dentro da tag `<body>`, substitua o comentário por um elemento `<div>` que tenha a classe "checkerboard":

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Checkerboard Pattern</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <div class="checkerboard"></div>
  </body>
</html>
```

3. Salve o arquivo `index.html` pressionando Ctrl+S ou clicando em File > Save.

4. Agora, vamos adicionar algum CSS básico para definir as dimensões do nosso quadriculado. Abra o arquivo `style.css` e adicione o seguinte código:

```css
.checkerboard {
  width: 240px;
  height: 240px;
  background-color: #fff;
}
```

Este código CSS faz o seguinte:

- Define a largura e a altura do nosso quadriculado para 240 pixels
- Define a cor de fundo para branco (#fff)

5. Salve o arquivo `style.css`.

6. Atualize a aba **Web 8080** para ver as alterações.

Você deve agora ver um quadrado branco com uma largura e altura de 240 pixels. Esta será a tela para o nosso padrão quadriculado.
