import nbformat as nbf
import os
from pathlib import Path

def create_notebook_22():
    """Create notebook for problem 22 (Extract category names)"""
    # Create a new notebook
    nb = nbf.v4.new_notebook()
    
    # Add cells
    nb['cells'] = [
        nbf.v4.new_markdown_cell('# 22. カテゴリ名の抽出\n\n記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．'),
        nbf.v4.new_code_cell('# 問題22: カテゴリ名の抽出\n\nimport os\nimport re\n\n# イギリスの記事ファイルのパス\ndata_dir = "../data"\nuk_article_file = os.path.join(data_dir, "uk_article.txt")\n\n# カテゴリ名を抽出する関数\ndef extract_category_names(text):\n    """記事からカテゴリ名を抽出する関数\n    \n    Args:\n        text: 記事のテキスト\n        \n    Returns:\n        カテゴリ名のリスト\n    """\n    # カテゴリ名のパターン\n    # [[Category:カテゴリ名]] または [[Category:カテゴリ名|ソート用キー]] の形式\n    pattern = r"\\[\\[Category:(.*?)(?:\\|.*?)?\\]\\]"\n    \n    # カテゴリ名を抽出\n    category_names = re.findall(pattern, text)\n    \n    return category_names\n\n# メイン処理\ntry:\n    # イギリスの記事を読み込む\n    if os.path.exists(uk_article_file):\n        with open(uk_article_file, "r", encoding="utf-8") as f:\n            uk_article = f.read()\n        \n        # カテゴリ名を抽出\n        category_names = extract_category_names(uk_article)\n        \n        # 結果を表示\n        print(f"カテゴリ名の数: {len(category_names)}\\n")\n        print("カテゴリ名一覧:")\n        for i, name in enumerate(category_names):\n            print(f"{i+1}. {name}")\n    else:\n        print(f"イギリスの記事ファイルが見つかりません: {uk_article_file}")\n        print("問題20を先に実行して、イギリスの記事を抽出してください。")\n        \nexcept Exception as e:\n    print(f"エラーが発生しました: {e}")'),
        nbf.v4.new_code_cell('# 別の方法: 行ごとに処理してカテゴリ名を抽出\n\ndef extract_category_names_by_line(text):\n    """行ごとに処理してカテゴリ名を抽出する関数\n    \n    Args:\n        text: 記事のテキスト\n        \n    Returns:\n        カテゴリ名のリスト\n    """\n    category_names = []\n    pattern = r"\\[\\[Category:(.*?)(?:\\|.*?)?\\]\\]"\n    \n    # 行ごとに処理\n    for line in text.split("\\n"):\n        matches = re.findall(pattern, line)\n        category_names.extend(matches)\n    \n    return category_names\n\n# イギリスの記事ファイルが存在する場合のみ実行\nif os.path.exists(uk_article_file):\n    with open(uk_article_file, "r", encoding="utf-8") as f:\n        uk_article = f.read()\n    \n    # 行ごとに処理してカテゴリ名を抽出\n    category_names_by_line = extract_category_names_by_line(uk_article)\n    \n    # 結果を表示\n    print(f"\\n行ごとに処理した場合のカテゴリ名の数: {len(category_names_by_line)}\\n")\n    \n    # 2つの方法の結果を比較\n    if set(category_names) == set(category_names_by_line):\n        print("2つの方法の結果は一致しています。")\n    else:\n        print("2つの方法の結果は一致していません。")\n        print("差分:")\n        print(f"方法1のみに含まれる要素: {set(category_names) - set(category_names_by_line)}")\n        print(f"方法2のみに含まれる要素: {set(category_names_by_line) - set(category_names)}")'),
        nbf.v4.new_markdown_cell('## 解説\n\nこの問題では、記事からカテゴリ名を抽出する方法を学びます。前の問題では行単位でカテゴリ宣言を抽出しましたが、今回はカテゴリ名そのものを抽出します。\n\n### カテゴリ名の形式\n\nWikipediaの記事では、カテゴリ名は以下の形式で宣言されています：\n\n```\n[[Category:カテゴリ名]]\n```\n\nまたは\n\n```\n[[Category:カテゴリ名|ソート用キー]]\n```\n\n### 正規表現を使用した抽出\n\n正規表現を使用して、カテゴリ名部分だけを抽出します。\n\n```python\npattern = r"\\[\\[Category:(.*?)(?:\\|.*?)?\\]\\]"\n```\n\nこの正規表現は以下のように解釈されます：\n\n- `\\[\\[` : 文字列 `[[` にマッチ\n- `Category:` : 文字列 `Category:` にマッチ\n- `(.*?)` : 任意の文字（`.`）が0回以上（`*`）、非貪欲（`?`）にマッチし、グループ化（`()`）\n- `(?:\\|.*?)?` : パイプ記号（`\\|`）とそれに続く任意の文字（`.*?`）にマッチするが、これは省略可能（`?`）で、グループ化しない（`?:`）\n- `\\]\\]` : 文字列 `]]` にマッチ\n\n### 2つの実装方法\n\n1. **テキスト全体に対して正規表現を適用する方法**：\n   - `re.findall()` を使用して、テキスト全体からカテゴリ名を抽出します。\n\n2. **行ごとに処理する方法**：\n   - テキストを行ごとに分割し、各行に対して正規表現を適用します。\n   - 各行から抽出したカテゴリ名をリストに追加します。\n\n### 注意点\n\n- 正規表現の `(.*?)` は非貪欲（non-greedy）マッチングを行い、カテゴリ名部分だけをキャプチャします。\n- `(?:\\|.*?)?` は、ソート用キーが存在する場合（`|` 以降の部分）を無視するための表現です。\n- 2つの方法の結果を比較することで、実装の正確性を確認しています。')
    ]
    
    # Create directory if it doesn't exist
    os.makedirs('notebooks/chapter03', exist_ok=True)
    
    # Write the notebook to a file
    notebook_path = Path('notebooks/chapter03/22_category_names.ipynb')
    notebook_path.write_text(nbf.v4.writes(nb))
    
    print(f"Notebook created at {notebook_path}")

if __name__ == "__main__":
    create_notebook_22()
