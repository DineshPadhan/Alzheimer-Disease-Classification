import streamlit as st

st.title("About This Application")
st.markdown("""
## Alzheimer's Disease Classification App

This application helps clinicians and researchers classify Alzheimer's disease stages through an interactive, experiment-driven interface.

### Capabilities
- Exploratory visualizations to inspect distributions, class balance, and key predictors.
- Guided data cleaning for missing values and outliers.
- Model training, tuning, and side-by-side metric comparison.
- Single and batch predictions with downloadable outputs.

### Workflow
- Ingest: Upload or choose a prepared dataset.
- Explore: Run EDA to validate quality before modeling.
- Train: Fit baseline and tuned models; compare precision, recall, F1, and ROC-AUC.
- Deploy: Use the best-performing model for interactive or batch inference.

### Models and Approach
- Traditional ML: Logistic Regression, Random Forests, Gradient Boosting, SVM.
- Deep Learning: Feed-forward networks for tabular signals when enabled.
- Emphasis on recall and balanced precision to avoid missed positive cases.
- Cross-validation and regularization to reduce overfitting on limited samples.

### Data and Preprocessing
- Works with demographic, cognitive scores, and imaging-derived features when available.
- Standardizes numeric fields and encodes categoricals for consistent inputs.
- Mitigates class imbalance with stratified splits and optional reweighting.

### Evaluation
- Accuracy for overall correctness.
- Precision, Recall, and F1 to balance false positives and false negatives.
- ROC-AUC to assess ranking quality across thresholds.

### Roadmap
- Add explainability (feature importance and SHAP-style insights).
- Integrate experiment tracking for reproducibility.
- Optimize for low-latency, region-aware deployment.

### Team
- Pornima Shrikant Shelke
- Ananya Indudhara
- Dinesh Padhan
- Avranil Dutta
- Adhul Paramel Sathish
- Venkata Nagaraju Jagu
- Subburu Manoj Kumar
- Mentor: RP Adhvaith
- Co-Mentor: Sunkarapelli Mounika
""")