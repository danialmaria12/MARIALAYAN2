import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Students' Social Media Addiction", layout="wide")

# Title and intro
st.title("📱 Students' Social Media Addiction Dashboard")
st.markdown("""
Welcome to our dashboard! This app explores students’ social media usage, sleep patterns, and addiction scores using visual analytics.
""")

# Load dataset
st.subheader("📂 Load Dataset")
try:
    df = pd.read_csv("Students Social Media Addiction.csv")
    st.success("CSV loaded successfully!")
except FileNotFoundError:
    st.error("❌ Could not find the file 'Students Social Media Addiction.csv'. Please make sure it's in the same folder as app.py.")
    st.stop()

# Show data preview
st.subheader("👀 Dataset Preview")
st.dataframe(df.head())

# Plot 1: Daily Social Media Usage
st.subheader("📊 Distribution of Daily Social Media Usage (Hours)")
fig1, ax1 = plt.subplots()
sns.histplot(data=df, x='Avg_Daily_Usage_Hours', bins=10, kde=True, ax=ax1)
ax1.set_title("Daily Social Media Usage")
ax1.set_xlabel("Hours")
ax1.set_ylabel("Number of Students")
st.pyplot(fig1)

# Plot 2: Addiction Score by Gender
st.subheader("🧠 Addiction Score by Gender")
fig2, ax2 = plt.subplots()
sns.boxplot(data=df, x='Gender', y='Addicted_Score', palette='Set2', ax=ax2)
ax2.set_title("Addiction Score by Gender")
ax2.set_xlabel("Gender")
ax2.set_ylabel("Addiction Score")
st.pyplot(fig2)

# Plot 3: Sleep vs Addiction
st.subheader("💤 Sleep Hours vs. Addiction Score")
fig3, ax3 = plt.subplots()
sns.lineplot(data=df, x='Sleep_Hours_Per_Night', y='Addicted_Score', ax=ax3)
ax3.set_title("Relationship Between Sleep and Addiction Score")
ax3.set_xlabel("Sleep Hours Per Night")
ax3.set_ylabel("Addiction Score")
st.pyplot(fig3)

# Footer
st.markdown("---")
st.markdown("✨ Created with ❤️ by Maria & Team | Reichman University 2025")
