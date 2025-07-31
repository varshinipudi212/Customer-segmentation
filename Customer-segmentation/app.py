import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

st.title("Customer Segmentation Explorer")
uploaded_file = st.file_uploader("Upload your wholesale.csv", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv('dataset/wholesale.csv')
st.write(df.head())

feature_cols = ['Fresh', 'Milk', 'Grocery', 'Frozen', 'Detergents_Paper', 'Delicassen']
k = st.slider('Number of customer segments (clusters):', 2, 6, 3)
X_scaled = StandardScaler().fit_transform(df[feature_cols])
kmeans = KMeans(n_clusters=k, random_state=42)
labels = kmeans.fit_predict(X_scaled)
df['Segment'] = labels

pca = PCA(n_components=2)
reduced = pca.fit_transform(X_scaled)
fig, ax = plt.subplots()
scatter = ax.scatter(reduced[:,0], reduced[:,1], c=labels, cmap='tab10', alpha=0.7)
legend1 = ax.legend(*scatter.legend_elements(), title="Segment")
ax.add_artist(legend1)
plt.xlabel("PCA 1")
plt.ylabel("PCA 2")
plt.title("Customer Segments (PCA)")
st.pyplot(fig)

st.subheader("Customers per Segment")
st.bar_chart(df['Segment'].value_counts(sort=False))

st.subheader("Average Spend per Segment")
st.dataframe(df.groupby('Segment')[feature_cols].mean().round(2))

csv = df.to_csv(index=False).encode('utf-8')
st.download_button("Download Segmented Data", data=csv, file_name="customers_segmented.csv")
