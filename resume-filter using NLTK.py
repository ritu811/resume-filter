import os
import PyPDF2
from docx import Document
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

def extract_text_from_pdf(pdf_file):
    with open(pdf_file, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        text = ''
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
        return text

def extract_text_from_docx(docx_file):
    doc = Document(docx_file)
    text = ''
    for paragraph in doc.paragraphs:
        text += paragraph.text + '\n'
    return text

def preprocess_text(text):
    # Tokenization and removing stop words
    tokens = nltk.word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words and word.isalnum()]
    return ' '.join(filtered_tokens)

def extract_keywords(text):
    # Extract keywords using TF-IDF
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([text])
    feature_names = vectorizer.get_feature_names_out()
    sorted_indices = tfidf_matrix.toarray().argsort()[0][::-1]
    top_keywords = [feature_names[idx] for idx in sorted_indices[:5]]  # Get top 5 keywords
    return top_keywords

def filter_resumes(resumes_folder, keywords):
    total_resumes = 0
    filtered_resumes = []
    for filename in os.listdir(resumes_folder):
        if filename.endswith('.pdf'):
            text = extract_text_from_pdf(os.path.join(resumes_folder, filename))
        elif filename.endswith('.docx'):
            text = extract_text_from_docx(os.path.join(resumes_folder, filename))
        else:
            continue
        
        # Preprocess text
        preprocessed_text = preprocess_text(text)
        
        # Check if any of the keywords are present in the resume
        if any(keyword.lower() in preprocessed_text.lower() for keyword in keywords):
            filtered_resumes.append(filename)
    
    return filtered_resumes

# Define roles and associated keywords
roles_keywords = {
    'Graphic Designer': ['graphic design', 'illustrator', 'photoshop'],
    'Software Engineer': ['programming', 'software development', 'coding'],
    'Data Analyst': ['data analysis', 'sql', 'excel']
}

# Prompt user to select a role
print("Select a role to hire:")
for i, role in enumerate(roles_keywords.keys(), 1):
    print(f"{i}. {role}")
choice = int(input("Enter the number corresponding to the role: "))
roles = list(roles_keywords.keys())
selected_role = roles[choice - 1]
keywords = roles_keywords[selected_role]

# Path to resumes folder
resumes_folder = r'C:\Users\Rana V\Desktop\internship\Resume Filter\resumes'

# Filter resumes based on selected role and keywords
filtered_resumes = filter_resumes(resumes_folder, keywords)

# Pie chart representation
total_resumes = len(os.listdir(resumes_folder))
percentage_filtered = (len(filtered_resumes) / total_resumes) * 100

labels = ['Filtered Resumes', 'Remaining Resumes']
sizes = [percentage_filtered, 100 - percentage_filtered]
colors = ['lightcoral', 'lightskyblue']
explode = (0.1, 0)  # explode 1st slice

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.title('Resumes Filtered')

# Adding annotation for the filtered resumes
annotation = "Filtered Resumes:\n" + "\n".join(filtered_resumes)
plt.text(1.5, 0.5, annotation, fontsize=10, va='top')

plt.show()