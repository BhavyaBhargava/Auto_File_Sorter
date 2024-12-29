# Automated file sorter for Large file Repositories
# v1.1
import os, pathlib, shutil

file_formats = {
    "Documents": ["pdf", "doc", "docx", "txt", "rtf", "odt"],
    "Spreadsheets": ["xls", "xlsx", "csv", "ods"],
    "Presentations": ["ppt", "pptx", "odp"],
    "Images": ["jpg", "jpeg", "png", "gif", "bmp", "tiff", "svg", "webp"],
    "Audio": ["mp3", "wav", "aac", "ogg", "flac"],
    "Video": ["mp4", "avi", "mkv", "mov", "wmv", "flv", "webm"],
    "Compressed Files": ["zip", "rar", "7z", "tar", "gz"],
    "Executable Files": ["exe", "msi", "bat", "sh", "apk", "jar"],
    "Code Files": ["py", "java", "js", "html", "htm", "css", "cpp", "c", "json", "xml", "php"],
    "Database Files": ["sql", "db", "sqlite", "mdb", "accdb"],
    "E-Books": ["epub", "mobi", "azw", "ibooks"],
    "System Files": ["dll", "sys", "ini", "log"],
}

print("Automated File Sorter Started")
for file in os.scandir():
    file_name = pathlib.Path(file)
    file_extension = file_name.suffix.lower()[1:]  # Remove the leading dot in the extension

    # Skip directories (already sorted folders)
    if file.is_dir():
        continue

    src = str(file_name)
    if file_extension == "":
        print(f"{src} has no file format")
        dest = "Others"
    else:
        dest = "Others"  # Default to "Others" if no format matches
        for category, formats in file_formats.items():
            if file_extension in formats:
                dest = category
                break

    # Create the destination folder if it doesn't exist
    if not os.path.exists(dest):
        os.mkdir(dest)

    print(f"{src} moved to {dest}!")
    shutil.move(src, dest)

input("\nPress ENTER to Exit.")
