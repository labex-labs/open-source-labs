# 접을 수 있는 콘텐츠

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

이 함수는 콘텐츠의 가시성을 토글하는 버튼이 있는 접을 수 있는 컴포넌트를 렌더링합니다. 사용 방법은 다음과 같습니다.

1. `useState()` 훅을 사용하여 콘텐츠가 현재 접혀 있는지 확장되었는지를 나타내는 `isCollapsed` 상태 변수를 생성합니다. 이를 `collapsed`로 초기화합니다.
2. `<button>` 요소를 사용하여 `isCollapsed` 상태를 토글하고 `children` prop 을 통해 전달된 콘텐츠를 표시/숨깁니다.
3. `isCollapsed`를 사용하여 콘텐츠 컨테이너에 적절한 CSS 클래스 (`collapsed` 또는 `expanded`) 를 적용하여 모양을 결정합니다.
4. `isCollapsed` 상태를 기반으로 콘텐츠 컨테이너의 `aria-expanded` 속성을 업데이트하여 장애가 있는 사용자가 컴포넌트에 접근할 수 있도록 합니다.

이 컴포넌트에 필요한 CSS 코드는 다음과 같습니다.

```css
.collapse-button {
  display: block;
  width: 100%;
}

.collapse-content.collapsed {
  display: none;
}

.collapse-content.expanded {
  display: block;
}
```

다음은 JavaScript 코드입니다.

```jsx
const Collapse = ({ collapsed, children }) => {
  const [isCollapsed, setIsCollapsed] = React.useState(collapsed);

  return (
    <>
      <button
        className="collapse-button"
        onClick={() => setIsCollapsed(!isCollapsed)}
      >
        {isCollapsed ? "Show" : "Hide"} content
      </button>
      <div
        className={`collapse-content ${isCollapsed ? "collapsed" : "expanded"}`}
        aria-expanded={isCollapsed}
      >
        {children}
      </div>
    </>
  );
};
```

이 컴포넌트를 사용하려면 접을 콘텐츠와 함께 간단히 호출하십시오.

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Collapse>
    <h1>This is a collapse</h1>
    <p>Hello world!</p>
  </Collapse>
);
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
