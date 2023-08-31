@ECHO OFF

python cp-docs.py
mkdocs serve
mkdocs gh-deploy