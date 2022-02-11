import pandas as pd
import plotly.express as px

df = pd.read_csv('data.csv')

trl_xsl = df.loc[df["student_id"] == "TRL_xsl"]
trl_abc = df.loc[df["student_id"] == "TRL_abc"]
trl_xyz = df.loc[df["student_id"] == "TRL_xyz"]
trl_zet = df.loc[df["student_id"] == "TRL_zet"]
trl_123 = df.loc[df["student_id"] == "TRL_123"]
trl_imb = df.loc[df["student_id"] == "TRL_imb"]
trl_rst = df.loc[df["student_id"] == "TRL_rst"]
trl_mno = df.loc[df["student_id"] == "TRL_mno"]
trl_987 = df.loc[df["student_id"] == "TRL_987"]
trl_mda = df.loc[df["student_id"] == "TRL_mda"]
trl_zny = df.loc[df["student_id"] == "TRL_zny"]

student_data = [trl_xsl, trl_abc, trl_xyz, trl_zet, trl_123, trl_imb, trl_rst, trl_mno, trl_987, trl_mda, trl_zny]
mean = ""

students = []
levels = []
attempts = []

for i in student_data:
    mean = i.groupby(["student_id", "level"], as_index = False)["attempt"].mean()
    for student in mean["student_id"]:
        students.append(student)
    for level in mean["level"]:
        levels.append(level)
    for attempt in mean["attempt"]:
        attempts.append(attempt)

fig = px.scatter(
    x = students,
    y = levels,
    color = attempts,
    size = attempts
)
fig.show()