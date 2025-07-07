# ブログビルドスクリプト - モジュール分割版

このディレクトリには、ブログサイトを生成するためのモジュール分割されたPythonスクリプトが含まれています。

## ファイル構成

### メインファイル
- `build.py` - メイン実行ファイル（全体の制御）

### モジュールファイル
- `config.py` - 設定管理（ディレクトリ設定、定数）
- `markdown_processor.py` - Markdown処理（Front Matter解析、Markdown変換）
- `template_engine.py` - テンプレート処理（HTMLテンプレートの読み込みと処理）
- `article_generator.py` - 記事ページ生成（個別記事ページの生成）
- `index_generator.py` - インデックスページ生成（トップページの生成）

### バックアップファイル
- `build_original.py` - 元の統合版ビルドスクリプト

## 使用方法

### 前提条件
必要なPythonパッケージをインストールしてください：
```bash
pip3 install markdown pyyaml
# または
sudo apt install python3-markdown python3-yaml
```

### 実行方法
```bash
cd scripts
python3 build.py
```

## モジュールの詳細

### config.py
- ディレクトリ設定（`SRC_DIR`, `TEMPLATE_DIR`, `OUTPUT_DIR`, `POSTS_DIR`）
- `ensure_directories()` - 必要なディレクトリの作成

### markdown_processor.py
- `parse_front_matter()` - Front Matterと本文の分離
- `extract_title()` - タイトルの抽出
- `process_markdown_file()` - Markdownファイルの処理

### template_engine.py
- `load_base_template()` - ベーステンプレートの読み込み
- `render_template()` - テンプレートのレンダリング
- `generate_article_page_content()` - 記事ページコンテンツの生成

### article_generator.py
- `generate_article_pages()` - 全記事ページの生成

### index_generator.py
- `generate_index_page()` - インデックスページの生成
- `generate_index_content()` - インデックスページコンテンツの生成

## 利点

1. **可読性の向上** - 各機能が独立したファイルに分離
2. **保守性の向上** - 特定の機能の修正が他に影響しない
3. **再利用性** - 各モジュールを他のプロジェクトで再利用可能
4. **テスト容易性** - 各モジュールを個別にテスト可能
5. **拡張性** - 新機能の追加が容易

## 注意事項

- 元のファイルは `build_original.py` としてバックアップされています
- 各モジュールは適切な依存関係を持っています
- 型ヒントを使用してコードの可読性を向上させています 