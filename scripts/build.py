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

# Markdown記事の処理
for filename in os.listdir(src_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(src_dir, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            md_content = f.read()
        
        # タイトルとコンテンツを分離
        lines = md_content.split("\n", 1)
        title = lines[0].lstrip('# ').strip() if lines[0].startswith('# ') else "No Title"
        content_without_title = lines[1] if len(lines) > 1 else ""

        # MarkdownをHTMLに変換
        html_content_body = markdown.markdown(content_without_title)

        # テンプレートに埋め込み
        final_html = base_template.replace("{{title}}", title).replace("{{content}}", html_content_body)

        # 出力ファイル名とパスを指定
        # 例：my-first-post.md -> public/posts/my-first-post.html
        output_filename = os.path.splitext(filename)[0] + ".html"
        output_filepath = os.path.join(output_dir, "posts", output_filename)

        # ファイルを出力
        with open(output_filepath, "w", encoding="utf-8") as f:
            f.write(final_html)

        print(f"{output_filename} を作成しました。")

# ホームページ（index.html）の簡易生成
# これは主導でリンクを埋め込むことでルーティングを把握するステップです
# 後で自動化します
index_html_content = """
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ホーム</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body>
    <h1>ようこそ！</h1>
    <p>私の自作ブログへようこそ！</p>
    <h2>最新の記事</h2>
    <ul>
        <li><a href="posts/my-first-post.html">最初の記事</a></li>
    </ul>
</body>
</html>
"""
with open(os.path.join(output_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_html_content)
print(f"{output_dir}/index.html を作成しました。")
