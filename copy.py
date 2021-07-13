import os
import shutil


def main():
    dirs_to_ignore = [
        ".foam",
        ".vscode",
        "_layouts",
        "assets",
        "site",
        "docs",
        "foam_docs",
    ]
    f_exts = [".md", ".png", ".jpg"]

    def ok_file(root_dir, filename):
        has_ext = os.path.splitext(filename)[-1] in f_exts
        is_file = os.path.isfile(os.path.join(root_dir, filename))
        use = filename.split(os.sep)[0] not in dirs_to_ignore
        return has_ext and is_file and use

    in_dir = os.path.dirname(os.path.abspath(__file__))

    onlyfiles = []
    start_root = in_dir
    for root, _, filenames in os.walk(in_dir):

        if len(root) == len(start_root):
            end_root = ""
        else:
            if in_dir.endswith(os.sep):
                end_root = root[len(in_dir) :]
            else:
                end_root = root[len(in_dir + os.sep) :]
        for filename in filenames:
            filename = os.path.join(end_root, filename)
            if ok_file(start_root, filename):
                onlyfiles.append(filename)

    from pprint import pprint

    shutil.rmtree(os.path.join(in_dir, "docs"))
    for fname in onlyfiles:
        source = os.path.join(in_dir, fname)
        dest = os.path.join(in_dir, "docs", fname)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        shutil.copyfile(source, dest)


if __name__ == "__main__":
    main()
