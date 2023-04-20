from train import *

# Set Page title as "Reverse Image Search" and icon as " Party "
st.set_page_config(page_title = "Reverse Image Search", 
                   page_icon = ":tada:",
                       layout = "wide")


# Add custom Theme
with open("cascade_style.css") as design:
     st.markdown(f"<style>{design.read()}</style>", unsafe_allow_html=True)

def urlInput(N_PICS, n_cols):
    url = st.text_input("Enter Image URL")
    if url!='':
         response=requests.get(url)
         img = Image.open(BytesIO(response.content))
         file_path = os.path.abspath(os.path.join("upload","temp.jpg"))
         
         with open(file_path,"wb") as f:
              f.write(response.content)
         
         image2 = Image.open(file_path)
         new_img = image2.resize((600,400))
         st.write("<div class='stAlert success'>{}</div>".format("Uploaded Image"), 
                  unsafe_allow_html=True)
         st.info('Image path of Upload Image to local storage: : {}'.format(file_path))
         st.image(new_img)

         st.write("<div class='stAlert success'>{}</div>".format("Predicted Images"), 
                  unsafe_allow_html=True)
         
         with st.spinner('Wait for it...'):
            indices, filenames = upload(N_PICS,file_path)
            time.sleep(5)
            
         n_rows = int(1 + N_PICS // n_cols)
         columns = [st.columns(n_cols) for n_rows in range(n_rows)]
         for row in range(n_rows):
            for col in range(n_cols):
                index = row * n_cols + col
            
                with columns[row][col]:
                    try:
                        img_paths = os.path.abspath(os.path.join("",filenames[indices[index]]))
                                                                
                        image1 = Image.open(img_paths)
                        new_image2 = image1.resize((600, 400))
                        st.warning('Image path of Predicted Image : {}'.format(img_paths))
                        st.image(new_image2, use_column_width=True)
                    except IndexError as e:
                        pass
         
         
    

def imgInput(N_PICS, n_cols):
     uploaded_file = st.file_uploader("Test Your Image Here...", type=['png', 'jpeg', 'jpg'])
     if uploaded_file is not None:
        img = Image.open(uploaded_file)
        file_path = os.path.abspath(os.path.join("upload", uploaded_file.name))
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        image = Image.open(file_path)
        new_image1 = image.resize((600, 400))
        
        st.write("<div class='stAlert success'>{}</div>".format("Uploaded Image"), unsafe_allow_html=True)
        st.info('Image path of Uploaed Image: : {}'.format(file_path))
        st.image(new_image1)
        
        st.write("<div class='stAlert success'>{}</div>".format("Predicted Images"), 
                  unsafe_allow_html=True)
        
        with st.spinner('Wait for it...'):
            indices, filenames = upload(N_PICS, file_path)
            time.sleep(5)        
                    
        n_rows = int(1 + N_PICS // n_cols)
                   
        columns = [st.columns(n_cols) for n_rows in range(n_rows)]
        for row in range(n_rows):
                        for col in range(n_cols):
                            index = row * n_cols + col
                            with columns[row][col]:
                                try:
                                    img_paths = os.path.abspath(os.path.join("",filenames[indices[index]]))
                                                                
                                    image1 = Image.open(img_paths)
                                    new_image2 = image1.resize((600, 400))
                                    st.warning('Image path of Predicted Image : {}'.format(img_paths))
                                    st.image(new_image2, use_column_width=True)
                                                        
                                except IndexError as e:
                                    pass
                             


def aboutMe():
     url = "https://pps.whatsapp.net/v/t61.24694-24/315364770_915441406250802_1676761084597339606_n.jpg?ccb=11-4&oh=01_AdRRcrw63nqMyFvgrdVx2AxO8t4QzNAXDsazgVRoVY-43w&oe=64422DF1"
     response=requests.get(url)
     img = Image.open(BytesIO(response.content))
     file_path = os.path.abspath(os.path.join("","author.jpg"))
     
     with open(file_path,"wb") as f:
          f.write(response.content)
     image2 = Image.open(file_path)
     new_img = image2.resize((600,400))
     st.image(new_img)
     os.remove(file_path)
     st.write("<div class='abc'> <div class='stAlert success12'>{}</div> </div>".format("Krup Kachhia"), 
                  unsafe_allow_html=True)
     st.write("\n")
     st.write("\n")
     st.write("<div class='about'>{}</div>".format(ABOUT_ME), unsafe_allow_html=True)
     




def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def main():
    st.write("<h1 class='h1_style'>Reverse Image Search</h1>", unsafe_allow_html=True)
    
    url = requests.get("https://assets4.lottiefiles.com/packages/lf20_69HH48.json")
    url_json = dict()

    if url.status_code == 200:
        url_json = url.json()
    else:
        print("Error in the URL")
    st_lottie(url_json,reverse = True,speed=1,loop=True,quality='high',key='Animation')


    with st.sidebar.container():
        st.sidebar.title(':toolbox: Options')

    with st.sidebar.container():   
         N_PICS = st.slider('Predicted Images', 0, 15, 5)
         n_cols = st.slider('No. of Grids', 0, 5, 2)
         st.sidebar.title(':house: Home')
         datasrc = st.sidebar.radio("Select Input Source",
                                    ['From Device', 'From URL']) 
           
    with st.sidebar.container():
         if st.button(':male-detective:  About Us'):
              datasrc = 'About Us'
       
    if datasrc == "From Device":
            imgInput(N_PICS,n_cols)

    elif datasrc == "From URL":
            urlInput(N_PICS,n_cols)
    
    elif datasrc == "About Me":
         aboutMe()
    


if __name__ == '__main__':
    main()
    