import sys

def reverse_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(output_path, 'w', encoding='utf-8') as f:
        for line in reversed(lines):
            if not line.endswith('\n'):
                line += '\n'
            f.write(line)

def copy_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    with open(output_path, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line)

def duplicate_file(input_path):
    print("複製する回数を入力してください:")
    num_copies = int(input())
    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    with open(input_path, 'w') as f:
        for i in range(num_copies):
            for line in lines:
                if not line.endswith('\n'):
                    line += '\n'
                f.write(line)

def replace_string(input_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    with open(input_path, 'w', encoding='utf-8') as f:
        f.write(content.replace('oldstring', 'newstring'))

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("使用例: python3 file_manipulator.py reverse <input_file> <output_file>")
        sys.exit(1)

    command = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]

    if command == 'reverse':
        reverse_file(input_file, output_file)
        print(f"'{input_file}'を受け取って'{output_file}を出力しました'")
    elif command == 'copy':
        copy_file(input_file, output_file)
        print(f"'{input_file}' をコピーして '{output_file}を出力しました'")
    elif command == 'duplicate':
        duplicate_file(input_file)
        print(f"'{input_file}' を複製しました")
    elif command == 'replace':
        replace_string(input_file)
        print(f"'{input_file}' の文字列を置き換えました")
    else:
        print(f"{command}は無効なコマンドです。")