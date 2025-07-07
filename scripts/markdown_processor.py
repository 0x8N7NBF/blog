import os
import markdown
import yaml
from typing import Dict, Tuple, Any

def parse_front_matter(content: str) -> Tuple[Dict[str, Any], str]:
    """
    MarkdownコンテンツからFront Matterと本文を分離する
    
    Args:
        content: Markdownファイルの内容
        
    Returns:
        Tuple[Dict[str, Any], str]: (Front Matter辞書, 本文)
    """
    front_matter = {}
    content_body = content

    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) > 3:
            try:
                front_matter = yaml.safe_load(parts[1])
                content_body = parts[2].strip()
            except yaml.YAMLError as e:
                print(f"YAML parsing error: {e}")
                content_body = content
        else:
            content_body = content
    
    return front_matter, content_body

def extract_title(front_matter: Dict[str, Any], content_body: str) -> str:
    """
    タイトルを抽出する（Front Matter優先、なければMarkdownのH1）
    
    Args:
        front_matter: Front Matter辞書
        content_body: Markdown本文
        
    Returns:
        str: 抽出されたタイトル
    """
    title = front_matter.get('title', 'No Title')
    if not title and content_body.startswith('#'):
        title = content_body.split("\n", 1)[0].lstrip('# ').strip()
    return title

def process_markdown_file(filepath: str) -> Dict[str, Any]:
    """
    Markdownファイルを処理して記事データを生成する
    
    Args:
        filepath: Markdownファイルのパス
        
    Returns:
        Dict[str, Any]: 記事のメタデータとコンテンツ
    """
    with open(filepath, "r", encoding="utf-8") as f:
        md_content = f.read()
    
    # Front Matterと本文を分離
    front_matter, content_body = parse_front_matter(md_content)
    
    # タイトル取得
    title = extract_title(front_matter, content_body)
    
    # その他のメタ情報
    date = front_matter.get('date', 'Unknown Date')
    tags = front_matter.get('tags', [])
    image = front_matter.get('image', None)
    description = front_matter.get('description', '')
    
    # MarkdownをHTMLに変換
    html_content_body = markdown.markdown(content_body)
    
    return {
        "title": title,
        "date": date,
        "tags": tags,
        "image": image,
        "description": description,
        "html_content": html_content_body,
        "content_body": content_body
    } 