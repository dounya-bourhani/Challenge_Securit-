# Challenge_Securite

## Lancement

Pour lancer l'application, veuillez clone le repo. Il suffit ensuite de lancer la commande `streamlit run Accueil.py`.

## Objectifs

Détecter les intrusions malveillantes dans nos données de sécurité réseau *attacks.csv*.

### Modèle apprentissage supervisé
  - Random Forest

### Amélioration Performance du modèle
  - oversampling SMOTE: déséquilibre des classes
  - recherche d'hyper paramètres à l'aide de GridSearch pour optimiser les performances du modèle.

### Modèle final
Sauvegardé sous le format pickle, *random_forest_model.pkl*, afin de pouvoir le réutiliser.
