# 캐러셀 (Carousel)

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

이 코드는 캐러셀 컴포넌트를 렌더링합니다. 수행하는 단계는 다음과 같습니다.

1. `useState()` 훅을 사용하여 `active` 상태 변수를 생성하고 `0`으로 초기화합니다 (캐러셀의 첫 번째 항목의 인덱스).
2. `useEffect()` 훅을 사용하여 `setTimeout()`으로 타이머를 설정합니다. 타이머가 실행되면 `active`의 값을 캐러셀의 다음 항목의 인덱스로 업데이트합니다 (필요한 경우 나머지 연산자를 사용하여 처음으로 돌아갑니다). 또한 컴포넌트가 언마운트될 때 타이머를 정리합니다.
3. 각 캐러셀 항목에 대한 `className`을 계산합니다. 항목을 매핑하고 항목이 현재 활성 상태인지 여부에 따라 적절한 클래스를 적용합니다.
4. `React.cloneElement()`를 사용하여 캐러셀 항목을 렌더링하고, `...rest`를 사용하여 추가 props 를 전달하고, 계산된 `className`을 각 항목에 추가합니다.

CSS 스타일은 캐러셀 및 해당 항목의 레이아웃을 정의합니다. 캐러셀 컨테이너는 `position: relative`를 가지며, 항목은 기본적으로 `position: absolute` 및 `visibility: hidden`을 갖습니다. 항목이 활성 상태가 되면 `visible` 클래스를 얻어 `visibility`를 `visible`로 설정합니다.

```css
.carousel {
  position: relative;
}

.carousel-item {
  position: absolute;
  visibility: hidden;
}

.carousel-item.visible {
  visibility: visible;
}
```

전체 코드는 다음과 같습니다.

```jsx
const Carousel = ({ carouselItems, ...rest }) => {
  const [active, setActive] = React.useState(0);
  let scrollInterval = null;

  React.useEffect(() => {
    scrollInterval = setTimeout(() => {
      setActive((active + 1) % carouselItems.length);
    }, 2000);
    return () => clearTimeout(scrollInterval);
  });

  return (
    <div className="carousel">
      {carouselItems.map((item, index) => {
        const activeClass = active === index ? " visible" : "";
        return React.cloneElement(item, {
          ...rest,
          className: `carousel-item${activeClass}`
        });
      })}
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <Carousel
    carouselItems={[
      <div>carousel item 1</div>,
      <div>carousel item 2</div>,
      <div>carousel item 3</div>
    ]}
  />
);
```

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
