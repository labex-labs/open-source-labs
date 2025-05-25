# React useDelayedState 훅

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

조건이 충족될 때까지 상태 값의 생성을 지연시키려면 다음 단계를 따르세요.

1. `useState()` 훅을 사용하여 실제 `state`와 부울 값인 `loaded`를 포함하는 상태 값을 생성합니다.
2. `condition` 또는 `loaded`가 변경되면 `useEffect()` 훅을 사용하여 상태 값을 업데이트합니다.
3. `loaded`가 참 (truthy) 일 경우에만 `state` 값을 업데이트하는 함수 `updateState`를 생성합니다.

```jsx
const useDelayedState = (initialState, condition) => {
  const [{ state, loaded }, setState] = React.useState({
    state: null,
    loaded: false
  });

  React.useEffect(() => {
    if (!loaded && condition) setState({ state: initialState, loaded: true });
  }, [condition, loaded]);

  const updateState = (newState) => {
    if (!loaded) return;
    setState({ state: newState, loaded });
  };

  return [state, updateState];
};
```

`useDelayedState` 훅을 사용하는 방법의 예는 다음과 같습니다.

```jsx
const App = () => {
  const [branches, setBranches] = React.useState([]);
  const [selectedBranch, setSelectedBranch] = useDelayedState(
    branches[0],
    branches.length
  );

  React.useEffect(() => {
    const handle = setTimeout(() => {
      setBranches(["master", "staging", "test", "dev"]);
    }, 2000);
    return () => {
      handle && clearTimeout(handle);
    };
  }, []);

  return (
    <div>
      <p>Selected branch: {selectedBranch}</p>
      <select onChange={(e) => setSelectedBranch(e.target.value)}>
        {branches.map((branch) => (
          <option key={branch} value={branch}>
            {branch}
          </option>
        ))}
      </select>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하세요. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
