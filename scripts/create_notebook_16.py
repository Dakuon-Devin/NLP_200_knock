import nbformat as nbf
import os
from pathlib import Path

def create_notebook_16():
    """Create notebook for problem 16 (Split file)"""
    # Create a new notebook
    nb = nbf.v4.new_notebook()
    
    # Add cells
    nb['cells'] = [
        nbf.v4.new_markdown_cell('# 16. ファイルをN分割する\n\n自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．'),
        nbf.v4.new_code_cell('# 問題16: ファイルをN分割する\n\nimport math\nimport os\n\n# PythonでファイルをN分割する関数\ndef split_file(file_path, n, output_dir=\'.\'):\n    """ファイルをN分割する関数\n    \n    Args:\n        file_path: 入力ファイルのパス\n        n: 分割数\n        output_dir: 出力ディレクトリ\n        \n    Returns:\n        分割されたファイルのパスのリスト\n    """\n    # 出力ファイルのパスのリスト\n    output_files = []\n    \n    # 入力ファイルの行数をカウント\n    with open(file_path, \'r\', encoding=\'utf-8\') as f:\n        lines = f.readlines()\n    \n    total_lines = len(lines)\n    lines_per_file = math.ceil(total_lines / n)  # 1ファイルあたりの行数（切り上げ）\n    \n    # ファイル名の基本部分とファイル拡張子を取得\n    base_name = os.path.basename(file_path)\n    name, ext = os.path.splitext(base_name)\n    \n    # ファイルを分割して保存\n    for i in range(n):\n        start_idx = i * lines_per_file\n        end_idx = min((i + 1) * lines_per_file, total_lines)\n        \n        if start_idx >= total_lines:\n            break\n        \n        output_path = os.path.join(output_dir, f"{name}_{i+1:02d}{ext}")\n        output_files.append(output_path)\n        \n        with open(output_path, \'w\', encoding=\'utf-8\') as f_out:\n            f_out.writelines(lines[start_idx:end_idx])\n    \n    return output_files\n\n# サンプルファイルのパス（実際の環境に合わせて変更してください）\nfile_path = \'../data/popular-names.txt\'\noutput_dir = \'../data\'\n\n# 分割数を指定（コマンドライン引数の代わりに直接指定）\nn = 5\n\n# ファイルをN分割\ntry:\n    output_files = split_file(file_path, n, output_dir)\n    print(f"ファイルを{n}分割しました:")\n    for file_path in output_files:\n        print(f"- {file_path}")\nexcept FileNotFoundError:\n    print(f"ファイル {file_path} が見つかりません。")\n    print("このノートブックを実行する前に、必要なデータファイルをダウンロードしてください。")\n    print("データファイルは https://nlp100.github.io/data/popular-names.txt からダウンロードできます。")'),
        nbf.v4.new_code_cell('# コマンドライン引数を受け取る場合の実装例\nimport sys\nimport math\nimport os\n\ndef split_file_with_args(file_path, n, output_dir=\'.\'):\n    """ファイルをN分割する関数\n    \n    Args:\n        file_path: 入力ファイルのパス\n        n: 分割数\n        output_dir: 出力ディレクトリ\n    """\n    try:\n        # 入力ファイルの行数をカウント\n        with open(file_path, \'r\', encoding=\'utf-8\') as f:\n            lines = f.readlines()\n        \n        total_lines = len(lines)\n        lines_per_file = math.ceil(total_lines / n)  # 1ファイルあたりの行数（切り上げ）\n        \n        # ファイル名の基本部分とファイル拡張子を取得\n        base_name = os.path.basename(file_path)\n        name, ext = os.path.splitext(base_name)\n        \n        # ファイルを分割して保存\n        for i in range(n):\n            start_idx = i * lines_per_file\n            end_idx = min((i + 1) * lines_per_file, total_lines)\n            \n            if start_idx >= total_lines:\n                break\n            \n            output_path = os.path.join(output_dir, f"{name}_{i+1:02d}{ext}")\n            \n            with open(output_path, \'w\', encoding=\'utf-8\') as f_out:\n                f_out.writelines(lines[start_idx:end_idx])\n            \n            print(f"ファイルを作成しました: {output_path}")\n    \n    except FileNotFoundError:\n        print(f"ファイル {file_path} が見つかりません。")\n\n# この関数をコマンドラインから実行する場合の例\n# python split_file.py popular-names.txt 5 output_dir\nif __name__ == \'__main__\' and len(sys.argv) > 2:\n    file_path = sys.argv[1]\n    n = int(sys.argv[2])\n    output_dir = sys.argv[3] if len(sys.argv) > 3 else \'.\'\n    split_file_with_args(file_path, n, output_dir)\n\n# Jupyter上では実行しない（デモンストレーションのみ）\nprint("これはコマンドライン引数を受け取る実装例です。")\nprint("実際にコマンドラインから実行する場合は、以下のようにします：")\nprint("python split_file.py popular-names.txt 5 output_dir")'),
        nbf.v4.new_code_cell('# UNIXコマンドでの確認（Jupyter上で実行）\n# splitコマンドを使用してファイルをN分割\n!mkdir -p /tmp/split_output 2>/dev/null\n!split -n l/5 ../data/popular-names.txt /tmp/split_output/popular-names_ 2>/dev/null && echo "splitコマンドで分割完了" || echo "splitコマンドでの分割に失敗しました"'),
        nbf.v4.new_code_cell('# 分割されたファイルの確認\n!ls -l /tmp/split_output/ 2>/dev/null || echo "ディレクトリが見つかりません"'),
        nbf.v4.new_markdown_cell('## 解説\n\nこの問題では、ファイルを行単位でN分割する方法を学びます。\n\n### Pythonでの実装\n\nPythonでファイルをN分割するには、以下の手順を実行します：\n\n1. 入力ファイルの全行を読み込みます。\n2. 全体の行数を分割数で割って、1ファイルあたりの行数を計算します。\n3. 計算した行数に基づいて、ファイルを分割して保存します。\n\n### コマンドライン引数を受け取る実装\n\nPythonスクリプトをコマンドラインから実行する場合、`sys.argv`を使用してコマンドライン引数を受け取ることができます。\n\n```python\nimport sys\n\nfile_path = sys.argv[1]  # 1番目の引数（ファイルパス）\nn = int(sys.argv[2])     # 2番目の引数（分割数）\noutput_dir = sys.argv[3] if len(sys.argv) > 3 else \'.\'  # 3番目の引数（出力ディレクトリ、省略可能）\n```\n\n### UNIXコマンドでの確認\n\nUNIXの`split`コマンドを使用して、ファイルをN分割できます：\n\n```bash\nsplit -n l/N input.txt output_prefix\n```\n\n`-n l/N`オプションは、ファイルをN個の部分に分割することを指定します。`l`は「行数で分割」を意味します。\n\n### 注意点\n\n- ファイルが存在しない場合のエラー処理を行っています。\n- 分割数が行数より多い場合の処理を考慮しています。\n- 文字エンコーディングを指定して、異なる言語や文字セットのファイルも正しく処理できるようにしています。\n- 実際のアプリケーションでは、コマンドライン引数やGUIなどを通じて、ユーザーから分割数を受け取ることができます。')
    ]
    
    # Create directory if it doesn't exist
    os.makedirs('notebooks/chapter02', exist_ok=True)
    
    # Write the notebook to a file
    notebook_path = Path('notebooks/chapter02/16_split_file.ipynb')
    notebook_path.write_text(nbf.v4.writes(nb))
    
    print(f"Notebook created at {notebook_path}")

if __name__ == "__main__":
    create_notebook_16()
