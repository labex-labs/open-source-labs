# 컨테이너에 이미지 맞추기

`index.html` 및 `style.css`는 이미 VM 에 제공되어 있습니다.

이미지의 종횡비를 유지하면서 컨테이너 내부에 이미지를 맞추려면 `object-fit: contain`을 사용할 수 있습니다. 종횡비를 유지하면서 컨테이너를 이미지로 채우려면 `object-fit: cover`를 사용하십시오. 이미지를 컨테이너 중앙에 배치하려면 `object-position: center`를 사용할 수 있습니다.

다음은 이러한 속성을 사용하는 예입니다.

```html
<img class="image image-contain" src="https://picsum.photos/600/200" />
<img class="image image-cover" src="https://picsum.photos/600/200" />
```

해당 CSS 는 다음과 같습니다.

```css
.image {
  background: #34495e;
  border: 1px solid #34495e;
  width: 200px;
  height: 200px;
}

.image-contain {
  object-fit: contain;
  object-position: center;
}

.image-cover {
  object-fit: cover;
  object-position: right top;
}
```

오른쪽 하단 모서리에서 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
