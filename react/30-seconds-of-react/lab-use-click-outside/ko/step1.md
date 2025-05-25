# React useClickOutside 훅

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

이 코드는 래핑된 컴포넌트 외부를 클릭하는 이벤트를 처리합니다. `click` 이벤트를 처리하기 위해 `ref`와 `callback`을 사용하는 커스텀 훅을 생성하여 작동합니다. `useEffect()` 훅은 `click` 이벤트를 추가하고 정리하는 데 사용되며, `useRef()` 훅은 클릭 컴포넌트에 대한 `ref`를 생성하고 이를 `useClickOutside` 훅에 전달하는 데 사용됩니다.

```jsx
const useClickOutside = (ref, callback) => {
  const handleClick = (e) => {
    if (ref.current && !ref.current.contains(e.target)) {
      callback();
    }
  };
  React.useEffect(() => {
    document.addEventListener("click", handleClick);
    return () => {
      document.removeEventListener("click", handleClick);
    };
  });
};

const ClickBox = ({ onClickOutside }) => {
  const clickRef = React.useRef();
  useClickOutside(clickRef, onClickOutside);
  return (
    <div
      className="click-box"
      ref={clickRef}
      style={{
        border: "2px dashed orangered",
        height: 200,
        width: 400,
        display: "flex",
        justifyContent: "center",
        alignItems: "center"
      }}
    >
      <p>Click out of this element</p>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <ClickBox onClickOutside={() => alert("click outside")} />
);
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
