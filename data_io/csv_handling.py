import csv

""" Reading in CSV """


# Define a function to process data in chunks (for large files)
def process_chunk(chunk):
    # This is where you process each chunk of data
    for row in chunk:
        print(row)  # Example: Print each row (can be replaced with other processing)


# Set the size of each chunk to be read at once
chunk_size = 1000
chunk = []  # Initialize an empty list to store rows

# Open the CSV file in read mode
with open('large_dataset.csv', mode='r') as file:
    csv_reader = csv.reader(file)  # Create a CSV reader object
    header = next(csv_reader)  # Skip the header row, if present

    # Iterate through each row in the CSV file
    for row in csv_reader:
        chunk.append(row)  # Add each row to the chunk

        # Once the chunk reaches the specified size, process it
        if len(chunk) >= chunk_size:
            process_chunk(chunk)  # Process the chunk of rows
            chunk = []  # Reset chunk for the next set of rows

    # Process any remaining rows that didn’t fit into a full chunk
    if chunk:
        process_chunk(chunk)  # Process the final chunk if there are any left

import pandas as pd

# Set chunk size (e.g., 1000 rows at a time)
chunk_size = 1000
chunks = pd.read_csv('large_dataset.csv', chunksize=chunk_size)  # Read the file in chunks

# Iterate over each chunk returned by pandas
for chunk in chunks:
    # Process each chunk (pandas DataFrame)
    print(chunk.head())  # Print the first few rows of the current chunk for review

""" Writing in CSV """

import csv

# Example data to write (you can replace this with your own data)
data = [['Name', 'Age'], ['Alice', 30], ['Bob', 25], ['Charlie', 35]]

# Set the chunk size for writing (e.g., writing 1000 rows at a time)
chunk_size = 1000
chunk = []  # Initialize an empty list to store rows to be written

# Open the output CSV file in write mode
with open('output.csv', mode='w', newline='') as file:
    csv_writer = csv.writer(file)  # Create a CSV writer object

    # Iterate through each row in the data
    for row in data:
        chunk.append(row)  # Add each row to the chunk

        # Once the chunk reaches the specified size, write it to the file
        if len(chunk) >= chunk_size:
            csv_writer.writerows(chunk)  # Write the chunk to the file
            chunk = []  # Reset the chunk for the next set of rows

    # Write any remaining rows that didn’t fit into a full chunk
    if chunk:
        csv_writer.writerows(chunk)  # Write the final chunk of rows

# ------------------------------------------

import pandas as pd

# Example data (this could be from processing a large CSV file)
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [30, 25, 35]}
df = pd.DataFrame(data)  # Convert data into a pandas DataFrame

# Save the DataFrame to a CSV file
df.to_csv('output.csv', index=False)  # Write the DataFrame to 'output.csv' without the index
