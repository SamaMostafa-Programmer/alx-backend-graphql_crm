from datetime import datetime
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

def log_crm_heartbeat():
    # GraphQL client
    transport = RequestsHTTPTransport(
        url="http://localhost:8000/graphql",
        verify=True,
        retries=3,
    )

    client = Client(
        transport=transport,
        fetch_schema_from_transport=True
    )

    # Optional hello query
    query = gql("""
    query {
        hello
    }
    """)

    try:
        client.execute(query)
    except Exception:
        pass

    timestamp = datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    with open("/tmp/crm_heartbeat_log.txt", "a") as f:
        f.write(f"{timestamp} CRM is alive\n")

from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from datetime import datetime

def update_low_stock():
    transport = RequestsHTTPTransport(
        url="http://localhost:8000/graphql",
        verify=True,
        retries=3,
    )

    client = Client(transport=transport, fetch_schema_from_transport=True)

    mutation = gql("""
    mutation {
      updateLowStockProducts {
        success
        products {
          name
          stock
        }
      }
    }
    """)

    result = client.execute(mutation)

    with open("/tmp/low_stock_updates_log.txt", "a") as f:
        for p in result["updateLowStockProducts"]["products"]:
            f.write(f"{datetime.now()} - {p['name']} new stock: {p['stock']}\n")
