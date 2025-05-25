# 파일 드래그 앤 드롭 영역

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

이 컴포넌트는 단일 파일에 대한 드래그 앤 드롭 기능을 제공합니다. 이 컴포넌트를 구현하려면 다음 단계를 따르세요.

1. `dropRef`라는 참조를 생성하고 컴포넌트의 래퍼에 바인딩합니다.
2. `useState()` 훅을 사용하여 `drag` 및 `filename` 변수를 생성합니다. 각각 `false`와 `''`로 초기화합니다.
3. `dragCounter` 및 `drag` 변수는 파일이 드래그되고 있는지 확인하는 데 사용되며, `filename`은 드롭된 파일의 이름을 저장하는 데 사용됩니다.
4. 드래그 앤 드롭 기능을 처리하기 위해 `handleDrag`, `handleDragIn`, `handleDragOut` 및 `handleDrop` 메서드를 생성합니다. `handleDrag`는 브라우저가 드래그된 파일을 여는 것을 방지하고, `handleDragIn` 및 `handleDragOut`은 드래그된 파일이 컴포넌트에 진입하고 나가는 것을 처리하며, `handleDrop`은 파일이 드롭되는 것을 처리하고 이를 `onDrop`에 전달합니다.
5. 이전에 생성된 메서드를 사용하여 각 드래그 앤 드롭 이벤트를 처리하기 위해 `useEffect()` 훅을 사용합니다.

다음은 컴포넌트의 CSS 입니다.

```css
.filedrop {
  min-height: 120px;
  border: 3px solid #d3d3d3;
  text-align: center;
  font-size: 24px;
  padding: 32px;
  border-radius: 4px;
}

.filedrop.drag {
  border: 3px dashed #1e90ff;
}

.filedrop.ready {
  border: 3px solid #32cd32;
}
```

다음은 컴포넌트의 JSX 입니다.

```jsx
const FileDrop = ({ onDrop }) => {
  const [drag, setDrag] = React.useState(false);
  const [filename, setFilename] = React.useState("");
  const dropRef = React.useRef(null);
  let dragCounter = 0;

  const handleDrag = (e) => {
    e.preventDefault();
    e.stopPropagation();
  };

  const handleDragIn = (e) => {
    e.preventDefault();
    e.stopPropagation();
    dragCounter++;
    if (e.dataTransfer.items && e.dataTransfer.items.length > 0) setDrag(true);
  };

  const handleDragOut = (e) => {
    e.preventDefault();
    e.stopPropagation();
    dragCounter--;
    if (dragCounter === 0) setDrag(false);
  };

  const handleDrop = (e) => {
    e.preventDefault();
    e.stopPropagation();
    setDrag(false);
    if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {
      onDrop(e.dataTransfer.files[0]);
      setFilename(e.dataTransfer.files[0].name);
      e.dataTransfer.clearData();
      dragCounter = 0;
    }
  };

  React.useEffect(() => {
    const div = dropRef.current;
    div.addEventListener("dragenter", handleDragIn);
    div.addEventListener("dragleave", handleDragOut);
    div.addEventListener("dragover", handleDrag);
    div.addEventListener("drop", handleDrop);
    return () => {
      div.removeEventListener("dragenter", handleDragIn);
      div.removeEventListener("dragleave", handleDragOut);
      div.removeEventListener("dragover", handleDrag);
      div.removeEventListener("drop", handleDrop);
    };
  }, []);

  return (
    <div
      ref={dropRef}
      className={
        drag ? "filedrop drag" : filename ? "filedrop ready" : "filedrop"
      }
    >
      {filename && !drag ? <div>{filename}</div> : <div>Drop a file here!</div>}
    </div>
  );
};
```

컴포넌트를 사용하려면 `ReactDOM.createRoot(document.getElementById('root')).render(<FileDrop onDrop={console.log} />);`를 호출하세요.

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하세요. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
