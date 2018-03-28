from mapr.ojai.ojai_query.QueryOp import QueryOp
from mapr.ojai.storage.ConnectionFactory import ConnectionFactory

# Create a connection to data access server
connection = ConnectionFactory.get_connection(url='localhost:5678')

# Get a store and assign it as a DocumentStore object
store = connection.get_store('/demo_table')

# Build an OJAI query
query = connection.new_query().where(connection.new_condition().is_('address.zipCode', QueryOp.EQUAL, 95196)
                                     .close().build()).build()

# fetch the OJAI Document by its '_id' field
doc_stream = store.find(query)

# Print OJAI Documents from document stream
for doc in doc_stream:
    print(doc.as_json_str())

# close the OJAI connection
connection.close()