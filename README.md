# News Topic Classifier Using BERT

## Project Overview

This project is a Natural Language Processing (NLP) application that classifies news headlines into different topic categories using a fine-tuned BERT transformer model. The model is trained on the AG News Dataset and predicts the category of a given news headline.

The application is deployed using Gradio for interactive real-time predictions.

---

## Objective

The objective of this project is to:

- Fine-tune a pretrained transformer model for text classification
- Perform NLP preprocessing and tokenization
- Evaluate model performance using classification metrics
- Deploy the trained model using Gradio

---

## Dataset

Dataset Used: AG News Dataset

Source:
Hugging Face Datasets

The dataset contains news headlines categorized into four classes:

- World
- Sports
- Business
- Sci/Tech

Each sample contains:
- Text (news headline/article)
- Label (category index)

---

## Model Used

Model:
bert-base-uncased

Framework:
Hugging Face Transformers

Architecture Flow:

Input Text  
→ Tokenizer  
→ BERT Encoder  
→ Classification Layer  
→ Predicted Category

---

## Technologies Used

- Python
- Hugging Face Transformers
- PyTorch
- Scikit-learn
- Datasets Library
- Gradio
- Google Colab

---

## Project Workflow

### 1. Data Loading
- Loaded AG News Dataset using Hugging Face Datasets library

### 2. Text Preprocessing
- Tokenized text using BERT tokenizer
- Applied truncation and padding

### 3. Model Fine-Tuning
- Loaded pretrained bert-base-uncased model
- Added classification layer for 4 classes
- Fine-tuned model on AG News dataset

### 4. Evaluation
Evaluated model using:
- Accuracy
- F1-score

### 5. Deployment
- Built interactive interface using Gradio
- Enabled real-time headline classification

---

## Model Performance

| Metric | Score |
|--------|--------|
| Accuracy | 93% - 95% |
| F1-score | 93% - 95% |

---

## Example Predictions

| News Headline | Predicted Category |
|---------------|-------------------|
| Pakistan wins cricket series | Sports |
| NASA discovers new planet | Sci/Tech |
| Stock market crashes globally | Business |
| UN climate summit begins today | World |

---

## How to Run the Project

### 1. Clone Repository

```bash
git clone https://github.com/your-username/Task1_BERT_News_Classifier.git
cd Task1_BERT_News_Classifier
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Notebook

Open notebook.ipynb in Google Colab or Jupyter Notebook.

### 4. Run Gradio Application

```bash
python app.py
```

---

## Project Structure

```text
Task1_BERT_News_Classifier/
│
├── notebook.ipynb
├── app.py
├── requirements.txt
├── README.md
└── screenshots/
```

---

## Key Learnings

- Transformer-based NLP models
- Fine-tuning pretrained BERT models
- Text tokenization and preprocessing
- Evaluation using classification metrics
- Model deployment using Gradio

---

## Future Improvements

- Deploy on Hugging Face Spaces
- Compare BERT with DistilBERT and RoBERTa
- Add confusion matrix visualization
- Improve UI design
- Integrate live news API

---

## Author

Musfira Zainab

AI/ML Engineering Internship Project  
DevelopersHub Corporation

---

## License

This project is developed for educational and internship purposes.
