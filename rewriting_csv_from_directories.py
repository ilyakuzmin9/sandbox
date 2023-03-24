import os
import csv

def process_csv_files(a_input_dir, a_output_dir):
    """
    Process all CSV files in the input directory, and write the processed data
    to new CSV files in the output directory.
    """

    # Create the output directory if it does not exist
    os.makedirs(a_output_dir, exist_ok=True)

    # Loop over all files in the input directory
    for filename in os.listdir(a_input_dir):
        if filename.endswith('.csv'):

            # Set the input and output file paths
            input_file = os.path.join(a_input_dir, filename)
            output_file = os.path.join(a_output_dir, filename)

            # Open the input file in read mode
            with open(input_file, 'r', newline='') as infile:
                reader = csv.reader(infile)

                # Check if the input file has a header
                has_header = csv.Sniffer().has_header(infile.read(1024))
                infile.seek(0)

                # If the input file does not have a header, add one
                if not has_header:
                    header = ['Hash']  # replace with your own header
                    rows = [header] + list(reader)
                else:
                    rows = list(reader)

            # Remove double newlines from the data
            processed_rows = []
            for row in rows:
                processed_row = [cell.replace('\n\n', '\n') if isinstance(cell, str) else cell for cell in row]
                if processed_row != []:
                    processed_rows.append(processed_row)

            # Open the output file in write mode
            with open(output_file, 'w', newline='') as outfile:
                writer = csv.writer(outfile)

                # Write the processed data to the output file
                writer.writerows(processed_rows)
