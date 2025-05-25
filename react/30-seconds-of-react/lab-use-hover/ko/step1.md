# React useHover 훅

> `index.html`과 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js`와 `style.css`에만 코드를 추가하면 됩니다.

이 코드는 래핑된 컴포넌트 위에 마우스를 올리는 (hovering) 이벤트를 처리하는 사용자 정의 훅을 생성합니다.

훅을 사용하려면:

- `useState()`를 사용하여 호버링 상태를 저장하는 변수를 생성합니다.
- `useCallback()`을 사용하여 상태를 업데이트하는 두 개의 핸들러 함수를 메모이제이션합니다.
- `useCallback()`을 사용하여 콜백 ref 를 생성하고 `'mouseover'` 및 `'mouseout'` 이벤트에 대한 리스너를 생성하거나 업데이트합니다.
- `useRef()`를 사용하여 `callbackRef`에 전달된 마지막 노드를 추적하여 리스너를 제거할 수 있도록 합니다.

```jsx
const useHover = () => {
  const [isHovering, setIsHovering] = React.useState(false);
  const handleMouseOver = React.useCallback(() => setIsHovering(true), []);
  const handleMouseOut = React.useCallback(() => setIsHovering(false), []);
  const nodeRef = React.useRef();
  const callbackRef = React.useCallback(
    (node) => {
      if (nodeRef.current) {
        nodeRef.current.removeEventListener("mouseover", handleMouseOver);
        nodeRef.current.removeEventListener("mouseout", handleMouseOut);
      }
      nodeRef.current = node;
      if (nodeRef.current) {
        nodeRef.current.addEventListener("mouseover", handleMouseOver);
        nodeRef.current.addEventListener("mouseout", handleMouseOut);
      }
    },
    [handleMouseOver, handleMouseOut]
  );

  return [callbackRef, isHovering];
};
```

다음은 훅의 사용 예시입니다:

```jsx
const MyApp = () => {
  const [hoverRef, isHovering] = useHover();
  return <div ref={hoverRef}>{isHovering ? "Hovering" : "Not hovering"}</div>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
