# Trello Workspace JSON Parser

This Python script is designed to take a JSON export of a Trello workspace and parse it into a more human-readable JSON format. This transformation allows for easier analysis, querying, or importing into other tools. The script focuses on extracting relevant information from Trello cards, categorising them based on activity, and ensuring a consistent format for further processing.

## Features

- **Comment Extraction**: Extracts comments from Trello cards for detailed analysis.
- **Card Categorisation**: Categorises cards into 'active' and 'inactive' (archived) based on the presence of comments and creation dates.
- **Data Normalization**: Ensures a consistent format for all cards, including handling missing dates and restructuring card information.
- **JSON Output**: Outputs the processed data into a well-formatted JSON file, making it easy to use in other applications.

## Prerequisites

Before running this script, ensure you have Python installed on your system. This script was developed with Python 3.x.

## Usage

1. **Export Trello Workspace Data**:
   - Navigate to your Trello board.
   - Open the board menu by clicking "Show Menu" on the right side.
   - Click "More" and then "Print and Export".
   - Select "Export as JSON". Save the file to your local machine.

2. **Run the Script**:
   - Open a terminal or command prompt.
   - Navigate to the directory containing `trelloParser.py`.
   - Run the script using the following command:
     ```
     python trelloParser.py <path_to_your_trello_export.json>
     ```
   - Replace `<path_to_your_trello_export.json>` with the actual path to your downloaded Trello JSON file.

3. **Review the Output**:
   - The script will generate a file named `trelloData.json` in the same directory.
   - Open this file to view the parsed and reformatted Trello data.

## Disclaimer

This script is not affiliated with, sponsored by, or endorsed by Trello or Atlassian.