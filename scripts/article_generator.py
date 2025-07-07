import os
from typing import Dict, Any, List
from config import SRC_DIR, POSTS_DIR
from markdown_processor import process_markdown_file
from template_engine import load_base_template, render_template, generate_article_page_content

def generate_article_pages() -> List[Dict[str, Any]]:
    """
    すべてのMarkdownファイルから記事ページを生成する
    
    Returns:
        List[Dict[str, Any]]: 記事のメタデータリスト
    """
    articles_data = []
    base_template = load_base_template()
    
    # Markdown記事の処理
    for filename in os.listdir(SRC_DIR):
        if filename.endswith(".md"):
            filepath = os.path.join(SRC_DIR, filename)
            
            # Markdownファイルを処理
            article_data = process_markdown_file(filepath)
            
            # 出力ファイル名とパスを指定
            output_filename_base = os.path.splitext(filename)[0]
            output_html_filepath = os.path.join(POSTS_DIR, f"{output_filename_base}.html")
            
            # URLを設定
            article_data["url"] = f"posts/{output_filename_base}.html"
            
            # 記事ページのコンテンツを生成
            article_page_content = generate_article_page_content(article_data)
            
            # テンプレートに埋め込み
            final_html = render_template(base_template, article_data["title"], article_page_content)
            
            # ファイルを出力
            with open(output_html_filepath, "w", encoding="utf-8") as f:
                f.write(final_html)
            
            print(f"{output_html_filepath} が生成されました。")
            
            # 記事のメタデータをリストに追加
            articles_data.append(article_data)
    
    return articles_data 