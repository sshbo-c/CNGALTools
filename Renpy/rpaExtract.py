import shutil
from pathlib import Path
import subprocess
import time

#Used tool from https://iwanplays.itch.io/rpaex

# 路径配置
current_dir = Path(__file__).parent
archive_path = current_dir / "game" / "archive.rpa"  # 输入文件
output_dir = current_dir / "rpaUnpacker"  # 输出目录
TOOL_NAME = current_dir / "rpaExtract.exe"  # 工具路径


def get_all_items(dir_path):
    return set(dir_path.glob("*"))


def move_item(src_path, dest_dir):
    dest_path = dest_dir / src_path.name
    if src_path.is_dir():
        shutil.move(str(src_path), str(dest_path))
    else:
        shutil.move(str(src_path), str(dest_path))


def extract_and_move():
    game_dir = current_dir / "game"

    try:
        before_items = get_all_items(game_dir)

        process = subprocess.Popen(
            [str(TOOL_NAME), str(archive_path)],
            cwd=str(current_dir),
            stdin=subprocess.PIPE
        )

        process.stdin.write(b"\n")
        process.stdin.flush()

        process.wait(timeout=60)

        after_items = get_all_items(game_dir)

        new_items = after_items - before_items
        if not new_items:
            raise RuntimeError("未检测到新生成文件，提取失败")

        output_dir.mkdir(exist_ok=True)
        for item in new_items:
            move_item(item, output_dir)

        print(f"Success！Moved {len(new_items)} to {output_dir}")

    except subprocess.TimeoutExpired:
        process.kill()
        print(f"Fail: timeout")
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    extract_and_move()