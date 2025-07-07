#!/usr/bin/env python3
"""
ブログビルドスクリプト - モジュール分割版

このスクリプトは以下のモジュールを使用してブログサイトを生成します：
- config: 設定管理
- markdown_processor: Markdown処理
- template_engine: テンプレート処理
- article_generator: 記事ページ生成
- index_generator: インデックスページ生成
"""

from config import ensure_directories
from article_generator import generate_article_pages
from index_generator import generate_index_page

def main():
    """メイン実行関数"""
    print("ブログビルドを開始します...")
    
    # 必要なディレクトリを作成
    ensure_directories()
    
    # 記事ページを生成
    print("記事ページを生成中...")
    articles_data = generate_article_pages()
    
    # インデックスページを生成
    print("インデックスページを生成中...")
    generate_index_page(articles_data)
    
    print(f"ビルド完了！ {len(articles_data)}個の記事を処理しました。")

if __name__ == "__main__":
    main() 