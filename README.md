# ORES Client Python module

`ores-python` is a Python API client for the [Objective Revision Evaluation Service](http://ores.wmflabs.org/)
for Wikipedia (ORES).

## Usage

```
usage: ores [-h]
            {query,list-wikis,list-models,check-reverted,check-goodfaith,check-damaging}
            ...

Query the ORES API with Python.

optional arguments:
  -h, --help            show this help message and exit

Subcommands:
  valid subcommands

  {query,list-wikis,list-models,check-reverted,check-goodfaith,check-damaging}
                        Additional help
```

### ores query

```
usage: ores query [-h] query_string

positional arguments:
  query_string  A free-form query

optional arguments:
  -h, --help    show this help message and exit
```

### ores query

```
usage: ores query [-h] query_string

positional arguments:
  query_string  A free-form query

optional arguments:
  -h, --help    show this help message and exit
```

### ores list-wikis

```
usage: ores list-wikis [-h]

optional arguments:
  -h, --help  show this help message and exit
```

### ores list-models

```
usage: ores list-models [-h] project

positional arguments:
  project     A Wikimedia project, supported projects can be obtained with
              list_wikis.

optional arguments:
  -h, --help  show this help message and exit
```

### ores check-reverted

```
usage: ores check-reverted [-h] project edits [edits ...]

positional arguments:
  project     A Wikimedia project, supported projects can be obtained with
              list_wikis.
  edits       A list of edit IDs, as integers.

optional arguments:
  -h, --help  show this help message and exit
```

### ores check-goodfaith

```
usage: ores check-goodfaith [-h] project edits [edits ...]

positional arguments:
  project     A Wikimedia project, supported projects can be obtained with
              list_wikis.
  edits       A list of edit IDs, as integers.

optional arguments:
  -h, --help  show this help message and exit

```

### ores check-damaging

```
usage: ores check-damaging [-h] project edits [edits ...]

positional arguments:
  project     A Wikimedia project, supported projects can be obtained with
              list_wikis.
  edits       A list of edit IDs, as integers.

optional arguments:
  -h, --help  show this help message and exit
```
