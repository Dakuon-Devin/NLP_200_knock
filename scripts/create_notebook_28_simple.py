import nbformat as nbf
import os
from pathlib import Path

def create_notebook_28():
    """Create notebook for problem 28 (Remove MediaWiki markup)"""
    # Create a new notebook
    nb = nbf.v4.new_notebook()
    
    # Add cells - simplified version with fewer cells to avoid size issues
    nb['cells'] = [
        nbf.v4.new_markdown_cell('# 28. MediaWikiマークアップの除去\n\n27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．'),
        nbf.v4.new_code_cell('# 問題28: MediaWikiマークアップの除去\n\nimport os\nimport re\n\n# イギリスの記事ファイルのパス\ndata_dir = "../data"\nuk_article_file = os.path.join(data_dir, "uk_article.txt")\n\n# 基礎情報テンプレートのフィールド名と値を抽出する関数（問題25の改良版）\ndef extract_basic_info_template(text):\n    """記事から基礎情報テンプレートのフィールド名と値を抽出する関数"""\n    # 基礎情報テンプレートの抽出\n    template_pattern = r"\\{\\{基礎情報[^|]*?\\|([\\s\\S]*?)\\}\\}"\n    template_match = re.search(template_pattern, text)\n    \n    if not template_match:\n        return {}\n    \n    template_content = template_match.group(1)\n    \n    # フィールドの抽出（行ごとに処理）\n    basic_info = {}\n    field_name = None\n    field_value = []\n    \n    for line in template_content.split("\\n"):\n        # 新しいフィールドの開始\n        field_match = re.match(r"\\|\\s*([^=]+?)\\s*=\\s*(.*)", line)\n        if field_match:\n            # 前のフィールドがあれば保存\n            if field_name is not None:\n                basic_info[field_name] = "\\n".join(field_value).strip()\n            \n            # 新しいフィールドの開始\n            field_name = field_match.group(1).strip()\n            field_value = [field_match.group(2).strip()]\n        else:\n            # 現在のフィールドの値の続き\n            if field_name is not None:\n                field_value.append(line.strip())\n    \n    # 最後のフィールドを保存\n    if field_name is not None:\n        basic_info[field_name] = "\\n".join(field_value).strip()\n    \n    return basic_info'),
        nbf.v4.new_code_cell('# マークアップ除去関数群\n\n# 強調マークアップを除去する関数\ndef remove_emphasis_markup(text):\n    """MediaWikiの強調マークアップを除去する関数"""\n    # 強い強調かつ斜体（5つのアポストロフィ）\n    text = re.sub(r"\'\'\'\'\'(.+?)\'\'\'\'\'", r"\\1", text)\n    # 強い強調（3つのアポストロフィ）\n    text = re.sub(r"\'\'\'(.+?)\'\'\'", r"\\1", text)\n    # 弱い強調（2つのアポストロフィ）\n    text = re.sub(r"\'\'(.+?)\'\'", r"\\1", text)\n    return text\n\n# 内部リンクマークアップを除去する関数\ndef remove_internal_links(text):\n    """MediaWikiの内部リンクマークアップを除去する関数"""\n    # パターン1: [[リンク先|表示テキスト]] → 表示テキスト\n    text = re.sub(r"\\[\\[(?:[^|\\]]+)\\|([^\\]]+)\\]\\]", r"\\1", text)\n    # パターン2: [[リンク先]] → リンク先\n    text = re.sub(r"\\[\\[([^\\]]+)\\]\\]", r"\\1", text)\n    return text\n\n# 外部リンクマークアップを除去する関数\ndef remove_external_links(text):\n    """MediaWikiの外部リンクマークアップを除去する関数"""\n    # パターン1: [URL 表示テキスト] → 表示テキスト\n    text = re.sub(r"\\[(?:https?|ftp)://[^\\s\\]]+\\s+([^\\]]+)\\]", r"\\1", text)\n    # パターン2: [URL] → URL\n    text = re.sub(r"\\[((?:https?|ftp)://[^\\s\\]]+)\\]", r"\\1", text)\n    return text\n\n# HTMLタグを除去する関数\ndef remove_html_tags(text):\n    """HTMLタグを除去する関数"""\n    # HTMLタグ: <タグ>内容</タグ> → 内容\n    text = re.sub(r"<[^>]+>([^<]*)</[^>]+>", r"\\1", text)\n    # 単独のHTMLタグ: <タグ /> → 空文字列\n    text = re.sub(r"<[^>]+/>", "", text)\n    # その他のHTMLタグ: <タグ> → 空文字列\n    text = re.sub(r"<[^>]+>", "", text)\n    return text\n\n# 参照タグを除去する関数\ndef remove_ref_tags(text):\n    """参照タグを除去する関数"""\n    # パターン1: <ref>内容</ref> → 空文字列\n    text = re.sub(r"<ref[^>]*>.*?</ref>", "", text)\n    # パターン2: <ref name="名前" /> → 空文字列\n    text = re.sub(r"<ref[^/>]*/>", "", text)\n    return text\n\n# コメントを除去する関数\ndef remove_comments(text):\n    """コメントを除去する関数"""\n    # コメント: <!-- コメント --> → 空文字列\n    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)\n    return text\n\n# テンプレート呼び出しを除去する関数\ndef remove_template_calls(text):\n    """テンプレート呼び出しを除去する関数"""\n    # 単純なテンプレート: {{テンプレート名}} → 空文字列\n    text = re.sub(r"\\{\\{[^|{}]*\\}\\}", "", text)\n    # パラメータ付きテンプレート: {{テンプレート名|パラメータ}} → 空文字列\n    text = re.sub(r"\\{\\{[^{}]*\\}\\}", "", text)\n    return text'),
        nbf.v4.new_code_cell('# すべてのマークアップを除去する関数\ndef remove_all_markup(text):\n    """すべてのMediaWikiマークアップを除去する関数"""\n    # コメントを除去\n    text = remove_comments(text)\n    # 参照タグを除去\n    text = remove_ref_tags(text)\n    # HTMLタグを除去\n    text = remove_html_tags(text)\n    # 外部リンクマークアップを除去\n    text = remove_external_links(text)\n    # 内部リンクマークアップを除去\n    text = remove_internal_links(text)\n    # 強調マークアップを除去\n    text = remove_emphasis_markup(text)\n    # テンプレート呼び出しを除去\n    text = remove_template_calls(text)\n    # 連続する空白を1つの空白に置換\n    text = re.sub(r"\\s+", " ", text)\n    # 前後の空白を削除\n    text = text.strip()\n    return text\n\n# 基礎情報テンプレートからマークアップを除去する関数\ndef remove_markup_from_template(basic_info):\n    """基礎情報テンプレートの値からマークアップを除去する関数"""\n    cleaned_info = {}\n    for name, value in basic_info.items():\n        cleaned_info[name] = remove_all_markup(value)\n    return cleaned_info\n\n# メイン処理\ntry:\n    # イギリスの記事を読み込む\n    if os.path.exists(uk_article_file):\n        with open(uk_article_file, "r", encoding="utf-8") as f:\n            uk_article = f.read()\n        \n        # 基礎情報テンプレートのフィールド名と値を抽出\n        basic_info = extract_basic_info_template(uk_article)\n        \n        # マークアップを除去\n        cleaned_info = remove_markup_from_template(basic_info)\n        \n        # 結果を表示\n        print(f"基礎情報テンプレートのフィールド数: {len(cleaned_info)}\\n")\n        print("マークアップを除去した基礎情報テンプレートの内容:")\n        \n        # 変更があったフィールドを表示\n        for name, value in cleaned_info.items():\n            print(f"\\n【フィールド名】{name}")\n            print(f"【変更前】{basic_info[name][:100]}..." if len(basic_info[name]) > 100 else f"【変更前】{basic_info[name]}")\n            print(f"【変更後】{value[:100]}..." if len(value) > 100 else f"【変更後】{value}")\n    else:\n        print(f"イギリスの記事ファイルが見つかりません: {uk_article_file}")\n        print("問題20を先に実行して、イギリスの記事を抽出してください。")\n        \nexcept Exception as e:\n    print(f"エラーが発生しました: {e}")'),
        nbf.v4.new_markdown_cell('## 解説\n\nこの問題では、前の問題（問題26と問題27）で実装した強調マークアップと内部リンクマークアップの除去に加えて、その他のMediaWikiマークアップも可能な限り除去する方法を学びます。\n\n### MediaWikiのマークアップの種類\n\nMediaWikiには、以下のようなさまざまなマークアップが存在します：\n\n1. **強調マークアップ**（問題26で対応）\n   - 弱い強調（`\'\'テキスト\'\'`）\n   - 強い強調（`\'\'\'テキスト\'\'\'`）\n   - 強い強調かつ斜体（`\'\'\'\'\'テキスト\'\'\'\'\'`）\n\n2. **内部リンクマークアップ**（問題27で対応）\n   - 基本形式（`[[リンク先]]`）\n   - 表示テキスト指定形式（`[[リンク先|表示テキスト]]`）\n\n3. **外部リンクマークアップ**\n   - 基本形式（`[URL]`）\n   - 表示テキスト指定形式（`[URL 表示テキスト]`）\n\n4. **HTMLタグ**\n   - 開始タグと終了タグのペア（`<タグ>内容</タグ>`）\n   - 単独のタグ（`<タグ />`）\n\n5. **参照タグ**\n   - 基本形式（`<ref>内容</ref>`）\n   - 名前付き参照（`<ref name="名前">内容</ref>`）\n   - 参照の再利用（`<ref name="名前" />`）\n\n6. **テンプレート呼び出し**\n   - 基本形式（`{{テンプレート名}}`）\n   - パラメータ付き（`{{テンプレート名|パラメータ}}`）\n\n### マークアップ除去の実装\n\nこれらのマークアップを除去するために、それぞれに対応する関数を実装し、最終的にすべての関数を組み合わせて使用します。処理の順序は重要です。例えば、コメントや参照タグは他のマークアップを含んでいる可能性があるため、先に除去する必要があります。')
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
    notebook_path = Path('notebooks/chapter03/28_remove_mediawiki_markup.ipynb')
    with open(notebook_path, 'w', encoding='utf-8') as f:
        f.write(nbf.v4.writes(nb))
    
    print(f'Notebook created at {notebook_path}')

if __name__ == "__main__":
    create_notebook_28()
