# F-A-C-E
## Framed Artistry Compliance Examiner

# Installation

Requires `python >=3.7`

1. Create a python virtual environment

```
python -m venv venv
```

2. Activate the virtual environment

```
./venv/Scripts/activate
```

3. Install dependencies

```
pip install -r requirements.txt
```

# How to use

--source" help="Path to the input folder containing the images"

--destination" help="Path to the pass folder for images that pass the test"

--rejects help="Path to the reject folder for images that fail the test"

```
python cli.py --source <image folder path> --destination <pass folder> --rejects <reject folder>
```

# TODO

- Sort images according to size
- Reject black or blank images
- Reject white/gray images
- Reject blurry images
- Progress functionality
