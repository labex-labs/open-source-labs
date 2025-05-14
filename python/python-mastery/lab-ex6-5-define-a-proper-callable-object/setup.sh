#!/bin/zsh

# Set up Python shell history
cd /tmp && curl -s https://cdn.jsdelivr.net/gh/labex-labs/common-scripts@master/python-shell-history/setup-python-history-v3.sh | bash

# Create initial validate.py file with validator classes
cat > /home/labex/project/validate.py << 'EOF'
# Basic Validator classes

class Validator:
    def __init__(self, name=None):
        self.name = name
    
    @classmethod
    def check(cls, value):
        pass

class Typed(Validator):
    expected_type = object
    
    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')

class Integer(Typed):
    expected_type = int

class Float(Typed):
    expected_type = float

class String(Typed):
    expected_type = str
EOF
