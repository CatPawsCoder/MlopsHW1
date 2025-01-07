import sys
import pandas as pd

input_file = sys.argv[1]   # data/raw_data.csv
output_file = sys.argv[2]  # data/cleaned_data.csv

df = pd.read_csv(input_file)
# Пример: удаляем строки с пропусками
df.dropna(inplace=True)

df.to_csv(output_file, index=False)
