# Automated file sorter for Large file Repositories
import os, pathlib, shutil


file_formats = {
    "Documents": [
        "pdf",  # Portable Document Format
        "doc", "docx",  # Microsoft Word documents
        "txt",  # Plain text files
        "rtf",  # Rich Text Format
        "odt"  # OpenDocument Text files
    ],
    "Spreadsheets": [
        "xls", "xlsx",  # Microsoft Excel spreadsheets
        "csv",  # Comma-Separated Values
        "ods"  # OpenDocument Spreadsheet files
    ],
    "Presentations": [
        "ppt", "pptx",  # Microsoft PowerPoint presentations
        "odp"  # OpenDocument Presentation files
    ],
    "Images": [
        "jpg", "jpeg",  # JPEG images
        "png",  # Portable Network Graphics
        "gif",  # Graphics Interchange Format
        "bmp",  # Bitmap images
        "tiff",  # Tagged Image File Format
        "svg",  # Scalable Vector Graphics
        "webp"  # WebP images
    ],
    "Audio": [
        "mp3",  # MP3 audio
        "wav",  # Waveform Audio File Format
        "aac",  # Advanced Audio Codec
        "ogg",  # Ogg Vorbis
        "flac"  # Free Lossless Audio Codec
    ],
    "Video": [
        "mp4",  # MPEG-4 video
        "avi",  # Audio Video Interleave
        "mkv",  # Matroska
        "mov",  # Apple QuickTime movie
        "wmv",  # Windows Media Video
        "flv",  # Flash Video
        "webm"  # WebM video
    ],
    "Compressed Files": [
        "zip",  # ZIP archive
        "rar",  # RAR archive
        "7z",  # 7-Zip archive
        "tar",  # Tarball
        "gz",  # Gzip
    ],
    "Executable Files": [
        "exe",  # Windows Executable
        "msi",  # Microsoft Installer
        "bat",  # Batch files
        "sh",  # Shell scripts
        "apk",  # Android Package
        "jar"  # Java Archive
    ],
    "Code Files": [
        "py",  # Python
        "java",  # Java
        "js",  # JavaScript
        "html", "htm",  # HTML files
        "css",  # Cascading Style Sheets
        "cpp", "c",  # C/C++ source files
        "json",  # JSON data files
        "xml",  # XML files
        "php",  # PHP files
    ],
    "Database Files": [
        "sql",  # SQL script
        "db", "sqlite",  # SQLite database
        "mdb", "accdb"  # Microsoft Access database
    ],
    "E-Books": [
        "epub",  # EPUB format
        "mobi",  # MOBI format
        "azw",  # Amazon Kindle format
        "ibooks"  # Apple iBooks format
    ],
    "System Files": [
        "dll",  # Dynamic-link library
        "sys",  # System file
        "ini",  # Initialization file
        "log",  # Log file
    ]
}

# Checking if the dictionary is properly read
for category, extensions in file_formats.items():
    print(f"{category}: {extensions}")

# Preparing for further processing
fileTypes = list(file_formats.keys())
fileFormats = list(file_formats.values())

