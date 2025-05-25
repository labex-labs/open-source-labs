# React useHash 훅

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

이 코드는 브라우저의 위치 해시 값을 추적하고 업데이트합니다. 사용하려면 다음 단계를 따르세요.

1. `useState()` 훅을 사용하여 `Location` 객체의 `hash` 속성을 지연 로딩 (lazily) 으로 가져옵니다.
2. `useCallback()` 훅을 사용하여 `'hashchange'` 이벤트가 발생할 때 `hash` 상태를 업데이트하는 핸들러를 생성합니다.
3. `useEffect()` 훅을 사용하여 마운트 시 `'hashchange'` 이벤트에 대한 리스너를 추가하고 언마운트 시 정리합니다.
4. `useCallback()` 훅을 사용하여 주어진 값으로 `Location` 객체의 `hash` 속성을 업데이트하는 함수를 생성합니다.
5. 컴포넌트에서 `useHash()`를 호출하여 현재 `hash` 값과 이를 변경하는 `updateHash()` 함수를 가져옵니다.
6. `updateHash()` 함수를 사용하여 `hash` 값을 변경합니다.
7. 컴포넌트에서 현재 `hash` 값을 렌더링합니다.
8. 사용자가 `hash` 값을 변경할 수 있는 입력 필드를 생성합니다.

다음은 코드입니다.

```jsx
const useHash = () => {
  const [hash, setHash] = React.useState(() => window.location.hash);

  const hashChangeHandler = React.useCallback(() => {
    setHash(window.location.hash);
  }, []);

  React.useEffect(() => {
    window.addEventListener("hashchange", hashChangeHandler);
    return () => {
      window.removeEventListener("hashchange", hashChangeHandler);
    };
  }, []);

  const updateHash = React.useCallback(
    (newHash) => {
      if (newHash !== hash) window.location.hash = newHash;
    },
    [hash]
  );

  return [hash, updateHash];
};

const MyApp = () => {
  const [hash, setHash] = useHash();

  React.useEffect(() => {
    setHash("#list");
  }, []);

  return (
    <>
      <p>Current hash value: {hash}</p>
      <p>Edit hash: </p>
      <input value={hash} onChange={(e) => setHash(e.target.value)} />
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
