import streamlit as st
from google.cloud import bigquery
from google.oauth2 import service_account

# Create API client.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)
client = bigquery.Client(credentials=credentials)


@st.cache_data(ttl=600, show_spinner="Running query...")  # cache for 10 minutes
def get_table_data():
    query_job = client.query("SELECT id, name, age, other_column FROM `data-test-warehouse.huat_test.test_table`")
    df = query_job.result().to_dataframe()
    return df


def sync_to_bigquery(df, table_id):
    job_config = bigquery.LoadJobConfig(
        write_disposition="WRITE_TRUNCATE"
    )
    client.load_table_from_dataframe(df, table_id, job_config=job_config).result()
    st.success("Table updated successfully in BigQuery!")
    get_table_data.clear()


data = get_table_data()

edited_data = st.data_editor(
    data,
    column_config={
        "id": st.column_config.NumberColumn("ID", min_value=0, step=1, required=True),
        "name": st.column_config.TextColumn("Name", help="Example tooltip to explain the column", required=True),
        "age": st.column_config.NumberColumn("Age", min_value=0, max_value=200, step=1, required=True),
        "other_column": st.column_config.TextColumn("Misc")
    },
    num_rows="dynamic"
)

if st.button("Sync Changes to BigQuery"):
    try:
        sync_to_bigquery(edited_data, "data-test-warehouse.huat_test.test_table")
        get_table_data.clear()  # clear cache
    except Exception as e:
        st.error(f"Failed to update table: {e}")

if st.button("Refresh table"):
    get_table_data.clear()  # clear cache
    st.rerun()
