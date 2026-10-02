import os


def rename_files(folder_path, prefix="file", extension=None):
    """
    Renames all files in the given folder to a pattern like prefix_1.ext, prefix_2.ext, etc.

    :param folder_path: Path to the folder containing files
    :param prefix: Prefix for the new file names (default: "file")
    :param extension: If set, only rename files with this extension (e.g. ".txt")
                       If None, keeps each file's original extension
    """
    if not os.path.isdir(folder_path):
        print(f"❌ Folder not found: {folder_path}")
        return

    # Get all files (ignore subfolders)
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    # Optionally filter by extension
    if extension:
        files = [f for f in files if f.lower().endswith(extension.lower())]

    if not files:
        print("📭 No matching files found to rename.")
        return

    files.sort()  # keep a consistent order

    print(f"Found {len(files)} file(s). Renaming...\n")

    for index, filename in enumerate(files, start=1):
        old_path = os.path.join(folder_path, filename)

        # Keep original extension unless one is forced
        file_ext = extension if extension else os.path.splitext(filename)[1]
        new_filename = f"{prefix}_{index}{file_ext}"
        new_path = os.path.join(folder_path, new_filename)

        # Avoid overwriting existing files
        if os.path.exists(new_path):
            print(f"⚠️ Skipped '{filename}' — '{new_filename}' already exists.")
            continue

        os.rename(old_path, new_path)
        print(f"✅ Renamed: '{filename}' → '{new_filename}'")

    print("\n🎉 Renaming complete!")


if __name__ == "__main__":
    folder = input("Enter the folder path: ").strip()
    prefix = input("Enter prefix for new file names (default 'file'): ").strip() or "file"
    ext_filter = input("Only rename files with a specific extension? (e.g. .txt, leave blank for all): ").strip()

    rename_files(folder, prefix, ext_filter if ext_filter else None)