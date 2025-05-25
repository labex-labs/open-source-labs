# React useGetSet 훅

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

이 코드 조각은 상태 값을 생성하고 해당 값을 가져오고 설정하기 위한 함수 쌍을 반환하는 `useGetSet`이라는 사용자 정의 React 훅을 정의합니다. `Counter` 컴포넌트는 이 훅을 사용하여 버튼에 표시된 카운트의 지연된 증가를 구현합니다.

```jsx
const useGetSet = (initialState) => {
  const stateRef = React.useRef(initialState);
  const [, update] = React.useReducer(() => ({}), {});

  const getState = React.useCallback(() => stateRef.current, []);
  const setState = React.useCallback((newState) => {
    stateRef.current = newState;
    update();
  }, []);

  return [getState, setState];
};

const Counter = () => {
  const [getCount, setCount] = useGetSet(0);
  const onClick = React.useCallback(() => {
    setTimeout(() => {
      setCount(getCount() + 1);
    }, 1000);
  }, [getCount, setCount]);

  return <button onClick={onClick}>Count: {getCount()}</button>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<Counter />);
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
