## 学んだこと
""" 
・情報がばらばらにならないように「データの構造化」を使う 
    →リスト(list)と辞書(dict)
    リスト：複数のデータを順番に管理する  "[]"
    辞書　：キーと値のセットを管理する    "{}"

"""

import csv
import sys

print("家計簿アプリ起動したで")
print("-" * 30)

file_name = 'kakeibo.csv'   # ファイル名を定数として定義
records = []                # 全記録を格納するグローバル関数

""" 
データ読み込み関数
"""
def load_records():
    """ csvファイルからデータを読み込み、recordsリストに格納する。 """
    try:
        with open(file_name, 'r', newline='', encoding='cp932') as f:   # newline='':CSVファイルを扱う際によく使われる設定で、改行コードの処理を適切に行うためのおまじないのようなもの

            reader = csv.DictReader(f)
            # 全データをグローバル関数の records に格納
            global records
            records = list(reader)  #readerからリストに変換して一括代入

        print(f"{file_name} から {len(records)} 件の記録を読み込みました。")
    except FileNotFoundError:
        print(f"{file_name} が見つかりません。新しい家計簿として開始します。")

""" 
残高計算・表示関数
"""
def show_balance():
    """ 記録されているデータを使って残高を計算・表示する。 """
    if not records:
        print("まだ記録ないやん( ﾟДﾟ)ﾊｧ?")
        return
    
    total_balance = 0

    for entry in records:
        try:
            amount = int(entry['amount'])
        except ValueError:
            print(f"エラー:金額データ {entry['amount']} が不正です。スキップします。")
            continue

        category = entry['category']

        if category == '給与':
            total_balance = total_balance + amount
        else:
            total_balance = total_balance - amount

    print("\n--- 現在の残高 ---")
    print(f"{total_balance}円")
    print("-" * 30)

def add_record():
    """ ユーザーから入力を受け付け、新しい記録をrecordsリストに追加する """
    global records
    print("\n---新規記録の入力や")
    date_input = input("日付(例: 2025-10-28)を入力してな: ")
    category = input("項目(例：食費、給与) を入力してな: ")                   # ユーザーに金額の入力を求める
    amount_str = input("金額(数字)を入力してな: ")

    try:
        amount_int  = int(amount_str)
    except ValueError:
        print("エラーや！：金額が不正な値になってるで、記録を追加させるにはあかん。")
        return # 関数の終了
    
    # 辞書の作成
    new_entry = {
        "date": date_input,
        "category": category,
        "amount": amount_int
    }

    records.append(new_entry)

    print(f"記録追加したで！：{category}{amount_int}円")


""" 
メインの処理ループ
"""
def main_loop():
    load_records()

    while True:
        print("\n--- メニュー ---")
        print("1: 記録すんで | 2:残高表示すんで | 3:終了")
        choice = input("どないするん!? (1~3) ：")

        if choice == '1':
            # 記録追加機能の呼び出し
            add_record()

            pass

        elif choice == '2':
            # 残高表示機能の呼び出し
            show_balance()

            pass

        elif choice == '3':
            # データの保存処理
            save_records()
            print("アプリ終了すんで！")
            sys.exit()  # プログラムを終了させる

        else:
            print("無効な数字や！しっかり確認しいや( ﾟДﾟ)」ﾊｧ?")

""" 
データ保存関数
"""
def save_records():
    """ 現在のrevordsリストの内容をCSVファイルに保存する"""
    if not records:
        print("保存する記録はないで！")
        return
    
    fieldnames = ['data', 'category', 'amount']

    try:
        with open(file_name, 'w', newline='', encoding='cp932') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(records)

        print(f"全{len(records)}件の記録を{file_name} に保存しました。")
    except Exception as e:
        print(f"ファイル保存中にエラーが発生しました:{e}")


if __name__ == "__main__":
    main_loop()




""" while True:

    print("\n---新しい記録を入力---")
    date_input = input("日付(例: 2025-10-28) か、 q(終了)を入力してな: ")    # ユーザーから「項目」の入力を受け付ける  #inputは文字列で受け取ってしまう

    if date_input == "q":
        print("じゃあな！")
        break

    category = input("項目(例：食費、給与) を入力してな: ")                   # ユーザーに金額の入力を求める
    amount_str = input("金額(数字)を入力してな: ")

    try:
        # aomunt_str(文字列から整数型に変換)
        amount_int = int(amount_str)
    except ValueError:
        print("エラー:金額は数字で入力してな！記録中止や( ﾟДﾟ)ﾊｧ?")
        continue

        # 取得した3つの変数を適切なキー名で辞書に格納する
    new_entry = {
        "date": date_input,
        "category": category,
        "amount_str": amount_int
    }

    records.append(new_entry)
    print("記録追加したで！")

    print("-" * 30)
    print("入力受付したで！")
    print("合計記録数:", len(records))
    print("記録されたデータや:", records)
 """

""" 
from datetime import datetime as dt
tdatetime = dt.now()
today = tdatetime.strftime('%Y/&m/%d')
"""

