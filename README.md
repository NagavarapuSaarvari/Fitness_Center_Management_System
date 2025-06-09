# 🏋️ Fitness Center Management System

A complete fitness center management solution built with **Streamlit** for the frontend, **Python + SQL** for the backend, and **Supabase** as the cloud-based database. This system enables efficient handling of member data, trainer assignments, attendance tracking, subscriptions, and more.

---

## 🖥️ Frontend – Python (Streamlit)

The frontend is developed using **Streamlit**, a powerful Python framework for building interactive web apps. It offers a clean and responsive UI for gym administrators and staff to:

- Register and manage member profiles  
- Assign trainers and schedule classes  
- Track member progress via reports and dashboards

Streamlit ensures fast development and easy deployment with intuitive UI elements and real-time interactivity.

---

## ⚙️ Backend – SQL (via Python)

The backend is powered by **Python scripts executing raw SQL queries** to perform all core operations such as:

- Inserting, updating, and retrieving data from Supabase  
- Validating user input and business logic  
- Generating dynamic dashboards and reports  
- Handling complex queries for trainer assignments and schedules

Python’s flexibility combined with SQL’s power ensures robust and scalable data manipulation.

---

## 🗄️ Database – Supabase (SQL)

All data is stored securely in **Supabase**, an open-source backend-as-a-service built on top of PostgreSQL. Supabase provides:

- Realtime updates with minimal latency  
- Authentication, row-level security, and role-based access  
- RESTful API and client libraries for database access  
- Simple integration with Python for executing SQL queries

### 📌 Key Tables:

- `members` – Personal and fitness details of gym members  
- `trainers` – Trainer information and specialties  
- `classes` – Class types, schedules, and assigned trainers  
- `attendance` – Member check-ins and attendance logs  
- `subscriptions` – Plan types, payment info, and validity periods

---

## 📦 Features Summary

✅ Member & Trainer Management  
✅ Class Scheduling & Assignment  
✅ Real-time Database with Supabase  
✅ Fully Interactive UI with Streamlit
