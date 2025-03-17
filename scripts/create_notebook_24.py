import nbformat as nbf
import os
from pathlib import Path

def create_notebook_24():
    """Create notebook for problem 24 (Extract file references)"""
    # Create a new notebook
    nb = nbf.v4.new_notebook()
    
    # Add cells
    nb['cells'] = [
        nbf.v4.new_markdown_cell('# 24. ファイル参照の抽出\n\n記事から参照されているメディアファイルをすべて抽出せよ．'),
        nbf.v4.new_code_cell('# 問題24: ファイル参照の抽出\n\nimport os\nimport re\n\n# イギリスの記事ファイルのパス\ndata_dir = "../data"\nuk_article_file = os.path.join(data_dir, "uk_article.txt")\n\n# メディアファイルの参照を抽出する関数\ndef extract_media_references(text):\n    """記事から参照されているメディアファイルを抽出する関数\n    \n    Args:\n        text: 記事のテキスト\n        \n    Returns:\n        メディアファイル名のリスト\n    """\n    # メディアファイル参照のパターン\n    # [[ファイル:ファイル名|オプション]] または [[File:ファイル名|オプション]] の形式\n    pattern = r"\\[\\[(ファイル|File):([^|\\]]+)(?:\\|[^\\]]*)?\\]\\]"\n    \n    # メディアファイル名を抽出\n    media_files = re.findall(pattern, text)\n    \n    # タプルのリストから、ファイル名のみを取得\n    media_filenames = [filename for _, filename in media_files]\n    \n    return media_filenames\n\n# メイン処理\ntry:\n    # イギリスの記事を読み込む\n    if os.path.exists(uk_article_file):\n        with open(uk_article_file, "r", encoding="utf-8") as f:\n            uk_article = f.read()\n        \n        # メディアファイルの参照を抽出\n        media_files = extract_media_references(uk_article)\n        \n        # 結果を表示\n        print(f"メディアファイルの参照数: {len(media_files)}\\n")\n        print("メディアファイル一覧:")\n        for i, filename in enumerate(media_files):\n            print(f"{i+1}. {filename}")\n    else:\n        print(f"イギリスの記事ファイルが見つかりません: {uk_article_file}")\n        print("問題20を先に実行して、イギリスの記事を抽出してください。")\n        \nexcept Exception as e:\n    print(f"エラーが発生しました: {e}")'),
        nbf.v4.new_code_cell('# ファイル拡張子ごとにメディアファイルを分類\n\ndef classify_media_files_by_extension(filenames):\n    """メディアファイルを拡張子ごとに分類する関数\n    \n    Args:\n        filenames: メディアファイル名のリスト\n        \n    Returns:\n        拡張子ごとのファイル名のディクショナリ\n    """\n    extensions = {}\n    \n    for filename in filenames:\n        # ファイル名から拡張子を取得\n        parts = filename.split(".")\n        if len(parts) > 1:\n            ext = parts[-1].lower()  # 拡張子を小文字に変換\n            \n            # 拡張子ごとにファイル名をリストに追加\n            if ext not in extensions:\n                extensions[ext] = []\n            extensions[ext].append(filename)\n    \n    return extensions\n\n# イギリスの記事ファイルが存在する場合のみ実行\nif os.path.exists(uk_article_file):\n    # 拡張子ごとにメディアファイルを分類\n    extensions = classify_media_files_by_extension(media_files)\n    \n    # 結果を表示\n    print("\\n拡張子ごとのメディアファイル数:")\n    for ext, files in sorted(extensions.items()):\n        print(f"{ext}: {len(files)}ファイル")\n    \n    # 各拡張子の最初のファイル名を表示\n    print("\\n各拡張子の最初のファイル例:")\n    for ext, files in sorted(extensions.items()):\n        print(f"{ext}: {files[0]}")'),
        nbf.v4.new_markdown_cell('## 解説\n\nこの問題では、記事から参照されているメディアファイルを抽出する方法を学びます。\n\n### メディアファイル参照の形式\n\nWikipediaの記事では、メディアファイル（画像、音声、動画など）は以下の形式で参照されています：\n\n```\n[[ファイル:ファイル名|オプション]]\n```\n\nまたは\n\n```\n[[File:ファイル名|オプション]]\n```\n\n「ファイル」は日本語版Wikipediaで使用され、「File」は英語版Wikipediaで使用されます。どちらも同じ機能を持ちます。\n\n### 正規表現を使用した抽出\n\n正規表現を使用して、メディアファイル参照からファイル名を抽出します。\n\n```python\npattern = r"\\[\\[(ファイル|File):([^|\\]]+)(?:\\|[^\\]]*)?\\]\\]"\n```\n\nこの正規表現は以下のように解釈されます：\n\n- `\\[\\[` : 文字列 `[[` にマッチ\n- `(ファイル|File)` : 「ファイル」または「File」にマッチし、グループ化（`()`）\n- `:` : コロンにマッチ\n- `([^|\\]]+)` : パイプ記号（`|`）または閉じ括弧（`]`）以外の1つ以上の文字にマッチし、グループ化（`()`）\n- `(?:\\|[^\\]]*)?` : パイプ記号（`\\|`）とそれに続く閉じ括弧（`]`）以外の任意の文字（`[^\\]]*`）にマッチするが、これは省略可能（`?`）で、グループ化しない（`?:`）\n- `\\]\\]` : 文字列 `]]` にマッチ\n\n### 拡張子による分類\n\n抽出したメディアファイル名を拡張子ごとに分類することで、どのような種類のメディアが記事で使用されているかを分析できます。\n\n```python\nparts = filename.split(".")\nif len(parts) > 1:\n    ext = parts[-1].lower()  # 拡張子を小文字に変換\n```\n\n### 注意点\n\n- ファイル名に特殊文字（スペースや記号など）が含まれる場合があります。\n- 同じファイルが記事内で複数回参照されている場合、重複して抽出される可能性があります。\n- Wikipediaのメディアファイルは、実際にはWikimedia Commonsというリポジトリに保存されています。\n- ファイル名の大文字と小文字は区別されますが、拡張子の分類では小文字に統一しています。')
    ]
    
    # Create directory if it doesn't exist
    os.makedirs('notebooks/chapter03', exist_ok=True)
    
    # Write the notebook to a file
    notebook_path = Path('notebooks/chapter03/24_media_files.ipynb')
    notebook_path.write_text(nbf.v4.writes(nb))
    
    print(f"Notebook created at {notebook_path}")

if __name__ == "__main__":
    create_notebook_24()
