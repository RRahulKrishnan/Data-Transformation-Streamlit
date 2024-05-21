import streamlit as st
import pandas as pd

def main():
  """Streamlit app's main function."""
  st.set_page_config(layout='wide')
  st.title("Data Preprocessing Preview")
  st.write("Upload your CSV data for a preview.")

  uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

  if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    #Start of Upload
    st.header("Uploaded Data Preview :")
    st.dataframe(df)  # Show a preview of the rows
    st.write("**Note:** This is just a preview, scroll down for analysed & transformed dataset")
    #End of Upload

    #Start of Analysis
    st.header("Analyzed Data Preview :")
    st.write("**Basic Analysed Data :**")
    st.write (df.describe()) #Show basic analysed data

    st.write("**Basic Information of Data :**")
    #Show basic information of data

    st.write("**Sum of rows that are null :**")
    st.write (df.isnull().sum()) # Show sum of rows that are null
    #Start of Analysis
    
    st.header("Transformed Data Preview :")

    st.write("**Preview after removing duplicates :**")
    df.drop_duplicates(inplace=True)
    st.write (df)


if __name__ == "__main__":
  main()
