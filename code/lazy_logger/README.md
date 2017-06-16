[![Build Status](https://travis-ci.org/Python-Logging-For-Human/lazy_logger.svg?branch=master)](https://travis-ci.org/Python-Logging-For-Human/lazy_logger)

# lazy_logger

__lazy_logger__ is a tool helping you to easily use Python's `logging` module by Python's `print` function.

## Quick start

### Requirements

- Git 1.8+
- Python 3.x


### Install

by `pip`

```
pip install lazy_logger
```

### Usage

```python
# demo.py

import lazy_logger
import sys

logger = lazy_logger.get_logger()

lazy_logger.log_to_console(logger)

lazy_logger.log_to_rotated_file(logger)

@logger.patch
def main():
    print('Hello World!') # expect acting as logger

    print('Hello stdout!', file=sys.stdout) # expect acting as normal print

if __name__ == '__main__':
    main()
```

+ `@logger.patch`: decorator making `print` without file argument to logger which you configured below
+ `log_to_console()`: set logger for sending the message to stderr
+ `log_to_rotated_file()`: set logger for saving the message in file (default: log.out) and rotating at same time
+ `log_to_syslogd():` set logger for sending data to sysemd

# test
py.test --capture=sys


# Thanks the contributions

+ tim(@timtan)
+ WendellLiu(@WendellLiu)
+ jackpan(@jackklpan)
+ Jason(@chairco)
