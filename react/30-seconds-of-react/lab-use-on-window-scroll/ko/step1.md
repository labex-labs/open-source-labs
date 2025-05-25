# React useOnWindowScroll 훅

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

이 함수는 윈도우가 스크롤될 때마다 콜백 함수를 실행합니다. 이를 구현하려면 다음 단계를 따르세요:

1. `useRef()` 훅을 사용하여 참조 변수 `listener`를 생성합니다.
2. `useEffect()` 훅과 `EventTarget.addEventListener()`를 사용하여 `Window` 객체의 `'scroll'` 이벤트를 리스닝하고, 리스너 참조를 `listener.current`에 할당합니다.
3. 컴포넌트가 언마운트될 때 `EventTarget.removeEventListener()`를 사용하여 기존 리스너를 제거합니다.

다음은 코드입니다:

```jsx
const useOnWindowScroll = (callback) => {
  const listener = React.useRef(null);

  React.useEffect(() => {
    if (listener.current) {
      window.removeEventListener("scroll", listener.current);
    }
    listener.current = () => {
      callback(window.pageYOffset);
    };
    window.addEventListener("scroll", listener.current);
    return () => {
      window.removeEventListener("scroll", listener.current);
    };
  }, [callback]);
};
```

이 함수를 테스트하려면 다음과 같이 컴포넌트에서 사용할 수 있습니다:

```jsx
const App = () => {
  useOnWindowScroll((scrollY) => console.log(`scroll Y: ${scrollY}`));
  return <p style={{ height: "300vh" }}>Scroll and check the console</p>;
};

ReactDOM.render(<App />, document.getElementById("root"));
```

이렇게 하면 윈도우가 스크롤될 때마다 윈도우의 수직 스크롤 위치가 콘솔에 기록됩니다.

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
