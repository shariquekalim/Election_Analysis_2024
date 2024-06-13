import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.header('2024 Election Analysis')
data=pd.read_csv('election_results_2024.csv')
# st.dataframe(data)

# st.subheader('Parties with seats')
seat_count=data['Leading Party'].value_counts()
plt.figure(figsize=(20,8))
sns.barplot(x=seat_count.index, y=seat_count.values,palette='viridis')
plt.xlabel('Party',fontsize=20)
plt.ylabel('Seats',fontsize=20)
plt.xticks(rotation=80)
st.title('1.Seats per Party')
st.pyplot(plt)

# Margin win for Rahul, Modi ,Amit
rahul_entries = data[data['Leading Candidate'] == 'RAHUL GANDHI']
modi_entries = data[data['Leading Candidate'] == 'NARENDRA MODI']
amit_entries = data[data['Leading Candidate'] == 'AMIT SHAH']

rahul_margin=rahul_entries['Margin'].values 
modi_margin=modi_entries['Margin'].values[0] if not modi_entries.empty else 0
amit_margin=amit_entries['Margin'].values[0] if not amit_entries.empty else 0

rahul_constituency=list(rahul_entries['Constituency'])
modi_constituency=modi_entries['Constituency'].values[0] if not modi_entries.empty else "Modi Constituency"
amit_constituency=amit_entries['Constituency'].values[0] if not amit_entries.empty else "Amit Constituency"

data_to_plot = pd.DataFrame({
    'Candidate': ['Rahul Gandhi'] * len(rahul_margin) + ['Narendra Modi', 'Amit Shah'],
    'Constituency': rahul_constituency + [modi_constituency, amit_constituency],
    'Votes': list(rahul_margin) + [modi_margin, amit_margin]
})

plt.figure(figsize=(12, 6))
sns.barplot(data=data_to_plot, x='Constituency', y='Votes', hue='Candidate', palette='muted')
plt.title('Comparison of Votes for Rahul Gandhi, Narendra Modi, and Amit Shah')
plt.xlabel('Constituency',fontsize=20)
plt.ylabel('Votes',fontsize=20)
plt.xticks(rotation=45)
st.title('2. Margin win for Rahul, Modi ,Amit ')
st.pyplot(plt)

# Candidate who win by Max & Min Margin

data['Margin'] = pd.to_numeric(data['Margin'], errors='coerce')
max_margin_row = data.loc[data['Margin'].idxmax()]
min_margin_row = data.loc[data['Margin'].idxmin()]

data_to_plot=pd.DataFrame({
    'Candidate':[max_margin_row['Leading Candidate'] ,min_margin_row['Leading Candidate']] ,
    'Party':[max_margin_row['Leading Party'] ,min_margin_row['Leading Party']],
    'Margin':[max_margin_row['Margin'],min_margin_row['Margin']]
})

plt.figure(figsize=(10, 6))
sns.barplot(data=data_to_plot, x='Candidate', y='Margin', hue='Party', palette='muted')
plt.title('Candidates with Highest and Lowest Margin of Victory')
plt.xlabel('Candidate',fontsize=20)
plt.ylabel('Margin of Victory',fontsize=20)
plt.xticks(rotation=45)
st.title('3. Candidate who win by Max & Min Margin ')
st.pyplot(plt)

# Party Seat with percentage

party_seat=data['Leading Party'].value_counts()

plt.figure(figsize=(10, 8))
wedges, texts, autotexts = plt.pie(party_seat, labels=None, autopct='%1.1f%%', startangle=140, wedgeprops=dict(edgecolor='w'))
plt.title('Votes Distribution by Party', pad=20)
plt.axis('equal')

plt.legend(labels=party_seat.index, loc='center left', bbox_to_anchor=(1, 0.5), fontsize='medium')

st.title('4. Party Seat with percentage')
st.pyplot(plt)

# Top 10 Leading Party by votes

leading_party=data.groupby('Leading Party')['Margin'].sum().sort_values(ascending=False)
plt.figure(figsize=(20, 6))
plt.subplot(1, 2, 1)
sns.barplot(x=leading_party.index[:10], y=leading_party.values[:10], palette='viridis')
plt.title('Top 10 Leading Parties by Votes')
plt.xlabel('Party')
plt.ylabel('Total Votes')
plt.xticks(rotation=45)
st.title('5. Top 10 Leading Party by votes ')
st.pyplot(plt)

# Top 10 Leading party by SEAT

leading_party_seat=data['Leading Party'].value_counts()
plt.figure(figsize=(20, 6))
plt.subplot(1, 2, 2)
sns.barplot(x=leading_party_seat.index[:10], y=leading_party_seat.values[:10], palette='viridis')
plt.title('Top 10 Leading Parties by Seats')
plt.xlabel('Party')
plt.ylabel('Number of Seats')
plt.xticks(rotation=90)
plt.tight_layout()

st.title('6. Top 10 Leading party by SEAT')
st.pyplot(plt)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.header('2024 Election Analysis')
data=pd.read_csv('election_results_2024.csv')
# st.dataframe(data)

# st.subheader('Parties with seats')
seat_count=data['Leading Party'].value_counts()
plt.figure(figsize=(20,8))
sns.barplot(x=seat_count.index, y=seat_count.values,palette='viridis')
plt.xlabel('Party',fontsize=20)
plt.ylabel('Seats',fontsize=20)
plt.xticks(rotation=80)
st.title('1.Seats per Party')
st.pyplot(plt)

# Margin win for Rahul, Modi ,Amit
rahul_entries = data[data['Leading Candidate'] == 'RAHUL GANDHI']
modi_entries = data[data['Leading Candidate'] == 'NARENDRA MODI']
amit_entries = data[data['Leading Candidate'] == 'AMIT SHAH']

rahul_margin=rahul_entries['Margin'].values 
modi_margin=modi_entries['Margin'].values[0] if not modi_entries.empty else 0
amit_margin=amit_entries['Margin'].values[0] if not amit_entries.empty else 0

rahul_constituency=list(rahul_entries['Constituency'])
modi_constituency=modi_entries['Constituency'].values[0] if not modi_entries.empty else "Modi Constituency"
amit_constituency=amit_entries['Constituency'].values[0] if not amit_entries.empty else "Amit Constituency"

data_to_plot = pd.DataFrame({
    'Candidate': ['Rahul Gandhi'] * len(rahul_margin) + ['Narendra Modi', 'Amit Shah'],
    'Constituency': rahul_constituency + [modi_constituency, amit_constituency],
    'Votes': list(rahul_margin) + [modi_margin, amit_margin]
})

plt.figure(figsize=(12, 6))
sns.barplot(data=data_to_plot, x='Constituency', y='Votes', hue='Candidate', palette='muted')
plt.title('Comparison of Votes for Rahul Gandhi, Narendra Modi, and Amit Shah')
plt.xlabel('Constituency',fontsize=20)
plt.ylabel('Votes',fontsize=20)
plt.xticks(rotation=45)
st.title('2. Margin win for Rahul, Modi ,Amit ')
st.pyplot(plt)

# Candidate who win by Max & Min Margin

data['Margin'] = pd.to_numeric(data['Margin'], errors='coerce')
max_margin_row = data.loc[data['Margin'].idxmax()]
min_margin_row = data.loc[data['Margin'].idxmin()]

data_to_plot=pd.DataFrame({
    'Candidate':[max_margin_row['Leading Candidate'] ,min_margin_row['Leading Candidate']] ,
    'Party':[max_margin_row['Leading Party'] ,min_margin_row['Leading Party']],
    'Margin':[max_margin_row['Margin'],min_margin_row['Margin']]
})

plt.figure(figsize=(10, 6))
sns.barplot(data=data_to_plot, x='Candidate', y='Margin', hue='Party', palette='muted')
plt.title('Candidates with Highest and Lowest Margin of Victory')
plt.xlabel('Candidate',fontsize=20)
plt.ylabel('Margin of Victory',fontsize=20)
plt.xticks(rotation=45)
st.title('3. Candidate who win by Max & Min Margin ')
st.pyplot(plt)

# Party Seat with percentage

party_seat=data['Leading Party'].value_counts()

plt.figure(figsize=(10, 8))
wedges, texts, autotexts = plt.pie(party_seat, labels=None, autopct='%1.1f%%', startangle=140, wedgeprops=dict(edgecolor='w'))
plt.title('Votes Distribution by Party', pad=20)
plt.axis('equal')

plt.legend(labels=party_seat.index, loc='center left', bbox_to_anchor=(1, 0.5), fontsize='medium')

st.title('4. Party Seat with percentage')
st.pyplot(plt)

# Top 10 Leading Party by votes

leading_party=data.groupby('Leading Party')['Margin'].sum().sort_values(ascending=False)
plt.figure(figsize=(20, 6))
plt.subplot(1, 2, 1)
sns.barplot(x=leading_party.index[:10], y=leading_party.values[:10], palette='viridis')
plt.title('Top 10 Leading Parties by Votes')
plt.xlabel('Party')
plt.ylabel('Total Votes')
plt.xticks(rotation=45)
st.title('5. Top 10 Leading Party by votes ')
st.pyplot(plt)

# Top 10 Leading party by SEAT

leading_party_seat=data['Leading Party'].value_counts()
plt.figure(figsize=(20, 6))
plt.subplot(1, 2, 2)
sns.barplot(x=leading_party_seat.index[:10], y=leading_party_seat.values[:10], palette='viridis')
plt.title('Top 10 Leading Parties by Seats')
plt.xlabel('Party')
plt.ylabel('Number of Seats')
plt.xticks(rotation=90)
plt.tight_layout()

st.title('6. Top 10 Leading party by SEAT')
st.pyplot(plt)
