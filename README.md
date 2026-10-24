# CSS Parser

## Overview

A Python project that reads a CSS stylesheet and extracts selectors and their property-value declarations into structured JSON.

## Features

* Reads CSS files from a specified path.
* Extracts CSS selectors, properties, and values.
* Converts parsed information into readable JSON.
* Ignores comments and whitespace.
* Handles missing CSS files with an error message.

## Technologies Used

* Python
* tinycss2
* JSON

## Installation

Install Python, then install the required dependency:

```bash
python -m pip install -r requirements.txt
```

## How to Run

Run the parser using the default `style.css` file:

```bash
python parser.py
```

To parse a different CSS file:

```bash
python parser.py another.css
```

## Example Input

```css
h1 {
    color: blue;
    font-size: 24px;
}
```

## Example Output

```json
[
  {
    "selector": "h1",
    "declarations": {
      "color": "blue",
      "font-size": "24px"
    }
  }
]
```

## Edge Case

If the specified CSS file does not exist, the program displays an error message instead of terminating with an unhandled exception.

## Current Limitations

The parser processes ordinary selector-based rules. Nested at-rules, such as `@media`, are not recursively parsed.

## Author

Dinesh Kanna
