import nbformat as nbf
import os
from pathlib import Path

def create_notebook_26():
    """Create notebook for problem 26 (Remove emphasis markup)"""
    # Create a new notebook
    nb = nbf.v4.new_notebook()
    
    # Add cells
    cells = []
    
    # Add markdown cell for problem description
    cells.append(nbf.v4.new_markdown_cell('# 26. 強調マークアップの除去\n\n25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強い強調，強い強調かつ斜体）を除去してテキストに変換せよ．'))
    
    # Add code cell for solution
    cells.append(nbf.v4.new_code_cell('''# 問題26: 強調マークアップの除去

import os
import re

# イギリスの記事ファイルのパス
data_dir = "../data"
uk_article_file = os.path.join(data_dir, "uk_article.txt")

# 基礎情報テンプレートのフィールド名と値を抽出する関数（問題25の改良版）
def extract_basic_info_template(text):
    """記事から基礎情報テンプレートのフィールド名と値を抽出する関数
    
    Args:
        text: 記事のテキスト
        
    Returns:
        フィールド名と値の辞書
    """
    # 基礎情報テンプレートの抽出
    template_pattern = r"\\{\\{基礎情報[^|]*?\\|([\\s\\S]*?)\\}\\}"
    template_match = re.search(template_pattern, text)
    
    if not template_match:
        return {}
    
    template_content = template_match.group(1)
    
    # フィールドの抽出（行ごとに処理）
    basic_info = {}
    field_name = None
    field_value = []
    
    for line in template_content.split("\\n"):
        # 新しいフィールドの開始
        field_match = re.match(r"\\|\\s*([^=]+?)\\s*=\\s*(.*)", line)
        if field_match:
            # 前のフィールドがあれば保存
            if field_name is not None:
                basic_info[field_name] = "\\n".join(field_value).strip()
            
            # 新しいフィールドの開始
            field_name = field_match.group(1).strip()
            field_value = [field_match.group(2).strip()]
        else:
            # 現在のフィールドの値の続き
            if field_name is not None:
                field_value.append(line.strip())
    
    # 最後のフィールドを保存
    if field_name is not None:
        basic_info[field_name] = "\\n".join(field_value).strip()
    
    return basic_info

# 強調マークアップを除去する関数
def remove_emphasis_markup(text):
    """MediaWikiの強調マークアップを除去する関数
    
    Args:
        text: 強調マークアップを含むテキスト
        
    Returns:
        強調マークアップを除去したテキスト
    """
    # 強い強調かつ斜体（5つのアポストロフィ）
    text = re.sub(r"\'\'\'\'\'(.+?)\'\'\'\'\'", r"\\1", text)
    
    # 強い強調（3つのアポストロフィ）
    text = re.sub(r"\'\'\'(.+?)\'\'\'", r"\\1", text)
    
    # 弱い強調（2つのアポストロフィ）
    text = re.sub(r"\'\'(.+?)\'\'", r"\\1", text)
    
    return text

# 基礎情報テンプレートから強調マークアップを除去する関数
def remove_emphasis_from_template(basic_info):
    """基礎情報テンプレートの値から強調マークアップを除去する関数
    
    Args:
        basic_info: 基礎情報テンプレートの辞書
        
    Returns:
        強調マークアップを除去した基礎情報テンプレートの辞書
    """
    cleaned_info = {}
    for name, value in basic_info.items():
        cleaned_info[name] = remove_emphasis_markup(value)
    
    return cleaned_info

# メイン処理
try:
    # イギリスの記事を読み込む
    if os.path.exists(uk_article_file):
        with open(uk_article_file, "r", encoding="utf-8") as f:
            uk_article = f.read()
        
        # 基礎情報テンプレートのフィールド名と値を抽出
        basic_info = extract_basic_info_template(uk_article)
        
        # 強調マークアップを除去
        cleaned_info = remove_emphasis_from_template(basic_info)
        
        # 結果を表示
        print(f"基礎情報テンプレートのフィールド数: {len(cleaned_info)}\\n")
        print("強調マークアップを除去した基礎情報テンプレートの内容（一部）:")
        
        # 変更があったフィールドを表示
        changes_found = False
        for name, value in cleaned_info.items():
            if value != basic_info[name]:
                changes_found = True
                print(f"\\n【フィールド名】{name}")
                print(f"【変更前】{basic_info[name][:100]}..." if len(basic_info[name]) > 100 else f"【変更前】{basic_info[name]}")
                print(f"【変更後】{value[:100]}..." if len(value) > 100 else f"【変更後】{value}")
        
        if not changes_found:
            print("強調マークアップが含まれているフィールドはありませんでした。")
    else:
        print(f"イギリスの記事ファイルが見つかりません: {uk_article_file}")
        print("問題20を先に実行して、イギリスの記事を抽出してください。")
        
except Exception as e:
    print(f"エラーが発生しました: {e}")'''))
    
    # Add code cell for examples
    cells.append(nbf.v4.new_code_cell('''# 強調マークアップの例を示す

def show_emphasis_markup_examples():
    """強調マークアップの例を示す関数"""
    examples = [
        "これは\'\'弱い強調\'\'の例です。",
        "これは\'\'\'強い強調\'\'\'の例です。",
        "これは\'\'\'\'\'強い強調かつ斜体\'\'\'\'\'の例です。",
        "これは\'\'弱い強調\'\'と\'\'\'強い強調\'\'\'が混在する例です。",
        "これは\'\'\'\'\'強い強調かつ斜体\'\'\'\'\'と\'\'弱い強調\'\'と\'\'\'強い強調\'\'\'が混在する例です。"
    ]
    
    print("強調マークアップの例:")
    for i, example in enumerate(examples):
        print(f"\\n例{i+1}:")
        print(f"変更前: {example}")
        print(f"変更後: {remove_emphasis_markup(example)}")

# 強調マークアップの例を示す
show_emphasis_markup_examples()'''))
    
    # Add markdown cell for explanation
    cells.append(nbf.v4.new_markdown_cell('''## 解説

この問題では、基礎情報テンプレートの値からMediaWikiの強調マークアップを除去する方法を学びます。

### MediaWikiの強調マークアップ

MediaWikiでは、以下の3種類の強調マークアップが使用されています：

1. **弱い強調**：`''テキスト''`（2つのアポストロフィで囲む）
   - HTMLでは `<i>テキスト</i>` に変換され、通常は斜体で表示されます。

2. **強い強調**：`'''テキスト'''`（3つのアポストロフィで囲む）
   - HTMLでは `<b>テキスト</b>` に変換され、通常は太字で表示されます。

3. **強い強調かつ斜体**：`'''''テキスト'''''`（5つのアポストロフィで囲む）
   - HTMLでは `<b><i>テキスト</i></b>` に変換され、通常は太字かつ斜体で表示されます。

### 強調マークアップの除去

正規表現を使用して、強調マークアップを除去します。除去の順序は重要で、最も長いパターン（5つのアポストロフィ）から順に処理します。

```python
# 強い強調かつ斜体（5つのアポストロフィ）
text = re.sub(r"\'\'\'\'\'(.+?)\'\'\'\'\'", r"\\1", text)

# 強い強調（3つのアポストロフィ）
text = re.sub(r"\'\'\'(.+?)\'\'\'", r"\\1", text)

# 弱い強調（2つのアポストロフィ）
text = re.sub(r"\'\'(.+?)\'\'", r"\\1", text)
```

### 正規表現の解説

- `r"\'\'\'\'\'(.+?)\'\'\'\'\'"`：
  - 5つのアポストロフィにマッチ
  - 1つ以上の任意の文字にマッチし、非貪欲（non-greedy）でグループ化
  - 5つのアポストロフィにマッチ

- `r"\'\'\'(.+?)\'\'\'"`：
  - 3つのアポストロフィにマッチ
  - 1つ以上の任意の文字にマッチし、非貪欲でグループ化
  - 3つのアポストロフィにマッチ

- `r"\'\'(.+?)\'\'"`：
  - 2つのアポストロフィにマッチ
  - 1つ以上の任意の文字にマッチし、非貪欲でグループ化
  - 2つのアポストロフィにマッチ

### 注意点

- 正規表現の `(.+?)` は非貪欲（non-greedy）マッチングを行います。これにより、最初のマッチングで終了します。
- 強調マークアップが入れ子になっている場合（例：`'''''テキスト'''''` の中に `''テキスト''` がある場合）、複数回の置換が必要になることがあります。
- 実際のWikipediaの記事では、強調マークアップが複雑に組み合わされている場合があります。'''))
    
    # Set cells to notebook
    nb['cells'] = cells
    
    # Create directory if it doesn't exist
    os.makedirs('notebooks/chapter03', exist_ok=True)
    
    # Write the notebook to a file
    notebook_path = Path('notebooks/chapter03/26_remove_emphasis.ipynb')
    notebook_path.write_text(nbf.v4.writes(nb))
    
    print(f"Notebook created at {notebook_path}")

if __name__ == "__main__":
    create_notebook_26()
