import sqlite3

# データベースを作成、自動コミット機能ON
dbname = 'main.sqlite'

conn = sqlite3.connect(dbname, isolation_level=None)

# SQLiteを操作するためのカーソルを作成
cursor = conn.cursor()

"""
・create table テーブル名（作成したいデータカラム）というSQL文でテーブルを宣言
    ※SQL命令は大文字でも小文字でもいい
・今回はtestテーブルに「id,name,date」カラム(列名称)を定義する※今回dateは生年月日という列
・「if not exists」はエラー防止の部分。すでに同じテーブルが作成されてるとエラーになる為
・カラム型は指定しなくても特には問題ない
    ※NULL, INTEGER(整数), REAL(浮動小数点), TEXT(文字列), BLOB(バイナリ)の5種類
"""
# テーブルの作成

sql = """CREATE TABLE IF NOT EXISTS test(id integer primary key autoincrement, name text, age integer)"""

cursor.execute(sql)
# conn.commit() #データベースにコミット(自動コミット設定がない場合記載必要)


# データベース中のテーブル名を取得するSQL関数
sql = """SELECT name FROM sqlite_master WHERE TYPE='table'"""

for t in cursor.execute(sql):  # for文で作成した全テーブルを確認していく
    print(t)

"""
select * ですべてのデータを参照し、fromでどのテーブルからデータを呼ぶのか指定
fetchallですべての行のデータを取り出す
"""
sql = """SELECT * FROM test"""
cursor.execute(sql)
print(cursor.fetchall())  # 全レコードを取り出す

# 作業完了したらDB接続を閉じる
conn.close()
