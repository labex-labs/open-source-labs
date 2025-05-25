# React useFetch 훅

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

다음은 코드입니다.

```jsx
const useFetch = (url, options) => {
  const [response, setResponse] = React.useState(null);
  const [error, setError] = React.useState(null);
  const [abort, setAbort] = React.useState(() => {});

  React.useEffect(() => {
    const abortController = new AbortController();
    const signal = abortController.signal;

    const fetchData = async () => {
      try {
        const res = await fetch(url, { ...options, signal });
        const json = await res.json();
        setResponse(json);
      } catch (error) {
        setError(error);
      }
    };
    fetchData();

    return () => {
      abort();
    };
  }, []);

  return { response, error, abort };
};

const ImageFetch = (props) => {
  const res = useFetch("https://dog.ceo/api/breeds/image/random", {});

  if (!res.response) {
    return <div>Loading...</div>;
  }

  const imageUrl = res.response.message;

  return (
    <div>
      <img src={imageUrl} alt="avatar" width={400} height="auto" />
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<ImageFetch />);
```

설명:

- 코드의 목적은 React 훅을 사용하여 `fetch()` 호출을 선언적으로 구현하는 것입니다.
- `useFetch` 훅은 `url`과 `options` 객체, 두 개의 매개변수를 받습니다.
- 훅은 `useState()` 훅을 사용하여 `response`, `error`, `abort` 세 개의 상태 변수를 초기화합니다.
- `useEffect()` 훅은 비동기적으로 `fetch()`를 호출하고 그에 따라 상태 변수를 업데이트하는 데 사용됩니다.
- `AbortController`는 요청을 중단하는 데 사용되며, 컴포넌트가 언마운트될 때 요청을 취소하는 데 사용됩니다.
- 훅은 `response`, `error`, `abort` 상태 변수를 포함하는 객체를 반환합니다.
- `ImageFetch` 컴포넌트는 `useFetch` 훅을 사용하여 무작위 강아지 이미지를 가져와 `<img>` 요소에 표시합니다.

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
