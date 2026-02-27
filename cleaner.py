import pandas as pd

df = pd.read_csv('linked_posts_aws cloud club ph.csv')

keywords = [
    'philippines', 'User Group', 'PH', 'PUP', 'AWS Student Community Night 2026'
]

def is_philippines(text):
    if pd.isna(text):
        return False
    text = str(text).lower()
    return any(keyword in text for keyword in keywords)

df['is_ph'] = df['Caption'].apply(is_philippines)

df['is_ph_link'] = df['Profile Link'].str.lower().str.contains('/ph', na=False)

df_clean = df[(df['is_ph'] == True) | (df['is_ph_link'] == True)].copy()

df_clean = df_clean.drop(columns=['is_ph', 'is_ph_link'])

df_clean.to_csv('philippines_only_posts.csv', index=False)

print(f"Filtering complete! Kept {len(df_clean)} posts out of {len(df)}.")  