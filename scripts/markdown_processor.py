import os
import markdown
import yaml
import re
from typing import Dict, Tuple, Any

def parse_front_matter(filepath: str, content: str) -> Tuple[Dict[str, Any], str]:
    """
    MarkdownコンテンツからFront Matterと本文を分離する
    
    Args:
        filepath: Markdownファイルのパス
        content: Markdownファイルの内容
        
    Returns:
        Tuple[Dict[str, Any], str]: (Front Matter辞書, 本文)
    """

    # 正規表現を使用してFront Matterを抽出
    front_matter_pattern = re.compile(r'^---\s*\n(.*?)\n---\s*\n(.*)', re.DOTALL)
    front_matter_match = front_matter_pattern.match(content)

    front_matter = {}
    content_body = content

    if front_matter_match:
        # マッチした場合、グループ1がFront Matter、グループ2が本文
        front_matter_str = front_matter_match.group(1)
        content_body = front_matter_match.group(2).strip() # 前後の空白を削除
        try:
            front_matter = yaml.safe_load(front_matter_str)
            if front_matter is None: # YAMLが空の場合
                front_matter = {}
        except yaml.YAMLError as e:
            print(f"YAML parsing error in {filepath}: {e}. Treating as no Front Matter.")

    else:
        print(f"No Front Matter found in {filepath}. Treating as no Front Matter.")
    
    return front_matter, content_body

def extract_title(filepath: str, front_matter: Dict[str, Any], content_body: str) -> str:
    """
    タイトルを抽出する（Front Matter優先、なければMarkdownのH1、それでもなければファイル名）
    
    Args:
        filepath: Markdownファイルのパス
        front_matter: Front Matter辞書
        content_body: Markdown本文
        
    Returns:
        str: 抽出されたタイトル
    """
    title = front_matter.get('title', None)
    if not title:
        # タイトルがない場合、MarkdownのH1を探す
        h1_match = re.search(r'^#+\s+(.*)', content_body, re.MULTILINE)
        if h1_match:
            title = h1_match.group(1).strip()
        else:
            title = os.path.splitext(os.path.basename(filepath))[0] # H1もなければファイル名
    
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
    front_matter, content_body = parse_front_matter(filepath, md_content)
    
    # タイトル取得
    title = extract_title(filepath, front_matter, content_body)
    
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
        "image": f"{image}" if image else None,
        "description": description,
        "html_content": html_content_body,
    } 