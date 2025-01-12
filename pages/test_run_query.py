import streamlit as st
from google.oauth2 import service_account
from google.cloud import bigquery

# Create API client.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)
client = bigquery.Client(credentials=credentials)


# Function to run the query
def run_query(query):
    query_job = client.query(query)
    # Convert query results to a pandas DataFrame
    df = query_job.result().to_dataframe()
    return df


# Streamlit app
st.title("BigQuery Explorer")

# Input field for SQL query
user_query = st.text_area("Enter your SQL query:", placeholder="Write your BigQuery SQL here...")

# Button to run the query
if st.button("Run Query"):
    if user_query.strip():  # Check if the query is not empty
        try:
            st.write("Executing query...")
            # Run the query and display results
            query_result = run_query(user_query)
            st.write("Query Results:")
            st.dataframe(query_result)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a valid SQL query.")
