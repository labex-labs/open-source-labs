# React useMutationObserver 훅

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js`와 `style.css`에만 코드를 추가하면 됩니다.

DOM 트리에 발생한 변경 사항을 감지하려면 `useMutationObserver` 훅을 사용할 수 있습니다. 작동 방식은 다음과 같습니다.

1. 훅은 `ref`, `callback`, 그리고 `options`의 세 가지 매개변수를 받습니다.
2. 훅 내부에서는 `callback`과 `options`의 값에 의존하는 `useEffect()` 훅이 사용됩니다.
3. 주어진 `ref`가 초기화되면 새로운 `MutationObserver`가 생성되고 `callback`이 전달됩니다.
4. `MutationObserver.observe()`는 주어진 `ref`에서 변경 사항을 감지하기 위해 주어진 `options`와 함께 호출됩니다.
5. 컴포넌트가 언마운트될 때 `MutationObserver.disconnect()`를 사용하여 옵저버를 `ref`에서 제거합니다.

다음은 코드입니다.

```jsx
const useMutationObserver = (
  ref,
  callback,
  options = {
    attributes: true,
    characterData: true,
    childList: true,
    subtree: true
  }
) => {
  React.useEffect(() => {
    if (!ref.current) return;

    const observer = new MutationObserver(callback);
    observer.observe(ref.current, options);

    return () => observer.disconnect();
  }, [callback, options, ref]);
};
```

`App` 컴포넌트에서 `useMutationObserver` 훅은 `mutationRef` 요소에 발생한 변경 사항을 감지하는 데 사용됩니다. `incrementMutationCount` 함수는 `callback`으로 전달됩니다.

```jsx
const App = () => {
  const mutationRef = React.useRef();
  const [mutationCount, setMutationCount] = React.useState(0);

  const incrementMutationCount = React.useCallback(() => {
    setMutationCount((count) => count + 1);
  }, []);

  useMutationObserver(mutationRef, incrementMutationCount);

  const [content, setContent] = React.useState("Hello world");

  return (
    <>
      <label htmlFor="content-input">Edit this to update the text:</label>
      <textarea
        id="content-input"
        style={{ width: "100%" }}
        value={content}
        onChange={(e) => setContent(e.target.value)}
      />
      <div style={{ width: "100%" }} ref={mutationRef}>
        <div
          style={{
            resize: "both",
            overflow: "auto",
            maxWidth: "100%",
            border: "1px solid black"
          }}
        >
          <h2>Resize or change the content:</h2>
          <p>{content}</p>
        </div>
      </div>
      <div>
        <h3>Mutation count {mutationCount}</h3>
      </div>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
