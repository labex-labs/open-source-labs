# React useClickInside 훅

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

컴포넌트 내부의 클릭 이벤트를 처리하려면 `ref`와 `callback`을 인수로 받는 `useClickInside`라는 사용자 정의 훅을 만들 수 있습니다. `useEffect()` 훅을 사용하여 `click` 이벤트를 추가하고 정리하고, `useRef()` 훅을 사용하여 클릭 컴포넌트에 대한 `ref`를 생성하고 이를 `useClickInside` 훅에 전달합니다. 코드는 다음과 같습니다.

```jsx
const useClickInside = (ref, callback) => {
  const handleClick = (e) => {
    if (ref.current && ref.current.contains(e.target)) {
      callback();
    }
  };

  React.useEffect(() => {
    document.addEventListener("click", handleClick);
    return () => {
      document.removeEventListener("click", handleClick);
    };
  }, [ref, callback]);
};
```

이 훅은 다음과 같이 컴포넌트에서 사용할 수 있습니다.

```jsx
const ClickBox = ({ onClickInside }) => {
  const clickRef = React.useRef();
  useClickInside(clickRef, onClickInside);

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
      <p>Click inside this element</p>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <ClickBox onClickInside={() => alert("click inside")} />
);
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
