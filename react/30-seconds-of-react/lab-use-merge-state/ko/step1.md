# React useMergeState 훅

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

제공된 새로운 상태를 병합하여 상태 값과 이를 업데이트하는 함수를 생성하려면, `useState()` 훅을 사용하여 상태 변수를 생성하고 `initialState`로 초기화합니다. 제공된 새로운 상태를 기존 상태와 병합하여 상태 변수를 업데이트하는 함수를 만듭니다. 새로운 상태가 함수인 경우, 이전 상태를 인수로 사용하여 해당 함수를 호출하고 결과를 사용합니다. 인수가 제공되지 않으면 상태 변수는 빈 객체 (`{}`) 로 초기화됩니다. 다음 코드는 `useMergeState` 사용자 지정 훅을 사용하여 이를 구현하는 방법을 보여줍니다.

```jsx
const useMergeState = (initialState = {}) => {
  const [value, setValue] = React.useState(initialState);

  const mergeState = (newState) => {
    if (typeof newState === "function") {
      newState = newState(value);
    }
    setValue({ ...value, ...newState });
  };

  return [value, mergeState];
};
```

다음은 `MyApp`이라는 컴포넌트에서 `useMergeState` 훅을 사용하는 예시입니다.

```jsx
const MyApp = () => {
  const [data, setData] = useMergeState({ name: "John", age: 20 });

  return (
    <>
      <input
        value={data.name}
        onChange={(e) => setData({ name: e.target.value })}
      />
      <button onClick={() => setData(({ age }) => ({ age: age - 1 }))}>
        -
      </button>
      {data.age}
      <button onClick={() => setData(({ age }) => ({ age: age + 1 }))}>
        +
      </button>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
