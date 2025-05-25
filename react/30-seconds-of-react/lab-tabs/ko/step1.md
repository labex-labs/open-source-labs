# 탭 (Tabs)

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

탭 메뉴 및 뷰 컴포넌트를 렌더링하려면 다음 단계를 따르세요.

1. `Tabs` 컴포넌트를 정의합니다. `useState()` 훅을 사용하여 `bindIndex` state 변수를 `defaultIndex`로 설정합니다.
2. `TabItem` 컴포넌트를 정의하고 `Tabs` 컴포넌트에 전달된 `children`을 필터링하여 `TabItem`을 제외한 불필요한 노드를 제거합니다. 함수의 이름을 식별하여 이 작업을 수행할 수 있습니다.
3. `changeTab`이라는 함수를 정의합니다. 이 함수는 사용자가 메뉴에서 `<button>`을 클릭하면 실행됩니다.
4. `changeTab`은 전달된 콜백, `onTabClick`을 실행하고 클릭된 요소를 기반으로 `bindIndex`를 업데이트합니다.
5. 수집된 노드에 `Array.prototype.map()`을 사용하여 탭의 메뉴와 뷰를 렌더링합니다.
6. `bindIndex`의 값을 사용하여 활성 탭을 결정하고 올바른 `className`을 적용합니다.

다음은 탭 메뉴 및 뷰의 스타일을 지정하는 CSS 코드입니다.

```css
.tab-menu > button {
  cursor: pointer;
  padding: 8px 16px;
  border: 0;
  border-bottom: 2px solid transparent;
  background: none;
}

.tab-menu > button.focus {
  border-bottom: 2px solid #007bef;
}

.tab-menu > button:hover {
  border-bottom: 2px solid #007bef;
}

.tab-content {
  display: none;
}

.tab-content.selected {
  display: block;
}
```

다음은 `Tabs` 컴포넌트를 구현하는 JavaScript 코드입니다.

```jsx
const TabItem = (props) => <div {...props} />;

const Tabs = ({ defaultIndex = 0, onTabClick, children }) => {
  const [bindIndex, setBindIndex] = React.useState(defaultIndex);

  const changeTab = (newIndex) => {
    if (typeof onTabClick === "function") onTabClick(newIndex);
    setBindIndex(newIndex);
  };

  const items = children.filter((item) => item.type.name === "TabItem");

  return (
    <div className="wrapper">
      <div className="tab-menu">
        {items.map(({ props: { index, label } }) => (
          <button
            key={`tab-btn-${index}`}
            onClick={() => changeTab(index)}
            className={bindIndex === index ? "focus" : ""}
          >
            {label}
          </button>
        ))}
      </div>
      <div className="tab-view">
        {items.map(({ props }) => (
          <div
            {...props}
            className={`tab-content ${
              bindIndex === props.index ? "selected" : ""
            }`}
            key={`tab-content-${props.index}`}
          />
        ))}
      </div>
    </div>
  );
};
```

마지막으로, `Tabs` 컴포넌트를 사용하는 방법의 예입니다.

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Tabs defaultIndex={1} onTabClick={console.log}>
    <TabItem label="A" index={1}>
      Lorem ipsum
    </TabItem>
    <TabItem label="B" index={2}>
      Dolor sit amet
    </TabItem>
  </Tabs>
);
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하세요. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
