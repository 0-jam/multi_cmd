from pathlib import Path


def find_files(target_dir, exts):
    target_path = Path(target_dir)
    file_paths = []

    for ext in exts:
        file_paths += [f for f in target_path.rglob('*' + ext)]

    return file_paths
