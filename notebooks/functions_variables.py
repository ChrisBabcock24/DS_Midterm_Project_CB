def encode_tags(df):

    """Use this function to manually encode tags from each sale.
    You could also provide another argument to filter out low 
    counts of tags to keep cardinality to a minimum.
       
    Args:
        pandas.DataFrame

    Returns:
        pandas.DataFrame: modified with encoded tags
    """
    tags = df["tags"].tolist()
    # create a unique list of tags and then create a new column for each tag
        
    return df

# Function to flatten a single dictionary entry
def flatten_entry(entry):

    if isinstance(entry, dict):
        # Flatten dictionary
        return pd.json_normalize(entry)
    elif isinstance(entry, list):
        # Handle lists of primitives or dictionaries
        if len(entry) > 0 and isinstance(entry[0], dict):
            # List of dictionaries
            flat_df = pd.json_normalize(entry)
            return flat_df
        else:
            # List of primitives (e.g., integers, strings)
            # Convert list to DataFrame
            return pd.DataFrame({'values': entry})
    else:
        # Handle non-list, non-dict items (like strings or integers)
        return pd.DataFrame({'value': [entry]})


def flatten_data_column_with_index(df, column_name):
    flattened_rows = []

    for i, entry in enumerate(df[column_name]):
        if isinstance(entry, list):
            # If entry is a list, process each dictionary in the list
            for item in entry:
                if isinstance(item, dict):
                    flattened_df = flatten_entry(item)
                    #keep the original index to maintain association with original row
                    flattened_df['original_index'] = i
                    flattened_rows.append(flattened_df)
                else:
                    #skip any other item type
                    print(f"Skipping non-dictionary item in list: {item}")
        elif isinstance(entry, dict):
            # If entry is a single dictionary, flatten it directly
            flattened_df = flatten_entry(entry)
            #keep the original index to maintain association with original row
            flattened_df['original_index'] = i
            flattened_rows.append(flattened_df)
        else:
            #skip any other item type
            print(f"Skipping unsupported entry type: {entry}")
            #concatenates all DataFrames in flattened_rows into a single DataFrame
    return pd.concat(flattened_rows, ignore_index=True) if flattened_rows else pd.DataFrame()

def save_dataframe(df, base_filename='merged_df'):
    """
    Save the DataFrame to a CSV file with a timestamp to avoid overwriting.
    
    Parameters:
    df (pd.DataFrame): The DataFrame to save.
    base_filename (str): The base name of the file to save.
    """
    # Generate a timestamp for the filename
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"{base_filename}_{timestamp}.csv"
    
    # Save the DataFrame to CSV
    df.to_csv(filename, index=False)
    print(f"DataFrame saved to {filename}")

def handle_missing_values(df, column_name, fill_value=0, dtype=int):
    """
    Handle missing numeric values in a DataFrame column.

    Parameters:
    df (pd.DataFrame): The DataFrame containing the column.
    column_name (str): The name of the column to process.
    fill_value (numeric): The value to fill in place of missing values. Default is 0.
    dtype (type): The data type to convert the column to. Default is int.

    Returns:
    pd.DataFrame: The DataFrame with the specified column processed.
    """
    # Convert the column to numeric, forcing errors to NaN
    df[column_name] = pd.to_numeric(df[column_name], errors='coerce')
    
    # Replace NaN with the specified fill value
    df[column_name] = df[column_name].fillna(fill_value)
    
    # Convert the column to the specified type
    df[column_name] = df[column_name].astype(dtype)
    
    return df

# function to handle date and time strings that are in various formats
# and convert them into a uniform 'datetime' format.
# if it cannot determine the format it tries to infer the correct format using to_datetime.

def parse_dates(series):
    """
    Function to handle date and time strings that are in various formats
    and convert them into a uniform 'datetime' format.
    if it cannot determine the format it tries to infer the correct format using to_datetime.

    """

    formats = [
        '%Y-%m-%dT%H:%M:%S%z',  # ISO8601 format with timezone
        '%Y-%m-%d %H:%M:%S',    # Common datetime format
        '%Y-%m-%d',             # Date only format
        '%d/%m/%Y',             # Day/Month/Year format
        '%m/%d/%Y',             # Month/Day/Year format
        '%Y-%m-%d %H:%M'        # Date and time without seconds
    ]
    for fmt in formats:
        try:
            return pd.to_datetime(series, format=fmt, errors='coerce')
        except ValueError:
            continue
    return pd.to_datetime(series, errors='coerce')  # fallback to infer format

def check_null_counts(df):
    """
    This function calculates, sorts, and displays the number of null values for each column
    in the DataFrame df, with the highest counts at the top.
    
    Parameters:
    df (pd.DataFrame): The DataFrame to check for null values.
    
    Returns:
    pd.Series: A Series with columns as index and the number of null values as values, sorted in descending order.
    """
    # Count the number of null values per column
    null_counts = df.isnull().sum()
    
    # Sort the null counts in descending order
    sorted_null_counts = null_counts.sort_values(ascending=False)
    
    # Display the sorted null counts
    print("Sorted null value counts per column (highest first):")
    
    return sorted_null_counts