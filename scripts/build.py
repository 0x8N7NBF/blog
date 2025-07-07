import os
import markdown
import yaml
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
        
        # Front Matterと本文を分離
        front_matter = {}
        content_body = md_content

        if md_content.startswith("---"):
            parts = md_content.split("---", 2) # 最初の---と2番目の---で分割
            if len(parts) > 3:
                try:
                    front_matter = yaml.safe_load(parts[1])
                    content_body = parts[2].strip()
                except yaml.YAMLError as e:
                    print(f"YAML parsing error in {filename}: {e}")
                    content_body = md_content # エラー時はFront Matterなしとして処理
            else:
                content_body = md_content # Front Matterの閉じタグがない場合
        
        # タイトル取得 (Front Matter優先、なければMarkdownのH1)
        title = front_matter.get('title', 'No Title')
        if not title and content_body.startswith('#'):
            title = content_body.split("\n", 1)[0].lstrip('# ').strip()
        
        # その他のメタ情報
        date = front_matter.get('date', 'Unknown Date')
        tags = front_matter.get('tags', [])
        image = front_matter.get('image', None)
        description = front_matter.get('description', '')

        # MarkdownをHTMLに変換
        html_content_body = markdown.markdown(content_body)

        # 出力ファイル名とパスを指定
        # 例：my-first-post.md -> public/posts/my-first-post.html
        output_filename_base = os.path.splitext(filename)[0]
        output_html_filepath = os.path.join(output_dir, "posts", f"{output_filename_base}.html")

        # 記事のメタデータをリストに追加
        articles_data.append({
            "title": title,
            "date": date,
            "tags": tags,
            "image": image,
            "description": description,
            "url": f"posts/{output_filename_base}.html", # トップページからの相対パス
            "html_content": html_content_body, # 記事自体のHTMLコンテンツも保持
        })

        # テンプレートに埋め込みとファイル書き出し
        # 各記事ページにもメタ情報を表示
        article_page_content = f"""
        <h1>{title}</h1>
        <p class="text-muted">公開日: {date}</p>
        {"<p>タグ: " + ", ".join(tags) + "</p>" if tags else ""}
        {"<img src='" + image + "' class='img-fluid mb-3' alt='Thumbnail'>" if image else ""}
        {html_content_body}
        """

        # base_templateを読み込み、{{ content }}を置き換える
        # 注: 'base_template'はファイルの冒頭で一度読み込んでおく必要がある
        final_html = base_template.replace("{{title}}", title).replace("{{content}}", article_page_content)

        # ファイルを出力
        with open(output_html_filepath, "w", encoding="utf-8") as f:
            f.write(final_html)

        print(f"{output_html_filepath} が生成されました。")

# index.htmlの生成
# articles_dataを日付順にソート (日付が文字列なので、適宜型変換やソート方法を調整)
try:
    articles_data.sort(key=lambda x: x['date'], reverse=True)
except TypeError:
    print("Warning: Could not sort articles by date. Ensure dates are comparable.")

index_page_content_html = """
<div class="container" my-4>
    <h1 class="mb-4">最新記事一覧</h1>
    <div class="row">
"""
for article in articles_data:
    index_page_content_html += f"""
    <div class="col-md-6 col-lg-4 mb-4">
        <div class="card h-100">
            {"<img src='" + article['image'] + "' class='card-img-top' alt='Thumbnail'>" if article['image'] else ""}
            <div class="card-body">
                <h5 class="card-title"><a href="{article['url']}" class="text-decoration-none">{article['title']}</a></h5>
                <p class="card-text"><small class="text-muted">{article['date']}</small></p>
                <p class="card-text">{article['description']}</p>
            </div>
            <div class="card-footer">
                {"".join([f"<span class='badge bg-secondary me-1'>{tag}</span>" for tag in article['tags']]) if article['tags'] else ""}
            </div>
        </div>
    </div>
    """
index_page_content_html += """
    </div>
</div>
"""

# ベーステンプレートにindex_page_contentを埋め込んでindex.htmlを生成
# 今回は簡易的にbodyタグの中身だけを生成と仮定
final_index_html = base_template.replace("{{title}}", "ホーム").replace("{{content}}", index_page_content_html)
with open(os.path.join(output_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(final_index_html)
print(f"{output_dir}/index.html が生成されました。")
