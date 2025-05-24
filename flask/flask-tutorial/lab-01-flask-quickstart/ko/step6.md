# 동적 콘텐츠 추가

Flask 를 사용하면 템플릿에 동적 콘텐츠를 전달할 수 있습니다. 경로에 이름 매개변수를 전달하고 개인화된 인사를 표시하도록 경로를 수정해 보겠습니다.

1. 경로에서 이름 매개변수를 허용하도록 `app.py` 파일을 수정합니다:

   ```python
   @app.route("/<name>")
   def hello(name):
       return render_template("index.html", name=name)
   ```

2. `index.html` 파일을 열고 개인화된 인사를 표시하도록 `<h1>` 태그를 수정합니다:

   ```html
   <h1>Hello, {{ name }}!</h1>
   ```
