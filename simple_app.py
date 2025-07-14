""""
[実行方法]　Anaconda promp で　streamlit　環境を起動して、
streamlit run simple_app.py
コマンドで実行する
"""


import streamlit as st

#タイトル表示
st.title("簡単な Streamlit アプリ")

#ユーザーテキスト入力をしてもらう
name = st.text_input("あなたの名前を入力してください")

#　ユーザーにスライダーで入力してもらう
age = st.slider("年齢を選んでください", 0,100,25)

#結果表示
if name: #nameという変数が空(null)ではなかったら
    st.write(f"こんにちは、{name}さん！　あなたは{age}歳ですね。")
    st.write(f"{age-5}歳にしか見えないですけど")
else:
    st.write("上の入力欄に名前を入力してください。")


