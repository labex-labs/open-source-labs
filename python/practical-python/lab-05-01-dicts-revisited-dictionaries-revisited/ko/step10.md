# 상속을 사용한 속성 읽기 (Reading Attributes with Inheritance)

논리적으로, 속성을 찾는 과정은 다음과 같습니다. 먼저, 로컬 `__dict__`를 확인합니다. 찾을 수 없으면, 클래스의 `__dict__`를 살펴봅니다. 클래스에서도 찾을 수 없으면, `__bases__`를 통해 기본 클래스를 살펴봅니다. 하지만, 이에 대한 몇 가지 미묘한 측면이 다음에 논의됩니다.
