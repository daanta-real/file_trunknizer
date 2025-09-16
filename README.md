# File Trunknizer - Make file sizes to 1

### Description
I created this Python app to add a large number of dummy sample files to the repository without the burden of large file sizes.

- Safely make target files' content to just one character "a" for reduce file size by 1.
- CLI only, no GUI
- No Python required, distributed as exe
- Language: Korean, English

### Release
- 250913 First release
  - `file_trunknizer_en_win.exe` → Windows 32/64bit English
  - `file_trunknizer_ko_win.exe` → Windows 32/64bit Korean

### Usage
#### Windows
1) DOUBLE CLICK
```text
Just double click the .exe file.
```
2) CLI
```bash
[Exact usage]
file_trunknizer.exe [-h] [--lang {ko,en}] [folder] [pattern]
file_trunknizer_en_win.exe [folder_path] [extension string]
file_trunknizer_ko_win.exe [folder_path] [extension string]

[Examples]
1) run EXE
   file_trunknizer_ko_win.exe "C:\txt_files" "*.txt"
2) Run python code
   python .\file_trunknizer.py --lang en "C:\txt_files" "*.txt"
3) Show help
   file_trunknizer_en_win.exe --help
```

Have a good day.
