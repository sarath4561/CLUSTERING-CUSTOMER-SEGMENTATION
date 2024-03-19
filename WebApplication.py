import pickle
import streamlit as st

st.title('Predict customer segmentation! :chart:')

# Load the model
load = open('rf.pkl','rb')
model = pickle.load(load)

# Define function to predict customer segment
def predict(income, recency, customer_age, total_purchases):
    prediction = model.predict([[income, recency, customer_age, total_purchases]])
    return prediction

# Define function to interpret predicted clusters
def interpret_cluster(cluster):
    if cluster == 0:
        return "0 (where Customer is having lowest income and lowest Expenditure.)"
    elif cluster == 1:
        return "1 (where Customer is having low income and low Expenditure.)"
    elif cluster == 2:
        return "2 (where Customer is having highest income and highest Expenditure.)"
    elif cluster == 3:
        return "3 (where Customer is having high income and high Expenditure.)"
    elif cluster == 4:
        return "4 (where Customer is having high income and highest Expenditure.)"
    else:
        return "Unknown cluster"

# Define main function
def main():
    st.markdown('This is a very simple webapp for customer segmentation! :chart:')
    
    # Input fields
    income = st.number_input('Income')
    recency = st.number_input('Recency', min_value=0, max_value=100)
    customer_age = st.number_input('Customer_Age', min_value=0, max_value=100)
    total_purchases = st.number_input('Total_purchases', min_value=0, max_value=100)
    
    # Prediction button
    if st.button('Predict'):
        result = predict(income, recency, customer_age, total_purchases)
        interpretation = interpret_cluster(result[0])
        st.success(f'Customer Segment: {interpretation}')

if __name__ == '__main__':
    main()
