import streamlit as st

# Create a form for the applicant to apply for a loan
st.title('Real Estate Approval Process')
st.markdown('Please complete the form below to apply for a loan:')

name = st.text_input('Name')
email = st.text_input('Email')
phone = st.text_input('Phone')
property_address = st.text_input('Property Address')
loan_amount = st.number_input('Loan Amount')

# Submit the form and check the loan approval status
if st.button('Submit'):
    if loan_amount > 1000000:
        st.success('Loan approved!')
        st.markdown('Our attorneys will now start mocking up the documents for the transferal process.')
    else:
        st.error('Loan declined')
        st.markdown('We apologize, but your loan request has been declined.')
