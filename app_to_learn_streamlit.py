#pip install streamlit matplotlib pandas

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Widgets", "Data Visualization", "File Uploader", "About","More Details"])


if page == "Home":
    # Title of the app
    st.title("st.title() is used to write titles .")

# Header
    st.header("st.header() is used to write headers.")

# Text
    st.write("st.write() is used to write text.")

    st.write("""
    ### What is Streamlit?
    Streamlit is a Python library that makes it easy to create web apps for data science and machine learning.
    """)
    
    st.image("https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png", width=300)

elif page == "Widgets":
    st.header("Interactive Widgets")
    st.write("""
    ### Try these widgets:
    """)

    slider_value = st.slider("Select a number", 0, 100)
    st.write(f"You selected: **{slider_value}**")

    
    name = st.text_input("Enter your name:")
    if name:
        st.write(f"Hello, **{name}**!")

    
    if st.button("Click me"):
        st.write("You clicked the button!")


elif page == "Data Visualization":
    st.header("Data Visualization with Matplotlib")
    st.write("""
    ### Simple Line Plot
    Below is a line plot generated using Matplotlib.
    """)
    #some data to check
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 7, 11]
    
    fig, ax = plt.subplots()
    ax.plot(x, y, marker="o")
    ax.set_title("Simple Line Plot")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    st.pyplot(fig)

# for uploading files
elif page == "File Uploader":
    st.header("File Uploader")
    st.write("""
    ### Upload a File
    You can upload a CSV or text file to see its contents.
    """)
    
    uploaded_file = st.file_uploader("Choose a file", type=["csv", "txt"])
    if uploaded_file is not None:
        
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
            st.write("### File Contents")
            st.write(df)
        
        elif uploaded_file.name.endswith(".txt"):
            text = uploaded_file.read().decode("utf-8")
            st.write("### File Contents")
            st.write(text)


elif page == "About":
    st.header("About This App")
    st.write("""
    ### This webapp is made by Sakir.
    """)
    
elif page == "More Details":
    st.header("More Details About Streamlit")
    st.write("""
    ### What is Streamlit?
    Streamlit is a powerful open-source Python library designed to simplify the creation and sharing of beautiful, interactive web applications for machine learning and data science projects. It eliminates the need for extensive front-end web development knowledge, allowing data scientists to focus on their core expertise: data and models.

    ### Why Streamlit is Ideal for Data Scientists:
    - **No Front-End Experience Required:** Streamlit abstracts away the complexities of HTML, CSS, and JavaScript, enabling data scientists to build web apps using only Python.
    - **Rapid Development:** Create functional and visually appealing applications in hours or even minutes, rather than days or weeks.
    - **Intuitive API:** Streamlit's API is designed for ease of use, with simple commands for displaying data, visualizations, and interactive widgets.
    - **Seamless Python Integration:** Works seamlessly with popular Python libraries like Pandas, Matplotlib, Seaborn, Plotly, Keras, PyTorch, and more.
    - **Data Caching:** Streamlit's caching mechanism optimizes performance by storing and reusing computation results, speeding up app execution.

    ### Installation:
    Streamlit can be installed using `pip`:
    ```bash
    pip install streamlit
    ```

    ### Running Streamlit Apps:
    To run your Streamlit app, save your Python code in a file (e.g., `my_app.py`) and execute the following command in your terminal:
    ```bash
    streamlit run my_app.py
    ```

    ### Core Streamlit Features and Commands:
    - **Displaying Text:** `st.write()`, `st.title()`, `st.header()`, `st.markdown()`, `st.subheader()`, `st.caption()`, `st.code()`, `st.latex()`
    - **Displaying Media:** `st.image()`, `st.audio()`, `st.video()`
    - **Input Widgets:** `st.checkbox()`, `st.button()`, `st.radio()`, `st.selectbox()`, `st.multiselect()`, `st.select_slider()`, `st.slider()`, `st.number_input()`, `st.text_input()`, `st.date_input()`, `st.time_input()`, `st.text_area()`, `st.file_uploader()`, `st.color_picker()`
    - **Progress and Status:** `st.balloons()`, `st.progress()`, `st.spinner()`, `st.success()`, `st.error()`, `st.warning()`, `st.info()`, `st.exception()`
    - **Layout and Structure:** `st.sidebar`, `st.container()`
    - **Data Visualization:** `st.pyplot()`, `st.line_chart()`, `st.bar_chart()`, `st.area_chart()`, `st.altair_chart()`, `st.graphviz_chart()`

    ### Example (Combining elements):
    ```python
    import streamlit as st
    import pandas as pd
    import matplotlib.pyplot as plt

    st.title("My Streamlit App")

    data = {'x': [1, 2, 3, 4, 5], 'y': [2, 4, 1, 3, 5]}
    df = pd.DataFrame(data)

    st.write("Here's my data:")
    st.dataframe(df)

    st.line_chart(df)

    if st.checkbox("Show bar chart"):
        fig, ax = plt.subplots()
        ax.bar(df['x'], df['y'])
        st.pyplot(fig)

    user_input = st.text_input("Enter some text:")
    st.write("You entered:", user_input)
    ```

    ### Learn More:
    - [Streamlit Tutorial by DataCamp](https://www.datacamp.com/tutorial/streamlit)
    - [Streamlit Documentation](https://www.datacamp.com/tutorial/streamlit)
    """)


if st.sidebar.button("This app is created to teach my beloved classmates the use of streamlit library"):
    st.balloons()