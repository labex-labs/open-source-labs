# React useKeyPress Hook

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

이 함수는 특정 키의 눌림 상태 변화를 감지합니다. 사용 방법은 다음과 같습니다.

- 대상 키를 인수로 사용하여 `useKeyPress()`를 호출합니다.
- `useKeyPress()`는 현재 키가 눌려져 있는지 여부를 나타내는 부울 값을 반환합니다.
- 이 함수는 `useState()` 훅을 사용하여 주어진 키의 눌림 상태를 저장하는 상태 변수를 생성합니다.
- 키 다운 또는 키 업 시 상태 변수를 업데이트하는 두 개의 핸들러 함수를 정의합니다.
- `useEffect()` 훅과 `EventTarget.addEventListener()`는 `'keydown'` 및 `'keyup'` 이벤트를 처리하는 데 사용됩니다.
- 마지막으로, 컴포넌트가 언마운트된 후 정리를 수행하기 위해 `EventTarget.removeEventListener()`가 사용됩니다.

```jsx
const useKeyPress = (targetKey) => {
  const [isKeyPressed, setKeyPressed] = React.useState(false);

  const handleKeyDown = ({ key }) => {
    if (key === targetKey) setKeyPressed(true);
  };

  const handleKeyUp = ({ key }) => {
    if (key === targetKey) setKeyPressed(false);
  };

  React.useEffect(() => {
    window.addEventListener("keydown", handleKeyDown);
    window.addEventListener("keyup", handleKeyUp);

    return () => {
      window.removeEventListener("keydown", handleKeyDown);
      window.removeEventListener("keyup", handleKeyUp);
    };
  }, [targetKey]);

  return isKeyPressed;
};
```

다음은 React 컴포넌트에서 `useKeyPress()`를 사용하는 예입니다.

```jsx
const MyApp = () => {
  const isWKeyPressed = useKeyPress("w");

  return <p>The "w" key is {!isWKeyPressed ? "not " : ""}pressed!</p>;
};

ReactDOM.render(<MyApp />, document.getElementById("root"));
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
