import streamlit as st
import pandas as pd
import datetime
import pytz
import base64


# Set timezone to Pakistan (Karachi)
pakistan_tz = pytz.timezone('Asia/Karachi')
current_time = datetime.datetime.now(pakistan_tz)
current_date = current_time.date()


# ✅ Set Page Config at the very top
st.set_page_config(page_title="CM gizri Roaster App",
    page_icon="📊",  # or link to your favicon
    layout="wide")


# ✅ Load Data Function
def load_data():
    data = [
        {   
            "Supervisor": "ZAHID HUSSAIN",
            "Emp#": "80023543", 
            "Task": "CM",
            "Lineman": "AKBAR HUSSAIN",
            "Lineman_Emp#": "80022050",
            "Fitter": "MUHAMMAD FAHIM",
            "Fitter_Emp#": "80023263 ",
            "Karkun": "ARSHAD",
            "Karkun_Emp#": "SE7121",
            "Off_Day": "Sunday",
            "Duty_Time": "M,M,M,M,   Mon-Sat"
        },
  {
    "Supervisor": "M.IRFAN ARAIN",
    "Emp#":" 80023407",
    "Task": "CM",
    "Lineman": "MUSLIM",
    "Lineman_Emp#": "80023758",
    "Fitter": "FAROOQ",
    "Fitter_Emp#": "80023268",
    "Karkun": "RIZWAN",
    "Karkun_Emp#": "C-2966",
    "Off_Day": "Saturday",
    "Duty_Time":"M,E,N,M,   Sun-Fri"
  },
  {
    "Supervisor": "RIASAT ALI",
    "Emp#": "4599",
    "Task": "CM",
    "Lineman": "MUQARRAM SHAH",
    "Lineman_Emp#": "8698",
    "Fitter": "IMRAN ALI",
    "Fitter_Emp#": "80022216",
    "Karkun": "BABOO HAROON",
    "Karkun_Emp#": "11993",
    "Off_Day": "Friday",
    "Duty_Time":"M,M,M,M,   Sat-Thu"
  },
  {
    "Supervisor": "WASEEM-UR-REHMAN",
    "Emp#": "80023743",
    "Task": "CM",
    "Lineman": "NASIM ANJUM",
    "Lineman_Emp#": "80023135",
    "Fitter": "MUHAMMAD ASHFAQ",
    "Fitter_Emp#": "80022868",
    "Karkun": "SAJJAD",
    "Karkun_Emp#": "HK-574",
    "Off_Day": "Saturday",
    "Duty_Time":"N,M,E,N,  Sun-Fri"
  },
  {
    "Supervisor": "AKHTAR HUSSAIN",
    "Emp#":" 8970",
    "Task": "CM",
    "Lineman": "MUHAMMAD ASIF",
    "Lineman_Emp#": "80022304",
    "Fitter": "NAZEER AHMED",
    "Fitter_Emp#": "80022037",
    "Karkun": "IRFAN AHMED KHAN",
    "Karkun_Emp#":" C-2835",
    "Off_Day": "Sunday",
    "Duty_Time":"E,E,E,E,   Mon-Sat"
  },

  {
    "Supervisor": "SHAZAIB AHMED",
    "Emp#": "80023818",
    "Task": "CM",
    "Lineman": "YASIR KHAN",
    "Lineman_Emp#": "80021985",
    "Fitter": "SHAHNAWAZ",
    "Fitter_Emp#": "80022870",
    "Karkun": "MUHAMMAD SHAHID",
    "Karkun_Emp#": "6598",
    "Off_Day": "Friday",
    "Duty_Time":"E,E,E,E,    Sat-Thu"
  },
  {
    "Supervisor": "SHEHZAD AHMED",
    "Emp#": "80023729",
    "Task": "CM",
    "Lineman": "MUHAMMAD DANISH",
    "Lineman_Emp#": "80022173",
    "Fitter": "JUNAID",
    "Fitter_Emp#":" 80022260",
    "Karkun": "MUHAMMAD LUQMAN",
    "Karkun_Emp#": "P-1913",
    "Off_Day": "Sunday",
    "Duty_Time":"N,M,E,N,  Mon-Sat"
  },
  {
    "Supervisor": "MUHAMMAD ZEESHAN",
    "Emp#": "80023745",
    "Task": "CM",
    "Lineman": "NOMAN AHMED",
    "Lineman_Emp#": "80022548",
    "Fitter": "MUHAMMAD ADIL BHATI",
    "Fitter_Emp#": "80022286",
    "Karkun": "DANISH AHMED",
    "Karkun_Emp#": "MM-6598",
    "Off_Day": "Monday",
    "Duty_Time":"N,M,E,N,  Tue-Sun"
  }
  ,
  {
    "Supervisor": "WAJID SOMROO",
    "Emp#": "80018698",  
    "Task": "CM",
    "Lineman": "MUHMMAD NADEEM",
    "Lineman_Emp#": "14316",
    "Fitter": "ZAFAR IQBAL",
    "Fitter_Emp#":" 23286",
    "Karkun": "IMRAN KHAN",
    "Karkun_Emp#": "0652",
    "Off_Day": "Tuesday",
    "Duty_Time":"N,M,E,N,  Wed-Mon"
  },

  {
    "Supervisor": "ALI REHAN",
    "Emp#":" 80023733",
    "Task": "CM",
    "Lineman": "SIRAJ",
    "Lineman_Emp#": "80022318",
    "Fitter": "AQIL AHMED",
    "Fitter_Emp#": "80023286",
    "Karkun": "MUHAMMAD KAMRAN",
    "Karkun_Emp#": "P-1934",
    "Off_Day": "Sunday",
    "Duty_Time":"E,N,M,E,    Mon-Sat"
  }
  ,
  {
    "Supervisor": "MUHAMMAD NASIR",
    "Emp#": "80023438",
    "Task": "CM",
    "Lineman": "SHAHZAD ABBASI",
    "Lineman_Emp#": "80022442",
    "Fitter": "MUHAMMAD FAIZ",
    "Fitter_Emp#": "80023269",
    "Karkun": "MUHAMMAD LAIQ",
    "Karkun_Emp#": "P-1942",
    "Off_Day": "Monday",
    "Duty_Time":"E,N,M,E,   Tue-Sun"
  }
  ,
  {
    "Supervisor": "M.ANUS",
    "Emp#": "80023960",
    "Task": "CM",
    "Lineman": "MUHAMMAD NASIR ALI",
    "Lineman_Emp#": "80023310",
    "Fitter": "IMRAN BALOCH",
    "Fitter_Emp#": "80023614",
    "Karkun": "FARAZ",
    "Karkun_Emp#": "SE-7123",
    "Off_Day": "Saturday",
    "Duty_Time":"E,N,M,E,   Sun-Fri"
  }
  ,
  {
    "Supervisor": "DIYAR GUL",
    "Emp#":" 80023098",
    "Task": "CM",
    "Lineman": "SARDAR",
    "Lineman_Emp#": "80023763",
    "Fitter": "VACANT",
    "Fitter_Emp#": "NONE",
    "Karkun": "KHALID",
    "Karkun_Emp#": "C-2894",
    "Off_Day": "Sunday",
    "Duty_Time":"E,N,M,E,    Mon-Sat"
  },
  {
    "Supervisor": "MUHAMMAD YAMEEN",
    "Emp#":" 80018664",
    "Task": "CM",
    "Lineman": "HAMEED BALOCH",
    "Lineman_Emp#": "80022318",
    "Fitter": "SAMEER",
    "Fitter_Emp#": "80021732",
    "Karkun": "NOOR HASSAN",
    "Karkun_Emp#": "C-2899",
    "Off_Day": "Thursday",
    "Duty_Time":"E,N,M,E,  Fri-Wed"
  },
  {
    "Supervisor": "SHABBER",
    "Emp#":" 80023546",
    "Task": "CM",
    "Lineman": "CHANZEB",
    "Lineman_Emp#":" 11917",
    "Fitter": "VACANT",
    "Karkun": "ARSHAD",
    "Karkun_Emp#": "P-0056",
    "Off_Day": "Thursday",
    "Duty_Time":"M,E,N,M,  Fri-Wed "
  },
  {
    "Supervisor": "ALTAF",
    "Emp#": "12592",
    "Task": "CM",
    "Lineman": "SULEMAN",
    "Lineman_Emp#": "15215",
    "Fitter": "VACANT",
    "Fitter_Emp#": "none",
    "Karkun": "QADIR BUX",
    "Karkun_Emp#": "P-0892",
    "Off_Day": "Thursday",
    "Duty_Time":"N,M,E,N,   Fri-Wed "
  },
  {
    "Supervisor": "MANSOOB",
    "Emp#": "80025358",
    "Lineman": "none",
    "Lineman_Emp#": "none",
    "Fitter": "none",
    "Fitter_Emp#": "none",
    "Karkun": "MIRZA FAIZAN",
    "Karkun_Emp#": "1170",
    "Off_Day": "Sunday",
    "Duty_Time":"M,M,M,M,   Mon-Sat"
  },
  {
    "Supervisor": "RASHID",
    "Emp#": "80010824",
    "Task": "SI MAINT",
    "Lineman": "none",
    "Lineman_Emp#": "none",
    "Fitter": "none",
    "Fitter_Emp#": "none",
    "Karkun": "none",
    "Karkun_Emp#": "none",
    "Off_Day": "Sunday",
    "Duty_Time":"M,M,M,M, Mon-Sat"
  },
  {
    "Supervisor": "NADEEM SARWAR",
    "Emp#": "80024426",
    "Task": "CM",
    "Lineman": "YASIR",
    "Lineman_Emp#": "80022006",
    "Fitter": "MUHAMMAD ASIM",
    "Fitter_Emp#": "5726",
    "Karkun": "UMAR FAROOQ",
    "Karkun_Emp#": "7997",
    "Off_Day": "Sunday",
    "Duty_Time":"M,M,M,M,  Mon-Sat"
  },
  {
    "Supervisor": "ZEESHAN SHAIKH",
    "Emp#": "80010182",
    "Task": "CM",
    "Lineman": "FARHAN KHAN",
    "Lineman_Emp#": "80022281",
    "Fitter": "VACANT",
    "Fitter_Emp#": "NONE",
    "Karkun": "MUHAMMAD ATIF",
    "Karkun_Emp#": "C-2850",
    "Off_Day": "Wednesday",
    "Duty_Time":"M,M,M,M,   Thu-Tue"
  },
  {
    "Supervisor": "NABEEL",
    "Emp#":" 14684",
    "Task": "CM",
    "Lineman": "SYED ZAMEER SHAH",
    "Lineman_Emp#": "15215",
    "Fitter": "WAQAR AHMED",
    "Fitter_Emp#":" 10801",
    "Karkun": "JHON",
    "Karkun_Emp#": "241",
    "Off_Day": "Tuesday",
    "Duty_Time":"M,E,N,M   Thu-Mon"
  },
  {
    "Supervisor": "ALFRED YOUSAF",
    "Emp#": "80014989",
    "Task": "CM",
    "Lineman": "ZUBAIR ASLAM",
    "Lineman_Emp#": "80021850",
    "Fitter": "MUHAMMAD ADNAN",
    "Fitter_Emp#": "80022285",
    "Karkun": "VISHAL MUNAWAR",
    "Karkun_Emp#": "F-KE-0605",
    "Off_Day": "Sunday",
    "Duty_Time":"M,E,N,M,   Mon-Sat"
  },
  {
    "Supervisor": "IMRAN KHAN",
    "Emp#":" 80023400",
    "Task": "CM",
    "Lineman": "MUHAMMAD DANISH",
    "Lineman_Emp#":"80022618",
    "Fitter": "ABDUL QADIR",
    "Fitter_Emp#":"80022283",
    "Karkun": "DANISH HUSSAIN",
    "Karkun_Emp#":"1157",
    "Off_Day": "Monday",
    "Duty_Time":"M,E,N,M,   Tue-Sun",

    
  }
    ]
    return pd.DataFrame(data)

# ✅ Load Data
data = load_data()

# ✅ Create Layout with Calendar at the Top Right
col1, col2 = st.columns([3, 1])
with col1:
    st.image("https://vtlogo.com/wp-content/uploads/2020/03/k-electric-vector-logo.png", width=120)

with col2:
    selected_date = st.date_input("📅 Select Date", current_date, min_value=datetime.date(2025, 10 , 5), max_value=datetime.date(2025, 11, 1))

# ✅ Display Titles
st.markdown("<h4 style='text-align: center; color:#3498db;'>📋 DUTY ROASTER CM GIZRI (5TH OCTUBER TO 1ST NOVEMBER)</h4>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color:#3256db;'>🤵‍♂️ GM CM Mr JAVED RAZA</h5>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color:#3256db;'>🤵‍♂️ DGM CM Mr REHAN MURTAZA</h5>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color:#3256db;'>👨‍💼 MANAGER CM Mr SAJID MEHMOOD</h5>", unsafe_allow_html=True)
st.markdown("---")

import os
import streamlit as st
import base64

# ---------------- Setup ---------------- #
plan_leave_path = "plan_leaves"
training_path = "trainings"
announcement_path = "announcements"  # ✅ NEW folder for announcements

# Create folders if they don't exist
for path in [plan_leave_path, training_path, announcement_path]:
    os.makedirs(path, exist_ok=True)

# ---------------- Authentication ---------------- #
st.title("📁 Plan Leaves, Trainings & Announcements")
password = st.text_input("🔐 Enter Password to Upload/Delete Files", type="password")
auth = password == "@yamEEnkE"

# ---------------- Upload Section ---------------- #
if auth:
    st.success("✅ Authenticated: You can upload or delete files.")
    upload_tab = st.radio("📂 Upload to Section:", ["Plan Leaves", "Trainings", "Announcements"])
    uploaded_file = st.file_uploader("📤 Upload File", type=["pdf", "jpg", "jpeg", "png"])

    if uploaded_file is not None:
        if upload_tab == "Plan Leaves":
            save_folder = plan_leave_path
        elif upload_tab == "Trainings":
            save_folder = training_path
        else:
            save_folder = announcement_path

        file_path = os.path.join(save_folder, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success(f"✅ File uploaded to {upload_tab} successfully!")
        st.experimental_rerun()

# ---------------- File Display & Delete ---------------- #
def list_and_display_files(folder, title):
    st.subheader(f"📂 {title}")
    files = os.listdir(folder)

    if not files:
        st.info("No files uploaded yet.")
    else:
        for file in sorted(files):
            file_path = os.path.join(folder, file)
            col1, col2 = st.columns([5, 1])

            with col1:
                if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                    with open(file_path, "rb") as img_file:
                        encoded = base64.b64encode(img_file.read()).decode()
                    st.markdown(
                        f"""
                        <img src="data:image/jpeg;base64,{encoded}" style="width:100%; max-width:800px;"/>
                        """,
                        unsafe_allow_html=True
                    )
                elif file.lower().endswith(".pdf"):
                    st.markdown(f"📄 [View PDF: {file}](./{file_path})", unsafe_allow_html=True)
                else:
                    st.write(f"📄 {file}")

            with col2:
                if auth and st.button(f"🗑️ Delete", key=f"{title}_{file}"):
                    try:
                        os.remove(file_path)
                        st.success(f"✅ Deleted: {file}")
                        st.experimental_rerun()
                    except Exception as e:
                        st.error(f"⚠️ Error deleting {file}: {e}")

# ---------------- Display All Files ---------------- #
list_and_display_files(plan_leave_path, "Plan Leaves")
list_and_display_files(training_path, "Trainings")
list_and_display_files(announcement_path, "Announcements")  # ✅ New section






def get_shift(duty_time, selected_date):
    start_date = datetime.date(2025, 5, 10)
    shift_intervals = [
        (start_date + datetime.timedelta(days=7 * i), start_date + datetime.timedelta(days=7 * (i + 1) - 1))
        for i in range(7)
    ]
    shifts = duty_time.split(",")
    for i, (start, end) in enumerate(shift_intervals):
        if start <= selected_date <= end:
            return shifts[i] if i < len(shifts) else ""
    return ""




# Categorize teams based on shifts
morning_shift  = []
evening_shift = []
night_shift = []
off_day_teams = []

for _, row in data.iterrows():
    if row['Off_Day'] == selected_date.strftime('%A'):
        off_day_teams.append(row)
        continue  # Skip off-day teams

    shift = get_shift(row['Duty_Time'], selected_date)
    team_info = f"**Supervisor:** {row['Supervisor']} (Emp#: {row['Emp#']})\n**Task:** {row['Task']}\n**Lineman:** {row['Lineman']} (Emp#: {row['Lineman_Emp#']})\n**Fitter:** {row['Fitter']} (Emp#: {row['Fitter_Emp#']})\n**Karkun:** {row['Karkun']} (Emp#: {row['Karkun_Emp#']})"
    
    if shift == "M":
        morning_shift.append(team_info)
    elif shift == "E":
        evening_shift.append(team_info)
    elif shift == "N":
        night_shift.append(team_info)

# ✅ Display Current Date & Time
st.markdown(f"<h5 style='text-align: center; color:#3256db;'>📅 Team Details for {selected_date.strftime('%A, %d %B %Y')}</h5>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center;'>⏰ Current Time in Karachi: {current_time.strftime('%I:%M %p')}</p>", unsafe_allow_html=True)

# ✅ Display Off-Day Teams
if off_day_teams:
    st.markdown("### ❌ Off-Day Teams")
    for team in off_day_teams:
        st.markdown(f"**Supervisor:** {team['Supervisor']} (Emp#: {team['Emp#']}) - Off Day: {team['Off_Day']}")
    st.markdown("---")

# ✅ Display Active Teams
if morning_shift:
    st.markdown("### ☀️ Morning Shift")
    for team in morning_shift:
        st.markdown(team)
        st.markdown("---")

if evening_shift:
    st.markdown("### 🌆 Evening Shift")
    for team in evening_shift:
        st.markdown(team)
        st.markdown("---")

if night_shift:
    st.markdown("### 🌙 Night Shift")
    for team in night_shift:
        st.markdown(team)
        st.markdown("---")

# ✅ Dropdown for Selecting Team Member Type
view_option = st.selectbox("🔍 Find a Team Member Type:", ["Supervisor", "Lineman", "Fitter", "Karkun", "Employee Number", "All Teams Details"])

# ✅ If "All Teams Details" is selected, show all team details
if view_option == "All Teams Details":
    st.markdown("<h5 style='text-align: center; color:#3256db;'>📋 Complete Team Roster</h5>", unsafe_allow_html=True)
    
    for _, row in data.iterrows():
        st.markdown(f"""
        <div style='background-color: white; padding: 12px; border-radius: 8px; 
                    box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1); margin-bottom: 10px;'>
            <h5>🏷️ Supervisor: {row['Supervisor']} (Emp#: {row['Emp#']})</h5>
            <p><b>🛠 Task:</b> {row['Task']}</p>
            <p><b>👷 Lineman:</b> {row['Lineman']} (Emp#: {row['Lineman_Emp#']})</p>
            <p><b>🔧 Fitter:</b> {row['Fitter']} (Emp#: {row['Fitter_Emp#']})</p>
            <p><b>📌 Karkun:</b> {row['Karkun']} (Emp#: {row['Karkun_Emp#']})</p>
            <p><b>📅 Off Day:</b> {row['Off_Day']}</p>
            <p><b>⏰ Duty Time:</b> {row['Duty_Time']}</p>
        </div>
        """, unsafe_allow_html=True)

        # ✅ Dropdown for Selecting Name
selected_name = None

if view_option == "Supervisor":
    selected_name = st.selectbox("Select a Supervisor:", [""] + data["Supervisor"].tolist())
elif view_option == "Lineman":
    selected_name = st.selectbox("Select a Lineman:", [""] + data["Lineman"].tolist())
elif view_option == "Fitter":
    selected_name = st.selectbox("Select a Fitter:", [""] + data["Fitter"].tolist())
elif view_option == "Karkun":
    selected_name = st.selectbox("Select a Karkun:", [""] + data["Karkun"].tolist())
elif view_option == "Employee Number":
    selected_name = st.selectbox("Select or type an Employee Number:", [""] + 
                                 pd.concat([data["Emp#"], data["Lineman_Emp#"], data["Fitter_Emp#"], data["Karkun_Emp#"]])
                                 .dropna().unique().tolist())

# ✅ Show Details Only After Selection
if selected_name and selected_name.strip():
    details = data[(data["Supervisor"] == selected_name) | 
                   (data["Lineman"] == selected_name) |
                   (data["Fitter"] == selected_name) | 
                   (data["Karkun"] == selected_name) |
                   (data["Emp#"] == selected_name) |
                   (data["Lineman_Emp#"] == selected_name) |
                   (data["Fitter_Emp#"] == selected_name) |
                   (data["Karkun_Emp#"] == selected_name)]
    
    if not details.empty:
        details = details.iloc[0]  # Get first matching record

        # ✅ Display Details in Card Format
        st.markdown("<div style='background-color: white; padding: 12px; border-radius: 8px; "
                    "box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);'>", unsafe_allow_html=True)
        st.markdown(f"<h5>🏷️ Supervisor: {details['Supervisor']} (Emp#: {details['Emp#']})</h5>", unsafe_allow_html=True)
        st.write(f"**🛠 Task:** {details['Task']}")
        st.write(f"**👷 Lineman:** {details['Lineman']} (Emp#: {details['Lineman_Emp#']})")
        st.write(f"**🔧 Fitter:** {details['Fitter']} (Emp#: {details['Fitter_Emp#']})")
        st.write(f"**📌 Karkun:** {details['Karkun']} (Emp#: {details['Karkun_Emp#']})")
        st.write(f"**📅 Off Day:** {details['Off_Day']}")
        st.write(f"**⏰ Duty Time:** {details['Duty_Time']}")
        st.markdown("</div>", unsafe_allow_html=True)
        

# ✅ Footer
st.markdown("<hr style='border: 1px solid #ddd;'>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 14px; color: #555;'>🚀 This application is created by <b>Muhammad Yameen Saleem</b></p>", unsafe_allow_html=True)












