import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

# st.write('DataFrame')

_ = """ !!!!!!!!!!streamlitで複数行コメントアウトは _ = を入れないとブラウザで表示されてしまう
df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})

st.dataframe(df)
st.dataframe(df, width=300, height=300)
st.dataframe(df.style.highlight_max(axis=0))
"""

_ = """マークダウン
# 章
# 節
# 項
```python
```
"""

_ = """
df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)
st.dataframe(df)
st.line_chart(df)
st.area_chart(df)
"""

_ = """
df = pd.DataFrame(
    np.random.rand(100, 2) / [50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)
# st.dataframe(df)
st.map(df)
"""

# st.write('Display Image')
_ = """
img = Image.open('kitten.jpeg')
st.image(img, caption='かわいい子猫', use_column_width=True)
"""

# st.write('Interactive widgets')
_ = """
if st.checkbox('Show Image'):
    img = Image.open('kitten.jpeg')
    st.image(img, caption='かわいい子猫')  # , use_column_width=True)
"""
_ = """
option = st.selectbox(
    'あなたが好きな数字を教えてください。',
    list(range(1, 11))
)
'あなたが好きな数字は、', option, 'です。'
"""
_ = """
text = st.text_input('あなたの趣味を教えてください')
'あなたの趣味：', text, 'です。'
"""
_ = """
condition = st.slider('アタなの今の調子は？', 0, 100, 50)
'コンディション：', condition
"""
_ = """
text = st.sidebar.text_input('あなたの趣味を教えてください')
'あなたの趣味：', text, 'です。'
condition = st.sidebar.slider('アタなの今の調子は？', 0, 100, 50)
'コンディション：', condition
"""

st.write('プログレスバーの表示')

'Start!!'
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.05)


left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の回答')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3の回答')
