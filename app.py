
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Customer Retention Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer Engagement & Product Utilisation Analytics")
st.subheader("Retention Strategy | Banking Analytics")
st.markdown("An analytical overview of customer churn, engagement and product usage.")

# KPI metrics
col1, col2, col3, col4, col5 = st.columns(5

)

col1.metric("Total Customers", "10,000")
col2.metric("Exited Customers", "2,037")
col3.metric("Retained Customers", "7,963")
col4.metric("Churn Rate", "20.37%")
col5.metric("Retention Rate", "79.63%")

st.divider()

# Age analysis
age_data = pd.DataFrame({
    "Age Group": ["18–24", "25–34", "35–44", "45–54", "55–64", "65+"],
    "Churn Rate (%)": [8.75, 7.76, 17.66, 48.15, 49.83, 15.25]
})

# Geography analysis
geo_data = pd.DataFrame({
    "Geography": ["France", "Germany", "Spain"],
    "Customers": [5014, 2509, 2477],
    "Churn Rate (%)": [16.15, 32.44, 16.67]
})

# Gender analysis
gender_data = pd.DataFrame({
    "Gender": ["Female", "Male"],
    "Customers": [4543, 5457],
    "Churn Rate (%)": [25.07, 16.45]
})

# Engagement analysis
engagement_data = pd.DataFrame({
    "Activity Status": ["Active", "Inactive"],
    "Customers": [5151, 4849],
    "Churn Rate (%)": [14.27, 26.85]
})

# Product analysis
product_data = pd.DataFrame({
    "Product Category": ["1 Product", "2 Products", "3 Products", "4 Products"],
    "Customers": [5084, 4590, 266, 60],
    "Churn Rate (%)": [27.71, 7.58, 82.71, 100.00]
})

# Relationship tier
tier_data = pd.DataFrame({
    "Relationship Tier": ["Strong", "Moderate", "Weak"],
    "Customers": [3095, 3235, 3710],
    "Churn Rate (%)": [11.80, 19.87, 28.17]
})

# Credit card
card_data = pd.DataFrame({
    "Credit Card": ["No Card", "Card"],
    "Customers": [2945, 7055],
    "Churn Rate (%)": [20.81, 20.18]
})

st.header("Customer Churn Analysis")

tab1, tab2, tab3 = st.tabs([
    "Age & Geography", "Engagement & Products", "Relationships"
])

with tab1:
    left, right = st.columns(2)

    with left:
        fig = px.bar(
            age_data, x="Age Group", y="Churn Rate (%)",
            title="Churn Rate by Age Group",
            text="Churn Rate (%)"
        )
        fig.update_traces(texttemplate="%{text:.1f}%", textposition="outside")
        st.plotly_chart(fig, use_container_width=True)

    with right:
        fig = px.bar(
            geo_data, x="Geography", y="Churn Rate (%)",
            title="Churn Rate by Geography",
            text="Churn Rate (%)"
        )
        fig.update_traces(texttemplate="%{text:.1f}%", textposition="outside")
        st.plotly_chart(fig, use_container_width=True)

    st.dataframe(age_data, use_container_width=True)
    st.dataframe(geo_data, use_container_width=True)

with tab2:
    left, right = st.columns(2)

    with left:
        fig = px.bar(
            engagement_data, x="Activity Status", y="Churn Rate (%)",
            title="Churn by Activity Status",
            text="Churn Rate (%)"
        )
        fig.update_traces(texttemplate="%{text:.1f}%", textposition="outside")
        st.plotly_chart(fig, use_container_width=True)

    with right:
        fig = px.bar(
            product_data, x="Product Category", y="Churn Rate (%)",
            title="Churn by Number of Products",
            text="Churn Rate (%)"
        )
        fig.update_traces(texttemplate="%{text:.1f}%", textposition="outside")
        st.plotly_chart(fig, use_container_width=True)

    st.dataframe(engagement_data, use_container_width=True)
    st.dataframe(product_data, use_container_width=True)

with tab3:
    left, right = st.columns(2)

    with left:
        fig = px.bar(
            tier_data, x="Relationship Tier", y="Churn Rate (%)",
            title="Churn by Relationship Tier",
            text="Churn Rate (%)"
        )
        fig.update_traces(texttemplate="%{text:.1f}%", textposition="outside")
        st.plotly_chart(fig, use_container_width=True)

    with right:
        fig = px.bar(
            card_data, x="Credit Card", y="Churn Rate (%)",
            title="Churn by Credit Card Ownership",
            text="Churn Rate (%)"
        )
        fig.update_traces(texttemplate="%{text:.1f}%", textposition="outside")
        st.plotly_chart(fig, use_container_width=True)

    st.dataframe(tier_data, use_container_width=True)
    st.dataframe(card_data, use_container_width=True)

st.divider()

st.header("Key Business Insights")

st.markdown("""
- Customers aged **45–64** show the highest churn rates.
- **Germany** has higher churn than France and Spain.
- **Inactive customers** have higher churn than active customers.
- Customers with **one product** show higher churn than those with two products.
- The three- and four-product groups show very high churn but contain relatively few customers.
- Customers in the **Weak relationship tier** show higher churn than Strong-tier customers.
- Credit card ownership shows only a small churn-rate difference.
""")

st.header("Retention Strategy Recommendations")

st.markdown("""
1. Prioritise retention outreach for customers aged 45–64.
2. Investigate customer experience and service issues in Germany.
3. Re-engage inactive customers through personalised communication.
4. Review the needs of single-product customers and offer relevant support.
5. Investigate the small high-churn multi-product segments before making decisions.
6. Strengthen relationships with customers in the Weak relationship tier.
7. Use customer-level evidence and testing before implementing retention campaigns.
""")

st.info(
    "This dashboard presents aggregated analysis. "
    "Relationship scores and tiers are exploratory indicators, not causal measures. "
    "The dataset does not include revenue, profit, campaign costs or customer lifetime value."
)

st.caption("Project | Financial Analytics | Unified Mentor")
