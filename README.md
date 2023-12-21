# Project Title

Savvy Security Website Testing

## Description

This project contains automated tests for the Savvy Security website using the Playwright framework. Two test cases are included to ensure specific functionalities are working as expected.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/HaimHamiel/playwright-pytest-example.git
cd playwright-pytest-example
```

2.  Install dependencies:

```bash
pip install playwright pytest
playwright install
```

## Usage

Run the tests with the following command:

```bash
pytest test_example.py
```

## Features

1. Test Has Title

- Description: Verifies that the website title contains the substring "Savvy".
  - Command: test_has_title

2. Test Terms of Use Link

- Description: Clicks on the "Reject All" button, then clicks on the "Terms of Use" link, and ensures the "Terms of Use" heading is visible.
- Command: test_terms_of_use_link

## Contributing

Feel free to contribute by opening issues or submitting pull requests. Contributions are welcome!

## License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/)
