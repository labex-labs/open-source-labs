# 접을 수 있는 아코디언 (Collapsible Accordion)

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

여러 개의 접을 수 있는 콘텐츠 요소를 갖춘 아코디언 메뉴를 렌더링하려면 다음 단계를 따르세요.

1. `<button>`을 렌더링하고 `handleClick` 콜백을 통해 부모에게 알리면서 컴포넌트를 업데이트하는 `AccordionItem` 컴포넌트를 정의합니다.
2. `AccordionItem`에서 `isCollapsed` prop 을 사용하여 모양을 결정하고 `className`을 설정합니다.
3. `Accordion` 컴포넌트를 정의하고 `useState()` 훅을 사용하여 `bindIndex` 상태 변수의 값을 `defaultIndex`로 초기화합니다.
4. 함수의 이름을 식별하여 `AccordionItem`을 제외하고 불필요한 노드를 제거하기 위해 `children`을 필터링합니다.
5. 수집된 노드에 `Array.prototype.map()`을 사용하여 개별 접을 수 있는 요소를 렌더링합니다.
6. `AccordionItem`의 `<button>`을 클릭할 때 실행될 `changeItem`을 정의합니다.
7. `changeItem`은 전달된 콜백인 `onItemClick`을 실행하고 클릭된 요소를 기반으로 `bindIndex`를 업데이트합니다.

다음은 코드입니다.

```css
.accordion-item.collapsed {
  display: none;
}

.accordion-item.expanded {
  display: block;
}

.accordion-button {
  display: block;
  width: 100%;
}
```

```jsx
const AccordionItem = ({ label, isCollapsed, handleClick, children }) => {
  return (
    <>
      <button className="accordion-button" onClick={handleClick}>
        {label}
      </button>
      <div
        className={`accordion-item ${isCollapsed ? "collapsed" : "expanded"}`}
        aria-expanded={isCollapsed}
      >
        {children}
      </div>
    </>
  );
};

const Accordion = ({ defaultIndex, onItemClick, children }) => {
  const [bindIndex, setBindIndex] = React.useState(defaultIndex);

  const changeItem = (itemIndex) => {
    if (typeof onItemClick === "function") onItemClick(itemIndex);
    if (itemIndex !== bindIndex) setBindIndex(itemIndex);
  };

  const items = children.filter((item) => item.type.name === "AccordionItem");

  return (
    <>
      {items.map(({ props }) => (
        <AccordionItem
          isCollapsed={bindIndex !== props.index}
          label={props.label}
          handleClick={() => changeItem(props.index)}
          children={props.children}
        />
      ))}
    </>
  );
};
```

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Accordion defaultIndex="1" onItemClick={console.log}>
    <AccordionItem label="A" index="1">
      Lorem ipsum
    </AccordionItem>
    <AccordionItem label="B" index="2">
      Dolor sit amet
    </AccordionItem>
  </Accordion>
);
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
