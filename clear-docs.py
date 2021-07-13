import shutil
import os

def main():
    here = os.path.dirname(os.path.abspath(__file__))

    docs_dir = os.path.join(here, "docs")
    site_dir = os.path.join(here, "site")

    shutil.rmtree(docs_dir)
    shutil.rmtree(site_dir)

if __name__ == "__main__":
    main()