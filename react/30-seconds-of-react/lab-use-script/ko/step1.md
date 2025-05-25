# React useScript Hook

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

외부 스크립트를 동적으로 로드하려면 `useState()` 훅을 사용하여 스크립트의 로드 상태를 저장하는 상태 변수를 만듭니다. 다음으로, `useEffect()` 훅을 사용하여 `src`가 변경될 때마다 스크립트를 로드하고 언로드하는 모든 로직을 처리합니다. `src` 값이 없으면 `status`를 `'idle'`로 설정하고 반환합니다. `Document.querySelector()`를 사용하여 적절한 `src` 값을 가진 `<script>` 요소가 존재하는지 확인합니다. 관련 요소가 없으면 `Document.createElement()`를 사용하여 하나를 생성하고 적절한 속성을 지정합니다. `data-status` 속성을 사용하여 스크립트의 상태를 나타내고, 초기에는 `'loading'`으로 설정합니다. 관련 요소가 있는 경우 초기화를 건너뛰고 `data-status` 속성에서 `status`를 업데이트합니다. 이렇게 하면 중복된 요소가 생성되지 않습니다. `EventTarget.addEventListener()`를 사용하여 `'load'` 및 `'error'` 이벤트를 수신 대기하고, `data-status` 속성 및 `status` 상태 변수를 업데이트하여 처리합니다. 마지막으로, 컴포넌트가 언마운트될 때 `Document.removeEventListener()`를 사용하여 요소에 바인딩된 모든 리스너를 제거합니다.

다음은 `useScript` 훅의 예시 구현입니다.

```jsx
const useScript = (src) => {
  const [status, setStatus] = React.useState(src ? "loading" : "idle");

  React.useEffect(() => {
    if (!src) {
      setStatus("idle");
      return;
    }

    let script = document.querySelector(`script[src="${src}"]`);

    if (!script) {
      script = document.createElement("script");
      script.src = src;
      script.async = true;
      script.setAttribute("data-status", "loading");
      document.body.appendChild(script);

      const setDataStatus = (event) => {
        script.setAttribute(
          "data-status",
          event.type === "load" ? "ready" : "error"
        );
      };
      script.addEventListener("load", setDataStatus);
      script.addEventListener("error", setDataStatus);
    } else {
      setStatus(script.getAttribute("data-status"));
    }

    const setStateStatus = (event) => {
      setStatus(event.type === "load" ? "ready" : "error");
    };

    script.addEventListener("load", setStateStatus);
    script.addEventListener("error", setStateStatus);

    return () => {
      if (script) {
        script.removeEventListener("load", setStateStatus);
        script.removeEventListener("error", setStateStatus);
      }
    };
  }, [src]);

  return status;
};
```

다음은 `useScript` 훅의 사용 예시입니다.

```jsx
const script =
  "data:text/plain;charset=utf-8;base64,KGZ1bmN0aW9uKCl7IGNvbnNvbGUubG9nKCdIZWxsbycpIH0pKCk7";

const Child = () => {
  const status = useScript(script);
  return <p>Child status: {status}</p>;
};

const MyApp = () => {
  const status = useScript(script);
  return (
    <>
      <p>Parent status: {status}</p>
      <Child />
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
