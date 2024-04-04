import pickle
import streamlit as st
from streamlit_option_menu import option_menu

model = pickle.load(open('model.pkl','rb'))



    st.title("Thyroid Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('Age')

    with col2:
        fhi = st.text_input('Sex(F or M)')

    with col3:
        flo = st.text_input('whether patient is on thyroxine(t or f)')

    with col4:
        Jitter_percent = st.text_input('query_on_thyroxine(t or f)')

    with col5:
        Jitter_Abs = st.text_input('whether patient is on antithyroid medication(t or f)')

    with col1:
        RAP = st.text_input('whether patient is sick(t or f)')

    with col2:
        PPQ = st.text_input('Patient is pregnant(t or f)')

    with col3:
        DDP = st.text_input('whether patient has undergone thyroid surgery(t or f)')

    with col4:
        Shimmer = st.text_input('whether patient is undergoing Iodine 131 treatment(t or f)')

    with col5:
        Shimmer_dB = st.text_input('whether patient believes they have hypothyroid(t or f)')

    with col1:
        APQ3 = st.text_input('whether patient believes they have hyperthyroid(t or f)')

    with col2:
        APQ5 = st.text_input('whether patient  lithium(t or f)')

    with col3:
        APQ = st.text_input('whether patient has goitre(t or f)')

    with col4:
        DDA = st.text_input('whether patient has tumor(t or f)')

    with col5:
        NHR = st.text_input('whether patient has hypopituitary(t or f)')

    with col1:
        HNR = st.text_input('whether patient has psych(t or f)')

    with col2:
        RPDE = st.text_input('whether TSH was measured(t or f)')

    with col3:
        DFA = st.text_input('TSH')

    with col4:
        spread1 = st.text_input('T3_measured(t or f)')

    with col5:
        spread2 = st.text_input('T3')

    with col1:
        D2 = st.text_input('TT4_measured(t or f)')

    with col2:
        PPE = st.text_input('TT4')

    with col3:
        PPE1 = st.text_input('T4U_measured(t or f)')

    with col4:
        PPE2 = st.text_input('T4U')

    with col5:
        PPE3 = st.text_input('FTI_measured(t or f)')

    with col1:
        PPE4 = st.text_input('FTI')

    with col2:
        PPE5 = st.text_input('TBG_measured(t or f)')

    with col3:
        PPE6 = st.text_input('TBG')





    # code for Prediction
    diagnosis = ''

    # creating a button for Prediction
    if st.button("Thyroid's Test Result"):
        prediction = model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])

        if (prediction[0] == 1):
          diagnosis = "The person has Parkinson's disease"
        else:
          diagnosis = "The person does not have Parkinson's disease"

    st.success(diagnosis)
