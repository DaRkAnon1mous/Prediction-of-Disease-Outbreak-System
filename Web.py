import os
import pickle ## for pre trained model loading
import streamlit as st ## for web app
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Prediction of Disease Outbreaks',
                   layout='wide',
                   page_icon="🧑‍⚕️")

model_dir = os.path.join(os.path.dirname(__file__), "Training_Models")

with open(os.path.join(model_dir, "diabetes_model.sav"), "rb") as model_file:
    diabetes_model = pickle.load(model_file)

with open(os.path.join(model_dir, "Heart_disease_model.sav"), "rb") as model_file:
    heart_disease_model = pickle.load(model_file)

with open(os.path.join(model_dir, "Parkinsons_Model.sav"), "rb") as model_file:
    parkinsons_model = pickle.load(model_file)



with st.sidebar:
    selected = option_menu('Prediction of disease outbreak system',['Diabetes Prediction','Heart Disease Prediction','Parkinsons Prediction'],
                           menu_icon='hospital-fill',icons=['activity','heart','person'],
                           default_index=0)

## Diabetes Prediction

if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    col1,col2,col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input("Number of Pregnancies")
    with col2:
        Glucose = st.text_input("Glucose Level")
    with col3:
        Bloodpressure = st.text_input('Blood Pressure Value')
    with col1:
        SkinThicknes = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input("Insulin Value")
    with col3:
        BMI = st.text_input("BMI value")
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Values')
    with col2:
        Age = st.text_input("Age of the person")


    diab_diagnosis = ''
    if st.button('Test Result'):
        try:
            user_input = [Pregnancies,Glucose,Bloodpressure,SkinThicknes,Insulin,BMI,DiabetesPedigreeFunction,Age]
            user_input=[float(x) for x in user_input]
            diab_prediction = diabetes_model.predict([user_input])
            if diab_prediction[0] == 1:
                diab_diagnosis='The person is Diabetic'
            else:
                diab_diagnosis = 'The person is not Diabetic'
        except ValueError:
            st.error("Please enter valid numeric values in all fields.")
    st.success(diab_diagnosis)



## Heart Disease Prediction
elif selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    col1,col2,col3 = st.columns(3)
    with col1:
        Age = st.text_input("Age of the Person")
    with col2:    
        Sex = st.text_input("Sex (Enter  '1'  if  Male  and  '0'  if  Female)")
    with col3:
        ChestPT = st.text_input('Chest Pain Types Total Count')
    with col1:
        RestBP = st.text_input('Resting Blood Pressure')
    with col2:
        SerumChl = st.text_input("Serum Cholestrol in mg/dl")
    with col3:
        FastBS = st.text_input("Fast Blood Sugar > 120 mg/dl")
    with col1:
        RestElecR = st.text_input("Resting Electocardiographic Results")
    with col2:
        MheartRate = st.text_input('Maximum Heart Rate Achieved')
    with col3:
        EandiceAng = st.text_input("Exercise Induced Angina")
    with col1:
        STdepres = st.text_input("ST depression induced by exercise")
    with col2:
        Slope = st.text_input("Slope of the peak exercise ST segment")
    with col3:
        Majorvessel = st.text_input("Major Vessels coloured by flourosopy")
    with col1:
        Thalassemia = st.text_input("Thalassemia")
    

    Heart_diagnosis = ''
    if st.button('Test Result'):
        try:
            user_input2 = [Age,Sex,ChestPT,RestBP,SerumChl,FastBS,RestElecR,MheartRate,EandiceAng,STdepres,Slope,Majorvessel,Thalassemia]
            user_input2=[float(x) for x in user_input2]
            if Sex and Sex not in ['0', '1']:
                st.error("Invalid input: Please enter only '0' for Female or '1' for Male")
            else:
                heart_prediction = heart_disease_model.predict([user_input2])
                if heart_prediction[0] == 1:
                    Heart_diagnosis='The person has Heart Disease'
                else:
                    Heart_diagnosis = 'The person does not have Heart Disease'
        except ValueError:
            st.error("Please enter valid numeric values in all fields.")
    st.success(Heart_diagnosis)




## Parkinsons Disease Prediction
elif selected == 'Parkinsons Prediction':
    st.title("Parkinson's Disease Prediction using ML")
    col1,col2,col3,col4,col5 = st.columns(5)
    
    with col1:
        MDVPFo = st.text_input("MDVP.FO(Hz)")
    with col2:
        MDVPFh = st.text_input("MDVP.Fhi(Hz)")
    with col3:
        MDVPfl = st.text_input('MDVP.flo(Hz)')
    with col4:
        Jitter = st.text_input('MDVP.Jitter(%)')
    with col5:
        Abs = st.text_input("MDVP.Jitter(Abs)")
    
    
    with col1:
        RAP = st.text_input("MDVP.RAP")
    with col2:
        PPQ = st.text_input('MDVP.PPQ')
    with col3:
        DDP = st.text_input("Jitter.DDP")
    with col4:
        Shimmer = st.text_input('MDVP.Shimmer')
    with col5:
        dB = st.text_input('MDVP.Shimmer(dB)')
    
    
    with col1:
        APQ3 = st.text_input("Shimmer.APQ3")
    with col2:
        APQ5 = st.text_input('Shimmer.APQ5')
    with col3:
        APQ = st.text_input("MDVP.APQ")
    with col4:
        DDA = st.text_input('Shimmer.DDA')
    with col5:
        NHR = st.text_input('NHR')
    
    with col1:
        HNR = st.text_input("HNR")
    with col2:
        RPDE = st.text_input('RPDE')
    with col3:
        DFA = st.text_input("DFA")
    with col4:
        spread1 = st.text_input('Spread1')
    with col5:
        spread2 = st.text_input('Spread2')
    
    with col1:
        D2 = st.text_input("D2")
    with col2:
        PPE = st.text_input('PPE')

    Parkinsons_diagnosis = ''
    if st.button('Test Result'):
        try:
            user_input3 = [MDVPFo,MDVPFh,MDVPfl,Jitter,Abs,RAP,PPQ,DDP,Shimmer,dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]
            user_input3=[float(x) for x in user_input3]
            Parkinsons_prediction = parkinsons_model.predict([user_input3])
            if Parkinsons_prediction[0] == 1:
                Parkinsons_diagnosis='The person has Parkinson Disease'
            else:
                Parkinsons_diagnosis = 'The person does not have Parkinson Disease'
        except ValueError:
            st.error("Please enter valid numeric values in all fields.")
    st.success(Parkinsons_diagnosis)