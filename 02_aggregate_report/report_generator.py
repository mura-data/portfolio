import pandas as pd
from pathlib import Path
import sys

def generate_report(
    input_file="data/merged.xlsx",
    output_file="output/report.xlsx",
    group_columns=["category"],
    agg_settings={"amount": "sum"}
):
    print("=== 集計レポート生成開始 ===")

    # 入力ファイルチェック
    input_path = Path(input_file)
    if not input_path.exists():
        print(f"[ERROR] 入力ファイルが存在しません: {input_file}")
        sys.exit(1)

    # 読み込み
    try:
        df = pd.read_excel(input_file)
        print("[INFO] データ読み込み完了")
    except Exception as e:
        print(f"[ERROR] 読み込み失敗 → {e}")
        sys.exit(1)

    # 集計処理
    try:
        report = df.groupby(group_columns).agg(agg_settings).reset_index()
        print("[INFO] 集計処理完了")
    except Exception as e:
        print(f"[ERROR] 集計処理失敗 → {e}")
        sys.exit(1)

    # 出力フォルダ作成
    output_path = Path(output_file).parent
    output_path.mkdir(exist_ok=True)

    # Excel 出力
    try:
        report.to_excel(output_file, index=False)
        print(f"[SUCCESS] レポート出力完了: {output_file}")
    except Exception as e:
        print(f"[ERROR] Excel出力失敗 → {e}")
        sys.exit(1)

    print("=== スクリプト終了 ===")


if __name__ == "__main__":
    generate_report(
        input_file="data/merged.xlsx",
        output_file="output/report.xlsx",
        group_columns=["category"],
        agg_settings={"amount": "sum"}
    )
