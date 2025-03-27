import streamlit as st

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
  username = st.text_input("username")
  pass1 = st.text_input("password", type="password")
  
  if st.button("Log in"):
    if username == "admin" and pass1 == "admin":
      st.session_state.logged_in = True
      st.rerun()
    else:
      st.error("Invalid username password")

def logout():
    if st.button("Log out"):
        st.session_state.logged_in = False
        st.rerun()

login_page = st.Page(login, title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")

dashboard = st.Page(
    "reports/hardword.py", title="Hardword Learner App", icon=":material/dashboard:", default=True
)
tables = st.Page("reports/tables.py", title="Math Tables", icon=":material/bug_report:")
calculation = st.Page(
    "reports/calculation.py", title="Math calculation", icon=":material/notification_important:"
)


if st.session_state.logged_in:
    pg = st.navigation(
        {
            "Account": [logout_page],
            "Reports": [dashboard, tables, calculation],
            
        }
    )
else:
    pg = st.navigation([login_page])

pg.run()