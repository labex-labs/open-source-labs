# Classificação por Estrelas (Star Rating)

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Crie um componente `Star` que renderize cada estrela individual com a aparência apropriada com base no estado do componente pai. Em seguida, defina um componente `StarRating` que usa o hook `useState()` para definir as variáveis de estado `rating` e `selection` com os valores iniciais apropriados.

Em `StarRating`, crie um método chamado `hoverOver` que atualiza `selection` de acordo com o `event` fornecido. Se `event` não for fornecido ou for `null`, redefina `selection` para `0`. Use o atributo `.data-star-id` do alvo do evento para determinar o valor de `selection`.

Em seguida, crie um array de 5 elementos usando `Array.from()` e crie componentes `<Star>` individuais usando `Array.prototype.map()`. Lide com os eventos `onMouseOver` e `onMouseLeave` do elemento de encapsulamento usando `hoverOver`. Lide com o evento `onClick` usando `setRating`.

```css
.star {
  color: #ff9933;
  cursor: pointer;
}
```

```jsx
const Star = ({ marked, starId }) => {
  return (
    <span data-star-id={starId} className="star" role="button">
      {marked ? "\u2605" : "\u2606"}
    </span>
  );
};

const StarRating = ({ value }) => {
  const [rating, setRating] = React.useState(parseInt(value) || 0);
  const [selection, setSelection] = React.useState(0);

  const hoverOver = (event) => {
    let val = 0;
    if (event && event.target && event.target.getAttribute("data-star-id"))
      val = event.target.getAttribute("data-star-id");
    setSelection(val);
  };

  return (
    <div
      onMouseLeave={() => hoverOver(null)}
      onMouseOver={hoverOver}
      onClick={(e) =>
        setRating(e.target.getAttribute("data-star-id") || rating)
      }
    >
      {Array.from({ length: 5 }, (v, i) => (
        <Star
          starId={i + 1}
          key={`star_${i + 1}`}
          marked={selection ? selection >= i + 1 : rating >= i + 1}
        />
      ))}
    </div>
  );
};
```

Finalmente, renderize o componente `StarRating` com um valor inicial de `2` chamando `ReactDOM.createRoot(document.getElementById('root')).render(<StarRating value={2} />);`.

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
