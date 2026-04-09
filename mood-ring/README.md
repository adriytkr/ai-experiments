# Mood Ring

Mood Ring is a **lightweight desktop application** designed to analyze the emotional tone and subjectivity of your text in **real-time**. It provides a clean, modern interface that is intuitive and easy to use.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
- [Enginnering](#engineering)
  - [Tools](#tools)
  - [How it works](#how-it-works)
  - [Under the hood](#under-the-hood)
  - [Limitations](#limitations)
- [License](#license)

## Getting Started

### Prerequisites

- [Python](https://www.python.org/)

### Installation

1. Step 1

```
$ command
```

### Usage

Run the following command at root level of Moon Ring folder:

```
$ python src/main.py
```

## Engineering

## Tools

[CustomTkitnter](https://customtkinter.tomschimansky.com/) to build a modern desktop interface.

[TextBlob](https://textblob.readthedocs.io/en/dev/) which performs all the heavy lifting, and scan the text to rate its polarity and subjectivity.

## How it works

After the user submits, their text is processed by TextBlog API, which returns two primary metrics:

- Polarity: A float ranging from -1 to 1 (Negative to Positive).
- Subjectivity: A float ranging from 0 to 1 (Fact to Opinion).

The GUI captures these values and updates accordingly to provide **visual feedback**.

### Under the hood

This should have a super detailed explanation exploring how TextBlog processes and yield polarity and subjectivity.

## Limitations

- While TextBlob is very powerful, it fails in identifying sarcams, Internet Slangs, and emojis due to how its lexicon-based system.

- Also, TextBlob **supports English text only**.

## License

This project is licensed under the **MIT License**.

Copyright (c) 2026 Adriano
