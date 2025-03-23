# fortune_package
![CI Status](https://github.com/software-students-spring2025/3-python-package-parallax/actions/workflows/build.yaml/badge.svg)

## Description
A small Python package to make your day just a bit brighter while coding! Test your luck and explore the many fortunes we've included. If you're lucky (or unlucky), the fortune you receive might just come true.

## PyPI Link
[fortune-package2607555](https://pypi.org/project/fortune-teller2607555/)

## Installation & Setup

### Installing Dependencies & Setting Up a Virtual Environment
To install the required dependencies and set up a virtual environment, use:
```sh
pipenv install
pipenv shell
pip install fortune-teller2607555==0.1.0
```

### Importing fortune_package
To use `fortune_teller` in your code, import it as follows:
```python
from fortune_teller.file_name import function_name
```

## Usage
Below is an example of how to use `fortune_teller`:
```python
from fortune_teller.cs_fortune import cs_fortune

fortune = cs_fortune("tech")
print(f"Your fortune: {fortune}")
```

For a complete example of all functions, check out [get_started.py](https://github.com/software-students-spring2025/3-python-package-parallax/blob/main/fortune_teller/get_started.py).

## Contribution Guidelines
We welcome contributions! If you'd like to contribute:
1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Ensure your changes integrate well with existing tests and add new tests if necessary.
4. Submit a pull request for review.

### Code Testing
Run tests before submitting your new code:

```sh
pipenv install --dev pytest
pipenv run python -m pytest tests/
```

## The Team
- [brian105](https://github.com/brian105)
- [Jibril1010](https://github.com/Jibril1010)
- [polinapianina](https://github.com/polinapianina)
- [naseem-student](https://github.com/naseem-student)

