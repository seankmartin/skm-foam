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
python merge-journal.py
python cp-docs.py
mkdocs build
```