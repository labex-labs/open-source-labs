# 닫을 수 있는 알림 (Closable Alert)

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

`type` prop 을 사용하여 알림 컴포넌트를 렌더링합니다.

`Alert` 컴포넌트는 다음 props 를 받습니다.

- `isDefaultShown`: 알림이 처음에 표시될지 여부를 결정하는 부울 값 (기본값은 `false`)
- `timeout`: 알림이 사라지기 전까지의 시간 (밀리초) 을 지정하는 숫자 (기본값은 `250`)
- `type`: 알림 유형을 결정하는 문자열 (예: "warning", "error", "info")
- `message`: 알림에 표시할 메시지를 포함하는 문자열

컴포넌트는 다음을 수행합니다.

- `useState()` 훅을 사용하여 `isShown` 및 `isLeaving` 상태 변수를 생성하고 둘 다 처음에 `false`로 설정합니다.
- 컴포넌트 언마운트 시 타이머 인스턴스를 지우기 위해 `timeoutId` 변수를 정의합니다.
- `useEffect()` 훅을 사용하여 `isShown`의 값을 `true`로 업데이트하고 컴포넌트가 언마운트될 때 `timeoutId`를 사용하여 인터벌을 지웁니다.
- `closeAlert` 함수를 정의하여 페이드 아웃 애니메이션을 표시하고 `setTimeout()`을 통해 `isShown`을 `false`로 설정하여 컴포넌트를 DOM 에서 제거된 것으로 설정합니다.
- `isShown`이 `true`인 경우 알림 컴포넌트를 렌더링합니다. 컴포넌트는 `type` prop 을 기반으로 적절한 스타일을 가지며 `isLeaving`이 `true`인 경우 페이드 아웃됩니다.

다음은 코드입니다.

```css
@keyframes leave {
  0% {
    opacity: 1;
  }
  100% {
    opacity: 0;
  }
}

.alert {
  padding: 0.75rem 0.5rem;
  margin-bottom: 0.5rem;
  text-align: left;
  padding-right: 40px;
  border-radius: 4px;
  font-size: 16px;
  position: relative;
}

.alert.warning {
  color: #856404;
  background-color: #fff3cd;
  border-color: #ffeeba;
}

.alert.error {
  color: #721c24;
  background-color: #f8d7da;
  border-color: #f5c6cb;
}

.alert.leaving {
  animation: leave 0.5s forwards;
}

.alert .close {
  position: absolute;
  top: 0;
  right: 0;
  padding: 0 0.75rem;
  color: #333;
  border: 0;
  height: 100%;
  cursor: pointer;
  background: none;
  font-weight: 600;
  font-size: 16px;
}

.alert .close::after {
  content: "x";
}
```

```jsx
const Alert = ({ isDefaultShown = false, timeout = 250, type, message }) => {
  const [isShown, setIsShown] = React.useState(isDefaultShown);
  const [isLeaving, setIsLeaving] = React.useState(false);

  let timeoutId = null;

  React.useEffect(() => {
    setIsShown(true);
    return () => {
      clearTimeout(timeoutId);
    };
  }, [isDefaultShown, timeout, timeoutId]);

  const closeAlert = () => {
    setIsLeaving(true);
    timeoutId = setTimeout(() => {
      setIsLeaving(false);
      setIsShown(false);
    }, timeout);
  };

  return (
    isShown && (
      <div
        className={`alert ${type} ${isLeaving ? "leaving" : ""}`}
        role="alert"
      >
        <button className="close" onClick={closeAlert} />
        {message}
      </div>
    )
  );
};
```

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Alert type="info" message="This is info" />
);
```

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
