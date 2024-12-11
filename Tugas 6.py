
import pandas as pd

df = pd.read_csv('students.csv')
print("Data:")
print(df)

print("\nBaris Pertama:")
print(df.head())

df.to_csv('output.txt', sep='|', index=False)

df.info()

df.describe()

df['Status']=['Lulus' if grade >= 80 else 'Tidak Lulus' for grade in df['Grade']]

df.to_csv('students.processed.csv', index=False)

rata_rata_alpro =  df['Grade'].mean()
print("Rata-rata nilai Alpro mahasiswa:",rata_rata_alpro)

kelompok = df.groupby('Grade').size()
print(kelompok)