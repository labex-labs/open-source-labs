# 툴팁 (Tooltip)

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

다음은 내용의 더 명확하고 간결하며 일관성 있는 버전입니다.

---

이 코드는 툴팁 컴포넌트를 생성합니다. 사용하려면 다음을 수행하십시오.

1. `useState()` 훅을 사용하여 `show` 변수를 생성하고 `false`로 설정합니다.
2. 툴팁 요소와 컴포넌트에 전달된 `children`을 포함하는 컨테이너 요소를 렌더링합니다.
3. `show` 변수에 의해 제어되는 툴팁의 `className`을 토글하여 `onMouseEnter` 및 `onMouseLeave` 이벤트를 처리합니다.

다음은 툴팁 컴포넌트의 코드입니다.

```css
.tooltip-container {
  position: relative;
}

.tooltip-box {
  position: absolute;
  top: calc(100% + 5px);
  display: none;
  padding: 5px;
  border-radius: 5px;
  background: rgba(0, 0, 0, 0.7);
  color: #fff;
}

.tooltip-box.visible {
  display: block;
}

.tooltip-arrow {
  position: absolute;
  top: -10px;
  left: 50%;
  border-width: 5px;
  border-style: solid;
  border-color: transparent transparent rgba(0, 0, 0, 0.7) transparent;
}
```

```jsx
const Tooltip = ({ children, text, ...rest }) => {
  const [show, setShow] = React.useState(false);

  return (
    <div className="tooltip-container">
      <div className={show ? "tooltip-box visible" : "tooltip-box"}>
        {text}
        <span className="tooltip-arrow" />
      </div>
      <div
        onMouseEnter={() => setShow(true)}
        onMouseLeave={() => setShow(false)}
        {...rest}
      >
        {children}
      </div>
    </div>
  );
};
```

툴팁 컴포넌트를 사용하려면 다음 코드로 `ReactDOM.createRoot()`를 호출하십시오.

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Tooltip text="Simple tooltip">
    <button>Hover me!</button>
  </Tooltip>
);
```

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
