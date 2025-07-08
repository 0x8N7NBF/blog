import os
import shutil

# ディレクトリ設定
SRC_DIR = "src"
TEMPLATE_DIR = "templates"
OUTPUT_DIR = "public"
POSTS_DIR = os.path.join(OUTPUT_DIR, "posts")
ASSETS_SRC_DIR = "assets_src"
ASSETS_OUTPUT_DIR = os.path.join(OUTPUT_DIR, "assets")
GITHUB_PAGES_BASE_URL = "https://0x8n7nbf.github.io/blog"

def ensure_directories():
    """必要なディレクトリが存在しない場合は作成する"""
    directories = [OUTPUT_DIR, POSTS_DIR, ASSETS_OUTPUT_DIR]
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)

def copy_assets():
    """アセットファイルをコピーする"""
    if os.path.exists(ASSETS_SRC_DIR):
        if os.path.exists(ASSETS_OUTPUT_DIR):
            shutil.rmtree(ASSETS_OUTPUT_DIR)
        shutil.copytree(ASSETS_SRC_DIR, ASSETS_OUTPUT_DIR)
        print(f"アセットファイルを {ASSETS_OUTPUT_DIR} にコピーしました。")
    else:
        print(f"Warning: {ASSETS_SRC_DIR} ディレクトリが見つかりません。") 