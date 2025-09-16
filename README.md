# File Trunknizer - Make file sizes to 1

### Description
- Safely truncate file contents for repository upload
- CLI only, no GUI
- No Python required, distributed as exe

### Release
- 250913 First release
  - `file_trunknizer_en_win.exe` → Windows 32/64bit English
  - `file_trunknizer_ko_win.exe` → Windows 32/64bit Korean

### Usage
#### Windows
- just double click the .exe file
- or if you want to run on CLI do this: (but not recommended for safety)
```bash
file_trunknizer.exe [-h] [--lang {ko,en}] [folder] [pattern]
file_trunknizer_en_win.exe [folder_path] [extension string]
file_trunknizer_ko_win.exe [folder_path] [extension string]

e.g.
file_trunknizer_ko_win.exe "C:\txt_files" "*.txt"
python .\file_trunknizer.py --lang en "C:\txt_files" "*.txt"
```
#### Options: use CLI help
```bash
file_trunknizer_en_win.exe --help
file_trunknizer_ko_win.exe --help
```
