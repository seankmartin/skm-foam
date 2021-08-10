@ECHO OFF

python merge-journal.py
python cp-docs.py
mkdocs serve