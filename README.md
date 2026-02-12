# GitHub Actions 勉強会デモ

## 📝 概要
GitHub Actionsを使ったシンプルなCI（継続的インテグレーション）のデモです。
コードをpushすると自動的にテストが実行されます。

## 🎯 デモの内容
1. **簡単な計算機プログラム** (`calculator.py`)
2. **ユニットテスト** (`test_calculator.py`)
3. **自動テスト実行** (GitHub Actions)

## 🚀 デモの流れ

### ステップ1: 正常なテストを実行
```bash
# ローカルでテストを実行
python -m unittest test_calculator.py -v
```

### ステップ2: コードをpushして自動テストを確認
```bash
git add .
git commit -m "初回コミット: 計算機とテストを追加"
git push origin main
```

GitHubのリポジトリページ → **Actions** タブで実行状況を確認！
✅ テストが成功するのを確認

### ステップ3: わざとテストを失敗させる
`calculator.py` の `add` 関数を壊してみます：

```python
def add(a, b):
    """2つの数値を足し算"""
    return a - b  # ← わざと引き算にする！
```

```bash
git add calculator.py
git commit -m "バグを混入させる（デモ用）"
git push origin main
```

GitHub Actions タブで ❌ 失敗を確認！

### ステップ4: バグを修正する
`calculator.py` を正しく修正：

```python
def add(a, b):
    """2つの数値を足し算"""
    return a + b  # ← 正しく修正
```

```bash
git add calculator.py
git commit -m "バグを修正"
git push origin main
```

GitHub Actions タブで ✅ 成功を確認！

## 📊 GitHub Actionsの確認方法
1. GitHubリポジトリページを開く
2. **Actions** タブをクリック
3. ワークフローの実行結果を確認
   - 緑のチェックマーク ✅ = 成功
   - 赤いバツマーク ❌ = 失敗

## 🔧 ワークフローファイル
`.github/workflows/test.yml` でCI設定を管理しています。

## 💡 実務での活用例
- プルリクエスト作成時に自動テスト
- mainブランチへのマージ前にテストを必須化
- テスト失敗時にSlack通知
- カバレッジレポートの自動生成

---

**作成日**: 2026-02-12
