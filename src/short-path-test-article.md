---
title: 短縮パステスト記事
date: 2025-01-18
tags: [テスト, 短縮パス, 画像]
image: "@thumbnails/short_path_test.jpg"
description: 短縮パス機能をテストする記事です。様々な短縮パス形式を使用して画像を表示します。
---

# 短縮パステスト記事

この記事は、新しく実装された短縮パス機能をテストするために作成されました。

## 短縮パスの種類

### 1. サムネイル画像（@thumbnails）
![サムネイル画像](@thumbnails/short_path_test.jpg)

### 2. 記事固有の画像（./）
![記事固有の画像](./feature-diagram.png)

### 3. デフォルトアセット（@）
![デフォルトアセット画像](@general-image.jpg)

### 4. 外部URL（そのまま）
![外部画像](https://via.placeholder.com/400x300/ff6b6b/ffffff?text=External+Image)

### 5. 完全パス（そのまま）
![完全パス画像](/blog/assets/images/post-images/another-article/image.jpg)

## 短縮パスの利点

1. **簡潔性**: 長いパスを書く必要がない
2. **可読性**: コードが読みやすくなる
3. **保守性**: パス構造を変更しても記事を修正する必要がない
4. **一貫性**: 統一されたパス形式

## エイリアス一覧

- `@thumbnails` → `/blog/assets/images/thumbnails`
- `@post-images` → `/blog/assets/images/post-images`
- `@assets` → `/blog/assets/images`
- `@` → `/blog/assets/images`（デフォルト）
- `./` → 記事固有のディレクトリ

この機能により、画像の管理が大幅に簡素化されました！ 