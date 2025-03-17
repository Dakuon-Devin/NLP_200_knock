# 問題29: 国旗画像のURLを取得する - 解説

## 問題の概要
この問題では、基礎情報テンプレートから国旗画像のファイル名を抽出し、MediaWiki APIを使用してその画像のURLを取得する方法を実装します。

## MediaWiki APIとは

MediaWiki APIは、WikipediaなどのMediaWikiベースのウェブサイトのコンテンツにプログラムからアクセスするためのインターフェースです。このAPIを使用することで、記事の内容、画像情報、編集履歴など、さまざまな情報を取得できます。

## 解法のポイント

### 1. 国旗画像のファイル名の抽出

基礎情報テンプレートには、「国旗画像」または「旗画像」というフィールドに国旗の画像ファイル名が記載されています。問題25で実装した基礎情報テンプレートの抽出関数を使用して、これらのフィールドから国旗画像のファイル名を抽出します。

```python
def extract_flag_filename(basic_info):
    """基礎情報テンプレートから国旗画像のファイル名を抽出する関数"""
    # 国旗画像のフィールド名（「国旗画像」または「旗画像」）
    flag_field_names = ["国旗画像", "旗画像"]
    
    # 国旗画像のフィールドを探す
    flag_filename = None
    for field_name in flag_field_names:
        if field_name in basic_info:
            flag_filename = basic_info[field_name]
            break
    
    return flag_filename
```

### 2. MediaWiki APIを使用した画像URLの取得

MediaWiki APIを使用して、抽出した国旗画像のファイル名からURLを取得します。APIリクエストには以下のパラメータを指定します：

- `action=query`: クエリアクションを指定
- `prop=imageinfo`: 画像情報を取得するプロパティを指定
- `titles=ファイル名`: 情報を取得するファイルのタイトルを指定
- `iiprop=url`: 画像のURLを取得するプロパティを指定

```python
def get_image_url(filename):
    """MediaWiki APIを使用して画像のURLを取得する関数"""
    # ファイル名の先頭に「ファイル:」または「File:」がない場合は追加
    if not filename.startswith(("ファイル:", "File:")):
        filename = "File:" + filename
    
    # MediaWiki APIのエンドポイント
    api_url = "https://ja.wikipedia.org/w/api.php"
    
    # APIリクエストのパラメータ
    params = {
        "action": "query",
        "format": "json",
        "prop": "imageinfo",
        "titles": filename,
        "iiprop": "url"
    }
    
    # APIリクエストを送信し、レスポンスから画像のURLを抽出
    response = requests.get(api_url, params=params)
    data = response.json()
    
    pages = data["query"]["pages"]
    for page_id in pages:
        if "imageinfo" in pages[page_id]:
            return pages[page_id]["imageinfo"][0]["url"]
    
    return None
```

## 実装上の注意点

1. **ファイル名の形式**：
   Wikipediaのファイル名は「ファイル:」または「File:」で始まる必要があります。抽出したファイル名にこのプレフィックスがない場合は追加する必要があります。

2. **APIの利用制限**：
   MediaWiki APIには利用制限があるため、大量のリクエストを短時間に送信すると制限される可能性があります。実際のアプリケーションでは、キャッシュやレート制限の対策を実装することが重要です。

3. **エラー処理**：
   APIリクエストが失敗した場合や、画像情報が取得できなかった場合のエラー処理を実装することが重要です。例外処理を使用して、エラーメッセージを表示するなどの対応が必要です。

4. **画像の著作権**：
   Wikipediaの画像には著作権があるため、利用する際は適切なライセンス表示が必要です。画像のライセンス情報も同様にAPIから取得できます（`iiprop=url|extmetadata`を指定）。

## 発展的な内容

この問題で学んだMediaWiki APIの使用方法は、他のさまざまな情報を取得する際にも応用できます。例えば：

- 記事の内容を取得する（`action=parse`）
- 記事の編集履歴を取得する（`prop=revisions`）
- カテゴリに属する記事のリストを取得する（`list=categorymembers`）
- 記事の検索を行う（`action=opensearch`）

APIの詳細なドキュメントは、[MediaWiki API:Main page](https://www.mediawiki.org/wiki/API:Main_page)で確認できます。
