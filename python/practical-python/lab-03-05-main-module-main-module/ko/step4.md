# 메인 프로그램 (Main programs) vs. 라이브러리 임포트 (library imports)

모든 Python 파일은 메인으로 실행되거나 라이브러리 임포트로 사용될 수 있습니다.

```bash
$ python3 prog.py # Running as main
```

```python
import prog   # Running as library import
```

두 경우 모두, `__name__`은 모듈의 이름입니다. 그러나 메인으로 실행되는 경우에만 `__main__`으로 설정됩니다.

일반적으로, 메인 프로그램의 일부인 문장이 라이브러리 임포트 시 실행되는 것을 원하지 않습니다. 따라서, 두 가지 방식으로 사용될 수 있는 코드에 `if` 검사를 사용하는 것이 일반적입니다.

```python
if __name__ == '__main__':
    # Does not execute if loaded with import ...
```
