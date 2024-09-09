import streamlit as st
from utils import YarnDetail, SampleFabric

if "is_y_density_needed" not in st.session_state:
    st.session_state.is_y_density_needed = False
if "is_weight_already" not in st.session_state:
    st.session_state.is_weight_already = False
if "yarns_count" not in st.session_state:
    st.session_state.yarns_count = 1
if "yarns_details" not in st.session_state:
    st.session_state.yarns_details = []
if "yarn_raw_count" not in st.session_state:
    st.session_state.yarn_raw_count = 0
if "sample_fabric" not in st.session_state:
    st.session_state.sample_fabric = SampleFabric()

st.header("✨样布规格计算器")
st.divider()
col1, col2 = st.columns(2)
col1.subheader("1️⃣基本规格")
col1.divider()
col1.markdown("##### 克重")

if col1.checkbox("是否已有克重？", value=False):
    st.session_state.is_weight_already = True
    st.session_state.sample_fabric.fabric_weight = col1.number_input("请输入克重（GSM）：")
else:
    st.session_state.is_weight_already = False
    st.session_state.sample_fabric.length = col1.number_input("请输入长（cm）：")
    st.session_state.sample_fabric.width = col1.number_input("请输入宽（cm）：")
    st.session_state.sample_fabric.weight = col1.number_input("请输入称重（g）：", format="%.3f")

col1.divider()
col1.markdown("##### 密度")

if col1.checkbox("是否需要纵密？", value=False):
    st.session_state.is_y_density_needed = True
    st.session_state.sample_fabric.density_x_count = col1.number_input("请输入针数：")
    st.session_state.sample_fabric.density_x_length = col1.number_input("请输入横向长度（cm）：")
    st.session_state.sample_fabric.density_y_count = col1.number_input("请输入路数：")
    st.session_state.sample_fabric.density_y_length = col1.number_input("请输入纵向长度（cm）：")
else:
    st.session_state.is_y_density_needed = False
    st.session_state.sample_fabric.density_x_count = col1.number_input("请输入针数：")
    st.session_state.sample_fabric.density_x_length = col1.number_input("请输入横向长度（cm）：")

col1.divider()
col1.markdown("##### 纱线")
st.session_state.yarns_count = col1.number_input("请输入所用纱线数：", min_value=1, max_value=10)

col2.subheader("2️⃣纱线详情")
st.session_state.yarns_details.clear()
for i in range(0, st.session_state.yarns_count):
    st.session_state.yarns_details.append(YarnDetail())

col2.divider()
col2.markdown("##### 线长")
st.session_state.yarn_raw_count = col2.number_input("请输入针数：", min_value=1, max_value=80, value=50)

for i in range(0, st.session_state.yarns_count):
    st.session_state.yarns_details[i].raw_length = col2.number_input(f"请输入纱线{i + 1}测量长度（cm）:", min_value=0.1)
    st.session_state.yarns_details[i].raw_count = st.session_state.yarn_raw_count

col2.divider()
col2.markdown("##### 纱支")
for i in range(0, st.session_state.yarns_count):
    st.session_state.yarns_details[i].cal_length = col2.number_input(f"请输入纱线{i + 1}纱支测量长度（cm）:",
                                                                     min_value=0.1)
    st.session_state.yarns_details[i].cal_count = col2.number_input(f"请输入纱线{i + 1}测量根数:")
    st.session_state.yarns_details[i].cal_weight = col2.number_input(f"请输入纱线{i + 1}测量重量（g）:", format="%.3f")
    col2.divider()

st.divider()
if st.button("开始计算"):
    st.divider()
    st.subheader("✅计算结果：")
    if st.session_state.is_weight_already:
        st.markdown(f"##### 克重：{st.session_state.sample_fabric.fabric_weight}")
    else:
        st.markdown("##### 克重：" + st.session_state.sample_fabric.get_gsm())

    st.markdown(f"##### 横密：" + st.session_state.sample_fabric.get_density_x())
    if st.session_state.is_y_density_needed:
        st.markdown(f"##### 纵密：" + st.session_state.sample_fabric.get_density_y())

    st.markdown("\n\n")
    st.markdown(f"##### 线长")

    for i in range(0, st.session_state.yarns_count):
        st.write(f"纱线{i + 1}：" + st.session_state.yarns_details[i].cal_line_length())

    st.markdown("\n\n")
    st.markdown(f"##### 纱支")
    for i in range(0, st.session_state.yarns_count):
        st.write(f"纱线{i + 1}支数：" + st.session_state.yarns_details[i].cal_staple())
        st.write(f"纱线{i + 1}旦数：" + st.session_state.yarns_details[i].cal_denier())
        st.markdown("\n\n")
