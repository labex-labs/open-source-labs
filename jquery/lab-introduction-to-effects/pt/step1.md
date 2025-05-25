# Mostrar e Ocultar Conteúdo

> `index.html` já foi fornecido na VM.

O jQuery pode mostrar ou ocultar conteúdo instantaneamente com `.show()` ou `.hide()`:

```js
// Instantaneamente ocultar todos os parágrafos
$("p").hide();

// Instantaneamente mostrar todas as divs que possuem a classe de estilo hidden
$("div.hidden").show();
```

Quando o jQuery oculta um elemento, ele define sua propriedade CSS `display` como `none`. Isso significa que o conteúdo terá largura e altura zero; não significa que o conteúdo simplesmente se tornará transparente e deixará uma área vazia na página.

O jQuery também pode mostrar ou ocultar conteúdo por meio de efeitos de animação. Você pode dizer a `.show()` e `.hide()` para usar a animação de algumas maneiras. Uma delas é passar um argumento de `'slow'`, `'normal'` ou `'fast'`:

```js
// Lentamente ocultar todos os parágrafos
$("p").hide("slow");

// Rapidamente mostrar todas as divs que possuem a classe de estilo hidden
$("div.hidden").show("fast");
```

Se você preferir um controle mais direto sobre a duração do efeito de animação, pode passar a duração desejada em milissegundos para `.show()` e `.hide()`:

```js
// Ocultar todos os parágrafos em meio segundo
$("p").hide(2000);

// Mostrar todas as divs que possuem a classe de estilo hidden em 1,25 segundos
$("div.hidden").show(1250);
```

A maioria dos desenvolvedores passa um número de milissegundos para ter um controle mais preciso sobre a duração.

> Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
