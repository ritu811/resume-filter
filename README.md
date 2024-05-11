Libraries Used:
os: Provides functions for interacting with the operating system, such as reading file paths.
PyPDF2: A library for reading and manipulating PDF files.
docx (python-docx): Used for reading and writing Microsoft Word (.docx) files.
matplotlib.pyplot: Used for creating visualizations, in this case, a pie chart.
nltk: Natural Language Toolkit, used for text processing tasks like tokenization and stop word removal.
sklearn.feature_extraction.text.TfidfVectorizer: A part of scikit-learn library, used for converting a collection of raw documents to a matrix of TF-IDF features.

Functionality:
extract_text_from_pdf(pdf_file): Reads text from a PDF file using PyPDF2 library.
extract_text_from_docx(docx_file): Reads text from a Word document (.docx) using python-docx library.
preprocess_text(text): Tokenizes the input text, removes stop words, and filters out non-alphanumeric characters.
extract_keywords(text): Extracts top keywords from the input text using TF-IDF.
filter_resumes(resumes_folder, keywords): Filters resumes in a specified folder based on keywords associated with different job roles. It uses the previously defined functions to extract text from resumes, preprocess it, and check for the presence of keywords.
roles_keywords: A dictionary containing predefined roles as keys and associated keywords as values.
User Prompt: Asks the user to select a role from the predefined roles.
Pie Chart Visualization: Generates a pie chart to visualize the percentage of resumes filtered. It calculates the percentage of filtered resumes out of total resumes and displays it along with the remaining percentage. Also, it annotates the chart with the filenames of the filtered resumes.
