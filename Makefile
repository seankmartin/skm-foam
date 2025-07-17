# SKM Foam Documentation Build and Deploy

.PHONY: install serve build deploy clean help

# Install dependencies
install:
	pip install -r requirements.txt

# Prepare docs and serve locally
serve:
	python cp-docs.py
	mkdocs serve

# Build the documentation
build:
	python cp-docs.py
	mkdocs build

# Deploy to GitHub Pages
deploy: build
	mkdocs gh-deploy

# Clean generated files
clean:
	rm -rf site/
	rm -rf docs/

# Open local documentation in browser (macOS)
open:
	open http://127.0.0.1:8000/

# Help target
help:
	@echo "Available targets:"
	@echo "  install  - Install Python dependencies"
	@echo "  serve    - Build docs and serve locally on http://127.0.0.1:8000/"
	@echo "  build    - Build documentation to site/ directory"
	@echo "  deploy   - Deploy to GitHub Pages"
	@echo "  clean    - Remove generated files"
	@echo "  open     - Open local documentation in browser"
	@echo "  help     - Show this help message"

# Default target
all: serve