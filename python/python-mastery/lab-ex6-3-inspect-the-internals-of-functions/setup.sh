#!/bin/zsh

# Download setup script for Python history tracking
cd /tmp && wget https://cdn.jsdelivr.net/gh/labex-labs/common-scripts@master/python-shell-history/.setup-python-shell-history.sh && zsh .setup-python-shell-history.sh

# Create the initial structure.py file
cat > /home/labex/project/structure.py << 'EOF'
class Structure:
    _fields = ()
    
    def _init(self):
        for name, arg in zip(self._fields, self.__init__.__code__.co_varnames[1:]):
            setattr(self, name, arg)
            
    def __setattr__(self, name, value):
        if name.startswith('_') or name in self._fields:
            super().__setattr__(name, value)
        else:
            raise AttributeError(f'No attribute {name}')
            
    def __repr__(self):
        args = ','.join(repr(getattr(self, name)) for name in self._fields)
        return f'{type(self).__name__}({args})'
EOF
