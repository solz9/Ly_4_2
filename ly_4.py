import pickle
import streamlit as st
import pandas as pd
import numpy as np
st.title('KẾT QUẢ HỌC TẬP LỚP LÝ 4')
y = st.text_input('Nhập họ và tên (Lưu ý: ghi hoa chữ cái đầu)')
if st.button('Kết quả'):
    df = pd.read_excel('DS_10Ly4.xlsx')
    df1 = df[df['Họ và tên'] == y]
    Names = df1['Họ và tên']
    HS1 = df1['HS1']
    BTDDS = df1['BT01 Đúng/Sai']
    BTMM = df1['BT02 Moment']
    Bonus = df1['Điểm cộng']
    KTGK = df1['Điểm KTGK']
    KTCK = df1['Điểm KTCK']
    a = np.array([Names, HS1, BTDDS, BTMM, Bonus, KTGK, KTCK])
    df1 = pd.DataFrame(
        {
            "Họ và tên": a[0],
            "HS1": a[1],
            'BT01 Đúng/Sai': a[2],
            'BT02 Moment': a[3],
            'Điểm cộng': a[4],
            'Điểm KTGK': a[5],
            'Điểm KTCK': a[6]
        }
    )
    hide_dataframe_row_index = """
            <style>
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """

    # Inject CSS with Markdown
    st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)

    # Display an interactive table
    st.table(df1)
