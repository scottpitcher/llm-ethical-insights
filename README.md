# LLM Sentiment and Ethical Evaluation Project

## Overview
This project evaluates the sentiment and ethical responses of popular LLMs (GPT, Gemini, etc.) to emotionally critical prompts. It is designed to assess their ethical alignment and emotional intelligence.

## Directory Structure
Due to the rise of recent queries into the ethical implications of LLM usage by everyday users, this project will serve to analyse the sentiment of these models (GPT, Claude, Gemini). The models will be fed sample conversations/prompts, and their responses will be analysed. The goal is to take a deeper look at human-machine interactions.

## Pipeline Overview
1. **Data Preparation**: Prepare prompts in `data/prompts.csv`.
2. **Response Collection**: Use `src/fetch_responses.py` to query LLMs and save responses in `data/llm_responses.csv`.
3. **Sentiment Analysis**: Run `src/sentiment_analysis.py` to analyze sentiment.
4. **Ethical Evaluation**: Use `src/ethical_evaluation.py` for ethicality scoring.
5. **Visualization**: Generate plots with `src/visualize_results.py`.
6. **Reporting**: Summarize findings in `results/`.

## Setup
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Run the pipeline: `python main.py`.

## Results
Final results, including visualizations and reports, can be found in the `results/` directory.

## Contributions
Feel free to submit issues or pull requests to improve the project!