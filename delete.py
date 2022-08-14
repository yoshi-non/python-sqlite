import sqlite3

# データベースを作成、自動コミット機能ON
dbname = 'main.sqlite'

conn = sqlite3.connect(dbname, isolation_level=None)

# SQLiteを操作するためのカーソルを作成
cursor = conn.cursor()

"""
whereのあとに消したいデータの条件を書いて指定
このテーブルの1行目の要素はidなので例としてidが2のデータを指定
"""

cursor.execute('delete from test where id=?', (1,))
conn.commit()  # コミットする

cursor.execute('select * from test')
print(cursor.fetchall())

# 作業完了したらDB接続を閉じる
conn.close()
