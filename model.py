import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

df = pd.read_csv('Domestic violence.csv')
df.columns = df.columns.str.strip()
for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].str.strip()

df['Violence_Numeric'] = df['Violence'].map({'yes': 1, 'no': 0})

plt.figure(figsize=(10, 5))
sns.histplot(data=df, x='Age', hue='Violence', multiple='stack', palette='coolwarm', kde=True)
plt.title('Violence Distribution Across Age Groups')
plt.savefig('violence_age_distribution.png')
plt.close()

df_encoded = pd.get_dummies(df.drop(columns=['SL. No', 'Violence', 'Violence_Numeric']), drop_first=True)
X = df_encoded
y = df['Violence_Numeric']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))
