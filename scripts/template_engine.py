import os
from typing import Dict, Any
from config import TEMPLATE_DIR

def load_base_template() -> str:
    """
    ベーステンプレートを読み込む
    
    Returns:
        str: ベーステンプレートの内容
    """
    template_path = os.path.join(TEMPLATE_DIR, "base.html")
    with open(template_path, "r", encoding="utf-8") as f:
        return f.read()

def render_template(template: str, title: str, content: str) -> str:
    """
    テンプレートにタイトルとコンテンツを埋め込む
    
    Args:
        template: ベーステンプレート
        title: ページタイトル
        content: ページコンテンツ
        
    Returns:
        str: レンダリングされたHTML
    """
    return template.replace("{{title}}", title).replace("{{content}}", content)

def generate_article_page_content(article_data: Dict[str, Any]) -> str:
    """
    記事ページのコンテンツを生成する
    
    Args:
        article_data: 記事データ
        
    Returns:
        str: 記事ページのHTMLコンテンツ
    """
    title = article_data["title"]
    date = article_data["date"]
    tags = article_data["tags"]
    image = article_data["image"]
    html_content = article_data["html_content"]
    
    # タグの表示部分
    tags_html = f"<p>タグ: {', '.join(tags)}</p>" if tags else ""
    
    # 画像の表示部分
    image_html = f"<img src='{image}' class='img-fluid mb-3' alt='Thumbnail'>" if image else ""
    
    return f"""
    <h1>{title}</h1>
    <p class="text-muted">{date}</p>
    {tags_html}
    {image_html}
    {html_content}
    """ 