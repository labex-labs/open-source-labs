# HTML 에서 CSS 파일 연결

이제 HTML 템플릿에서 CSS 파일을 연결해야 합니다. Flask 는 정적 파일을 제공하는 `static` 뷰를 자동으로 추가합니다. `base.html` 템플릿에서 `url_for` 함수를 사용하여 CSS 파일을 연결할 수 있습니다.

```html+jinja
<!-- base.html -->

{{ url_for('static', filename='style.css') }}
```
