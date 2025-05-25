# React useSet 훅

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

이 함수는 상태를 가진 `Set` 객체와 상태를 조작할 수 있는 함수 집합을 생성합니다.

이 함수를 사용하려면:

- `useState()`와 `Set` 생성자를 호출하여 `initialValue`에서 새로운 `Set`을 생성합니다.
- `useMemo()`를 사용하여 `set` 상태 변수를 조작할 수 있는 비변이 함수 집합을 생성합니다. 매번 새로운 `Set`을 생성하기 위해 상태 설정자를 사용합니다.
- `set` 상태 변수와 생성된 `actions`를 모두 반환합니다.

다음은 이 함수의 예시 구현입니다:

```jsx
const useSet = (initialValue) => {
  const [set, setSet] = React.useState(new Set(initialValue));

  const actions = React.useMemo(
    () => ({
      add: (item) => setSet((prevSet) => new Set([...prevSet, item])),
      remove: (item) =>
        setSet((prevSet) => new Set([...prevSet].filter((i) => i !== item))),
      clear: () => setSet(new Set())
    }),
    [setSet]
  );

  return [set, actions];
};
```

다음은 이 함수의 예시 사용법입니다:

```jsx
const MyApp = () => {
  const [set, { add, remove, clear }] = useSet(new Set(["apples"]));

  return (
    <div>
      <button onClick={() => add(String(Date.now()))}>Add</button>
      <button onClick={() => clear()}>Reset</button>
      <button onClick={() => remove("apples")} disabled={!set.has("apples")}>
        Remove apples
      </button>
      <pre>{JSON.stringify([...set], null, 2)}</pre>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
