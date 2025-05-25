# React useCopyToClipboard 훅

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js`와 `style.css`에만 코드를 추가하면 됩니다.

주어진 텍스트를 클립보드에 복사하려면 `/js/s/copy-to-clipboard/`에 제공된 `copyToClipboard` 스니펫과 `useState()` 훅을 사용하여 `copied` 변수를 초기화합니다. `copyToClipboard` 메서드에 대한 콜백을 생성하려면 `useCallback()` 훅을 사용합니다. `text`가 변경될 때 `copied` 상태 변수를 재설정하려면 `useEffect()` 훅을 사용합니다. 마지막으로, `copied` 상태 변수와 `copy` 콜백을 반환합니다.

다음 코드는 이러한 훅과 메서드를 사용하여 `TextCopy` 컴포넌트를 생성하는 예시를 보여줍니다. 사용자가 "Click to copy" 버튼을 클릭하면 `copy` 함수가 호출되고 `copied` 변수가 `true`로 설정됩니다. 복사가 성공하면 "Copied!"가 표시됩니다.

```jsx
const useCopyToClipboard = (text) => {
  const copyToClipboard = (str) => {
    const el = document.createElement("textarea");
    el.value = str;
    el.setAttribute("readonly", "");
    el.style.position = "absolute";
    el.style.left = "-9999px";
    document.body.appendChild(el);
    const selected =
      document.getSelection().rangeCount > 0
        ? document.getSelection().getRangeAt(0)
        : false;
    el.select();
    const success = document.execCommand("copy");
    document.body.removeChild(el);
    if (selected) {
      document.getSelection().removeAllRanges();
      document.getSelection().addRange(selected);
    }
    return success;
  };

  const [copied, setCopied] = React.useState(false);

  const copy = React.useCallback(() => {
    if (!copied) setCopied(copyToClipboard(text));
  }, [text]);

  React.useEffect(() => () => setCopied(false), [text]);

  return [copied, copy];
};

const TextCopy = (props) => {
  const [copied, copy] = useCopyToClipboard("Lorem ipsum");

  return (
    <div>
      <button onClick={copy}>Click to copy</button>
      <span>{copied && "Copied!"}</span>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<TextCopy />);
```

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
