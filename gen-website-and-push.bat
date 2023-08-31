@ECHO OFF

python cp-docs.py
mkdocs build
mkdocs gh-deploy