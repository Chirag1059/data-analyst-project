import pandas as pd


def load_data(file_path):
    """Load data from a specified file path."""
    return pd.read_csv(file_path)


def handle_missing_values(df):
    """Handle missing values in the DataFrame."""
    # Example strategy: Fill missing values with the mean of each column
    return df.fillna(df.mean())


def remove_duplicates(df):
    """Remove duplicate rows from the DataFrame."""
    return df.drop_duplicates()


def detect_outliers(df):
    """Detect outliers in the DataFrame using the IQR method."""
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1
    return df[~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]


def save_processed_data(df, output_file_path):
    """Save processed DataFrame to a specified output file path."""
    df.to_csv(output_file_path, index=False)