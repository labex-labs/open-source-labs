# React useUpdate 훅

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

호출 시 컴포넌트를 강제로 다시 렌더링하려면 `useReducer()` 훅을 사용하여 업데이트될 때마다 새 객체를 생성하고 해당 dispatch 를 반환합니다. 다음은 `useUpdate()` 함수의 예시 구현입니다.

```jsx
const useUpdate = () => {
  const [, update] = React.useReducer(() => ({}));
  return update;
};
```

그런 다음 필요할 때 다시 렌더링을 트리거하기 위해 컴포넌트에서 `useUpdate()`를 사용할 수 있습니다.

```jsx
const MyApp = () => {
  const update = useUpdate();

  return (
    <>
      <div>Time: {Date.now()}</div>
      <button onClick={update}>Update</button>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
