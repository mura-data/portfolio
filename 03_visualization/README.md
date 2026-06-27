# Visualization Tool  
集計済みデータ（report.xlsx）を読み込み、カテゴリ別売上などのグラフを自動生成する Python 可視化ツールです。

01_csv_merge → 02_aggregate_report → 03_visualization  
という一連のデータ分析パイプラインの最終ステップとして利用できます。

---

## 🚀 機能概要

- Excel（report.xlsx）を読み込み
- 指定した列を使って棒グラフを生成
- PNG 画像として output/ に保存
- ログ表示による処理状況の可視化
- エラーハンドリング付き

---

## 📁 フォルダ構成

```
03_visualization/
├── visualize.py
├── README.md
├── data/
│   └── report.xlsx        ← 02_aggregate_report の出力をコピー
└── output/
└── chart_category_amount.png   ← グラフ（自動生成）
```
---
## 🛠 使い方

### 1. 必要ライブラリのインストール

```bash
pip install pandas matplotlib openpyxl
```

### 2. 入力データを配置
`data/` フォルダに report.xlsx を置きます。
（02_aggregate_report の出力をコピー）

### 3. スクリプトを実行
```bash
python visualize.py
```

### 4. 出力
`output/chart_category_amount.png` が生成されます。