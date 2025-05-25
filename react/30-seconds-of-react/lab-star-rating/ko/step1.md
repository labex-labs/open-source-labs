# 별점 (Star Rating)

> `index.html`과 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js`와 `style.css`에만 코드를 추가하면 됩니다.

부모 컴포넌트의 상태에 따라 적절한 모양으로 각 개별 별을 렌더링하는 `Star` 컴포넌트를 만듭니다. 그런 다음, `useState()` 훅을 사용하여 적절한 초기 값으로 `rating` 및 `selection` 상태 변수를 정의하는 `StarRating` 컴포넌트를 정의합니다.

`StarRating`에서 제공된 `event`에 따라 `selection`을 업데이트하는 `hoverOver`라는 메서드를 만듭니다. `event`가 제공되지 않거나 `null`인 경우 `selection`을 `0`으로 재설정합니다. 이벤트 대상의 `.data-star-id` 속성을 사용하여 `selection`의 값을 결정합니다.

다음으로, `Array.from()`을 사용하여 5 개의 요소 배열을 만들고 `Array.prototype.map()`을 사용하여 개별 `<Star>` 컴포넌트를 만듭니다. `hoverOver`를 사용하여 래핑 요소의 `onMouseOver` 및 `onMouseLeave` 이벤트를 처리합니다. `onClick` 이벤트를 `setRating`을 사용하여 처리합니다.

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

마지막으로, `ReactDOM.createRoot(document.getElementById('root')).render(<StarRating value={2} />);`를 호출하여 초기 값 `2`로 `StarRating` 컴포넌트를 렌더링합니다.

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
