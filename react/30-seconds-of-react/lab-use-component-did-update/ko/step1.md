# React useComponentDidUpdate 훅

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

이 코드는 컴포넌트가 업데이트될 때마다 제공된 `callback` 함수를 실행하는 `useComponentDidUpdate`라는 사용자 정의 훅을 제공합니다. 훅이 따르는 단계는 다음과 같습니다.

1. `useRef()` 훅을 사용하여 `mounted` 변수를 생성합니다. 이 변수는 컴포넌트가 마운트되었는지 여부를 추적합니다.
2. `useEffect()` 훅을 사용하여 훅이 처음 실행될 때 `mounted`의 값을 `true`로 설정합니다.
3. 후속 훅 실행 시, 컴포넌트가 이미 마운트된 경우에만 제공된 `callback` 함수를 실행합니다.
4. 두 번째 인자 `condition`이 제공되면, 훅은 해당 종속성 중 하나라도 변경될 경우에만 실행됩니다.
5. 이 훅은 클래스 컴포넌트의 `componentDidUpdate()` 라이프사이클 메서드처럼 동작합니다.

다음은 코드입니다.

```jsx
const useComponentDidUpdate = (callback, condition) => {
  const isMounted = React.useRef(false);
  React.useEffect(() => {
    if (isMounted.current) {
      callback();
    } else {
      isMounted.current = true;
    }
  }, condition);
};

const App = () => {
  const [value, setValue] = React.useState(0);
  const [otherValue, setOtherValue] = React.useState(1);

  useComponentDidUpdate(() => {
    console.log(`Current value is ${value}.`);
  }, [value]);

  return (
    <>
      <p>
        Value: {value}, other value: {otherValue}
      </p>
      <button onClick={() => setValue(value + 1)}>Increment value</button>
      <button onClick={() => setOtherValue(otherValue + 1)}>
        Increment other value
      </button>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
