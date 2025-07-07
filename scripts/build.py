import os
import markdown

# ディレクトリ設定
src_dir = "src"
template_dir = "templates"
output_dir = "public"

# 出力ディレクトリが存在しなければ作成
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
if not os.path.exists(os.path.join(output_dir, "posts")):
    os.makedirs(os.path.join(output_dir, "posts")) # 記事用ディレクトリ

# ベーステンプレートの読み込み
with open(os.path.join(template_dir, "base.html"), "r", encoding="utf-8") as f:
    base_template = f.read()

articles_data = [] # 記事のメタデータを格納するリスト

# Markdown記事の処理
for filename in os.listdir(src_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(src_dir, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            md_content = f.read()
        
        # ここでタイトルとコンテンツを分離するロジックをより堅牢にする
        # 例えば、Markdownファイルの先頭にFront Matter (YAML形式のメタデータ)を追加する
        # 現状は簡易的にタイトルだけ取得
        lines = md_content.split("\n", 1)
        title = lines[0].lstrip('# ').strip() if lines[0].startswith('#') else os.path.splitext(filename)[0]
        content_without_title = lines[1] if len(lines) > 1 else ""

        # MarkdownをHTMLに変換
        html_content_body = markdown.markdown(content_without_title)

        # テンプレートに埋め込み
        final_html = base_template.replace("{{title}}", title).replace("{{content}}", html_content_body)

        # 出力ファイル名とパスを指定
        # 例：my-first-post.md -> public/posts/my-first-post.html
        output_filename_base = os.path.splitext(filename)[0]
        output_html_filepath = os.path.join(output_dir, "posts", f"{output_filename_base}.html")

        # 記事のメタデータをリストに追加
        articles_data.append({
            "title": title,
            "url": f"posts/{output_filename_base}.html", # トップページからの相対パス
        })

        # ファイルを出力
        with open(output_html_filepath, "w", encoding="utf-8") as f:
            f.write(final_html)

        print(f"{output_filename} を作成しました。")

# index.htmlの生成
index_html_content = """
<div class="container" my-4>
    <h1>ブログ記事一覧</h1>
    <ul class="list-group">
"""
# 日付降順などでソートする場合は、ここでarticles_dataをソートする
# articles_data.sort(key=lambda x: x["date"], reverse=True) # メタ情報導入後に実装可能

for article in articles_data:
    index_page_content += f"""
    <li class="list-group-item">
        <a href="{article["url"]}" class="text-decoration-none">{article["title"]}</a>
    </li>
    """
index_page_content += """
    </ul>
</div>
"""

# ベーステンプレートにindex_page_contentを埋め込んでindex.htmlを生成
# 今回は簡易的にbodyタグの中身だけを生成と仮定
final_index_html = base_template.replace("{{title}}", "ホーム").replace("{{content}}", index_page_content)

with open(os.path.join(output_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_html_content)
print(f"{output_dir}/index.html を作成しました。")
