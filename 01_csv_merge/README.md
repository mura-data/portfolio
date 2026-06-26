# CSV Merge Tool  
複数の CSV ファイルを結合し、日付整形・不要列削除を行ったうえで Excel ファイルとして出力する Python スクリプトです。

中小企業の業務自動化や、定期レポート作成の前処理として利用できます。

---

## 🚀 機能概要

- 指定フォルダ内の CSV をすべて読み込み
- 1つの DataFrame に結合
- 指定した日付列を datetime 型に変換
- 指定した不要列を削除
- Excel（.xlsx）として出力
- ログ表示による処理状況の可視化
- エラーハンドリング付き

---

## 📁 フォルダ構成
```
├── merge_csv.py
└── data/
    ├── sample1.csv
    └── sample2.csv
```

`data/` フォルダ内の CSV が自動的に処理対象になります。

---

## 🛠 使い方

### 1. 必要ライブラリのインストール

```bash
pip install pandas openpyxl
```

### 2. data/ フォルダに CSV を配置
例：
date,category,amount,unused
2024-01-01,A,100,xxx
複数ファイルを入れると自動で結合されます。

### 3. スクリプトを実行
```bash
python merge_csv.py
```

### 4. 出力
同じフォルダに merged.xlsx が生成されます。

