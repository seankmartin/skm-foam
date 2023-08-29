# SKM Foam

My knowledge base in foam.

## Build a local website version

```Bash
pip install -r requirements.txt
python merge-journal.py
python cp-docs.py
mkdocs serve
```

Then:

```Bash
start chrome http://127.0.0.1:8000/
```

OR

```Bash
python cp-docs.py
mkdocs build
mkdocs gh-deploy
```

## Convert a file to another format

For instance, to convert projects\open-data to latex

```Bash
pandoc -r markdown-auto_identifiers projects\open-data.md -t latex -o open_data.tex 
```
