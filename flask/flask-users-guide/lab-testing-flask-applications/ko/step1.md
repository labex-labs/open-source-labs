# 테스트 환경 설정

Flask 애플리케이션에 대한 테스트를 작성하기 전에 테스트 환경을 설정해야 합니다. 다음은 그 단계입니다.

1. 다음 명령을 실행하여 `pytest` 프레임워크를 설치합니다.

   ```bash
   pip install pytest
   ```

2. Flask 애플리케이션의 `tests` 폴더에 `conftest.py`라는 새 파일을 생성합니다.

3. `conftest.py` 파일에서 필요한 모듈을 가져옵니다.

   ```python
   import pytest
   from my_app import create_app
   ```

4. 앱 인스턴스를 생성하고 구성하는 `app`이라는 픽스처 (fixture) 를 정의합니다.

   ```python
   @pytest.fixture()
   def app():
       app = create_app()
       app.config.update({
           "TESTING": True,
       })
       yield app
   ```

   애플리케이션 팩토리 패턴 (application factory pattern) 을 사용하는 경우, 픽스처를 적절하게 수정해야 합니다.

5. 테스트 클라이언트 (test client) 및 CLI 러너 (CLI runner) 에 대한 픽스처를 정의합니다.

   ```python
   @pytest.fixture()
   def client(app):
       return app.test_client()

   @pytest.fixture()
   def runner(app):
       return app.test_cli_runner()
   ```
