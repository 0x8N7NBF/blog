import os

# ディレクトリ設定
SRC_DIR = "src"
TEMPLATE_DIR = "templates"
OUTPUT_DIR = "public"
POSTS_DIR = os.path.join(OUTPUT_DIR, "posts")

def ensure_directories():
    """必要なディレクトリが存在しない場合は作成する"""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    if not os.path.exists(POSTS_DIR):
        os.makedirs(POSTS_DIR) 