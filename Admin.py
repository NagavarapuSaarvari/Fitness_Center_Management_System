import streamlit as st
import os
from supabase import create_client

st.title("Login to Access Fitness Center Data")
user_id = st.text_input("ID")
password = st.text_input("Password", type="password")
login_button = st.button("Login")
admin_id="Fitness@123"
admin_password="fit777"

if user_id == "" and password == "":
    st.write("Enter the username and password")

elif user_id == admin_id and password == admin_password:
    # Supabase credentials
    url = "https://epibswfajpuyarvkzekb.supabase.co"
    key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVwaWJzd2ZhanB1eWFydmt6ZWtiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTA3NTIyMzQsImV4cCI6MjAyNjMyODIzNH0.j9M9su73lgCWLMKpC2mU9INh-vUta_Py0ScZpKPFoqY"
    supabase = create_client(url, key)

    # Fetch data from the fitness_center table
    try:
        branches_data = supabase.table("fitness_center").select("branch_name,branch_id,city").execute().data 
        equipment_data = supabase.table("equipments").select("equipment_name,date_of_purchase,maintenance_cost,branch_id").execute().data
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        branches_data = []
        equipment_data = []

    # Display data using Streamlit
    st.title("Branch Details")
    if branches_data:
        st.table(branches_data)
    else:
        st.write("No data available")
        
    st.title("Details of Equipments")
    if equipment_data:
        st.table(equipment_data)
else:
    st.write("Enter the correct credentials")








