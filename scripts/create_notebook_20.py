import nbformat as nbf
import os
from pathlib import Path

def create_notebook_20():
    """Create notebook for problem 20 (JSON data reading)"""
    # Create a new notebook
    nb = nbf.v4.new_notebook()
    
    # Add cells
    nb['cells'] = [
        nbf.v4.new_markdown_cell('# 20. JSONデータの読み込み\n\n[Wikipedia記事のJSONファイル](http://www.cl.ecei.tohoku.ac.jp/nlp100/data/jawiki-country.json.gz)を読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．'),
        nbf.v4.new_code_cell('# 問題20: JSONデータの読み込み\n\nimport json\nimport gzip\nimport urllib.request\nimport os\n\n# データファイルのURL\ndata_url = "http://www.cl.ecei.tohoku.ac.jp/nlp100/data/jawiki-country.json.gz"\n\n# データファイルのパス\ndata_dir = "../data"\ndata_file = os.path.join(data_dir, "jawiki-country.json.gz")\n\n# データディレクトリが存在しない場合は作成\nos.makedirs(data_dir, exist_ok=True)\n\n# データファイルをダウンロード（存在しない場合）\ndef download_data():\n    if not os.path.exists(data_file):\n        print(f"データファイルをダウンロード中: {data_url}")\n        urllib.request.urlretrieve(data_url, data_file)\n        print(f"ダウンロード完了: {data_file}")\n    else:\n        print(f"データファイルは既に存在します: {data_file}")\n\n# JSONデータを読み込み、「イギリス」に関する記事を抽出する関数\ndef extract_uk_article():\n    with gzip.open(data_file, "rt", encoding="utf-8") as f:\n        for line in f:\n            article = json.loads(line)\n            if article["title"] == "イギリス":\n                return article["text"]\n    return None\n\n# メイン処理\ntry:\n    # データファイルをダウンロード\n    download_data()\n    \n    # イギリスの記事を抽出\n    uk_article = extract_uk_article()\n    \n    if uk_article:\n        # 記事の最初の500文字を表示（長すぎるため）\n        print("イギリスの記事（冒頭500文字）:")\n        print(uk_article[:500])\n        print("...")\n        \n        # 記事の長さを表示\n        print(f"\\n記事の全体の長さ: {len(uk_article)}文字")\n    else:\n        print("イギリスの記事が見つかりませんでした。")\n        \nexcept Exception as e:\n    print(f"エラーが発生しました: {e}")\n    print("データファイルのダウンロードや読み込みに問題がある可能性があります。")\n    print(f"手動でデータをダウンロードする場合は、{data_url}からダウンロードし、{data_file}に保存してください。")'),
        nbf.v4.new_code_cell('# イギリスの記事を変数に保存（後続の問題で使用するため）\n\n# データファイルが存在するか確認\nif os.path.exists(data_file):\n    # イギリスの記事を抽出\n    uk_article = extract_uk_article()\n    \n    if uk_article:\n        # 記事を保存するファイルパス\n        uk_article_file = os.path.join(data_dir, "uk_article.txt")\n        \n        # 記事をファイルに保存\n        with open(uk_article_file, "w", encoding="utf-8") as f:\n            f.write(uk_article)\n        \n        print(f"イギリスの記事を保存しました: {uk_article_file}")\n    else:\n        print("イギリスの記事が見つかりませんでした。")\nelse:\n    print(f"データファイルが見つかりません: {data_file}")'),
        nbf.v4.new_markdown_cell('## 解説\n\nこの問題では、JSONデータの読み込みと特定の記事の抽出方法を学びます。\n\n### データの取得\n\n問題で指定されたURLからJSONファイルをダウンロードします。このファイルはgzip形式で圧縮されているため、`gzip`モジュールを使用して解凍しながら読み込みます。\n\n### JSONデータの読み込み\n\nPythonの`json`モジュールを使用して、JSONデータを読み込みます。各行が1つの記事を表すJSONオブジェクトになっています。\n\n```python\nwith gzip.open(data_file, "rt", encoding="utf-8") as f:\n    for line in f:\n        article = json.loads(line)\n```\n\n### 「イギリス」に関する記事の抽出\n\n各記事には`title`と`text`のフィールドがあります。タイトルが「イギリス」の記事を見つけたら、その本文を返します。\n\n```python\nif article["title"] == "イギリス":\n    return article["text"]\n```\n\n### 注意点\n\n- データファイルが大きい場合があるため、ダウンロード済みかどうかを確認してから取得しています。\n- 文字エンコーディングを`utf-8`に指定して、日本語を正しく処理できるようにしています。\n- 記事本文が非常に長いため、表示する際は冒頭の一部だけを表示しています。\n- 後続の問題（21-29）で使用するために、抽出した記事をファイルに保存しています。')
    ]
    
    # Create directory if it doesn't exist
    os.makedirs('notebooks/chapter03', exist_ok=True)
    
    # Write the notebook to a file
    notebook_path = Path('notebooks/chapter03/20_json_data.ipynb')
    notebook_path.write_text(nbf.v4.writes(nb))
    
    print(f"Notebook created at {notebook_path}")

if __name__ == "__main__":
    create_notebook_20()
