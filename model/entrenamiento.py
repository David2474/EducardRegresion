# model/entrenamiento_bosque.py
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

def generar_ejemplos(n=100):
    X = []
    y = []
    for _ in range(n):
        X.append(np.random.permutation([1]*12 + [2, 3, 3]))  
        y.append('visual')
        X.append(np.random.permutation([2]*12 + [1, 3, 3]))  
        y.append('auditivo')
        X.append(np.random.permutation([3]*12 + [1, 2, 1]))  
        y.append('kinestesico')
    return np.array(X), y

X, y = generar_ejemplos(100)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Entrenar modelo de Random Forest
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

os.makedirs("model", exist_ok=True)

joblib.dump(clf, "model/modelo_bosque.pkl")
print("Modelo Random Forest guardado en model/modelo_bosque.pkl")
