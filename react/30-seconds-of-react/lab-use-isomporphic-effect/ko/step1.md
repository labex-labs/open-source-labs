# React useIsomporphicEffect 훅

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

서버에서 `useEffect()`를, 클라이언트에서 `useLayoutEffect()`를 올바르게 사용하려면 `typeof`를 사용하여 `Window` 객체가 정의되었는지 확인할 수 있습니다. 정의되어 있다면 `useLayoutEffect()`를 반환하고, 그렇지 않으면 `useEffect()`를 반환합니다. 다음은 이를 구현하는 방법의 예시입니다.

```jsx
const useIsomorphicEffect =
  typeof window !== "undefined" ? React.useLayoutEffect : React.useEffect;
```

그런 다음, 코드에서 이 예제와 같이 `useIsomorphicEffect()`를 사용할 수 있습니다.

```jsx
const MyApp = () => {
  useIsomorphicEffect(() => {
    window.console.log("Hello");
  }, []);

  return null;
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

이렇게 하면 컴포넌트가 마운트될 때 콘솔에 'Hello'가 기록되며, 서버와 클라이언트 모두에서 올바르게 작동합니다.

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
