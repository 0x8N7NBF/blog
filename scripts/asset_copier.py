import os
import shutil
from config import OUTPUT_DIR

def copy_assets():

    asset_src_dir = "assets_src"
    asset_dest_dir = os.path.join(OUTPUT_DIR, "assets")

    # 既存のOUTPUT_DIR/assetsを削除
    if os.path.exists(asset_dest_dir):
        shutil.rmtree(asset_dest_dir)

    # アセットをコピー
    if os.path.exists(asset_src_dir):
        shutil.copytree(asset_src_dir, asset_dest_dir)
    else:
        print(f"Warning: '{asset_src_dir}' not found.")
