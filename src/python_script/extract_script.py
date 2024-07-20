import pandas as pd
df = pd.read_excel(r"python_script\assignment data.xlsx")
df = df.drop('Title', axis=1)
def clean_data(x):
    if isinstance(x, str):
        cleaned_value = x.replace('\n', ', ').replace('\/', '//').strip()
        print(cleaned_value)
        return cleaned_value
    else:
        return x
    
df_cleaned = df.map(clean_data)
df_json = df_cleaned.to_json(orient='records')
with open(r'python_script\data.json', 'w') as f:
    f.write(df_json)