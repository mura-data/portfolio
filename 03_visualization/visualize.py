import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import sys

def visualize(
    input_file="data/report.xlsx",
    output_dir="output",
    x_column="category",
    y_column="amount",
    chart_title="Sales by Category",
    chart_file="chart_category_amount.png"
):
    print("=== 可視化処理開始 ===")

    # 入力チェック
    input_path = Path(input_file)
    if not input_path.exists():
        print(f"[ERROR] 入力ファイルが存在しません: {input_file}")
        sys.exit(1)

    # データ読み込み
    try:
        df = pd.read_excel(input_file)
        print("[INFO] データ読み込み完了")
    except Exception as e:
        print(f"[ERROR] 読み込み失敗 → {e}")
        sys.exit(1)

    # 出力フォルダ作成
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)

    # グラフ作成
    try:
        plt.figure(figsize=(8, 5))
        plt.bar(df[x_column], df[y_column], color="skyblue")
        plt.title(chart_title)
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.tight_layout()

        save_path = output_path / chart_file
        plt.savefig(save_path)
        plt.close()

        print(f"[SUCCESS] グラフ出力完了: {save_path}")
    except Exception as e:
        print(f"[ERROR] グラフ作成失敗 → {e}")
        sys.exit(1)

    print("=== 可視化処理終了 ===")


if __name__ == "__main__":
    visualize(
        input_file="data/report.xlsx",
        output_dir="output",
        x_column="category",
        y_column="amount",
        chart_title="Sales by Category",
        chart_file="chart_category_amount.png"
    )
