import gradio as gr
from transformers import pipeline

# Load saved model and tokenizer
classifier = pipeline(
    "text-classification",
    model="saved_model",
    tokenizer="saved_model"
)

# Label mapping
labels = {
    "LABEL_0": "World",
    "LABEL_1": "Sports",
    "LABEL_2": "Business",
    "LABEL_3": "Sci/Tech"
}

# Prediction function
def predict_news(text):

    # Handle empty input
    if text.strip() == "":
        return "Please enter a news headline."

    # Get prediction
    prediction = classifier(text)[0]

    # Extract values
    category = labels[prediction["label"]]
    confidence = prediction["score"]

    # Return formatted result
    return f"""
Predicted Category: {category}

Confidence Score: {confidence:.4f}
"""

# Create Gradio interface
interface = gr.Interface(
    fn=predict_news,

    inputs=gr.Textbox(
        lines=3,
        placeholder="Enter a news headline here..."
    ),

    outputs=gr.Textbox(),

    title="News Topic Classifier Using BERT",

    description="""
This application classifies news headlines into:
- World
- Sports
- Business
- Sci/Tech

Model: bert-base-uncased fine-tuned on AG News Dataset
"""
)

# Launch app
interface.launch(share=True)
