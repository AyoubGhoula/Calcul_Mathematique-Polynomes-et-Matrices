# Calcul Mathématique - Polynômes et Matrices

Ce projet propose une bibliothèque en Python permettant d'effectuer des opérations mathématiques sur les polynômes et les matrices.

## Fonctionnalités

### Polynômes
- Addition, soustraction, multiplication de polynômes
- Évaluation d'un polynôme pour une valeur donnée
- Calcul de la dérivée d'un polynôme
- Intégration d'un polynôme

### Matrices
- Addition, soustraction, multiplication de matrices
- Calcul du déterminant
- Transposition d'une matrice
- Calcul de l'inverse (si possible)

## Comment Utiliser

### Exemple pour les Polynômes

```python
from polynome import Polynome

p1 = Polynome([1, -2, 0, 3])  # 1x^3 - 2x^2 + 3
p2 = Polynome([0, 1, -1])      # x^2 - x

result_addition = p1 + p2
result_multiplication = p1 * p2
