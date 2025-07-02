# 소개

이 랩에서는 Python 의 타입 검사 (type checking) 와 인터페이스에 대한 이해를 높이는 방법을 배우게 됩니다. 테이블 형식 모듈을 확장하여 추상 기본 클래스 (abstract base classes) 및 인터페이스 유효성 검사 (interface validation) 와 같은 개념을 구현하여 더욱 강력하고 유지 관리 가능한 코드를 만들 것입니다.

이 랩은 이전 연습의 개념을 기반으로 하며, 타입 안전성 (type safety) 과 인터페이스 디자인 패턴에 중점을 둡니다. 목표는 함수 매개변수에 대한 타입 검사 구현, 추상 기본 클래스를 사용한 인터페이스 생성 및 사용, 그리고 코드 중복을 줄이기 위한 템플릿 메서드 패턴 (template method pattern) 적용을 포함합니다. 데이터 테이블 형식 지정을 위한 모듈인 `tableformat.py`와 CSV 파일을 읽기 위한 모듈인 `reader.py`를 수정하게 됩니다.

<div class="text-xs text-gray-500 dark:text-gray-400 mt-4 border-t border-l-2 border-gray-300 dark:border-gray-600 pt-2 pl-4">
이것은 가이드 실험입니다. 학습과 실습을 돕기 위한 단계별 지침을 제공합니다.각 단계를 완료하고 실무 경험을 쌓기 위해 지침을 주의 깊게 따르세요. 과거 데이터에 따르면, 이것은 <span class="text-green-600 dark:text-green-400">초급</span> 레벨의 실험이며 완료율은 <span class="text-green-600 dark:text-green-400">92%</span>입니다.학습자들로부터 <span class="text-primary-600 dark:text-primary-400">90%</span>의 긍정적인 리뷰율을 받았습니다.
</div>
