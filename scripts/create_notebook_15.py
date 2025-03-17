import nbformat as nbf
import os
from pathlib import Path

def create_notebook_15():
    """Create notebook for problem 15 (Last N lines)"""
    # Create a new notebook
    nb = nbf.v4.new_notebook()
    
    # Add cells
    nb['cells'] = [
        nbf.v4.new_markdown_cell('# 15. 末尾のN行を出力\n\n自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．'),
        nbf.v4.new_code_cell('# 問題15: 末尾のN行を出力\n\n# Pythonで末尾N行を出力する関数\ndef tail(file_path, n):\n    """ファイルの末尾N行を出力する関数\n    \n    Args:\n        file_path: 入力ファイルのパス\n        n: 出力する行数\n        \n    Returns:\n        末尾N行の文字列のリスト\n    """\n    # 方法1: 全行を読み込んでから末尾N行を取得\n    with open(file_path, \'r\', encoding=\'utf-8\') as f:\n        lines = f.readlines()\n    return [line.rstrip(\'\\n\') for line in lines[-n:]]\n\n# 方法2: collections.dequeを使用して効率的に末尾N行を取得する関数\nfrom collections import deque\n\ndef tail_efficient(file_path, n):\n    """ファイルの末尾N行を効率的に出力する関数\n    \n    大きなファイルでも効率的に処理できるように、\n    固定サイズのキューを使用して末尾N行を保持します。\n    \n    Args:\n        file_path: 入力ファイルのパス\n        n: 出力する行数\n        \n    Returns:\n        末尾N行の文字列のリスト\n    """\n    with open(file_path, \'r\', encoding=\'utf-8\') as f:\n        # 最大サイズnの両端キューを作成\n        queue = deque(maxlen=n)\n        for line in f:\n            queue.append(line.rstrip(\'\\n\'))\n    return list(queue)\n\n# サンプルファイルのパス（実際の環境に合わせて変更してください）\nfile_path = \'../data/popular-names.txt\'\n\n# 行数を指定（コマンドライン引数の代わりに直接指定）\nn = 5\n\n# 末尾N行を出力（効率的な方法を使用）\ntry:\n    result = tail_efficient(file_path, n)\n    print(f"末尾{n}行:")\n    for line in result:\n        print(line)\nexcept FileNotFoundError:\n    print(f"ファイル {file_path} が見つかりません。")\n    print("このノートブックを実行する前に、必要なデータファイルをダウンロードしてください。")\n    print("データファイルは https://nlp100.github.io/data/popular-names.txt からダウンロードできます。")'),
        nbf.v4.new_code_cell('# コマンドライン引数を受け取る場合の実装例\nimport sys\n\ndef tail_with_args(file_path, n):\n    """ファイルの末尾N行を出力する関数\n    \n    Args:\n        file_path: 入力ファイルのパス\n        n: 出力する行数\n    """\n    try:\n        from collections import deque\n        with open(file_path, \'r\', encoding=\'utf-8\') as f:\n            queue = deque(maxlen=n)\n            for line in f:\n                queue.append(line.rstrip(\'\\n\'))\n        for line in queue:\n            print(line)\n    except FileNotFoundError:\n        print(f"ファイル {file_path} が見つかりません。")\n\n# この関数をコマンドラインから実行する場合の例\n# python tail.py popular-names.txt 5\nif __name__ == \'__main__\' and len(sys.argv) > 2:\n    file_path = sys.argv[1]\n    n = int(sys.argv[2])\n    tail_with_args(file_path, n)\n\n# Jupyter上では実行しない（デモンストレーションのみ）\nprint("これはコマンドライン引数を受け取る実装例です。")\nprint("実際にコマンドラインから実行する場合は、以下のようにします：")\nprint("python tail.py popular-names.txt 5")'),
        nbf.v4.new_code_cell('# UNIXコマンドでの確認（Jupyter上で実行）\n# tailコマンドを使用して末尾N行を出力\n!tail -n 5 ../data/popular-names.txt 2>/dev/null || echo "ファイルが見つかりません"'),
        nbf.v4.new_markdown_cell('## 解説\n\nこの問題では、ファイルの末尾から指定された行数だけを出力する方法を学びます。\n\n### Pythonでの実装\n\nPythonでファイルの末尾N行を出力するには、いくつかの方法があります：\n\n1. **全行を読み込む方法**：\n   - ファイルの全行を読み込み、スライシングを使用して末尾N行を取得します。\n   - 小さなファイルには適していますが、大きなファイルではメモリ効率が悪くなります。\n\n2. **`collections.deque`を使用する方法**：\n   - 固定サイズの両端キュー（deque）を使用して、常に最新のN行だけをメモリに保持します。\n   - 大きなファイルでも効率的に処理できます。\n\n### コマンドライン引数を受け取る実装\n\nPythonスクリプトをコマンドラインから実行する場合、`sys.argv`を使用してコマンドライン引数を受け取ることができます。\n\n```python\nimport sys\n\nfile_path = sys.argv[1]  # 1番目の引数（ファイルパス）\nn = int(sys.argv[2])     # 2番目の引数（行数）\n```\n\n### UNIXコマンドでの確認\n\nUNIXの`tail`コマンドを使用して、ファイルの末尾N行を表示できます：\n\n```bash\ntail -n N input.txt\n```\n\n`-n`オプションは、表示する行数を指定します。\n\n### 注意点\n\n- ファイルが存在しない場合のエラー処理を行っています。\n- 大きなファイルを効率的に処理するために、`collections.deque`を使用した実装を提供しています。\n- 文字エンコーディングを指定して、異なる言語や文字セットのファイルも正しく処理できるようにしています。\n- 実際のアプリケーションでは、コマンドライン引数やGUIなどを通じて、ユーザーから行数を受け取ることができます。')
    ]
    
    # Create directory if it doesn't exist
    os.makedirs('notebooks/chapter02', exist_ok=True)
    
    # Write the notebook to a file
    notebook_path = Path('notebooks/chapter02/15_tail.ipynb')
    notebook_path.write_text(nbf.v4.writes(nb))
    
    print(f"Notebook created at {notebook_path}")

if __name__ == "__main__":
    create_notebook_15()
