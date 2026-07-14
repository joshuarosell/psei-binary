# Stock Market Prediction Dashboard

A Streamlit-based dashboard for stock market prediction using machine learning and AI-powered analysis.

## Features

- 📊 Interactive stock market data visualization
- 🤖 Binary classification for stock movement prediction (Up/Down)
- 🔍 AI-powered analysis using OpenAI and HuggingFace models
- 📄 PDF document processing capabilities
- 📈 Real-time predictions with Plotly visualizations

## Project Structure

```
STREAMLIT BINARY/
├── stocks_dashboard.py          # Main Streamlit dashboard application
├── convert_to_binary.py         # Data preprocessing script for binary classification
├── data.csv                     # Main dataset
├── data_3class_backup.csv       # Backup of 3-class data
├── shapley.md                   # SHAP analysis documentation
├── OPENAI_API_KEY.txt          # OpenAI API key (not tracked)
├── HUGGINGFACE_API_KEY.txt     # HuggingFace API key (not tracked)
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

## Setup

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. Clone or download this repository

2. Create a virtual environment (recommended):
   ```bash
   python -m venv ai_env
   ```

3. Activate the virtual environment:
   - Windows:
     ```bash
     ai_env\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source ai_env/bin/activate
     ```

4. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

### API Keys Configuration

Create the following text files in the project root directory:

1. **OPENAI_API_KEY.txt** - Contains your OpenAI API key
2. **HUGGINGFACE_API_KEY.txt** - Contains your HuggingFace API key

Alternatively, for cloud deployment, set these as Streamlit secrets:
```toml
# .streamlit/secrets.toml
OPENAI_API_KEY = "your-openai-key"
HUGGINGFACE_API_KEY = "your-huggingface-key"
```

## Usage

### Running the Dashboard

```bash
streamlit run stocks_dashboard.py
```

The dashboard will open in your default web browser at `http://localhost:8501`

### Data Preprocessing

To convert the data from 3-class to binary classification:

```bash
python convert_to_binary.py
```

This script:
- Converts FLAT entries to Up/Down based on price change percentage
- Encodes targets as binary: Down=0.0, Up=1.0
- Updates the `data.csv` file

## Data Format

The dataset should include:
- `target`: Stock movement direction (Up/Down)
- `target_encoded`: Binary encoding (0.0/1.0)
- `price_change_pct`: Percentage price change
- Additional features for prediction

## Technologies Used

- **Streamlit**: Web application framework
- **Pandas**: Data manipulation and analysis
- **Plotly**: Interactive visualizations
- **OpenAI API**: Advanced AI text analysis
- **HuggingFace**: Pre-trained model inference
- **Scikit-learn/Joblib**: Machine learning model persistence
- **PyPDF2**: PDF document processing

## License

This project is part of an AI Capstone project.

## Notes

- API keys are excluded from version control for security
- Model files (.pkl, .joblib) should be generated or obtained separately
- Ensure data files are present before running the dashboard

## Demo
You can view the live interactive dashboard here: [Live Streamlit App](https://pseibinary.streamlit.app/)

## Citation

If you use this repository, please cite it as follows:

### APA
Joshua P. Rosell. (2026). *FinSight: A Hybrid Technical and Sentiment Approach to PSEi Stock Direction Prediction Using FinBERT and Machine Learning Models*. GitHub Repository. https://github.com/joshuarosell/psei-binary

### BibTeX
'''bibtex
@misc{rosell_2026,
  author = {Joshua P. Rosell},
  title = {FinSight: A Hybrid Technical and Sentiment Approach to PSEi Stock Direction Prediction Using FinBERT and Machine Learning Models},
  year = {2026},
  publisher = {GitHub},
  journal = {GitHub Repository},
  howpublished = {\url{https://github.com/joshuarosell/psei-binary}}
}
'''



