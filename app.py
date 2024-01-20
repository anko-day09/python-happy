import streamlit as st
import random
import time
from math import sin, cos

def get_happy_word():
    happy_words = ["お疲れ様！", "がんばってるね！", "自分をほめちゃお！", "こんなに頑張ってるなんて惚れちゃう！", "休憩もとってね", "ご褒美何にする？", "めっちゃ頭いいやん！", "すばらしい！", "こんなことできるなんて素敵！", "自信もって！！"]
    return random.choice(happy_words)

def get_random_heart_position():
    # ハート型の方程式
    t = random.uniform(0, 2 * 3.14159)
    x = 16 * pow(sin(t), 3)
    y = 13 * cos(t) - 5 * cos(2*t) - 2 * cos(3*t) - cos(4*t)
    scale = 0.04  # スケール調整
    return (x * scale + 0.5, y * scale + 0.5)

def get_random_font_and_size():
    fonts = ["Arial", "Helvetica", "Times New Roman", "Courier New"]
    font = random.choice(fonts)
    size = random.randint(14, 20)
    return {"font": font, "size": size}

def happy_words_heart_app():
    st.title("メンタルわっしょいジェネレータ")

    # ループでランダムな座標に幸せな言葉を表示
    while True:
        # 幸せな言葉とその他のランダムな設定を取得
        happy_word = get_happy_word()
        position = get_random_heart_position()
        text_style = get_random_font_and_size()

        # ユーザーにメッセージを表示
        st.markdown(
            f"""
            <div id="word" style="position:absolute; left:{position[0] * 100}%; top:{position[1] * 100}%; font-family:{text_style["font"]}; font-size:{text_style["size"]}px; animation: fade 8s linear; opacity: 0;">{happy_word}</div>
            <style>
                @keyframes fade {{
                    from {{ opacity: 1; }}
                    to {{ opacity: 0; }}
                }}
            </style>
            """,
            unsafe_allow_html=True
        )

        # 少し待機して次の言葉へ
        time.sleep(1)

# Streamlitアプリを起動
if __name__ == '__main__':
    happy_words_heart_app()
