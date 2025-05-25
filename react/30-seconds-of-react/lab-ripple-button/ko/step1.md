# 리플 효과 (Ripple Effect) 가 있는 버튼

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

이 코드는 클릭 시 리플 효과를 생성하는 버튼 컴포넌트를 렌더링합니다. 작동 방식은 다음과 같습니다.

- `useState()` 훅 (hook) 은 `coords`와 `isRippling`의 두 가지 상태 변수를 생성하는 데 사용됩니다. `coords` 변수는 포인터의 좌표를 저장하고, `isRippling`은 버튼의 애니메이션 상태를 저장합니다.
- `useEffect()` 훅은 `coords` 상태 변수가 변경될 때마다 `isRippling`의 값을 변경하는 데 사용됩니다. 이는 리플 효과의 애니메이션을 시작합니다.
- `setTimeout()`은 이전 훅에서 애니메이션이 완료된 후 애니메이션을 지우는 데 사용됩니다.
- 다른 `useEffect()` 훅은 `isRippling` 상태 변수가 `false`일 때마다 `coords`를 재설정하는 데 사용됩니다.
- `onClick` 이벤트는 `coords` 상태 변수를 업데이트하고 전달된 콜백 함수를 호출하여 처리됩니다.

다음은 `RippleButton` 컴포넌트의 코드입니다.

```jsx
const RippleButton = ({ children, onClick }) => {
  const [coords, setCoords] = React.useState({ x: -1, y: -1 });
  const [isRippling, setIsRippling] = React.useState(false);

  React.useEffect(() => {
    if (coords.x !== -1 && coords.y !== -1) {
      setIsRippling(true);
      setTimeout(() => setIsRippling(false), 300);
    } else setIsRippling(false);
  }, [coords]);

  React.useEffect(() => {
    if (!isRippling) setCoords({ x: -1, y: -1 });
  }, [isRippling]);

  return (
    <button
      className="ripple-button"
      onClick={(e) => {
        const rect = e.target.getBoundingClientRect();
        setCoords({ x: e.clientX - rect.left, y: e.clientY - rect.top });
        onClick && onClick(e);
      }}
    >
      {isRippling && (
        <span
          className="ripple"
          style={{
            left: coords.x,
            top: coords.y
          }}
        />
      )}
      <span className="content">{children}</span>
    </button>
  );
};
```

이 컴포넌트는 다음과 같이 사용할 수 있습니다.

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <RippleButton onClick={(e) => console.log(e)}>Click me</RippleButton>
);
```

다음은 `RippleButton` 컴포넌트의 CSS 입니다.

```css
.ripple-button {
  border-radius: 4px;
  border: none;
  margin: 8px;
  padding: 14px 24px;
  background: #1976d2;
  color: #fff;
  overflow: hidden;
  position: relative;
  cursor: pointer;
}

.ripple-button > .ripple {
  width: 20px;
  height: 20px;
  position: absolute;
  background: #63a4ff;
  display: block;
  content: "";
  border-radius: 9999px;
  opacity: 1;
  animation: 0.9s ease 1 forwards ripple-effect;
}

@keyframes ripple-effect {
  0% {
    transform: scale(1);
    opacity: 1;
  }
  50% {
    transform: scale(10);
    opacity: 0.375;
  }
  100% {
    transform: scale(35);
    opacity: 0;
  }
}

.ripple-button > .content {
  position: relative;
  z-index: 2;
}
```

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
