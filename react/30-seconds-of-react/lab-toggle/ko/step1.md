# 토글 (Toggle)

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

토글 컴포넌트를 렌더링하려면 다음 단계를 따르세요.

1. `useState()` 훅을 사용하여 `isToggledOn` 상태 변수를 `defaultToggled`로 초기화합니다.
2. `<input>` 요소를 렌더링하고 해당 `onClick` 이벤트를 바인딩하여 `isToggledOn` 상태 변수를 업데이트합니다. 래핑하는 `<label>` 요소에 적절한 `className`을 적용합니다.
3. 다음 CSS 를 사용하여 토글 컴포넌트의 스타일을 지정합니다.

```css
.toggle input[type="checkbox"] {
  display: none;
}

.toggle.on {
  background-color: green;
}

.toggle.off {
  background-color: red;
}
```

다음은 코드입니다.

```jsx
const Toggle = ({ defaultToggled = false }) => {
  const [isToggleOn, setIsToggleOn] = React.useState(defaultToggled);

  return (
    <label className={isToggleOn ? "toggle on" : "toggle off"}>
      <input
        type="checkbox"
        checked={isToggleOn}
        onChange={() => setIsToggleOn(!isToggleOn)}
      />
      {isToggleOn ? "ON" : "OFF"}
    </label>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<Toggle />);
```

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하세요. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
