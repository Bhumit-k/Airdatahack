
import streamlit as st
import pandas as pd
import home
import plots
# Configure your home page by setting its title and icon that will be displayed in a browser tab.

st.set_page_config(page_title='Dublin Air Quality',
                   page_icon='random',
                   layout='wide',
                   initial_sidebar_state='auto'
                   )
st.title("Dublin Air Quality Measure")
st.sidebar.title("Menu")


# Loading the dataset.
@st.cache()
def load_data():
    # Load the Diabetes dataset into DataFrame.

    df1 = pd.read_csv('Dublin road.csv')
    df1.head()
    df2 = pd.read_csv('https://data.smartdublin.ie/dataset/4976e11e-a015-4ef9-9179-dc7c27fb5a81/resource/a58428ad-3815-4454-82a4-c0e98aca3844/download/airview_dublincity_measurements_ugm3_csv.zip')
    df2.head()
    # Rename the column names in the DataFrame.

    return df1, df2


df_road_data = load_data()

st.title('Dublin Street Air Quality Measure Web App')
pages_dict = {"Home": home,
              "Visualise Decision Tree": plots}

st.sidebar.title('Navigation')
user_choice = st.sidebar.radio('Go To', tuple(pages_dict.keys()))
selected_page = pages_dict[user_choice]
selected_page.app(df_road_data, df_measure_data)
