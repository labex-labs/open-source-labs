# 비밀번호 표시/숨기기 토글

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

다음 코드는 표시 버튼이 있는 비밀번호 입력 필드를 렌더링합니다. `useState()` 훅을 사용하여 `shown` 상태 변수를 생성하고 초기 값을 `false`로 설정합니다. "표시/숨기기" 버튼을 클릭하면 `setShown` 함수가 호출되어 입력의 `type`을 `'text'`와 `'password'` 사이에서 토글합니다.

```jsx
const PasswordRevealer = ({ value }) => {
  const [shown, setShown] = React.useState(false);
  return (
    <>
      <input type={shown ? "text" : "password"} value={value} />
      <button onClick={() => setShown(!shown)}>Show/Hide</button>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <PasswordRevealer />
);
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
