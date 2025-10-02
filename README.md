# mischievousmink

Escape/unescape delimiters in txtar files.

## Usage

```bash
# Install and run via uvx
uvx --from git+https://github.com/taylormonacelli/mischievousmink mischievousmink escape
uvx --from git+https://github.com/taylormonacelli/mischievousmink mischievousmink unescape

# Escape delimiters (-- to @@)
mischievousmink escape

# Unescape delimiters (@@ to --)
mischievousmink unescape

# Custom options
mischievousmink escape --dir /path/to/files --pattern "*.txt" --old-delim "--" --new-delim "@@"

# Verbose output
mischievousmink escape -v
mischievousmink escape -vv
mischievousmink escape -vvv
```

## Options

- `--dir`: Starting directory (default: `.`)
- `--pattern`: File pattern (default: `*.txtar`)
- `--old-delim`: Original delimiter (default: `--`)
- `--new-delim`: Replacement delimiter (default: `@@`)
- `-v`: Increase verbosity
