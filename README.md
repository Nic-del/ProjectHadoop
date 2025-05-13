# 🎓 Mini-Projet Hadoop

## 📘 Description
Ce projet utilise **Hadoop Streaming** avec des scripts Python pour analyser les données de naissances en France (source INSEE). L'objectif est d'identifier les **prénoms les plus populaires** selon l'année et le sexe, via des traitements **MapReduce**.

---

## 📂 Fichiers fournis

| Fichier                  | Description |
|--------------------------|-------------|
| `validation.py`          | Nettoyage et validation du fichier source (`nat2022.csv`) |
| `mapper.py`              | Mapper Hadoop pour émettre des paires clé/valeur (`sexe-prénom`, nombre) |
| `reducer.py`             | Reducer Hadoop pour agréger les totaux et filtrer les prénoms peu fréquents |
| `post_traitement.py`     | Trie les résultats finaux et extrait les top 5 |
| `resultat.txt`           | Résultat final du traitement : top 5 prénoms |
---

