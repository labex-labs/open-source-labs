# React usePrevious Hook

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

이전 상태 또는 props 를 저장하려면 사용자 정의 훅을 만들 수 있습니다. 다음은 단계별 안내입니다.

1. `value` 인수를 받는 사용자 정의 훅을 정의합니다.
2. `useRef()` 훅을 사용하여 `value`에 대한 `ref`를 생성합니다.
3. `useEffect()` 훅을 사용하여 최신 `value`를 기억합니다.
4. `ref.current` 값을 반환합니다.

```jsx
const usePrevious = (value) => {
  const ref = React.useRef();
  React.useEffect(() => {
    ref.current = value;
  });
  return ref.current;
};
```

`usePrevious` 훅을 사용하는 예시는 다음과 같습니다.

```jsx
const Counter = () => {
  const [value, setValue] = React.useState(0);
  const lastValue = usePrevious(value);

  return (
    <div>
      <p>
        Current: {value} - Previous: {lastValue}
      </p>
      <button onClick={() => setValue(value + 1)}>Increment</button>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<Counter />);
```

`Counter` 컴포넌트는 `value`의 현재 값과 이전 값을 표시합니다. `Increment` 버튼을 클릭하면 `value`가 업데이트되고 `usePrevious` 훅을 사용하여 이전 값이 저장됩니다.

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
