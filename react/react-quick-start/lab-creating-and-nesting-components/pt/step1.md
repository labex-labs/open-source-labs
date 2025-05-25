# Criando e Aninhando Componentes

> O projeto React já foi fornecido na VM. Em geral, você só precisa adicionar código ao `App.js`.

Por favor, use o seguinte comando para instalar as dependências:

```bash
npm i
```

Aplicativos React são feitos de componentes. Um componente é uma parte da UI (interface do usuário) que possui sua própria lógica e aparência. Um componente pode ser tão pequeno quanto um botão ou tão grande quanto uma página inteira.

Componentes React são funções JavaScript que retornam markup:

```js
// App.js
function MyButton() {
  return <button>I'm a button</button>;
}
```

Agora que você declarou `MyButton`, você pode aninhá-lo em outro componente:

```js
// App.js
export default function MyApp() {
  return (
    <div>
      <h1>Welcome to my app</h1>
      <MyButton />
    </div>
  );
}
```

Observe que `<MyButton />` começa com uma letra maiúscula. É assim que você sabe que é um componente React. Nomes de componentes React devem sempre começar com uma letra maiúscula, enquanto as tags HTML devem ser minúsculas.

As palavras-chave `export default` especificam o componente principal no arquivo. Se você não estiver familiarizado com alguma parte da sintaxe JavaScript, [MDN](https://developer.mozilla.org/en-US/docs/web/javascript/reference/statements/export) e [javascript.info](https://javascript.info/import-export) têm ótimas referências.

Para executar o projeto, use o seguinte comando. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.

```bash
npm start
```
