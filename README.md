🛍️ Customer Segmentation Project


A data science workflow for segmenting wholesale customers based on spending habits, using KMeans clustering and Python.


📑 Overview

Goal: Identify natural customer groups (segments) to enable personalized marketing and business strategies.

Approach: Clean and analyze spending data, cluster customers using KMeans, and visualize segment characteristics
<img width="925" height="792" alt="Screenshot 2025-07-31 155656" src="https://github.com/user-attachments/assets/5dd43bce-bc2c-464b-acf5-a5cc4ea6d651" />


🗂️ Project Structure


customer-segmentation/

├── dataset/

│   └── wholesale.csv                  # Customer data

├── notebooks/

│   └── customer_segmentation.ipynb    # Main analysis notebook

├── requirements.txt                   # Dependencies

├── README.md                          # Project summary and instructions

└── .gitignore

🚀 Getting Started

1.Place your wholesale.csv inside /dataset.

2.Install dependencies:
pip install -r requirements.txt

3.Open and run notebooks/customer_segmentation.ipynb.


🔍 Features
  Exploratory Data Analysis: Histograms, correlation heatmap of spending features.

  Data Preprocessing: Feature selection and scaling.

  KMeans Clustering: Unsupervised segmentation.

  Visualization: PCA scatter plots of clusters, cluster size bar chart.

  Cluster Interpretation: Average spend per cluster, segment profiling.

🛠 Tech Stack

->Python 3.x

->pandas, numpy

->scikit-learn

->matplotlib, seaborn

->Jupyter Notebook

📊 Example Outputs

 •Histograms: Show the spending distribution for each product category.

 •Correlation Heatmap: Highlights relationships between spending features.

 •PCA Plot: Reveals customer groups in 2D space, colored by segment.

 •Cluster Counts: Bar chart showing the size of each customer segment.

 •Feature Means Table: Summarizes typical buyer behavior for each segment.


 📝 Interpretation
 
  Each segment represents a distinct customer type based on purchase behavior (e.g., "Bulk       Grocery Buyers", "Fresh Product Specialists", "Small-Volume Customers"), helping guide business insights and targeted actions.
  
👤 Author

P.Haritha varshini

You can use this README.md as is, or adapt it for your specific output and insights in your project notebook and images.
