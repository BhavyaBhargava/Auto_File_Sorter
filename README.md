# Automated File Sorter for Large File Repositories

## Introduction
File management is a universal struggle for anyone using a computer, especially when it comes to managing cluttered folders like the Downloads folder. Over time, these folders become filled with a chaotic mix of documents, images, audio files, videos, and more, making it difficult to locate specific files.  

This problem inspired the creation of **Automated File Sorter**, a Python script designed to bring order to your unorganized folders. It efficiently scans through all the files, identifies their type based on the file format, and moves them into categorized folders such as `Documents`, `Images`, `Videos`, and more. For unknown or uncommon file formats, it creates an "Others" folder.

## Features
- Categorizes files into predefined folders based on their type:
  - Documents, Spreadsheets, Presentations, Images, Audio, Video, and more.
- Automatically creates folders if they don’t already exist.
- Handles files with no extensions by skipping or reporting them.
- Places unsupported or uncategorized files into an `Others` folder.
- Simple and efficient sorting mechanism using Python's `os` and `shutil` modules.

## File Types Supported
The script supports the following file types:

### Categories and Extensions
| **Category**         | **Extensions**                                  |
|-----------------------|------------------------------------------------|
| **Documents**         | pdf, doc, docx, txt, rtf, odt                  |
| **Spreadsheets**      | xls, xlsx, csv, ods                            |
| **Presentations**     | ppt, pptx, odp                                 |
| **Images**            | jpg, jpeg, png, gif, bmp, tiff, svg, webp      |
| **Audio**             | mp3, wav, aac, ogg, flac                       |
| **Video**             | mp4, avi, mkv, mov, wmv, flv, webm             |
| **Compressed Files**  | zip, rar, 7z, tar, gz                          |
| **Executable Files**  | exe, msi, bat, sh, apk, jar                    |
| **Code Files**        | py, java, js, html, htm, css, cpp, c, json, xml, php |
| **Database Files**    | sql, db, sqlite, mdb, accdb                    |
| **E-Books**           | epub, mobi, azw, ibooks                        |
| **System Files**      | dll, sys, ini, log                             |

Files not matching any of the above categories are moved to the `Others` folder.

## How It Works
1. The script scans all files in the current directory.
2. For each file, it checks the extension and determines its category using a predefined dictionary of file formats.
3. It creates a folder for the category (if not already present) and moves the file into the appropriate folder.
4. Files without extensions or unsupported extensions are moved to the `Others` folder.

## Case Study: Cleaning the Downloads Folder
**Scenario:**  
Imagine your Downloads folder is a mess after weeks of downloading work files, images, movies, and software installers. Looking for a specific file feels like finding a needle in a haystack. This script automates the process of sorting those files into meaningful categories, saving you time and effort.

**Outcome:**  
After running the script, your Downloads folder is transformed into an organized repository with folders like `Documents`, `Images`, `Videos`, and `Compressed Files`. You can now easily locate any file you need.

## Usage
### Prerequisites
- Python 3.x installed on your system.

### Steps to Run the Script
1. Save the script file in the directory you want to organize.
2. Open a terminal or command prompt.
3. Navigate to the folder containing the script.
4. Run the script using:
   ```bash
   python file_sorter.py

>>> Watch your files get organized into categorized folders!
