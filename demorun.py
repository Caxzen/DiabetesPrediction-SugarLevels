import streamlit as st
import pickle
from streamlit_option_menu import option_menu



    
    # sidebar for navigation
with st.sidebar:
        
    selected = option_menu('Multiple Disease Prediction',['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Hepatitis Prediction','Breast Cancer Prediction'],
                            icons=['activity','heart','person'],
                            default_index=0)
    # Load the saved models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
hepatitis_model = pickle.load(open("hepatitis_model.sav",'rb'))
cancer_model = pickle.load(open("cancer_model.sav",'rb'))
        
    # Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
        
    # page title
    st.title('Diabetes Prediction')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Age = st.text_input('Age of the Person')
        
    with col2:
        Gender = st.text_input('Gender - Male-1 , Female-0')
    
    with col3:
        Genetic = st.text_input('Genetic - Yes: 1,No: 0,Not Sure: 2')
    
    with col1:
        Lifestyle = st.text_input('Lifestyle - Normal: 1,Active:0,Sedentary:2')
    
    with col2:
        Eduration = st.text_input('Eduration')

    with col3:
        Area = st.text_input('Area - Urban:1,Metro:0,Rural:2')
    
    with col1:
        BMI = st.text_input('BMI value')
    
    with col2:
        Stress = st.text_input('Stress - Normal:1,Low:0,High:2')
    
    
    
    # code for Prediction and medication info
    diab_diagnosis = ''
    medication_info = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):

        Age = int(Age)
        Gender = int(Gender)
        Genetic = int(Genetic)
        Lifestyle = int(Lifestyle)
        Eduration = int(Eduration)
        Area = int(Area)
        BMI = int(BMI)
        Stress = int(Stress)
    


        diab_prediction = diabetes_model.predict([[Age,Gender,Genetic,Lifestyle,Eduration,Area,BMI,Stress]])
        

        
        if (diab_prediction[0] > 100 and diab_prediction[0] < 125):
            diab_diagnosis = 'Pre - Diabetes' 
                        
            # add medication information to diagnosis
            medication_info = 'metformin, Glumetza. Medications to control cholestrol and high blood pressure might also be prescribed'

        elif (diab_prediction[0] > 125):
            diab_diagnosis = 'Type 2 Diabetes '
                        
            # add medication information to diagnosis
            medication_info = 'Sulfonylureas , Glinides , Thiazolidinediones and DPP - 4 inhibitors'
        else:
            diab_diagnosis = 'The person is normal'
        
    st.success(diab_diagnosis)
    
    if (medication_info != ''):
        st.info(medication_info)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3   :
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
    
    # code for Prediction and Medications
    # code for Prediction and Medications
    heart_diagnosis = ''
    heart_prediction = -1 


        # creating a button for Prediction

    if st.button('Heart Disease Test Result'):
        age = float(age)
        sex = int(sex)
        cp = int(cp)
        trestbps = float(trestbps)
        chol = float(chol)
        fbs = int(fbs)
        restecg = int(restecg)
        thalach = float(thalach)
        oldpeak = float(oldpeak)
        thal = int(thal)
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,oldpeak,thal]])  
        medication_info = ''                        
        if (heart_prediction[0] > 0.5):
            heart_diagnosis = ' the person does have heart disease'
                        
            # add medication information to diagnosis
            medication_info = 'Keep stress under control , Exercise regularly , Avoid smoking , Manage BP and Cholestrol level'
        
        else:
            heart_diagnosis = 'The person doesnt have Heart Disease'
            
        st.success(heart_diagnosis)
        
        if (medication_info != ''):
            st.info(medication_info)



def yesto(val):
    if val=="Yes":
        return 1
    else:
        return 0


if (selected == 'Hepatitis Prediction'):
    
    # page title
    st.title('Hepatitis Prediction')

    col1, col2, col3 = st.columns(3)
            
    with col1:
        apetite = st.radio("Loss of apetite",("Yes","No"))
        
    with col2:
        vomit = st.radio("Vomitting ?",("Yes","No"))

    with col3:
        diar = st.radio("Facing Diarrhoea",("Yes","No"))

    with col1:
        fever = st.radio("You having Mild Fever",("Yes","No"))
        
    with col2:
        nausea = st.radio("Facing Nausea ?",("Yes","No"))

    with col3:
        skin = st.radio("Having Yellowish Skin ?",("Yes","No"))

    with col1:
        urine = st.radio("Dark Urine ?",("Yes","No"))
        
    with col2:
        pain = st.radio("Any Abdominal pain ?",("Yes","No"))

    with col3:
        fatigue = st.radio("Do you feel Fatigue ?",("Yes","No"))

    if st.button('Hepatitis Prediction'):
        apetite = yesto(apetite)
        vomit = yesto(vomit)
        diar = yesto(diar)
        fever = yesto(fever)
        nausea = yesto(nausea)
        skin = yesto(skin)
        urine = yesto(urine)
        pain = yesto(pain)
        fatigue = yesto(fatigue)
        hep_prediction = hepatitis_model.predict([[apetite,vomit,diar,fever,nausea,skin,urine,pain,fatigue]])

        medication_info = ''                        
        if (hep_prediction[0]=='hepatitis A'):
            hep_diagnosis = 'Hepatitis A'
                        
            # add medication information to diagnosis
            medication_info = 'No specific treatment for Hepatitis A, your body will clean it on its own '
        
        elif (hep_prediction[0]=='Hepatitis B'):
            hep_diagnosis = 'Hepatitis B'
                        
            # add medication information to diagnosis
            medication_info = 'Interferon alfa-2b , Intron A , Liver transplant'

        elif (hep_prediction[0]=='Hepatitis C'):
            hep_diagnosis = 'Hepatitis C'
                        
            # add medication information to diagnosis
            medication_info = 'Anti-viral Medications , Best to discuss your treatment options with a specialist'

        st.success(hep_diagnosis)
        
        if (medication_info != ''):
            st.info(medication_info)

if (selected == 'Breast Cancer Prediction'):
    
    # page title
    st.title('Breast Cancer Prediction')

    col1, col2, col3 , col4= st.columns(4)

    with col1:
        radius_mean = st.text_input('Radius mean')
        
    with col2:
        texture_mean = st.text_input('Texture mean')
        
    with col3:
        perimeter_mean = st.text_input('Perimeter mean')
        
    with col4:
        area_mean = st.text_input('Area mean')
        
    with col1:
        smoothness_mean = st.text_input('Smoothness mean')
        
    with col2:
        compactness_mean = st.text_input('compactness_mean')
        
    with col3:
        concavity_mean = st.text_input('Concavity mean')
        
    with col4:
        concave_points_mean = st.text_input('Concave points mean')
        
    with col1   :
        symmetry_mean = st.text_input('Symmetry mean')
        
    with col2:
        radius_se = st.text_input('Radius se')
    with col3:
        perimeter_se = st.text_input('Perimeter se')
    with col4:
        area_se = st.text_input('Area se')
    with col1:
        compactness_se = st.text_input('Compactness se')
    with col2:
        concavity_se = st.text_input('Concavity se')
    with col3:
        concave_points_se = st.text_input('Concave points se')
    with col4:
        fractal_dimension_se = st.text_input('Fractal dimension se')
    with col1:
        radius_worst = st.text_input('Radius worst')
    with col2:
        texture_worst = st.text_input('Texture worst')
    with col3:
        perimeter_worst = st.text_input('Perimeter worst')
    with col4:
        area_worst = st.text_input('Area worst')
    with col1:
        smoothness_worst = st.text_input('Smoothness worst')
    with col2:
        compactness_worst = st.text_input('Compactness worst')
    with col3:
        concavity_worst = st.text_input('Concavity worst')
    with col4:
        concave_points_worst = st.text_input('Concave points worst')
    with col1:
        symmetry_worst = st.text_input('Symmetry worst')
    with col2:
        fractal_dimension_worst = st.text_input('Fractal dimension worst')
    
        
    
    # code for Prediction and Medications
    # code for Prediction and Medications
    heart_diagnosis = ''
    heart_prediction = -1 


        # creating a button for Prediction

    if st.button('Diabetes Test Result'):
        radius_mean = float(radius_mean)
        texture_mean = float(texture_mean)
        perimeter_mean = float(perimeter_mean)
        area_mean = float(area_mean)
        smoothness_mean = float(smoothness_mean)
        compactness_mean = float(compactness_mean)
        concavity_mean = float(concavity_mean)
        concave_points_mean = float(concave_points_mean)
        symmetry_mean = float(symmetry_mean)
        radius_se = float(radius_se)
        perimeter_se = float(perimeter_se)
        area_se = float(area_se)
        compactness_se = float(compactness_se)
        concavity_se = float(concavity_se)
        concave_points_se = float(concave_points_se)
        fractal_dimension_se = float(fractal_dimension_se)
        radius_worst = float(radius_worst)
        texture_worst = float(texture_worst)
        perimeter_worst = float(perimeter_worst)
        area_worst = float(area_worst)
        smoothness_worst = float(smoothness_worst)
        compactness_worst = float(compactness_worst)
        concavity_worst = float(concavity_worst)
        concave_points_worst = float(concave_points_worst)
        symmetry_worst = float(symmetry_worst)
        fractal_dimension_worst = float(fractal_dimension_worst)

        
        cancer_prediction = cancer_model.predict([[radius_mean,texture_mean,perimeter_mean,area_mean,smoothness_mean,compactness_mean,concavity_mean,concave_points_mean,symmetry_mean,radius_se,perimeter_se,area_se,compactness_se,concavity_se,concave_points_se,fractal_dimension_se,radius_worst,texture_worst,perimeter_worst,area_worst,smoothness_worst,compactness_worst,concavity_worst,concave_points_worst,symmetry_worst,fractal_dimension_worst]])  
                      
        if (heart_prediction == 0):
            cancer_diagnosis = 'Person does not have breast cancer'
                        
        else:
            cancer_diagnosis = 'The person doesnt have breast cancer'
            
        st.success(cancer_diagnosis)
    