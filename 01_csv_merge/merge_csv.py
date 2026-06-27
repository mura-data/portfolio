import pandas as pd
import glob
from pathlib import Path
import sys

def merge_csv_files(
    input_dir="data",
    output_file="merged.xlsx",
    date_columns=None,
    drop_columns=None
):
    print("=== CSV 結合スクリプト開始 ===")

    # フォルダ存在チェック
    input_path = Path(input_dir)
    if not input_path.exists():
        print(f"[ERROR] 入力フォルダが存在しません: {input_dir}")
        sys.exit(1)

    # CSVファイル取得
    files = glob.glob(f"{input_dir}/*.csv")
    if len(files) == 0:
        print(f"[ERROR] CSVファイルが見つかりません: {input_dir}")
        sys.exit(1)

    print(f"[INFO] 読み込むCSVファイル数: {len(files)}")

    # CSV読み込み
    df_list = []
    for f in files:
        try:
            print(f"[INFO] 読み込み中: {f}")
            df = pd.read_csv(f)
            df_list.append(df)
        except Exception as e:
            print(f"[ERROR] 読み込み失敗: {f} → {e}")

    # 結合
    df = pd.concat(df_list, ignore_index=True)
    print("[INFO] CSV結合完了")

    # 日付列の整形
    if date_columns:
        for col in date_columns:
            if col in df.columns:
                print(f"[INFO] 日付整形: {col}")
                df[col] = pd.to_datetime(df[col], errors="coerce")
            else:
                print(f"[WARN] 日付列が存在しません: {col}")

    # 不要列削除
    if drop_columns:
        for col in drop_columns:
            if col in df.columns:
                print(f"[INFO] 不要列削除: {col}")
                df = df.drop(columns=[col])
            else:
                print(f"[WARN] 削除対象列が存在しません: {col}")

    # Excel出力
    try:
        df.to_excel(output_file, index=False)
        print(f"[SUCCESS] Excel出力完了: {output_file}")
    except Exception as e:
        print(f"[ERROR] Excel出力失敗 → {e}")
        sys.exit(1)

    print("=== スクリプト終了 ===")


if __name__ == "__main__":
    merge_csv_files(
        input_dir="data",
        output_file="merged.xlsx",
        date_columns=["date", "created_at"],
        drop_columns=["unused", "temp"]
    )
