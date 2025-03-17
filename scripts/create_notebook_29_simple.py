import nbformat as nbf
import os
from pathlib import Path

def create_notebook_29():
    """Create notebook for problem 29 (Get flag image URL)"""
    # Create a new notebook
    nb = nbf.v4.new_notebook()
    
    # Add cells
    nb['cells'] = [
        nbf.v4.new_markdown_cell('# 29. 国旗画像のURLを取得する\n\nテンプレートの内容を利用し，国旗画像のURLを取得せよ．（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）'),
        nbf.v4.new_code_cell('# 問題29: 国旗画像のURLを取得する\n\nimport os\nimport re\nimport requests\n\n# イギリスの記事ファイルのパス\ndata_dir = "../data"\nuk_article_file = os.path.join(data_dir, "uk_article.txt")\n\n# 基礎情報テンプレートのフィールド名と値を抽出する関数（問題25の関数）\ndef extract_basic_info_template(text):\n    """記事から基礎情報テンプレートのフィールド名と値を抽出する関数"""\n    # 基礎情報テンプレートの抽出\n    template_pattern = r"\\{\\{基礎情報[^|]*?\\|([\\s\\S]*?)\\}\\}"\n    template_match = re.search(template_pattern, text)\n    \n    if not template_match:\n        return {}\n    \n    template_content = template_match.group(1)\n    \n    # フィールドの抽出（行ごとに処理）\n    basic_info = {}\n    field_name = None\n    field_value = []\n    \n    for line in template_content.split("\\n"):\n        # 新しいフィールドの開始\n        field_match = re.match(r"\\|\\s*([^=]+?)\\s*=\\s*(.*)", line)\n        if field_match:\n            # 前のフィールドがあれば保存\n            if field_name is not None:\n                basic_info[field_name] = "\\n".join(field_value).strip()\n            \n            # 新しいフィールドの開始\n            field_name = field_match.group(1).strip()\n            field_value = [field_match.group(2).strip()]\n        else:\n            # 現在のフィールドの値の続き\n            if field_name is not None:\n                field_value.append(line.strip())\n    \n    # 最後のフィールドを保存\n    if field_name is not None:\n        basic_info[field_name] = "\\n".join(field_value).strip()\n    \n    return basic_info'),
        nbf.v4.new_code_cell('# 国旗画像のファイル名を抽出する関数\ndef extract_flag_filename(basic_info):\n    """基礎情報テンプレートから国旗画像のファイル名を抽出する関数"""\n    # 国旗画像のフィールド名（「国旗画像」または「旗画像」）\n    flag_field_names = ["国旗画像", "旗画像"]\n    \n    # 国旗画像のフィールドを探す\n    flag_filename = None\n    for field_name in flag_field_names:\n        if field_name in basic_info:\n            flag_filename = basic_info[field_name]\n            break\n    \n    return flag_filename\n\n# MediaWiki APIを使用して画像のURLを取得する関数\ndef get_image_url(filename):\n    """MediaWiki APIを使用して画像のURLを取得する関数"""\n    # ファイル名の先頭に「ファイル:」または「File:」がない場合は追加\n    if not filename.startswith(("ファイル:", "File:")):\n        filename = "File:" + filename\n    \n    # MediaWiki APIのエンドポイント\n    api_url = "https://ja.wikipedia.org/w/api.php"\n    \n    # APIリクエストのパラメータ\n    params = {\n        "action": "query",\n        "format": "json",\n        "prop": "imageinfo",\n        "titles": filename,\n        "iiprop": "url"\n    }\n    \n    try:\n        # APIリクエストを送信\n        response = requests.get(api_url, params=params)\n        data = response.json()\n        \n        # レスポンスから画像のURLを抽出\n        pages = data["query"]["pages"]\n        for page_id in pages:\n            if "imageinfo" in pages[page_id]:\n                return pages[page_id]["imageinfo"][0]["url"]\n        \n        return None\n    except Exception as e:\n        print(f"APIリクエストでエラーが発生しました: {e}")\n        return None'),
        nbf.v4.new_code_cell('# メイン処理\ntry:\n    # イギリスの記事を読み込む\n    if os.path.exists(uk_article_file):\n        with open(uk_article_file, "r", encoding="utf-8") as f:\n            uk_article = f.read()\n        \n        # 基礎情報テンプレートのフィールド名と値を抽出\n        basic_info = extract_basic_info_template(uk_article)\n        \n        # 国旗画像のファイル名を抽出\n        flag_filename = extract_flag_filename(basic_info)\n        \n        if flag_filename:\n            print(f"国旗画像のファイル名: {flag_filename}")\n            \n            # 国旗画像のURLを取得\n            flag_url = get_image_url(flag_filename)\n            \n            if flag_url:\n                print(f"国旗画像のURL: {flag_url}")\n            else:\n                print("国旗画像のURLを取得できませんでした。")\n        else:\n            print("国旗画像のファイル名を抽出できませんでした。")\n    else:\n        print(f"イギリスの記事ファイルが見つかりません: {uk_article_file}")\n        print("問題20を先に実行して、イギリスの記事を抽出してください。")\n        \nexcept Exception as e:\n    print(f"エラーが発生しました: {e}")'),
        nbf.v4.new_markdown_cell('## 解説\n\nこの問題では、基礎情報テンプレートから国旗画像のファイル名を抽出し、MediaWiki APIを使用してその画像のURLを取得する方法を学びます。\n\n### MediaWiki APIとは\n\nMediaWiki APIは、WikipediaなどのMediaWikiベースのウェブサイトのコンテンツにプログラムからアクセスするためのインターフェースです。このAPIを使用することで、記事の内容、画像情報、編集履歴など、さまざまな情報を取得できます。\n\n### 国旗画像のURLを取得する手順\n\n1. **基礎情報テンプレートから国旗画像のファイル名を抽出する**\n   - 基礎情報テンプレートには、「国旗画像」または「旗画像」というフィールドに国旗の画像ファイル名が記載されています。\n\n2. **MediaWiki APIを使用して画像のURLを取得する**\n   - `action=query`と`prop=imageinfo`を使用して、画像の情報を取得します。\n   - `iiprop=url`パラメータを指定することで、画像のURLを取得できます。\n\n### 実装のポイント\n\n1. **APIリクエストの構築**\n   - APIエンドポイント（`https://ja.wikipedia.org/w/api.php`）に対して、適切なパラメータを指定してリクエストを送信します。\n\n2. **レスポンスの解析**\n   - APIからのレスポンスはJSON形式で返されるため、`json()`メソッドを使用して解析します。\n   - 画像情報は`pages`オブジェクト内の`imageinfo`配列に含まれています。\n\n3. **エラー処理**\n   - APIリクエストが失敗した場合や、画像情報が取得できなかった場合のエラー処理を実装します。\n\n### 注意点\n\n1. **ファイル名の形式**\n   - Wikipediaのファイル名は「ファイル:」または「File:」で始まる必要があります。抽出したファイル名にこのプレフィックスがない場合は追加する必要があります。\n\n2. **APIの利用制限**\n   - MediaWiki APIには利用制限があるため、大量のリクエストを短時間に送信すると制限される可能性があります。\n\n3. **画像の著作権**\n   - Wikipediaの画像には著作権があるため、利用する際は適切なライセンス表示が必要です。')
    ]
    
    # Set metadata
    nb['metadata'] = {
        'kernelspec': {
            'display_name': 'Python 3',
            'language': 'python',
            'name': 'python3'
        },
        'language_info': {
            'codemirror_mode': {
                'name': 'ipython',
                'version': 3
            },
            'file_extension': '.py',
            'mimetype': 'text/x-python',
            'name': 'python',
            'nbconvert_exporter': 'python',
            'pygments_lexer': 'ipython3',
            'version': '3.12.0'
        }
    }
    
    # Create directory if it doesn't exist
    os.makedirs('notebooks/chapter03', exist_ok=True)
    
    # Write the notebook to a file
    notebook_path = Path('notebooks/chapter03/29_flag_image_url.ipynb')
    with open(notebook_path, 'w', encoding='utf-8') as f:
        f.write(nbf.v4.writes(nb))
    
    print(f'Notebook created at {notebook_path}')

if __name__ == "__main__":
    create_notebook_29()
