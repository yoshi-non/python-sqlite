import sqlite3

# データベースを作成、自動コミット機能ON
dbname = 'main.sqlite'

conn = sqlite3.connect(dbname, isolation_level=None)

# SQLiteを操作するためのカーソルを作成
cursor = conn.cursor()

"""
レコードを追加する場合はinsert文を使う。
SQLインジェクションという不正SQL命令への脆弱性対策でpythonの場合は「？」を使用して記載するのが基本。
"""
sql = """INSERT INTO test (name, age) VALUES(?, ?)"""  # ?は後で値を受け取るよという意味

data = (('Pekora', 2000000))  # 挿入するレコードを指定
cursor.execute(sql, data)  # executeコマンドでSQL文を実行
conn.commit()  # コミットする

# 作業完了したらDB接続を閉じる
conn.close()
