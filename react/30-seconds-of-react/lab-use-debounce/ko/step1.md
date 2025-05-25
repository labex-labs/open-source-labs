# React useDebounce Hook

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

주어진 값을 디바운싱하려면 `value`와 `delay`를 사용하는 사용자 지정 훅을 만들 수 있습니다. `useState()` 훅을 사용하여 디바운싱된 값을 저장하고, `useEffect()` 훅을 사용하여 `value`가 업데이트될 때마다 디바운싱된 값을 업데이트합니다. 이전 상태 변수의 setter 를 `delay` ms 만큼 지연시키려면 `setTimeout()`을 사용합니다. 컴포넌트를 언마운트할 때 정리하려면 `clearTimeout()`을 사용합니다. 이는 사용자 입력을 처리할 때 특히 유용합니다.

다음은 `useDebounce()` 훅의 예시 구현입니다.

```jsx
const useDebounce = (value, delay) => {
  const [debouncedValue, setDebouncedValue] = React.useState(value);

  React.useEffect(() => {
    const handler = setTimeout(() => {
      setDebouncedValue(value);
    }, delay);

    return () => {
      clearTimeout(handler);
    };
  }, [value, delay]);

  return debouncedValue;
};
```

다음과 같이 컴포넌트에서 `useDebounce()` 훅을 사용할 수 있습니다.

```jsx
const Counter = () => {
  const [value, setValue] = React.useState(0);
  const lastValue = useDebounce(value, 500);

  return (
    <div>
      <p>
        Current: {value} - Debounced: {lastValue}
      </p>
      <button onClick={() => setValue(value + 1)}>Increment</button>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<Counter />);
```

오른쪽 하단 모서리에서 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
