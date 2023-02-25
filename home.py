import streamlit as st

def app(road_df, measure_df):
    st.markdown(
        "<p style='color:red'>Diabetes is a chronic (long-lasting) health condition that affects how your body turns food into energy."
        "There isn’t a cure yet for diabetes, but losing weight, eating healthy food, and being active can really help in reducing the impact of diabetes."
        "This Web app will help you to predict whether a person has diabetes or is prone to get diabetes in future by analysing the values of several features using the Decision Tree Classifier.",
        unsafe_allow_html=True)
    # For road data df
    with st.expander('View Road Data Database'):
        st.dataframe(road_df)
    st.subheader('Columns description for road data')
    col_name, col_dtype, col_display = st.columns(3)
    if col_name.checkbox('Show all column names'):
        st.table(road_df.columns)
    if col_dtype.checkbox('View column datatype'):
        st.write(list(road_df.dtypes))
    if col_display.checkbox('View Column data'):
        col = st.selectbox('Select columns', road_df.columns)
        st.table(road_df[col])
    # For measure data df
    with st.expander('View Time Wise Measure Database'):
        st.dataframe(measure_df)
    st.subheader('Columns description for measure data')
    col_names, col_dtypes, col_displays = st.columns(3)
    if col_names.checkbox('Show all column name'):
        st.table(measure_df.columns)
    if col_dtypes.checkbox('View column datatypes'):
        st.write(list(measure_df.dtypes))
    if col_displays.checkbox('View Column wise data'):
        col = st.selectbox('Select columns', measure_df.columns)
        st.table(measure_df[col])