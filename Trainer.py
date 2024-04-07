import streamlit as st
from supabase import create_client

st.title("Trainer Login")
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
        trainer_details = supabase.table("trainer").select("entry_password").eq("trainer_id", user_id).execute().data
        if trainer_details:
            # Check if the provided password matches the branch's password
            if password == trainer_details[0]["entry_password"]:
                # Fetch data from the equipments table
                trainer_data = supabase.table("trainer").select("trainer_id,first_name,last_name,fees,experience").eq("trainer_id", user_id).execute().data
                trainer_contact = supabase.table("trainer_contact").select("mobile_number").eq("trainer_id", user_id).execute().data
                members_trained = supabase.table("member").select("first_name").eq("tr_id",user_id).execute().data
                # Display data using Streamlit
                st.title("Trainer Details")
                if trainer_data:
                    st.table(trainer_data)
                if trainer_contact:
                    st.title("Contact Details")
                    st.table(trainer_contact)
                if members_trained:
                    st.title("Members Trained")
                    st.table(members_trained)
            else:
                st.write("Incorrect password. Please try again.")
        else:
            st.write("Branch ID not found.")
    except Exception as e:
        st.error(f"Error fetching data: {e}")
else:
    st.write("Enter the correct credentials")
