
import joblib
import numpy as np
import streamlit as st

model=joblib.load(open("/content/model1.pkl",'rb'))
scaler=joblib.load(open("/content/mscaler.pkl",'rb'))
st.title('Steel Power Conception Prediction')

st.markdown(
  f"""
  <style>
  .stApp {{
     background: url("https://images.unsplash.com/photo-1496247749665-49cf5b1022e9?q=80&w=2073&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
     background-size: cover
         }}
   </style>
     """,
     unsafe_allow_html=True
     )

a=st.number_input('Lagging_Current_Reactive.Power_kVarh')
b=st.number_input('Leading_Current_Reactive_Power_kVarh')
c=st.number_input('CO2(tCO2)')
d=st.number_input('Lagging_Current_Power_Factor')
e=st.number_input('Leading_Current_Power_Factor')
f=st.number_input('NSM(Number of Seconds from midnight)')
opt={'select an option':3,'Weekday':0,'Weekend':1}
opt1={'Select an option':7,'Monday':0,'Tuesday':1,'Wednesday':2,'Friday':3}
opt2={'Select an option':7,'Saturday':4,'Sunday':6}
y=0
selected_option = st.selectbox('WeekStatus:', list(opt.keys()))
if selected_option=='Weekend':
  st.write('You selected:', selected_option)
  s_opt=st.selectbox('Day_of_week:',list(opt2.keys()))
  y=opt2[s_opt]
  if s_opt!='Select an option':
    st.write('You selected:',s_opt)
  else:
    st.warning('Please select an option')
elif selected_option=='Weekday':
  st.write('You selected:', selected_option)
  s_opt=st.selectbox('Day_of_week:',list(opt1.keys()))
  y=opt1[s_opt]
  if s_opt!='Select an option':
    st.write('You selected:',s_opt)
  else:
      st.warning('Please select an option')
else:
    st.warning('Please select an option.')


opt3={'Select an option':3,'Light_Load':0,'Medium_Load':1,'Maximum_Load':2}
s_opt1=st.selectbox('Load_Type:',list(opt3.keys()))
if s_opt1!='Select an option':
  st.write('You selected:',s_opt1)

x=opt[selected_option]
z=opt3[s_opt1]
k=scaler.transform([[a,b,c,d,e,f,x,y,z]])
if st.button('Predict'):
  pred=model.predict(k)
  st.write('predicted Usage is:',pred,'kWh')
