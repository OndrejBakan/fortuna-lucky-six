import pandas as pd
import tabula

dfs = tabula.read_pdf("Výsledky LUCKY SIX za 01.11.2022.pdf",
    pages='all',
    lattice=True,
    encoding='Ansi',
    pandas_options={'header': None})

df = pd.concat(dfs)

# name columns
df.columns = df.values.tolist()[0]

# remove first row
df = df.iloc[1:].reset_index()

df = df['Vylosovaná čísla (v pořadí)'].str.split(',', expand=True)

for column in df.columns:
    print(f'Nejčastější čísla v {column+1}. tahu:')
    print(', '.join(df[column].mode()))

modes = df.mode()

print(modes.mode(axis='columns'))