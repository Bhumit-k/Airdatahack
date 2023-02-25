import warnings
from io import StringIO
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import streamlit as st
from sklearn import tree
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


def app(road_df, measure_df):
    warnings.filterwarnings('ignore')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.title("Visualise Dublin Air Quality")

    if st.checkbox("Show the correlation heatmap"):
        st.subheader("Correlation Heatmap")
        plt.figure(figsize=(10, 6))
        ax = sns.heatmap(road_df.iloc[:, 1:].corr(),
                         annot=True)  # Creating an object of seaborn axis and storing it in 'ax' variable
        bottom, top = ax.get_ylim()  # Getting the top and bottom margin limits.
        ax.set_ylim(bottom + 0.5, top - 0.5)  # Increasing the bottom and decreasing the top margins respectively.
        st.pyplot()

    st.subheader("Predictor Selection")
