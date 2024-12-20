# prepare_prompts.py
import pandas as pd

# Define emotionally critical and ethically challenging prompts
prompts = [
   # Define prompts here
]

# Save to a CSV file
df_prompts = pd.DataFrame(prompts, columns=["prompt"])
df_prompts.to_csv("data/prompts.csv", index=False)

print("Prompts saved to 'data/prompts.csv'")
