import nbformat as nbf
import os
from pathlib import Path

def create_notebook_26():
    """Create notebook for problem 26 (Remove emphasis markup)"""
    # Create a new notebook
    nb = nbf.v4.new_notebook()
    
    # Add cells
    nb['cells'] = [
        nbf.v4.new_markdown_cell('# 26. 強調マークアップの除去\n\n25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強い強調，強い強調かつ斜体）を除去してテキストに変換せよ．'),
        nbf.v4.new_code_cell('# 問題26: 強調マークアップの除去\n\nimport os\nimport re\n\n# イギリスの記事ファイルのパス\ndata_dir = "../data"\nuk_article_file = os.path.join(data_dir, "uk_article.txt")\n\n# 基礎情報テンプレートのフィールド名と値を抽出する関数（問題25の改良版）\ndef extract_basic_info_template(text):\n    """記事から基礎情報テンプレートのフィールド名と値を抽出する関数\n    \n    Args:\n        text: 記事のテキスト\n        \n    Returns:\n        フィールド名と値の辞書\n    """\n    # 基礎情報テンプレートの抽出\n    template_pattern = r"\\{\\{基礎情報[^|]*?\\|([\\s\\S]*?)\\}\\}"\n    template_match = re.search(template_pattern, text)\n    \n    if not template_match:\n        return {}\n    \n    template_content = template_match.group(1)\n    \n    # フィールドの抽出（行ごとに処理）\n    basic_info = {}\n    field_name = None\n    field_value = []\n    \n    for line in template_content.split("\\n"):\n        # 新しいフィールドの開始\n        field_match = re.match(r"\\|\\s*([^=]+?)\\s*=\\s*(.*)", line)\n        if field_match:\n            # 前のフィールドがあれば保存\n            if field_name is not None:\n                basic_info[field_name] = "\\n".join(field_value).strip()\n            \n            # 新しいフィールドの開始\n            field_name = field_match.group(1).strip()\n            field_value = [field_match.group(2).strip()]\n        else:\n            # 現在のフィールドの値の続き\n            if field_name is not None:\n                field_value.append(line.strip())\n    \n    # 最後のフィールドを保存\n    if field_name is not None:\n        basic_info[field_name] = "\\n".join(field_value).strip()\n    \n    return basic_info\n\n# 強調マークアップを除去する関数\ndef remove_emphasis_markup(text):\n    """MediaWikiの強調マークアップを除去する関数\n    \n    Args:\n        text: 強調マークアップを含むテキスト\n        \n    Returns:\n        強調マークアップを除去したテキスト\n    """\n    # 強い強調かつ斜体（5つのアポストロフィ）\n    text = re.sub(r"\'\'\'\'\'(.+?)\'\'\'\'\'", r"\\1", text)\n    \n    # 強い強調（3つのアポストロフィ）\n    text = re.sub(r"\'\'\'(.+?)\'\'\'", r"\\1", text)\n    \n    # 弱い強調（2つのアポストロフィ）\n    text = re.sub(r"\'\'(.+?)\'\'", r"\\1", text)\n    \n    return text\n\n# 基礎情報テンプレートから強調マークアップを除去する関数\ndef remove_emphasis_from_template(basic_info):\n    """基礎情報テンプレートの値から強調マークアップを除去する関数\n    \n    Args:\n        basic_info: 基礎情報テンプレートの辞書\n        \n    Returns:\n        強調マークアップを除去した基礎情報テンプレートの辞書\n    """\n    cleaned_info = {}\n    for name, value in basic_info.items():\n        cleaned_info[name] = remove_emphasis_markup(value)\n    \n    return cleaned_info\n\n# メイン処理\ntry:\n    # イギリスの記事を読み込む\n    if os.path.exists(uk_article_file):\n        with open(uk_article_file, "r", encoding="utf-8") as f:\n            uk_article = f.read()\n        \n        # 基礎情報テンプレートのフィールド名と値を抽出\n        basic_info = extract_basic_info_template(uk_article)\n        \n        # 強調マークアップを除去\n        cleaned_info = remove_emphasis_from_template(basic_info)\n        \n        # 結果を表示\n        print(f"基礎情報テンプレートのフィールド数: {len(cleaned_info)}\\n")\n        print("強調マークアップを除去した基礎情報テンプレートの内容（一部）:")\n        \n        # 変更があったフィールドを表示\n        changes_found = False\n        for name, value in cleaned_info.items():\n            if value != basic_info[name]:\n                changes_found = True\n                print(f"\\n【フィールド名】{name}")\n                print(f"【変更前】{basic_info[name][:100]}..." if len(basic_info[name]) > 100 else f"【変更前】{basic_info[name]}")\n                print(f"【変更後】{value[:100]}..." if len(value) > 100 else f"【変更後】{value}")\n        \n        if not changes_found:\n            print("強調マークアップが含まれているフィールドはありませんでした。")\n    else:\n        print(f"イギリスの記事ファイルが見つかりません: {uk_article_file}")\n        print("問題20を先に実行して、イギリスの記事を抽出してください。")\n        \nexcept Exception as e:\n    print(f"エラーが発生しました: {e}")'),
        nbf.v4.new_code_cell('# 強調マークアップの例を示す\n\ndef show_emphasis_markup_examples():\n    """強調マークアップの例を示す関数"""\n    examples = [\n        "これは\'\'弱い強調\'\'の例です。",\n        "これは\'\'\'強い強調\'\'\'の例です。",\n        "これは\'\'\'\'\'強い強調かつ斜体\'\'\'\'\'の例です。",\n        "これは\'\'弱い強調\'\'と\'\'\'強い強調\'\'\'が混在する例です。",\n        "これは\'\'\'\'\'強い強調かつ斜体\'\'\'\'\'と\'\'弱い強調\'\'と\'\'\'強い強調\'\'\'が混在する例です。"\n    ]\n    \n    print("強調マークアップの例:")\n    for i, example in enumerate(examples):\n        print(f"\\n例{i+1}:")\n        print(f"変更前: {example}")\n        print(f"変更後: {remove_emphasis_markup(example)}")\n\n# 強調マークアップの例を示す\nshow_emphasis_markup_examples()'),
        nbf.v4.new_markdown_cell('## 解説\n\nこの問題では、基礎情報テンプレートの値からMediaWikiの強調マークアップを除去する方法を学びます。\n\n### MediaWikiの強調マークアップ\n\nMediaWikiでは、以下の3種類の強調マークアップが使用されています：\n\n1. **弱い強調**：`\'\'テキスト\'\'`（2つのアポストロフィで囲む）\n   - HTMLでは `<i>テキスト</i>` に変換され、通常は斜体で表示されます。\n\n2. **強い強調**：`\'\'\'テキスト\'\'\'`（3つのアポストロフィで囲む）\n   - HTMLでは `<b>テキスト</b>` に変換され、通常は太字で表示されます。\n\n3. **強い強調かつ斜体**：`\'\'\'\'\'テキスト\'\'\'\'\'`（5つのアポストロフィで囲む）\n   - HTMLでは `<b><i>テキスト</i></b>` に変換され、通常は太字かつ斜体で表示されます。\n\n### 強調マークアップの除去\n\n正規表現を使用して、強調マークアップを除去します。除去の順序は重要で、最も長いパターン（5つのアポストロフィ）から順に処理します。\n\n```python\n# 強い強調かつ斜体（5つのアポストロフィ）\ntext = re.sub(r"\'\'\'\'\'(.+?)\'\'\'\'\'", r"\\1", text)\n\n# 強い強調（3つのアポストロフィ）\ntext = re.sub(r"\'\'\'(.+?)\'\'\'", r"\\1", text)\n\n# 弱い強調（2つのアポストロフィ）\ntext = re.sub(r"\'\'(.+?)\'\'", r"\\1", text)\n```\n\n### 正規表現の解説\n\n- `r"\'\'\'\'\'(.+?)\'\'\'\'\'"`：\n  - 5つのアポストロフィにマッチ\n  - 1つ以上の任意の文字にマッチし、非貪欲（non-greedy）でグループ化\n  - 5つのアポストロフィにマッチ\n\n- `r"\'\'\'(.+?)\'\'\'"`：\n  - 3つのアポストロフィにマッチ\n  - 1つ以上の任意の文字にマッチし、非貪欲でグループ化\n  - 3つのアポストロフィにマッチ\n\n- `r"\'\'(.+?)\'\'"`：\n  - 2つのアポストロフィにマッチ\n  - 1つ以上の任意の文字にマッチし、非貪欲でグループ化\n  - 2つのアポストロフィにマッチ\n\n### 注意点\n\n- 正規表現の `(.+?)` は非貪欲（non-greedy）マッチングを行います。これにより、最初のマッチングで終了します。\n- 強調マークアップが入れ子になっている場合（例：`\'\'\'\'\'テキスト\'\'\'\'\'` の中に `\'\'テキスト\'\'` がある場合）、複数回の置換が必要になることがあります。\n- 実際のWikipediaの記事では、強調マークアップが複雑に組み合わされている場合があります。')
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
    notebook_path = Path('notebooks/chapter03/26_remove_emphasis.ipynb')
    with open(notebook_path, 'w', encoding='utf-8') as f:
        f.write(nbf.v4.writes(nb))
    
    print(f'Notebook created at {notebook_path}')

def create_notebook_27():
    """Create notebook for problem 27 (Remove internal links)"""
    # Create a new notebook
    nb = nbf.v4.new_notebook()
    
    # Add cells
    nb['cells'] = [
        nbf.v4.new_markdown_cell('# 27. 内部リンクの除去\n\n26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ．'),
        nbf.v4.new_code_cell('# 問題27: 内部リンクの除去\n\nimport os\nimport re\n\n# イギリスの記事ファイルのパス\ndata_dir = "../data"\nuk_article_file = os.path.join(data_dir, "uk_article.txt")\n\n# 基礎情報テンプレートのフィールド名と値を抽出する関数（問題25の改良版）\ndef extract_basic_info_template(text):\n    """記事から基礎情報テンプレートのフィールド名と値を抽出する関数\n    \n    Args:\n        text: 記事のテキスト\n        \n    Returns:\n        フィールド名と値の辞書\n    """\n    # 基礎情報テンプレートの抽出\n    template_pattern = r"\\{\\{基礎情報[^|]*?\\|([\\s\\S]*?)\\}\\}"\n    template_match = re.search(template_pattern, text)\n    \n    if not template_match:\n        return {}\n    \n    template_content = template_match.group(1)\n    \n    # フィールドの抽出（行ごとに処理）\n    basic_info = {}\n    field_name = None\n    field_value = []\n    \n    for line in template_content.split("\\n"):\n        # 新しいフィールドの開始\n        field_match = re.match(r"\\|\\s*([^=]+?)\\s*=\\s*(.*)", line)\n        if field_match:\n            # 前のフィールドがあれば保存\n            if field_name is not None:\n                basic_info[field_name] = "\\n".join(field_value).strip()\n            \n            # 新しいフィールドの開始\n            field_name = field_match.group(1).strip()\n            field_value = [field_match.group(2).strip()]\n        else:\n            # 現在のフィールドの値の続き\n            if field_name is not None:\n                field_value.append(line.strip())\n    \n    # 最後のフィールドを保存\n    if field_name is not None:\n        basic_info[field_name] = "\\n".join(field_value).strip()\n    \n    return basic_info\n\n# 強調マークアップを除去する関数（問題26の関数）\ndef remove_emphasis_markup(text):\n    """MediaWikiの強調マークアップを除去する関数\n    \n    Args:\n        text: 強調マークアップを含むテキスト\n        \n    Returns:\n        強調マークアップを除去したテキスト\n    """\n    # 強い強調かつ斜体（5つのアポストロフィ）\n    text = re.sub(r"\'\'\'\'\'(.+?)\'\'\'\'\'", r"\\1", text)\n    \n    # 強い強調（3つのアポストロフィ）\n    text = re.sub(r"\'\'\'(.+?)\'\'\'", r"\\1", text)\n    \n    # 弱い強調（2つのアポストロフィ）\n    text = re.sub(r"\'\'(.+?)\'\'", r"\\1", text)\n    \n    return text\n\n# 内部リンクマークアップを除去する関数\ndef remove_internal_links(text):\n    """MediaWikiの内部リンクマークアップを除去する関数\n    \n    Args:\n        text: 内部リンクマークアップを含むテキスト\n        \n    Returns:\n        内部リンクマークアップを除去したテキスト\n    """\n    # パターン1: [[リンク先|表示テキスト]] → 表示テキスト\n    text = re.sub(r"\\[\\[(?:[^|\\]]+)\\|([^\\]]+)\\]\\]", r"\\1", text)\n    \n    # パターン2: [[リンク先]] → リンク先\n    text = re.sub(r"\\[\\[([^\\]]+)\\]\\]", r"\\1", text)\n    \n    return text\n\n# マークアップを除去する関数（強調マークアップと内部リンクの両方）\ndef remove_markup(text):\n    """MediaWikiのマークアップ（強調と内部リンク）を除去する関数\n    \n    Args:\n        text: マークアップを含むテキスト\n        \n    Returns:\n        マークアップを除去したテキスト\n    """\n    # 強調マークアップを除去\n    text = remove_emphasis_markup(text)\n    \n    # 内部リンクマークアップを除去\n    text = remove_internal_links(text)\n    \n    return text\n\n# 基礎情報テンプレートからマークアップを除去する関数\ndef remove_markup_from_template(basic_info):\n    """基礎情報テンプレートの値からマークアップを除去する関数\n    \n    Args:\n        basic_info: 基礎情報テンプレートの辞書\n        \n    Returns:\n        マークアップを除去した基礎情報テンプレートの辞書\n    """\n    cleaned_info = {}\n    for name, value in basic_info.items():\n        cleaned_info[name] = remove_markup(value)\n    \n    return cleaned_info\n\n# メイン処理\ntry:\n    # イギリスの記事を読み込む\n    if os.path.exists(uk_article_file):\n        with open(uk_article_file, "r", encoding="utf-8") as f:\n            uk_article = f.read()\n        \n        # 基礎情報テンプレートのフィールド名と値を抽出\n        basic_info = extract_basic_info_template(uk_article)\n        \n        # マークアップを除去\n        cleaned_info = remove_markup_from_template(basic_info)\n        \n        # 結果を表示\n        print(f"基礎情報テンプレートのフィールド数: {len(cleaned_info)}\\n")\n        print("マークアップを除去した基礎情報テンプレートの内容（一部）:")\n        \n        # 変更があったフィールドを表示\n        changes_found = False\n        for name, value in cleaned_info.items():\n            if value != basic_info[name]:\n                changes_found = True\n                print(f"\\n【フィールド名】{name}")\n                print(f"【変更前】{basic_info[name][:100]}..." if len(basic_info[name]) > 100 else f"【変更前】{basic_info[name]}")\n                print(f"【変更後】{value[:100]}..." if len(value) > 100 else f"【変更後】{value}")\n        \n        if not changes_found:\n            print("マークアップが含まれているフィールドはありませんでした。")\n    else:\n        print(f"イギリスの記事ファイルが見つかりません: {uk_article_file}")\n        print("問題20を先に実行して、イギリスの記事を抽出してください。")\n        \nexcept Exception as e:\n    print(f"エラーが発生しました: {e}")'),
        nbf.v4.new_code_cell('# 内部リンクマークアップの例を示す\n\ndef show_internal_link_examples():\n    """内部リンクマークアップの例を示す関数"""\n    examples = [\n        "[[イギリス]]は島国である。",\n        "[[イギリス|英国]]は島国である。",\n        "[[ロンドン]]は[[イギリス|英国]]の首都である。",\n        "[[ヨーロッパ]]の[[イギリス]]は[[イギリス連邦]]の中心国である。",\n        "[[イギリス女王|女王]]\'\'エリザベス2世\'\'は\'\'\'長寿\'\'\'である。"\n    ]\n    \n    print("内部リンクマークアップの例:")\n    for i, example in enumerate(examples):\n        print(f"\\n例{i+1}:")\n        print(f"変更前: {example}")\n        print(f"内部リンクのみ除去: {remove_internal_links(example)}")\n        print(f"強調マークアップのみ除去: {remove_emphasis_markup(example)}")\n        print(f"両方除去: {remove_markup(example)}")\n\n# 内部リンクマークアップの例を示す\nshow_internal_link_examples()'),
        nbf.v4.new_markdown_cell('## 解説\n\nこの問題では、前の問題（問題26）で実装した強調マークアップの除去に加えて、内部リンクマークアップも除去する方法を学びます。\n\n### MediaWikiの内部リンクマークアップ\n\nMediaWikiでは、内部リンク（同じWiki内の他のページへのリンク）は以下の形式で記述されます：\n\n1. **基本形式**：`[[リンク先]]`\n   - 例：`[[イギリス]]` → 「イギリス」というテキストが表示され、「イギリス」のページへのリンクになります。\n\n2. **表示テキスト指定形式**：`[[リンク先|表示テキスト]]`\n   - 例：`[[イギリス|英国]]` → 「英国」というテキストが表示され、「イギリス」のページへのリンクになります。\n\n### 内部リンクマークアップの除去\n\n正規表現を使用して、内部リンクマークアップを除去します。2つのパターンを順に処理します。\n\n```python\n# パターン1: [[リンク先|表示テキスト]] → 表示テキスト\ntext = re.sub(r"\\[\\[(?:[^|\\]]+)\\|([^\\]]+)\\]\\]", r"\\1", text)\n\n# パターン2: [[リンク先]] → リンク先\ntext = re.sub(r"\\[\\[([^\\]]+)\\]\\]", r"\\1", text)\n```\n\n### 正規表現の解説\n\n- `r"\\[\\[(?:[^|\\]]+)\\|([^\\]]+)\\]\\]"`：\n  - `\\[\\[` : 文字列 `[[` にマッチ\n  - `(?:[^|\\]]+)` : パイプ記号（`|`）または閉じ括弧（`]`）以外の1つ以上の文字にマッチし、グループ化しない（`?:`）\n  - `\\|` : パイプ記号（`|`）にマッチ\n  - `([^\\]]+)` : 閉じ括弧（`]`）以外の1つ以上の文字にマッチし、グループ化（`()`）\n  - `\\]\\]` : 文字列 `]]` にマッチ\n\n- `r"\\[\\[([^\\]]+)\\]\\]"`：\n  - `\\[\\[` : 文字列 `[[` にマッチ\n  - `([^\\]]+)` : 閉じ括弧（`]`）以外の1つ以上の文字にマッチし、グループ化（`()`）\n  - `\\]\\]` : 文字列 `]]` にマッチ\n\n### 処理の順序\n\n内部リンクマークアップの除去と強調マークアップの除去を組み合わせる場合、どちらを先に処理しても結果は同じになります。ただし、実際のWikipediaの記事では、内部リンクと強調マークアップが入れ子になっている場合があるため、両方の処理を行うことが重要です。\n\n### 注意点\n\n- 内部リンクの中に強調マークアップが含まれている場合や、強調マークアップの中に内部リンクが含まれている場合があります。\n- 実際のWikipediaの記事では、より複雑なリンク形式（例：`[[リンク先#セクション|表示テキスト]]`）が使用されることがあります。\n- カテゴリリンク（`[[Category:カテゴリ名]]`）やファイルリンク（`[[File:ファイル名]]`）など、特殊なリンク形式もあります。')
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
    notebook_path = Path('notebooks/chapter03/27_remove_internal_links.ipynb')
    with open(notebook_path, 'w', encoding='utf-8') as f:
        f.write(nbf.v4.writes(nb))
    
    print(f'Notebook created at {notebook_path}')

if __name__ == "__main__":
    create_notebook_26()
    create_notebook_27()
