# React useToggler 훅

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

두 상태 간에 토글될 수 있는 부울 (boolean) 상태 변수를 생성하려면 다음 단계를 따르세요.

1. `useState()` 훅을 사용하여 `value` 상태 변수와 해당 setter 를 생성합니다.
2. `useCallback()` 훅을 사용하여 `value` 상태 변수의 값을 토글하고 메모이제이션 (memoization) 하는 함수를 생성합니다.
3. `value` 상태 변수와 메모이제이션된 토글러 함수를 반환합니다.

다음은 구현 예시입니다.

```jsx
const useToggler = (initialState) => {
  const [value, setValue] = React.useState(initialState);

  const toggleValue = React.useCallback(() => setValue((prev) => !prev), []);

  return [value, toggleValue];
};
```

그런 다음 다음과 같이 컴포넌트에서 이 훅을 사용할 수 있습니다.

```jsx
const Switch = () => {
  const [val, toggleVal] = useToggler(false);
  return <button onClick={toggleVal}>{val ? "ON" : "OFF"}</button>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<Switch />);
```

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하세요. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
