from typing import Dict, Any, List
from config import OUTPUT_DIR
from template_engine import load_base_template, render_template
import os

def generate_index_page(articles_data: List[Dict[str, Any]]) -> None:
    """
    トップページ（インデックスページ）を生成する
    
    Args:
        articles_data: 記事のメタデータリスト
    """
    # 記事を日付順にソート
    try:
        articles_data.sort(key=lambda x: x['date'], reverse=True)
    except TypeError:
        print("Warning: Could not sort articles by date. Ensure dates are comparable.")
    
    # インデックスページのコンテンツを生成
    index_page_content_html = generate_index_content(articles_data)
    
    # ベーステンプレートを読み込み
    base_template = load_base_template()
    
    # テンプレートに埋め込み（index.html用にCSSパスを修正）
    final_index_html = render_template(base_template, "ホーム", index_page_content_html, css_path="assets/css/style.css")
    
    # ファイルを出力
    index_path = os.path.join(OUTPUT_DIR, "index.html")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(final_index_html)
    
    print(f"{OUTPUT_DIR}/index.html が生成されました。")

def generate_index_content(articles_data: List[Dict[str, Any]]) -> str:
    """
    インデックスページのコンテンツを生成する
    
    Args:
        articles_data: 記事のメタデータリスト
        
    Returns:
        str: インデックスページのHTMLコンテンツ
    """
    content = """
<div class="container">
    <div class="blog-content">
        <h1 class="text-gradient mb-5">最新記事一覧</h1>
        <div class="row g-4">
"""
    
    for article in articles_data:
        # 画像の表示部分
        image_html = f"<img src='{article['image']}' class='card-img-top' alt='{article['title']}'>" if article['image'] else ""
        
        # タグの表示部分
        tags_html = "".join([f"<span class='badge bg-secondary'>{tag}</span>" for tag in article['tags']]) if article['tags'] else ""
        
        content += f"""
        <div class="col-md-6 col-lg-4">
            <div class="card h-100">
                {image_html}
                <div class="card-body d-flex flex-column">
                    <h5 class="card-title">
                        <a href="{article['url']}">{article['title']}</a>
                    </h5>
                    <p class="card-text text-muted mb-2">
                        <small class="article-date">{article['date']}</small>
                    </p>
                    <p class="card-text flex-grow-1">{article['description']}</p>
                </div>
                <div class="card-footer">
                    <div class="article-tags">
                        {tags_html}
                    </div>
                </div>
            </div>
        </div>
        """
    
    content += """
        </div>
    </div>
</div>
"""
    
    return content 