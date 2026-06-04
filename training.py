import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Load CSV (make sure CSV is in same folder)
df = pd.read_csv('laptop_data.csv')

# Basic preprocessing
df['Ram'] = df['Ram'].str.replace('GB','').astype(int)
df['Weight'] = df['Weight'].str.replace('kg','').astype(float)
df['Touchscreen'] = df['ScreenResolution'].apply(lambda x: 1 if 'Touchscreen' in x else 0)
df['IPS'] = df['ScreenResolution'].apply(lambda x: 1 if 'IPS' in x else 0)
X_res = df['ScreenResolution'].str.split('x', expand=True)
df['X_res'] = X_res[0].str.extract(r'(\d+)').astype(int)
df['Y_res'] = X_res[1].astype(int)
df['ppi'] = ((df['X_res']**2 + df['Y_res']**2)**0.5) / df['Inches']
df['Cpu brand'] = df['Cpu'].apply(lambda x: x.split()[0])
df['Gpu brand'] = df['Gpu'].apply(lambda x: x.split()[0])
df['os'] = df['OpSys'].apply(lambda x: 'Windows' if 'Windows' in x else ('Mac' if 'Mac' in x else 'Other'))

# Drop unused columns
df.drop(columns=['ScreenResolution','Inches','X_res','Y_res','Cpu','Gpu','OpSys'], inplace=True)

# Features & target
X = df.drop(columns=['Price'])
y = np.log(df['Price'])

categorical = ['Company','TypeName','Cpu brand','Gpu brand','os']

# Column transformer
ct = ColumnTransformer([
    ('ohe', OneHotEncoder(sparse_output=False, drop='first'), categorical)
], remainder='passthrough')

# Pipeline
pipe = Pipeline([
    ('transform', ct),
    ('model', LinearRegression())
])

# Train
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=42)
pipe.fit(X_train, y_train)

# Save model & dataframe in same folder
pickle.dump(pipe, open('pipe.pkl','wb'))
pickle.dump(df, open('df.pkl','wb'))

print("✅ Model trained and saved!")