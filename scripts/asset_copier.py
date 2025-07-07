import os
import shutil
from config import OUTPUT_DIR

def copy_assets():

    asset_src_dir = "assets_src"
    asset_dest_dir = os.path.join(OUTPUT_DIR, "assets")

    print(f"Attempting to copy assets from {asset_src_dir} to {asset_dest_dir}")

    # 既存のOUTPUT_DIR/assetsを削除
    if os.path.exists(asset_dest_dir):
        print(f"Deleting existing '{asset_dest_dir}'...")
        shutil.rmtree(asset_dest_dir)
        print(f"Deleted '{asset_dest_dir}'.")

    # アセットをコピー
    if os.path.exists(asset_src_dir):
        try:
            shutil.copytree(asset_src_dir, asset_dest_dir)
            print(f"SUCCESS: Copied assets from '{asset_src_dir}' to '{asset_dest_dir}'.")
        except Exception as e:
            print(f"ERROR: Failed to copy assets. Reason: {e}")
    else:
        print(f"Warning: Source directory '{asset_src_dir}' not found. No assets copied.")
