---
title: スクリプトテスト用記事 - 全機能テスト
date: 2025-01-15
tags: [テスト, 技術, Python, Markdown, ブログ]
image: /assets/images/thumbnails/test_article_thumbnail.jpg
description: この記事はブログ生成スクリプトの全機能をテストするために作成されました。Front Matter、Markdown記法、画像、タグ、説明文など全ての機能が含まれています。
---

# スクリプトテスト用記事 - 全機能テスト

この記事は、ブログ生成スクリプト（`scripts/`）が正しく動作することを確認するためのテスト記事です。

## テスト対象機能

### 1. Front Matter の処理
- **タイトル**: スクリプトテスト用記事 - 全機能テスト
- **日付**: 2025-01-15
- **タグ**: テスト, 技術, Python, Markdown, ブログ
- **画像**: /assets/images/test_article_thumbnail.jpg
- **説明**: この記事はブログ生成スクリプトの全機能をテストするために作成されました。

### 2. Markdown記法のテスト

#### 見出しレベルのテスト
# H1見出し
## H2見出し
### H3見出し
#### H4見出し

#### テキスト装飾
**太字テキスト** と *斜体テキスト* と ***太字斜体テキスト***

#### リストのテスト
**番号付きリスト:**
1. 最初の項目
2. 二番目の項目
3. 三番目の項目

**番号なしリスト:**
- 項目A
- 項目B
  - ネストした項目B-1
  - ネストした項目B-2
- 項目C

#### リンクと画像
[Google](https://www.google.com) へのリンク

ここに画像を挿入します。

![これはキャプションです](/assets/images/post-images/test-article-with-all-features/diagram.png)

この画像は、記事の内容を説明するために使われます。

#### コードブロック
```python
def test_function():
    """テスト用の関数"""
    print("Hello, World!")
    return True
```

**インラインコード**: `print("Hello, World!")`

#### 引用
> これは引用文です。
> 
> 複数行の引用文も
> 正しく表示されるはずです。

#### 水平線
---

## テスト結果の確認ポイント

1. **Front Matter解析**: タイトル、日付、タグ、画像、説明が正しく抽出されるか
2. **Markdown変換**: 各種Markdown記法が正しくHTMLに変換されるか
3. **テンプレート適用**: ベーステンプレートに正しく埋め込まれるか
4. **インデックス生成**: 記事一覧ページに正しく表示されるか
5. **ファイル出力**: HTMLファイルが正しい場所に生成されるか

## 期待される動作

この記事を処理すると、以下のファイルが生成されるはずです：
- `public/posts/test-article-with-all-features.html`
- `public/index.html`（更新される）

スクリプトが正常に動作していれば、この記事は美しくフォーマットされたHTMLページとして表示されるはずです。 