#!/bin/zsh

# Create structure.py if it doesn't exist
if [ ! -f /home/labex/project/structure.py ]; then
  cat > /home/labex/project/structure.py << 'EOF'
class Structure:
    # This method is called when a new instance is created
    def __init__(self, *args, **kwargs):
        if len(args) != 0:
            raise TypeError("Expected keyword arguments")
        for name in self._fields:
            setattr(self, name, kwargs.pop(name))
        
        # Check for any remaining unknown arguments
        if kwargs:
            raise TypeError(f"Invalid argument(s): {','.join(kwargs)}")
    
    # Restrict attribute assignment
    def __setattr__(self, name, value):
        if name.startswith('_') or name in self._fields:
            super().__setattr__(name, value)
        else:
            raise AttributeError(f"No attribute {name}")
    
    # String representation for debugging
    def __repr__(self):
        args = ', '.join(repr(getattr(self, name)) for name in self._fields)
        return f"{type(self).__name__}({args})"

class Stock(Structure):
    _fields = ('name', 'shares', 'price')
    
    def _init(self):
        pass
    
    @classmethod
    def set_fields(cls):
        # This is what we'll replace with create_init
        pass
EOF
fi

# Create test_structure.py if it doesn't exist
if [ ! -f /home/labex/project/test_structure.py ]; then
  cat > /home/labex/project/test_structure.py << 'EOF'
import unittest
from structure import Stock

class TestStock(unittest.TestCase):
    def test_create(self):
        s = Stock(name='GOOG', shares=100, price=490.1)
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)
    
    def test_invalid_attribute(self):
        s = Stock(name='GOOG', shares=100, price=490.1)
        with self.assertRaises(AttributeError):
            s.share = 50  # 'share' is not a valid attribute (should be 'shares')

if __name__ == '__main__':
    unittest.main()
EOF
fi

cd /tmp && curl -s https://cdn.jsdelivr.net/gh/labex-labs/common-scripts@master/python-shell-history/setup-python-history-v3.sh | bash
