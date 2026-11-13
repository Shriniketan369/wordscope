# wordscope

A tiny Python command-line tool that reads a text file and shows its most frequent words, ignoring common filler words like "the" and "and".

## Usage

```
python wordscope.py sample.txt
python wordscope.py sample.txt 5
```

The second argument is optional and sets how many top words to show (default: 10).

## Features

- Case-insensitive counting
- Strips punctuation
- Filters common stop words
- Configurable number of results

## Requirements

Python 3.6+. No external libraries needed.
