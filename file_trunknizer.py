# PATH: /file_trunknizer.py

import argparse
import glob
import os
import sys

# -----------------------------
# 다국어 문자열 정의 (locale)
# -----------------------------
LOCALES = {
    "ko": {
        "title": "📂 PDF 파일 초기화 프로그램",
        "desc": "이 프로그램은 1)폴더 위치, 2) 폴더 내 검색자 두 가지를 입력받아,\n"
                "이와 일치하는 모든 파일의 내용을 완전히 없애고 1바이트 문자 'a'로 만들어 용량을 1로 줄여줍니다..\n"
                "⚠️ 경고: 이 작업은 되돌릴 수 없습니다.",
        "input_folder": "입력절차 1 of 2) 작업할 폴더 경로를 입력하세요: ",
        "input_pattern": "입력절차 2 of 2) 검색할 패턴을 입력하세요 (예: *.pdf): ",
        "no_folder": "❌ 경로가 존재하지 않습니다: {}",
        "folder_ok": "✔ 입력된 폴더: {}",
        "no_files": "⚠️ 일치하는 파일이 없습니다.",
        "found_files": "📑 검색된 파일 목록:",
        "confirm1": "\n이 파일들의 내용을 'a'로 초기화합니다. 계속하시겠습니까? (y/n): ",
        "cancelled": "작업이 취소되었습니다.",
        "final_warning": "⚠️ 최종 확인: 다음 파일들의 내용을 'a'로 초기화합니다.",
        "confirm2": "정말로 계속하시겠습니까? (y/n): ",
        "running": "🚀 작업 실행 중...",
        "done": "✔ 완료: {}",
        "fail": "❌ 실패: {} ({})",
        "all_done": "✅ 모든 작업이 완료되었습니다.",
        "exit_prompt": "종료하려면 아무 키나 누르십시오..."
    },
    "en": {
        "title": "📂 PDF File Reset Program",
        "desc": "This program takes 1) folder path, 2) file pattern,\n"
                "and resets all matching files to a single byte 'a', reducing their size to 1.\n"
                "⚠️ WARNING: This operation cannot be undone.",
        "input_folder": "Step 1 of 2) Enter the folder path: ",
        "input_pattern": "Step 2 of 2) Enter the search pattern (e.g., *.pdf): ",
        "no_folder": "❌ Path does not exist: {}",
        "folder_ok": "✔ Folder entered: {}",
        "no_files": "⚠️ No matching files found.",
        "found_files": "📑 Found files:",
        "confirm1": "\nReset the contents of these files to 'a'. Continue? (y/n): ",
        "cancelled": "Operation cancelled.",
        "final_warning": "⚠️ FINAL WARNING: The following files will be reset to 'a':",
        "confirm2": "Are you sure you want to continue? (y/n): ",
        "running": "🚀 Executing...",
        "done": "✔ Done: {}",
        "fail": "❌ Failed: {} ({})",
        "all_done": "✅ All tasks completed.",
        "exit_prompt": "Press any key to exit..."
    }
}

def main():
    # -----------------------------
    # CLI 파서
    # -----------------------------
    parser = argparse.ArgumentParser(description="File Trunknizer")
    parser.add_argument("--lang", default="ko", choices=LOCALES.keys(),
                        help="Language (ko or en)")

    # 'folder'와 'pattern' 인자
    parser.add_argument('folder', nargs='?', default=None, help="작업할 폴더 경로")
    parser.add_argument('pattern', nargs='?', default=None, help="검색할 파일 패턴")

    args = parser.parse_args()
    text = LOCALES[args.lang]

    print("=" * 60)
    print(text["title"])
    print("=" * 60)
    print(text["desc"])
    print("=" * 60)

    # 1. 폴더 입력: 명령줄 인자(args.folder)가 없으면 사용자에게 입력받음
    if args.folder:
        folder = args.folder
    else:
        folder = input("\n" + text["input_folder"]).strip()

    if not os.path.isdir(folder):
        print(text["no_folder"].format(folder))
        sys.exit(1)
    print("\n" + text["folder_ok"].format(folder))

    # 2. 검색 패턴 입력: 명령줄 인자(args.pattern)가 없으면 사용자에게 입력받음
    if args.pattern:
        pattern = args.pattern
    else:
        pattern = input("\n" + text["input_pattern"]).strip()

    search_path = os.path.join(folder, pattern)
    files = glob.glob(search_path)

    if not files:
        print(text["no_files"])
        sys.exit(0)

    print("\n" + text["found_files"])
    for f in files:
        print(" -", os.path.basename(f))

    # 3. 1차 확인
    confirm1 = input("\n" + text["confirm1"]).lower()
    if confirm1 != "y":
        print(text["cancelled"])
        sys.exit(0)

    # 4. 최종 확인
    print("\n\033[91m" + text["final_warning"] + "\033[0m")
    for f in files:
        print(" -", os.path.basename(f))

    confirm2 = input("\033[91m" + text["confirm2"] + "\033[0m").lower()
    if confirm2 != "y":
        print(text["cancelled"])
        sys.exit(0)

    # 5. 실행
    print("\n" + text["running"])
    for f in files:
        try:
            with open(f, "wb") as fh:
                fh.write(b"a")
            print(text["done"].format(os.path.basename(f)))
        except Exception as e:
            print(text["fail"].format(os.path.basename(f), e))

    print("\n" + text["all_done"])
    input(text["exit_prompt"])

if __name__ == "__main__":
    main()
