import streamlit as st
from model import evaluation_score


st.title('Report Evaluation System') 
st.write('Welcome to my project for report evaluation!') 

def evaluation_project():
    doc2 = st.text_input('Enter your document on ferrari:', ' ')
    score = evaluation_score(doc2)
    grade = ''

    if score>=0.7:
        grade='A'
    elif score>=0.5:
        grade='B'
    elif score>=0.3:
        grade='C'
    else:
        grade='F'
        
    # Display the customized message 
    st.write('Your score is ', score.item())
    st.write('You have achieved',grade,'grade.')
    
if __name__ == '__main__':
    try:
        evaluation_project()
    
    except:
        st.write("Enter your document to see the result.")
    
    