import nbformat as nbf
import os
from pathlib import Path

def create_notebook_21():
    """Create notebook for problem 21 (Extract lines with category names)"""
    # Create a new notebook
    nb = nbf.v4.new_notebook()
    
    # Add cells
    nb['cells'] = [
        nbf.v4.new_markdown_cell('# 21. カテゴリ名を含む行を抽出\n\n記事中でカテゴリ名を宣言している行を抽出せよ．'),
        nbf.v4.new_code_cell('# 問題21: カテゴリ名を含む行を抽出\n\nimport os\nimport re\n\n# イギリスの記事ファイルのパス\ndata_dir = "../data"\nuk_article_file = os.path.join(data_dir, "uk_article.txt")\n\n# カテゴリ名を宣言している行を抽出する関数\ndef extract_category_lines(text):\n    """カテゴリ名を宣言している行を抽出する関数\n    \n    Args:\n        text: 記事のテキスト\n        \n    Returns:\n        カテゴリ名を宣言している行のリスト\n    """\n    # カテゴリ名を宣言している行のパターン\n    # [[Category:カテゴリ名]] または [[Category:カテゴリ名|ソート用キー]] の形式\n    pattern = r"\\[\\[Category:.*?\\]\\]"\n    \n    # 行ごとに処理\n    category_lines = []\n    for line in text.split("\\n"):\n        if re.search(pattern, line):\n            category_lines.append(line)\n    \n    return category_lines\n\n# メイン処理\ntry:\n    # イギリスの記事を読み込む\n    if os.path.exists(uk_article_file):\n        with open(uk_article_file, "r", encoding="utf-8") as f:\n            uk_article = f.read()\n        \n        # カテゴリ名を宣言している行を抽出\n        category_lines = extract_category_lines(uk_article)\n        \n        # 結果を表示\n        print(f"カテゴリ名を宣言している行の数: {len(category_lines)}\\n")\n        print("カテゴリ名を宣言している行の例:")\n        for i, line in enumerate(category_lines):\n            if i < 10:  # 最初の10行だけ表示\n                print(f"{i+1}. {line}")\n            else:\n                print("...")\n                break\n    else:\n        print(f"イギリスの記事ファイルが見つかりません: {uk_article_file}")\n        print("問題20を先に実行して、イギリスの記事を抽出してください。")\n        \nexcept Exception as e:\n    print(f"エラーが発生しました: {e}")'),
        nbf.v4.new_code_cell('# 別の方法: 正規表現のマルチラインモードを使用\n\ndef extract_category_lines_multiline(text):\n    """正規表現のマルチラインモードを使用してカテゴリ名を宣言している行を抽出する関数\n    \n    Args:\n        text: 記事のテキスト\n        \n    Returns:\n        カテゴリ名を宣言している行のリスト\n    """\n    # カテゴリ名を宣言している行のパターン\n    # ^ は行の先頭、$ は行の末尾を表す（マルチラインモードの場合）\n    pattern = r"^.*\\[\\[Category:.*?\\]\\].*$"\n    \n    # re.MULTILINE フラグを使用して、複数行にまたがるマッチングを行う\n    matches = re.findall(pattern, text, re.MULTILINE)\n    \n    return matches\n\n# イギリスの記事ファイルが存在する場合のみ実行\nif os.path.exists(uk_article_file):\n    with open(uk_article_file, "r", encoding="utf-8") as f:\n        uk_article = f.read()\n    \n    # マルチラインモードを使用してカテゴリ名を宣言している行を抽出\n    category_lines_multiline = extract_category_lines_multiline(uk_article)\n    \n    # 結果を表示\n    print(f"\\nマルチラインモードを使用した場合のカテゴリ名を宣言している行の数: {len(category_lines_multiline)}\\n")\n    print("カテゴリ名を宣言している行の例（マルチラインモード）:")\n    for i, line in enumerate(category_lines_multiline):\n        if i < 10:  # 最初の10行だけ表示\n            print(f"{i+1}. {line}")\n        else:\n            print("...")\n            break'),
        nbf.v4.new_markdown_cell('## 解説\n\nこの問題では、記事中でカテゴリ名を宣言している行を抽出する方法を学びます。\n\n### カテゴリ名の宣言形式\n\nWikipediaの記事では、カテゴリ名は以下の形式で宣言されています：\n\n```\n[[Category:カテゴリ名]]\n```\n\nまたは\n\n```\n[[Category:カテゴリ名|ソート用キー]]\n```\n\n### 正規表現を使用した抽出\n\n正規表現を使用して、カテゴリ名を宣言している行を抽出します。\n\n```python\npattern = r"\\[\\[Category:.*?\\]\\]"\n```\n\nこの正規表現は以下のように解釈されます：\n\n- `\\[\\[` : 文字列 `[[` にマッチ（`[` は正規表現の特殊文字なのでエスケープが必要）\n- `Category:` : 文字列 `Category:` にマッチ\n- `.*?` : 任意の文字（`.`）が0回以上（`*`）、非貪欲（`?`）にマッチ\n- `\\]\\]` : 文字列 `]]` にマッチ\n\n### 2つの実装方法\n\n1. **行ごとに処理する方法**：\n   - テキストを行ごとに分割し、各行に対して正規表現を適用します。\n   - カテゴリ名を含む行だけをリストに追加します。\n\n2. **正規表現のマルチラインモードを使用する方法**：\n   - `re.MULTILINE` フラグを使用して、複数行にまたがるマッチングを行います。\n   - 行の先頭（`^`）と行の末尾（`$`）を表す特殊文字を使用できます。\n\n### 注意点\n\n- 正規表現の `.*?` は非貪欲（non-greedy）マッチングを行います。これにより、最初の `]]` までの文字列にマッチします。\n- カテゴリ名が複数行にまたがる場合は、適切に処理する必要があります（この問題では考慮していません）。\n- 実際のWikipediaの記事では、カテゴリ名は通常、記事の末尾に集中しています。')
    ]
    
    # Create directory if it doesn't exist
    os.makedirs('notebooks/chapter03', exist_ok=True)
    
    # Write the notebook to a file
    notebook_path = Path('notebooks/chapter03/21_category_lines.ipynb')
    notebook_path.write_text(nbf.v4.writes(nb))
    
    print(f"Notebook created at {notebook_path}")

if __name__ == "__main__":
    create_notebook_21()
