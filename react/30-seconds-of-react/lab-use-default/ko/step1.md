# React useDefault 훅

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

다음은 코드입니다.

```jsx
const useDefault = (defaultState, initialState) => {
  const [value, setValue] = React.useState(initialState);
  const isEmpty = value === undefined || value === null;
  return [isEmpty ? defaultState : value, setValue];
};
```

```jsx
const UserCard = () => {
  const [user, setUser] = useDefault({ name: "Adam" }, { name: "John" });

  return (
    <>
      <div>User: {user.name}</div>
      <input onChange={(e) => setUser({ name: e.target.value })} />
      <button onClick={() => setUser(null)}>Clear</button>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<UserCard />);
```

기본 폴백 (fallback) 값을 가진 상태 값을 생성하려면 React 에서 `useState()` 훅을 사용합니다. 초기 값이 `null` 또는 `undefined`인지 확인합니다. 그렇다면 `defaultState`를 반환하고, 그렇지 않으면 실제 `value` 상태와 `setValue` 함수를 반환합니다. 위의 코드는 `useDefault`라는 사용자 정의 훅에서 이 기능을 구현하는 방법을 보여줍니다.

제공된 예제에서 `useDefault`는 기본값 `{ name: 'Adam' }`을 가진 `user` 상태를 생성하는 데 사용됩니다. 초기 상태는 `{ name: 'John' }`으로 설정됩니다. `UserCard` 컴포넌트에서 `user`는 이름을 업데이트할 수 있는 입력 필드와 함께 표시됩니다. 상태를 `null`로 재설정하는 지우기 버튼도 제공됩니다. 마지막으로, 컴포넌트는 `ReactDOM.createRoot()`를 사용하여 렌더링됩니다.

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
