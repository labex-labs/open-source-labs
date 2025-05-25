# React useBodyScrollLock 훅

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

이 코드 조각을 사용하면 모달이 열려 있을 때 body 스크롤을 잠글 수 있습니다. 작동 방식은 다음과 같습니다.

먼저, `useBodyScrollLock` 함수가 정의됩니다. 이 함수는 `useLayoutEffect` 훅을 사용하여 `body` 요소의 스크롤을 잠급니다. 이 훅은 컴포넌트가 마운트될 때 한 번만 실행되며, `body` 요소의 `overflow` 값을 `'hidden'`으로 설정합니다. 컴포넌트가 언마운트되면 원래의 `overflow` 값이 복원됩니다.

```jsx
const useBodyScrollLock = () => {
  React.useLayoutEffect(() => {
    const originalStyle = window.getComputedStyle(document.body).overflow;
    document.body.style.overflow = "hidden";
    return () => (document.body.style.overflow = originalStyle);
  }, []);
};
```

그런 다음, `Modal` 컴포넌트가 정의되며, 이 컴포넌트는 `useBodyScrollLock` 함수를 활용합니다. 이 컴포넌트는 화면 중앙에 위치한 상자에 메시지를 표시합니다. 상자를 클릭하면 모달이 닫히고 body 스크롤이 잠금 해제됩니다.

```jsx
const Modal = ({ onClose }) => {
  useBodyScrollLock();

  return (
    <div
      style={{
        zIndex: 100,
        background: "rgba(0,0,0,0.25)",
        display: "flex",
        justifyContent: "center",
        alignItems: "center"
      }}
      onClick={onClose}
    >
      <p style={{ padding: 8, borderRadius: 8, background: "#fff" }}>
        Scroll locked! <br /> Click me to unlock
      </p>
    </div>
  );
};
```

마지막으로, `MyApp` 컴포넌트가 정의됩니다. 이 컴포넌트는 클릭 시 `Modal` 컴포넌트를 여는 버튼을 렌더링합니다.

```jsx
const MyApp = () => {
  const [modalOpen, setModalOpen] = React.useState(false);

  return (
    <div
      style={{
        height: "400vh",
        textAlign: "center",
        paddingTop: 100,
        background: "linear-gradient(to bottom, #1fa2ff, #12d8fa, #a6ffcb)"
      }}
    >
      <button onClick={() => setModalOpen(true)}>Open modal</button>
      {modalOpen && <Modal onClose={() => setModalOpen(false)} />}
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
