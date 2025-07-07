# CSS カスタマイズガイド

このディレクトリには、ブログサイト用のカスタムCSSファイルが含まれています。

## ファイル構成

- `style.css` - メインのカスタムCSSファイル

## カスタマイズ方法

### 1. カラーパレットの変更

`style.css`の`:root`セクションで、CSS変数を変更することで簡単にカラーパレットを変更できます：

```css
:root {
  /* プライマリカラー */
  --primary-color: #2563eb;      /* メインカラー */
  --primary-hover: #1d4ed8;      /* ホバー時の色 */
  --accent-color: #f59e0b;       /* アクセントカラー */
  
  /* テキストカラー */
  --text-primary: #1e293b;       /* メインテキスト */
  --text-secondary: #64748b;     /* サブテキスト */
  --text-muted: #94a3b8;         /* 薄いテキスト */
  
  /* 背景色 */
  --bg-primary: #ffffff;         /* メイン背景 */
  --bg-secondary: #f8fafc;       /* サブ背景 */
  --bg-dark: #1e293b;            /* ダーク背景 */
}
```

### 2. フォントの変更

Google Fontsを使用しています。`templates/base.html`でフォントを変更できます：

```html
<link href="https://fonts.googleapis.com/css2?family=YOUR_FONT:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
```

そして`style.css`で：

```css
:root {
  --font-family: 'YOUR_FONT', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}
```

### 3. スペーシングの調整

```css
:root {
  --spacing-xs: 0.5rem;    /* 8px */
  --spacing-sm: 1rem;      /* 16px */
  --spacing-md: 1.5rem;    /* 24px */
  --spacing-lg: 2rem;      /* 32px */
  --spacing-xl: 3rem;      /* 48px */
}
```

### 4. ボーダーとシャドウの調整

```css
:root {
  --border-radius: 12px;           /* 角丸 */
  --border-radius-sm: 8px;         /* 小さい角丸 */
  --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
  --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1);
  --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1);
}
```

## セクション別カスタマイズ

### ナビゲーション

```css
.navbar {
  background: linear-gradient(135deg, var(--bg-dark) 0%, #334155 100%);
  /* グラデーション背景を変更 */
}

.navbar-brand {
  font-weight: 700;
  font-size: 1.5rem;
  /* ブランド名のスタイル */
}
```

### 見出し

```css
.blog-content h1 {
  font-size: 2.5rem;
  font-weight: 800;
  /* H1のスタイル */
}

.blog-content h1::after {
  background: linear-gradient(90deg, var(--primary-color), var(--accent-color));
  /* 下線のグラデーション */
}
```

### カード

```css
.card {
  border-radius: var(--border-radius);
  box-shadow: var(--shadow-md);
  transition: all 0.3s ease;
  /* カードの基本スタイル */
}

.card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-xl);
  /* ホバー効果 */
}
```

### 画像

```css
.blog-content img {
  border-radius: var(--border-radius);
  box-shadow: var(--shadow-lg);
  transition: all 0.3s ease;
  /* 画像の基本スタイル */
}

.blog-content img:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-xl);
  /* ホバー効果 */
}
```

## レスポンシブデザイン

モバイル対応のブレークポイント：

```css
@media (max-width: 768px) {
  /* タブレット以下 */
}

@media (max-width: 576px) {
  /* スマートフォン以下 */
}
```

## ユーティリティクラス

追加で使用できるクラス：

- `.text-gradient` - グラデーションテキスト
- `.shadow-custom` - カスタムシャドウ
- `.rounded-custom` - カスタム角丸

## ダークモード対応

将来的なダークモード対応のための準備：

```css
@media (prefers-color-scheme: dark) {
  :root {
    --text-primary: #f8fafc;
    --bg-primary: #0f172a;
    /* ダークモード用の色 */
  }
}
```

## ベストプラクティス

1. **CSS変数を使用**: 色やサイズの変更は`:root`の変数を変更
2. **セクション別にコメント**: コードの可読性を保つ
3. **レスポンシブ対応**: 必ずモバイル対応を考慮
4. **パフォーマンス**: 不要なスタイルは削除
5. **一貫性**: デザインシステムを統一

## トラブルシューティング

### スタイルが適用されない場合

1. CSSファイルのパスが正しいか確認
2. ブラウザのキャッシュをクリア
3. CSSの優先度（詳細度）を確認

### レイアウトが崩れる場合

1. Bootstrapのクラスとの競合を確認
2. レスポンシブブレークポイントを確認
3. コンテナの幅設定を確認 