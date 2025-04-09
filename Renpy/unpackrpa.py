import  os
import unrpa
import subprocess
import sys
from pathlib import Path

def extract_rpa_archive():
    # 定义路径
    current_dir = Path(__file__).parent
    archive_path = current_dir / "game" / "archive.rpa"
    output_dir = current_dir / "rpaUnpacker"

    output_dir.mkdir(exist_ok=True)

    command = [
        sys.executable,
        "-m", "unrpa",
        "-mp", str(output_dir),
        str(archive_path)
    ]

    try:
        print("Extracting RPA...")
        subprocess.run(command, check=True)
        print("Success！")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Fail: {e}")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False


if __name__ == "__main__":
    print("=== RPA提取 ===")
    print("如果提取失败，尝试添加-f参数指定版本,或选择rpaExtract工具"
          "https://iwanplays.itch.io/rpaex")
    extract_rpa_archive()
