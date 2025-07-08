import os
from typing import Dict, Any
from config import TEMPLATE_DIR, GITHUB_PAGES_BASE_URL

def load_base_template() -> str:
    """
    ベーステンプレートを読み込む
    
    Returns:
        str: ベーステンプレートの内容
    """
    template_path = os.path.join(TEMPLATE_DIR, "base.html")
    with open(template_path, "r", encoding="utf-8") as f:
        return f.read()

def render_template(template: str, title: str, content: str, css_path: str = "../assets/css/style.css", base_url: str = GITHUB_PAGES_BASE_URL) -> str:
    """
    テンプレートにタイトルとコンテンツ、CSSパスを埋め込む
    
    Args:
        template: ベーステンプレート
        title: ページタイトル
        content: ページコンテンツ
        css_path: CSSファイルへのパス
        base_url: ベースURL
    Returns:
        str: レンダリングされたHTML
    """
    return (
        template
        .replace("{{title}}", title)
        .replace("{{content}}", content)
        .replace("{{css_path}}", css_path)
        .replace("{{base_url}}", base_url)
    )

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
    
    # メタ情報の表示部分
    meta_html = f"""
    <div class="article-meta">
        <p class="article-date">{date}</p>
        {f'<div class="article-tags">{" ".join([f"<span class=\"badge bg-secondary\">{tag}</span>" for tag in tags])}</div>' if tags else ""}
    </div>
    """
    
    # サムネイル画像の表示部分
    image_html = f"""
    <div class="text-center mb-4">
        <img src='{image}' class='img-fluid rounded-custom shadow-custom' alt='{title}' style='max-width: 400px;'>
    </div>
    """ if image else ""
    
    return f"""
    <h1>{title}</h1>
    {meta_html}
    {image_html}
    {html_content}
    """ 