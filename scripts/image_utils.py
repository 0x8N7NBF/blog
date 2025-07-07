import os
import re
from typing import Dict, Optional
from config import SRC_DIR

class ImagePathManager:
    """
    画像パスの短縮化と管理を行うクラス
    """
    
    # パスエイリアスの定義
    PATH_ALIASES = {
        "@thumbnails": "/blog/assets/images/thumbnails",
        "@post-images": "/blog/assets/images/post-images",
        "@assets": "/blog/assets/images",
        "@": "/blog/assets/images"  # デフォルトエイリアス
    }
    
    @classmethod
    def expand_image_path(cls, image_path: str, article_filename: str = None) -> str:
        """
        短縮パスを完全パスに展開する
        
        Args:
            image_path: 画像パス（短縮形式または完全パス）
            article_filename: 記事ファイル名（相対パス用）
            
        Returns:
            str: 展開された完全パス
        """
        if not image_path:
            return ""
        
        # 既に完全パスの場合はそのまま返す
        if image_path.startswith(("http://", "https://", "/")):
            return image_path
        
        # エイリアスを展開
        for alias, full_path in cls.PATH_ALIASES.items():
            if image_path.startswith(alias):
                return image_path.replace(alias, full_path, 1)
        
        # 記事固有の画像ディレクトリの場合
        if article_filename and image_path.startswith("./"):
            article_name = os.path.splitext(article_filename)[0]
            return f"/blog/assets/images/post-images/{article_name}/{image_path[2:]}"
        
        # デフォルトエイリアスを適用
        if not image_path.startswith(("/", "http")):
            return f"{cls.PATH_ALIASES['@']}/{image_path}"
        
        return image_path
    
    @classmethod
    def get_short_path(cls, full_path: str) -> str:
        """
        完全パスを短縮パスに変換する
        
        Args:
            full_path: 完全パス
            
        Returns:
            str: 短縮パス
        """
        for alias, full_alias_path in cls.PATH_ALIASES.items():
            if full_path.startswith(full_alias_path):
                return full_path.replace(full_alias_path, alias, 1)
        
        return full_path

def process_markdown_images(content: str, article_filename: str = None) -> str:
    """
    Markdownコンテンツ内の画像パスを処理する
    
    Args:
        content: Markdownコンテンツ
        article_filename: 記事ファイル名
        
    Returns:
        str: 処理されたMarkdownコンテンツ
    """
    # 画像リンクのパターンを検出
    image_pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
    
    def replace_image(match):
        alt_text = match.group(1)
        image_path = match.group(2)
        
        # パスを展開
        expanded_path = ImagePathManager.expand_image_path(image_path, article_filename)
        
        return f'![{alt_text}]({expanded_path})'
    
    return re.sub(image_pattern, replace_image, content)

def validate_image_paths(content: str, article_filename: str = None) -> Dict[str, bool]:
    """
    画像パスの有効性を検証する
    
    Args:
        content: Markdownコンテンツ
        article_filename: 記事ファイル名
        
    Returns:
        Dict[str, bool]: パスとその有効性の辞書
    """
    image_pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
    matches = re.findall(image_pattern, content)
    
    results = {}
    for alt_text, image_path in matches:
        expanded_path = ImagePathManager.expand_image_path(image_path, article_filename)
        
        # ローカルファイルの場合は存在確認
        if expanded_path.startswith("/") and not expanded_path.startswith(("http://", "https://")):
            # パブリックディレクトリからの相対パスに変換
            relative_path = expanded_path.replace("/blog/assets", "assets")
            file_exists = os.path.exists(relative_path)
            results[image_path] = file_exists
        else:
            # 外部URLの場合は有効とみなす
            results[image_path] = True
    
    return results 