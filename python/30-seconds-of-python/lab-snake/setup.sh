#!/bin/bash

# Create a test file to verify our snake case function
cat > ~/project/test_snake.py << 'EOF'
from snake_case import snake

# Test cases
test_cases = [
    ('camelCase', 'camel_case'),
    ('some text', 'some_text'),
    ('some-mixed_string With spaces_underscores-and-hyphens', 'some_mixed_string_with_spaces_underscores_and_hyphens'),
    ('AllThe-small Things', 'all_the_small_things'),
    ('ILovePython', 'i_love_python'),
    ('HelloWorld', 'hello_world')
]

# Run tests
for input_str, expected_output in test_cases:
    result = snake(input_str)
    assert result == expected_output, f"Failed for '{input_str}': expected '{expected_output}', got '{result}'"

print("All tests passed! Your snake case function works correctly.")
EOF

touch ~/project/snake_case.py