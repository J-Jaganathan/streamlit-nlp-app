# Streamlit NLP App

This project is a Streamlit application that allows users to upload a PDF file and extract specific information using Natural Language Processing (NLP) techniques. The application utilizes the PyPDF2 library to read PDF files and regex patterns to extract relevant data.

## Project Structure

```
streamlit-nlp-app
├── src
│   ├── app.py          # Main entry point for the Streamlit application
│   ├── nlp.py          # Contains NLP functionality for PDF text extraction
├── requirements.txt     # Lists the dependencies required for the project
└── README.md            # Documentation for the project
```

## Installation

To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd streamlit-nlp-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit application:
   ```
   streamlit run src/app.py
   ```

2. Open your web browser and navigate to `http://localhost:8501`.

3. Use the file uploader to upload a PDF file. The application will extract and display the relevant information from the PDF.

## Dependencies

The project requires the following Python packages:

- Streamlit
- PyPDF2

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.