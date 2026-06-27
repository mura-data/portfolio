# Aggregate Report Tool  
結合済みデータ（merged.xlsx）を読み込み、指定した項目で集計レポートを自動生成する Python スクリプトです。

01_csv_merge の次工程として利用でき、月次レポートや売上集計などの業務自動化に役立ちます。

---

## 🚀 機能概要

- Excel（merged.xlsx）を読み込み
- 指定した列でグループ化（例：category）
- 指定した集計方法で集計（例：amount の合計）
- 集計結果を Excel（report.xlsx）として出力
- ログ表示による処理状況の可視化
- エラーハンドリング付き

---

## 📁 フォルダ構成
```
02_aggregate_report/
├── report_generator.py
├── README.md
├── data/
│   └── merged.xlsx        ← 01_csv_merge の出力をコピー
└── output/
└── report.xlsx        ← 集計結果（自動生成）
```

---

## 🛠 使い方

### 1. 必要ライブラリのインストール

```bash
pip install pandas openpyxl

```

### 2. 入力データを配置
data/ フォルダに merged.xlsx を置きます。
（01_csv_merge の出力をコピー）

### 3. スクリプトを実行
```bash
python report_generator.py
```

### 4. 出力
`output/report.xlsx` が生成されます。

