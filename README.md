# Data Processing Pipeline Portfolio  
このリポジトリは、データ分析の基本プロセスである  
**「データ結合 → 集計 → 可視化」**  
を Python で自動化した 3 つのツールで構成されています。

業務の定型処理やレポート作成を効率化するための、  
実務レベルのデータ処理パイプラインを再現しています。

---

## 📦 プロジェクト構成
01_csv_merge/          ← CSV 結合ツール

02_aggregate_report/   ← 集計レポート生成ツール

03_visualization/      ← 可視化ツール


---

## ① CSV Merge Tool（01_csv_merge）

複数の CSV ファイルを読み込み、  
- 結合  
- 日付整形  
- 不要列削除  
- Excel 出力（merged.xlsx）  
を自動で行うツールです。

**想定用途：**  
日次・週次で届く CSV の統合、レポート前処理、データクレンジング。

---

## ② Aggregate Report Tool（02_aggregate_report）

01 で作成した merged.xlsx を読み込み、  
- 指定列でグループ化  
- 合計・平均などの集計処理  
- Excel 出力（report.xlsx）  
を自動化するツールです。

**想定用途：**  
カテゴリ別売上集計、店舗別集計、月次レポート作成。

---

## ③ Visualization Tool（03_visualization）

02 の report.xlsx を読み込み、  
- 棒グラフなどの可視化  
- PNG 画像として保存  
を行うツールです。

**想定用途：**  
レポート資料のグラフ作成、売上の視覚的分析、ダッシュボードの素材生成。

---

## 🧭 全体の流れ（Pipeline）
CSV → ①結合 → merged.xlsx   
↓   
②集計 → report.xlsx     
↓   
③可視化 → chart.png


この 3 ステップで、  
**データ前処理 → 集計 → 可視化**  
という分析の基本プロセスを自動化できます。

---

## 🛠 使用技術

- Python  
- pandas  
- openpyxl  
- matplotlib  
- Git / GitHub（ブランチ運用）

---
