import streamlit as st
from supabase import create_client

st.title("Member Login")
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

    # Fetch member's password from Supabase based on user_id
    try:
        member_details = supabase.table("member").select("*").eq("member_id", user_id).execute().data
        if member_details:
            # Check if the provided password matches the member's password
            if password == member_details[0]["entry_password"]:
                # Fetch additional member details
                member_branch_id = member_details[0]["br_id"]
                member_trainer_id = member_details[0]["tr_id"]
                member_contact = supabase.table("member_contact").select("mobile_number").eq("member_id", user_id).execute().data
                member_email = supabase.table("member_mail").select("e_mail").eq("member_id", user_id).execute().data
                trainer_name = supabase.table("trainer").select("first_name").eq("trainer_id", member_trainer_id).execute().data
                branch_name = supabase.table("fitness_center").select("branch_name,city").eq("branch_id", member_branch_id).execute().data
                
                # Display member details using Streamlit
                st.title("Member Details")
                if member_details:
                    st.table(member_details)
                if member_contact:
                    st.title("Contact Details")
                    st.table(member_contact)
                if member_email:
                    st.title("Email Details")
                    st.table(member_email)
                if trainer_name:
                    st.title("Trainer Details")
                    st.table(trainer_name)
                if branch_name:
                    st.title("Branch Details")
                    st.table(branch_name)
            else:
                st.write("Incorrect password. Please try again.")
        else:
            st.write("Member ID not found.")
    except Exception as e:
        st.error(f"Error fetching data: {e}")
else:
    st.write("Enter the correct credentials")
