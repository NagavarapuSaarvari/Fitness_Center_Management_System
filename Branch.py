import streamlit as st
from supabase import create_client

st.title("Login to Access Fitness Center Data")
user_id = st.text_input("ID")
password = st.text_input("Password", type="password")
login_button = st.button("Login")

if user_id == "" and password == "":
    st.write("Enter the username and password")
elif login_button:
    # Supabase credentials
    url = "https://epibswfajpuyarvkzekb.supabase.co"
    key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVwaWJzd2ZhanB1eWFydmt6ZWtiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTA3NTIyMzQsImV4cCI6MjAyNjMyODIzNH0.j9M9su73lgCWLMKpC2mU9INh-vUta_Py0ScZpKPFoqY"
    supabase = create_client(url, key)

    # Fetch branch's password from Supabase based on user_id
    try:
        branch_data = supabase.table("fitness_center").select("password").eq("branch_id", user_id).execute().data
        branch_contact = supabase.table("fitness_center_contact").select("phone_number").eq("branch_id", user_id).execute().data
        trainer_data = supabase.table("trainer").select("first_name").eq("b_id", user_id).execute().data
        if branch_data:
            # Check if the provided password matches the branch's password
            if password == branch_data[0]["password"]:
                # Fetch data from the equipments table
                equipments_data = supabase.table("equipments").select("*").eq("branch_id", user_id).execute().data
                # Display data using Streamlit
                st.title("Equipment Details")
                if equipments_data:
                    st.table(equipments_data)
                else:
                    st.write("No equipment data available")
                if branch_contact:
                    st.write("Contact Details")
                    st.table(branch_contact)
                if trainer_data:
                    st.title("Trainers Available")
                    st.table(trainer_data)
                else:
                    st.write("No Trainers Availavble")
            else:
                st.write("Incorrect password. Please try again.")
        else:
            st.write("Branch ID not found.")
    except Exception as e:
        st.error(f"Error fetching data: {e}")
else:
    st.write("Enter the correct credentials")
