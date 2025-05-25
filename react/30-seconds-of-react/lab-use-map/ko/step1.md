# React useMap 훅

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

- `useMap()` 훅은 React 훅을 사용하여 상태를 관리하는 `Map` 객체와 이를 조작하기 위한 일련의 함수들을 생성합니다.
- `useState()` 훅은 `initialValue`로 `Map` 상태를 초기화합니다.
- `useMemo()` 훅은 상태 설정자를 사용하여 `map` 상태 변수를 조작하는 일련의 비변이적 (non-mutating) 액션을 생성하여 매번 새로운 `Map`을 생성합니다.
- `useMap()` 훅은 `map` 상태 변수와 생성된 `actions`를 포함하는 배열을 반환합니다.
- `MyApp` 컴포넌트는 `useMap()` 훅을 사용하여 상태를 관리하는 `Map` 객체를 초기화하고, `Map`에서 항목을 추가, 재설정 및 제거하는 버튼을 제공합니다.
- `JSON.stringify()` 함수는 `Map` 객체를 읽기 쉬운 JSON 문자열로 형식화합니다.

```jsx
const useMap = (initialValue) => {
  const [map, setMap] = React.useState(new Map(initialValue));

  const actions = React.useMemo(
    () => ({
      set: (key, value) =>
        setMap((prevMap) => {
          const nextMap = new Map(prevMap);
          nextMap.set(key, value);
          return nextMap;
        }),
      remove: (key) =>
        setMap((prevMap) => {
          const nextMap = new Map(prevMap);
          nextMap.delete(key);
          return nextMap;
        }),
      clear: () => setMap(new Map())
    }),
    [setMap]
  );

  return [map, actions];
};

const MyApp = () => {
  const [map, { set, remove, clear }] = useMap([["apples", 10]]);

  const handleAdd = () => set(Date.now(), new Date().toJSON());
  const handleReset = () => clear();
  const handleRemove = () => remove("apples");

  return (
    <div>
      <button onClick={handleAdd}>Add</button>
      <button onClick={handleReset}>Reset</button>
      <button onClick={handleRemove} disabled={!map.has("apples")}>
        Remove apples
      </button>
      <pre>{JSON.stringify(Object.fromEntries(map), null, 2)}</pre>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
