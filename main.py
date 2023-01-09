import streamlit as st
import numpy as np
import pandas as pd
st.title('Steamlit 基礎')
st.write('Hello World!')
st.write('I love World')

df = pd.DataFrame({
    '1列目': [1,2,3,4],
    '2列目': [10,20,30,40]
})
st.dataframe(df.style.highlight_between(axis=1), width=300,height=150)
df_1 = pd.DataFrame(
    np.random.rand(10,3),
    columns=['a','b','c'])
st.dataframe(df_1)
st.line_chart(df_1)
st.bar_chart(df_1)
df_m = pd.DataFrame(

    # 乱数 + 新宿の緯度と経度
    np.random.rand(100,2) / [50, 50] + [35.69, 139.70],
    columns = ['lat', 'lon']
)
st.map(df_m)
from PIL import Image
if st.checkbox('Show Image'):  
    img = Image.open('/Users/tetsu/Desktop/streamlit/Iris.jpg')
    st.image(img, caption='Iris', use_column_width=True)
option = st.selectbox('好きな数字を入れてください。', list(range(1,11)))
'好きな数字は、',option,'です。'
text = st.sidebar.text_input('好きなスポーツを入力してください。')
'好きなスポーツは　　',text,'です。'
condition = st.sidebar.slider('貴方の調子は',0,100,50)
'Condition', condition
expander1 =st.expander('Question1')
expander1.write('Answer of Question1')
expander2 =st.expander('Question2')
expander2.write('Answer of Question2')
import time

latest_iteration = st.empty()
bar = st.progress(0)

# プログレスバーを0.1秒毎に進める
for i in range(100):
    latest_iteration.text(f'Iteration{i + 1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done'