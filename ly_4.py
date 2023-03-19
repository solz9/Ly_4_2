import pickle
import streamlit as st
import pandas as pd
import numpy as np
st.title('KẾT QUẢ HỌC TẬP LỚP LÝ 4')
y = st.text_input('Nhập họ và tên (Lưu ý: ghi hoa chữ cái đầu)')
x = st.text_input("Nhập mật khẩu", type="password")
if st.button('Xem kết quả'):
    df = pd.read_excel('DS_10Ly4 - Copy.xlsx')
    df1 = df[df['Họ và tên'] == y]
    if df1['Password'].values != x:
        st.warning('Bạn đã nhập sai mật khẩu hoặc họ và tên, vui lòng nhập lại')
    else:
        df1 = pd.DataFrame(
            {
                "Họ và tên": df1['Họ và tên'],
                "HS1": df1['HS1'],
                'BT01 Đúng/Sai': df1['BT01 Đúng/Sai'],
                'BT02 Moment': df1['BT02 Moment'],
                'Điểm cộng': df1['Điểm cộng'],
                'Điểm KTGK': df1['Điểm KTGK'],
                'Điểm KTCK':  df1['Điểm KTCK']
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
