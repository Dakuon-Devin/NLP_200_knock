import nbformat as nbf
import os
from pathlib import Path

def create_notebook_23():
    """Create notebook for problem 23 (Section structure)"""
    # Create a new notebook
    nb = nbf.v4.new_notebook()
    
    # Add cells
    nb['cells'] = [
        nbf.v4.new_markdown_cell('# 23. セクション構造\n\n記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．'),
        nbf.v4.new_code_cell('# 問題23: セクション構造\n\nimport os\nimport re\n\n# イギリスの記事ファイルのパス\ndata_dir = "../data"\nuk_article_file = os.path.join(data_dir, "uk_article.txt")\n\n# セクション名とそのレベルを抽出する関数\ndef extract_sections(text):\n    """記事からセクション名とそのレベルを抽出する関数\n    \n    Args:\n        text: 記事のテキスト\n        \n    Returns:\n        (セクション名, レベル)のタプルのリスト\n    """\n    # セクションのパターン\n    # == セクション名 == または === セクション名 === などの形式\n    pattern = r"^(={2,})\\s*(.+?)\\s*\\1$"\n    \n    sections = []\n    for line in text.split("\\n"):\n        match = re.match(pattern, line)\n        if match:\n            level = len(match.group(1)) - 1  # レベルは = の数 - 1\n            section_name = match.group(2)\n            sections.append((section_name, level))\n    \n    return sections\n\n# メイン処理\ntry:\n    # イギリスの記事を読み込む\n    if os.path.exists(uk_article_file):\n        with open(uk_article_file, "r", encoding="utf-8") as f:\n            uk_article = f.read()\n        \n        # セクション名とそのレベルを抽出\n        sections = extract_sections(uk_article)\n        \n        # 結果を表示\n        print(f"セクションの数: {len(sections)}\\n")\n        print("セクション構造:")\n        for i, (name, level) in enumerate(sections):\n            indent = "  " * (level - 1)  # レベルに応じてインデント\n            print(f"{i+1}. {indent}{name} (レベル{level})")\n    else:\n        print(f"イギリスの記事ファイルが見つかりません: {uk_article_file}")\n        print("問題20を先に実行して、イギリスの記事を抽出してください。")\n        \nexcept Exception as e:\n    print(f"エラーが発生しました: {e}")'),
        nbf.v4.new_code_cell('# 別の方法: 正規表現のマルチラインモードを使用\n\ndef extract_sections_multiline(text):\n    """正規表現のマルチラインモードを使用してセクション名とそのレベルを抽出する関数\n    \n    Args:\n        text: 記事のテキスト\n        \n    Returns:\n        (セクション名, レベル)のタプルのリスト\n    """\n    # セクションのパターン\n    pattern = r"^(={2,})\\s*(.+?)\\s*\\1$"\n    \n    # re.MULTILINE フラグを使用して、複数行にまたがるマッチングを行う\n    matches = re.finditer(pattern, text, re.MULTILINE)\n    \n    sections = []\n    for match in matches:\n        level = len(match.group(1)) - 1  # レベルは = の数 - 1\n        section_name = match.group(2)\n        sections.append((section_name, level))\n    \n    return sections\n\n# イギリスの記事ファイルが存在する場合のみ実行\nif os.path.exists(uk_article_file):\n    with open(uk_article_file, "r", encoding="utf-8") as f:\n        uk_article = f.read()\n    \n    # マルチラインモードを使用してセクション名とそのレベルを抽出\n    sections_multiline = extract_sections_multiline(uk_article)\n    \n    # 結果を表示\n    print(f"\\nマルチラインモードを使用した場合のセクションの数: {len(sections_multiline)}\\n")\n    \n    # 2つの方法の結果を比較\n    if sections == sections_multiline:\n        print("2つの方法の結果は一致しています。")\n    else:\n        print("2つの方法の結果は一致していません。")\n        print(f"方法1の結果数: {len(sections)}")\n        print(f"方法2の結果数: {len(sections_multiline)}")'),
        nbf.v4.new_code_cell('# セクション構造をツリー形式で表示\n\ndef print_section_tree(sections):\n    """セクション構造をツリー形式で表示する関数\n    \n    Args:\n        sections: (セクション名, レベル)のタプルのリスト\n    """\n    print("セクション構造（ツリー形式）:")\n    \n    # 最小レベルを取得\n    min_level = min(level for _, level in sections) if sections else 0\n    \n    for name, level in sections:\n        # レベルに応じてインデントとマーカーを設定\n        indent = "  " * (level - min_level)\n        marker = "■" if level == min_level else "●" if level == min_level + 1 else "◆" if level == min_level + 2 else "◇"\n        \n        print(f"{indent}{marker} {name}")\n\n# イギリスの記事ファイルが存在する場合のみ実行\nif os.path.exists(uk_article_file):\n    # セクション構造をツリー形式で表示\n    print_section_tree(sections)'),
        nbf.v4.new_markdown_cell('## 解説\n\nこの問題では、記事中に含まれるセクション名とそのレベルを抽出する方法を学びます。\n\n### セクションの形式\n\nWikipediaの記事では、セクションは以下の形式で表現されています：\n\n```\n== セクション名 ==    （レベル1）\n=== サブセクション名 ===    （レベル2）\n==== サブサブセクション名 ====    （レベル3）\n```\n\nセクションのレベルは、`=` の数によって決まります。この問題では、`=` の数から1を引いたものをレベルとしています。\n\n### 正規表現を使用した抽出\n\n正規表現を使用して、セクション名とそのレベルを抽出します。\n\n```python\npattern = r"^(={2,})\\s*(.+?)\\s*\\1$"\n```\n\nこの正規表現は以下のように解釈されます：\n\n- `^` : 行の先頭にマッチ\n- `(={2,})` : 2つ以上の連続する `=` にマッチし、グループ化（`()`）\n- `\\s*` : 0個以上の空白文字にマッチ\n- `(.+?)` : 1つ以上の任意の文字（`.`）にマッチし、非貪欲（`?`）でグループ化（`()`）\n- `\\s*` : 0個以上の空白文字にマッチ\n- `\\1` : 1番目のグループ（`(={2,})`）と同じ文字列にマッチ（後方参照）\n- `$` : 行の末尾にマッチ\n\n### 2つの実装方法\n\n1. **行ごとに処理する方法**：\n   - テキストを行ごとに分割し、各行に対して正規表現を適用します。\n   - セクション行にマッチした場合、セクション名とレベルを抽出します。\n\n2. **正規表現のマルチラインモードを使用する方法**：\n   - `re.MULTILINE` フラグを使用して、複数行にまたがるマッチングを行います。\n   - `re.finditer()` を使用して、すべてのマッチを取得します。\n\n### セクション構造の表示\n\nセクション構造を視覚的に理解しやすくするために、ツリー形式で表示する関数も実装しています。レベルに応じてインデントとマーカーを変更することで、階層構造を表現しています。\n\n### 注意点\n\n- セクション名に `=` が含まれる場合、正規表現のパターンを調整する必要があります。\n- 実際のWikipediaの記事では、セクションの階層構造が複雑な場合があります。\n- 後方参照（`\\1`）を使用することで、セクションの開始と終了の `=` の数が同じであることを確認しています。')
    ]
    
    # Create directory if it doesn't exist
    os.makedirs('notebooks/chapter03', exist_ok=True)
    
    # Write the notebook to a file
    notebook_path = Path('notebooks/chapter03/23_section_structure.ipynb')
    notebook_path.write_text(nbf.v4.writes(nb))
    
    print(f"Notebook created at {notebook_path}")

if __name__ == "__main__":
    create_notebook_23()
