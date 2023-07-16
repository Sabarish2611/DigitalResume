# ---- Importing Required Packages ----

import json
from PIL import Image
import streamlit as st
from pathlib import Path
from streamlit_lottie import st_lottie


def load_lottiefile(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)


lottie_hello = load_lottiefile(r'hello.json')

# ---- Path Settings ----
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file_path = current_dir / "styles" / "main.css"
resume_file_path = current_dir / "assets" / "Sabarishwaran's_Resume.pdf"
profile_pic_path = current_dir / "assets" / "pp.jpeg"

# ---- General Settings ----
page_title = 'Digital Resume | Sabarishwaran G'
page_icon = ':wave:'
name = 'Sabarishwaran G'
description = 'Data Scientist, Trellix'
email = 'sabarish261101@gmail.com'
social_media = {
    'LinkedIn': 'https://www.linkedin.com/in/sabarish2611/',
    'GitHub': 'https://github.com/Sabarish2611',
    'Kaggle': 'https://www.kaggle.com/sabarish2611'
}

st.set_page_config(page_title, page_icon)
st.title('Hello There :wave:')

# ---- Loading Assets ----
with open(css_file_path) as css_file:
    st.markdown("<style>{}<style>".format(css_file.read()), unsafe_allow_html=True)

profile_pic = Image.open(profile_pic_path)

with open(resume_file_path, 'rb') as file:
    pdf_byte = file.read()

# ---- Profile Section ----
col1, col2 = st.columns(2, gap='small')

with col1:
    st_lottie(
        lottie_hello,
        speed=1,
        reverse=False,
        loop=True,
        quality='high',
    )

with col2:
    st.title(name)
    st.write(description)
    st.download_button(label='Download Resume ⇩', data=pdf_byte, file_name=resume_file_path.name,
                       mime='application/octet-stream')
    st.write(f'✉️ {email}')

# ---- Social Links ----
st.write('#')

cols = st.columns(len(social_media))
for index, (platform, link) in enumerate(social_media.items()):
    cols[index].write(f'[{platform}]({link})')

# ---- Education ----
st.write('#')
st.subheader('Education')
st.write(
    """ 
    - ⟣ B.Tech in Artificial Intelligence, Amrita Vishwa Vidyapeetham, Coimbatore.
    - ⟣ XII, Kamala Niketan Montessori School, Trichy.
    - ⟣ X, kamla Niketan Montessori School, Trichy.
    """
)

# ---- Skills ----
st.write('#')
st.subheader('Skills')
st.write(
    """ 
    - ⟣ ⌨️ Programming : Python, SQL, MATLAB
    - ⟣ 📉 Data Analysis : PowerBi, MySQL, Tableu
    - ⟣ ☁️ Cloud : AWS
    - ⟣ 🤖️ Artificial Intelligence : Machine Learning, Deep Learning
    - ⟣ 📚 Statistical Analysis
    """
)

# ---- Experience ----
st.write('#')
st.subheader('Experience')
st.write("---------")
st.write("- Data Scientist at Trellix")
st.write("06/2023 --> Present")

# ---- Internships ----
st.write('#')
st.subheader('Internships')
st.write("----")
st.write("- Data Science Intern at Trellix")
st.write("03/2023 --> 06/2023")

st.write("- Software Engineer Intern at Trellix")
st.write("01/2023 --> 03/2023")

st.write("- Computational Linguist Intern at PanLingua")
st.write("05/2021 --> 08/2023")
