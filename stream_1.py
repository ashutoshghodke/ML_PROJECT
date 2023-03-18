import pandas as pd
import streamlit as st
import pickle as pkl


# Add a custom CSS file to your Streamlit app.
def add_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

add_css("./style.css")





# os.chdir(r"C:\Users\utkar\OneDrive\Desktop\Project")
# pip install bz2file
# import bz2file as bz2
# from git import Repo

# from PIL import Image



# image = '''
# <style>
# [data-testid='stAppViewContainer']{
# background-image: url('https://www.apnabank.co.in/uploads/products/1411737727term-deposit_lg.jpg');
# background-size: cover;
# }
# '''
# st.markdown(image, unsafe_allow_html=True)


# def decompress_pickle(file):
#     data=bz2.BZ2File(file,'rb')
#     data=pkl.load(data)
#     return data

# AdaBoostClassifier=pkl.load(open('AdaBoostClassifier','rb'))
# LogisticRegression=pkl.load(open('./LogisticRegression','rb'))
RFClassifier=pkl.load(open('./RFClassifier','rb'))
# VotingClassifier=pkl.load(open('VotingClassifier','rb'))

#AdaBoostClassifier=decompress_pickle('AdaCompressed.pbz2')
#LogisticRegression=decompress_pickle('LORCompressed.pbz2')
#RFClassifier=decompress_pickle('RFCompressed.pbz2')
#VotingClassifier=decompress_pickle('VotCompressed.pbz2')


# st.image(image, caption='Term Deposit')https://github.com/Utkarshmavi0406/desktop-tutorial/blob/main/stream_1.py
df=pd.read_csv("./file1.csv")

# Title of the page
st.title("Deposit Prediction for Bank Marketing Campaign")

# Write method is used to write a line below the heading
st.write("This app is based on 16 inputs that predict whether a customer will deposit or not? Using this app, a bank can identify specific customer segments; that will make deposits.")
st.write("Please use the following form to get started!")
#st.markdown('<p class="big-font">(NOTE: For convinience, usual values are pre-selected in the form.)</p>', unsafe_allow_html=True)


# Selecting age
st.subheader("Select Customer's Age")
selected_age = st.number_input("Enter your age: ", step= 0.1)
st.write("Selected Age:", selected_age)


# Making a radio button to select a single value from the job column
# selecting job
st.subheader("Select Customer's Job")
selected_job = st.radio("", df['job'].unique(), index = 3)
st.write("Selected Job:", selected_job)

# Performing LabelEncoding as per our model requirement
## Encode the job entered by user
### Declaring function for encoding
def encode_job(selected_item):
    dict_job = {'management':0, 'technician':1, 'entrepreneur':2, 'blue-collar':3, 'unknown':4, 'retired':5, 'admin.':6, 'services':7, 'self-employed':8, 'unemployed':9, 'housemaid':10, 'student':11}
    return dict_job.get(selected_item, 'No info available')

# Calling the above function
### Using function for encoding
selected_job = encode_job(selected_job)  


# Making a radio button to select a single value from the Marital column
# For marital Status column 
# selecting marital status
st.subheader("Select Customer's Marital Status")
selected_marital = st.radio("", df['marital'].unique())
st.write("Selected Marital:", selected_marital)


## Encode the marital entered by user
### Declaring function for encoding
def encode_marital(selected_item):
    dict_marital = {'married':0, 'single':1, 'divorced':2}
    return dict_marital.get(selected_item, 'No info available')

# Calling the above function
### Using function for encoding
selected_marital = encode_marital(selected_marital)


# Making a radio button to select a single value from the Education column
# selecting education of the customer
st.subheader("Select Customer's Education")
selected_education = st.radio("", df['education'].unique())
st.write("Selected Education:", selected_education)
## Encode the education entered by user
### Declaring function for encoding
def encode_education(selected_item):
    dict_education = {'primary':3, 'secondary':1, 'tertiary':0, 'unknown':2}
    return dict_education.get(selected_item, 'No info available')

# Calling the above function
### Using function for encoding
selected_education = encode_education(selected_education)  


# Making a radio button to select a single value from the default column
# selecting default status
st.subheader("Select Customer's Default Status")
selected_default = st.radio("", df['default'].unique()[::-1])
st.write("Selected Default Status", selected_default)
## Encode the default entered by user
### Declaring function for encoding
def encode_default(selected_item):
    dict_default = {'no':0, 'yes':1}
    return dict_default.get(selected_item, 'No info available')

#Caling the above function
### Using function for encoding
selected_default = encode_default(selected_default)  


# selecting balance
# User can enter the balance here, Balance can also be negative if the user has a loan
st.subheader("Select Customer's Balance")
selected_balance = st.number_input("Enter your Balance",step=1.00)
st.write("Selected Customer Balance", selected_balance)   


# Making a radio button to select a single value from the housing column
# selecting housing status
st.subheader("Select Customer's Housing Status")
selected_housing = st.radio("", df['housing'].unique(), 
                            index = 1, key = "1")
st.write("Selected Housing Status", selected_housing)


## Encode the housing entered by user
### Declaring function for encoding
def encode_housing(selected_item):
    dict_housing= {'no':0, 'yes':1}
    return dict_housing.get(selected_item, 'No info available')

# Calling the above function
### Using function for encoding
selected_housing = encode_housing(selected_housing)  


# Making a radio button to select a single value from the Loan column
# selecting loan status
st.subheader('Select Loan Status')
selected_loan = st.radio("", df['loan'].unique()[::-1], index = 1, key = "2")
st.write("Selected Loan Status", selected_loan)
## Encode the loan entered by user
### Declaring function for encoding
def encode_loan(selected_item):
    dict_loan= {'no':0, 'yes':1}
    return dict_loan.get(selected_item, 'No info available')


# Calling the above function
### Using function for encoding
selected_loan = encode_loan(selected_loan)  


# Making a radio button to select a single value from the contact column
# selecting contact
# st.title("Select Customer's Contact")
st.subheader("Select Customer's Contact")
selected_contact = st.radio("Select Contact", df['contact'].unique(), 
                            index = 1)
st.write("Selected Contact Type", selected_contact)
## Encode the contact entered by user
### Declaring function for encoding
def encode_contact(selected_item):
    dict_contact= {'cellular':1, 'telephone':2, 'unknown':0}
    return dict_contact.get(selected_item, 'No info available')

# Calling the above function
### Using function for encoding
selected_contact = encode_contact(selected_contact) 

# selecting day
# User will enter the day of the month on which he was called

st.subheader('Select day')
selected_day = st.number_input('Select Day:',step=1.00)
st.write('You selected:', selected_day)

# Making a radio button to select a single value from the month column
# selecting month
st.subheader('Select Last Contact Month of Customer')
selected_month = st.radio("Select Month", ['January','february','March','April','May','June','July','August','September','October','November','December'], 
                            index = 1)
st.write("Selected Month", selected_month)
## Encode the month entered by user
### Declaring function for encoding
def encode_month(selected_item):
    dict_month = {'January':0, 'february':1, 'March':2, 'April':3, 'May':4, 'June':5, 'July':6, 'August':7, 'September':8, 'October':9, 'November':10, 'December':11}
    return dict_month.get(selected_item, 'No info available')

#  Calling the above function
### Using function for encoding
selected_month = encode_month(selected_month) 


# Taking input of call duration in seconds from the user
# selecting duration
st.subheader("Select Customer's Call Duration ")
selected_duration = st.number_input('Enter Customer Call Duration in seconds',step=1.00)
st.write("Selected Customer Duration", selected_duration)

# Taking input of number of contacts made during the campaign from the user
# selecting campaign
st.subheader('Select Number of Contacts Performed in this Campaign')
selected_campaign = st.number_input('Select Campaign:',step=1.00)
st.write('You selected:', selected_campaign)

# Taking input of Number of Days Before the Customer was Contacted from the user
# selecting pdays
st.subheader('Select Number of Days Before the Customer was Contacted')
selected_pdays = st.number_input('Select pdays:',step=1.00)
st.write('You selected:', selected_pdays)


# Taking input of Number of Contacts Performed Before this Campaign from the user
# selecting previous
st.subheader('Select Number of Contacts Performed Before this Campaign')
selected_previous = st.number_input('Select previous:',step=1.00)
st.write('You selected:', selected_previous)


# Making a radio button for selecting Outcome of Previous campaigbn
# selecting poutcome
st.subheader('Select Outcome of Previous Campaign') 
selected_poutcome = st.radio("Select poutcome", df['poutcome'].unique(), index = 0)
st.write("Selected poutcome:", selected_poutcome)


## Encode the poutcome entered by user
### Declaring function for encoding
def encode_pout(selected_item):
    dict_pout = {'failure':1, 'other':2, 'success':3, 'unknown':0}
    return dict_pout.get(selected_item, 'No info available')

# Calling the above Function
### Using function for encoding
selected_poutcome = encode_pout(selected_poutcome) 


st.subheader("Now, we will predict whether customer will buy it or not.")

# AdaBoostClassifier=pkl.load(open('AdaBoostClassifier','rb'))
# LogisticRegression=pkl.load(open('LogisticRegression','rb'))
# RFClassifier=pkl.load(open('RFClassifier','rb'))
# VotingClassifier=pkl.load(open('VotingClassifier','rb'))

# predictionUsingVC= VotingClassifier.predict([[selected_age,selected_job, selected_marital, 
#                                   selected_education,selected_default, selected_balance,  
#                                   selected_housing, selected_loan,selected_contact, 
#                                   selected_day, selected_month,selected_duration,selected_campaign, 
#                                   selected_pdays,selected_previous ,selected_poutcome 
#                                   ]])

# proba=round((VotingClassifier.predict_proba([[selected_age,selected_job, selected_marital, 
#                                   selected_education,selected_default, selected_balance,  
#                                   selected_housing, selected_loan,selected_contact, 
#                                   selected_day, selected_month,selected_duration,selected_campaign, 
#                                   selected_pdays,selected_previous ,selected_poutcome
#                                   ]])[0][1])*100,2)
# # # Adding Predict Button
# # st.write(predict_button)
# predict_button = st.button('Predict using Voting Classifier')

# if predict_button:
#     if(predictionUsingVC == 1):
#         st.success('This customer will SUBSCRIBE Term Deposit with probability percentage {}: '.format(proba))
#     else:
#         st.success('This customer will NOT SUBSCRIBE Term Deposit with probability percentage :{}'.format(proba))


# predictionUsingLR= LogisticRegression.predict([[selected_age,selected_job, selected_marital, 
#                                   selected_education,selected_default, selected_balance,  
#                                   selected_housing, selected_loan,selected_contact, 
#                                   selected_day, selected_month,selected_duration,selected_campaign, 
#                                   selected_pdays,selected_previous ,selected_poutcome 
#                                    ]])

# proba=round((LogisticRegression.predict_proba([[selected_age,selected_job, selected_marital, 
#                                   selected_education,selected_default, selected_balance,  
#                                   selected_housing, selected_loan,selected_contact, 
#                                   selected_day, selected_month,selected_duration,selected_campaign, 
#                                   selected_pdays,selected_previous ,selected_poutcome
#                                   ]])[0][1])*100,2)


# # # Adding Predict Button
# predict_button2 = st.button('Predict using Logistic Regression')
# # st.write(predict_button2)
# if predict_button2:
#     if(predictionUsingLR == 1):
#         st.success('This customer will SUBSCRIBE Term Deposit with probability percentage {}: '.format(proba))
#     else:
#         st.success('This customer will not SUBSCRIBE Term Deposit with probability percentage {}: '.format(proba)) 
    

predictionUsingRF= RFClassifier.predict([[selected_age,selected_job, selected_marital, 
                                  selected_education,selected_default, selected_balance,  
                                  selected_housing, selected_loan,selected_contact, 
                                  selected_day, selected_month,selected_duration,selected_campaign, 
                                  selected_pdays,selected_previous ,selected_poutcome 
                                  ]])


proba=round((RFClassifier.predict_proba([[selected_age,selected_job, selected_marital, 
                                  selected_education,selected_default, selected_balance,  
                                  selected_housing, selected_loan,selected_contact, 
                                  selected_day, selected_month,selected_duration,selected_campaign, 
                                  selected_pdays,selected_previous ,selected_poutcome
                                  ]])[0][1])*100,2)

# # # Adding Predict Button
predict_button3 = st.button('Predict using Random Forest')
# st.write(predict_button)
if predict_button3:
    if(predictionUsingRF == 1):
        st.success('This customer will subscribe to the Term Deposit and percentage of subscribing is  {}% '.format(proba))
    else:
        st.success('This customer will not subscribe to the Term Deposit and percentage of subscribing is {}% '.format(proba)) 


# predictionUsingAda= AdaBoostClassifier.predict([[selected_age,selected_job, selected_marital, 
#                                   selected_education,selected_default, selected_balance,  
#                                   selected_housing, selected_loan,selected_contact, 
#                                   selected_day, selected_month,selected_duration,selected_campaign, 
#                                   selected_pdays,selected_previous ,selected_poutcome 
#                                   ]])



# # # Adding Predict Button
# predict_button4 = st.button('Predict using Ada Boost Classifier')
# # st.write(predict_button)
# if predict_button4:
#     if(predictionUsingAda == 1):
#         st.success('This customer segment will Deposit')
#     else:
#         st.success('This customer segment will NOT Deposit') 




