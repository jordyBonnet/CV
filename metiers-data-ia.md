# Les métiers de la Data & de l'IA : missions et responsabilités

> Synthèse basée sur une recherche web (sources : stid-france.fr, planetegrandesecoles.com, alyra.fr, hellowork.com, studyrama.com, 3wacademy.fr, free-work.com, careerhub.mu, analytics.fr).

---

## 📌 Vue d'ensemble

| Métier | Cœur du métier | Position dans la chaîne de valeur |
|---|---|---|
| **Data Engineer** | Construire les infrastructures et pipelines de données | Amont (rendre la donnée exploitable) |
| **Data Scientist** | Analyser, modéliser, extraire de la valeur | Milieu (expérimentation & insights) |
| **ML Engineer** | Développer et industrialiser des modèles de ML | Milieu/Aval (prototypes → services) |
| **MLOps** | Déployer, superviser, fiabiliser l'IA en production | Aval (production & maintenance) |

```
Donnée brute → [Data Engineer] → Données fiables → [Data Scientist / ML Engineer] → Modèles → [MLOps] → IA en production
```

---

## 1. 🧱 Data Engineer

**Rôle :** spécialiste du développement appliqué aux problématiques data. Il veille à ce que les informations circulent correctement, qu'elles soient accessibles, fiables et exploitables à tout moment. C'est « l'architecte du Big Data ».

### Missions principales

- **Concevoir et construire les architectures de données** (data warehouses, data lakes, lakehouses, architectures distribuées)
- **Créer et maintenir les pipelines ETL/ELT** : ingestion, nettoyage, transformation, structuration des données
- **Ingestion temps réel** de données (flux via Kafka, Pulsar, API)
- **Assurer le stockage et le traitement** de volumes massifs (Hadoop, Spark, Hive)
- **Optimiser les performances, la robustesse et la sécurité** des systèmes data
- **Orchestration et monitoring** des pipelines (Airflow, dbt, Great Expectations)
- **Collaborer** avec les Data Scientists et les équipes dev pour intégrer les solutions aux projets de l'entreprise

### Compétences clés

- Python (manipulation de données), SQL avancé
- Big Data : Hadoop, Spark, Kafka
- Bases SQL et NoSQL, outils ETL/ELT
- Cloud (AWS / GCP / Azure), conteneurisation (Docker, Kubernetes)
- Notions RGPD, confidentialité, cybersécurité
- *Soft skills* : sens de l'analyse, rigueur, travail en équipe, curiosité technologique

### Distinction clé

> Le Data Engineer **bâtit les infrastructures** ; le Data Scientist **les exploite** pour analyser et modéliser. Sans les environnements du DE, les modèles du DS ne pourraient ni apprendre ni être déployés.

### Salaire & évolution (France)

- ~80 % des salaires bruts annuels entre **35 k€ et 60 k€**, moyenne ~47 k€
- Évolutions : Architecte Big Data, Chef de projet data, ML Engineer, freelance

---

## 2. 📊 Data Scientist

**Rôle :** transformer des données brutes en informations stratégiques. Il combine analyse statistique, programmation et IA pour résoudre des problèmes business et orienter les décisions.

### Missions principales

- **Collecte, nettoyage et structuration des données** (souvent 80 % du temps de travail !)
- **Analyse statistique et exploratoire** : tendances, anomalies, corrélations cachées
- **Conception de modèles prédictifs** et d'algorithmes de ML / deep learning
- **Création de visualisations et tableaux de bord** pour communiquer les résultats
- **Traduction des analyses techniques** en recommandations concrètes pour les dirigeants et équipes non techniques
- Intégrer les contraintes **RGPD et éthique de l'IA** dès la conception des modèles

### Compétences clés

- Python (pandas, scikit-learn, TensorFlow/Keras), R, SQL, NoSQL
- Statistiques, algorithmique, mathématiques (réseaux de neurones, arbres de décision, optimisation)
- Big Data : Hadoop, Spark
- Visualisation : Tableau, Power BI ; Git
- *Soft skills* : **communication** (expliquer des concepts complexes à des non-techniques), rigueur scientifique, esprit de synthèse, curiosité, adaptation

### Évolution du métier

- L'IA générative et l'automatisation redéfinissent certaines missions traditionnelles
- Évolutions : **Chef de projet data / Chief Data Officer**, Data Engineer, spécialisation sectorielle (santé, finance, industrie)

### Salaire & évolution (France)

- Débutant : ~26-30 k€ ; 2-5 ans d'expérience : ~46 k€ ; senior 10 ans+ : 80 k€+
- Formation type : Bac+5 (ingénieur, master data science/IA)

---

## 3. 🤖 Machine Learning Engineer

**Rôle :** expert qui conçoit, développe et déploie des modèles d'apprentissage intelligents et complexes, capables d'analyser de gros volumes de données. Il transforme un **prototype/notebook en service fiable, scalable et monitoré**.

### Missions principales

- **Développer et optimiser des modèles** de machine learning (classification, régression, NLP, CV, deep learning)
- **Transformer les prototypes en applications/produits** : APIs de prédiction, services scalables
- **Industrialiser les pipelines d'entraînement** et de re-entraînement des modèles
- **Optimiser les performances** des modèles (latence, précision, coût d'inférence)
- **Mettre en production et superviser** les systèmes d'IA
- **Collaborer étroitement** avec Data Scientists (modèles), Data Engineers (données) et MLOps (déploiement)
- Travailler sur l'**optimisation opérationnelle** des entreprises grâce à des systèmes qui apprennent des données

### Compétences clés

- Python, frameworks ML : TensorFlow, PyTorch, scikit-learn, Keras
- Solide compréhension des algorithmes (régression, classification, réseaux de neurones)
- Développement logiciel : APIs (FastAPI, Flask), microservices, Git
- Data engineering de base : bases de données, pipelines
- Cloud & conteneurs : Docker, Kubernetes
- Connaissances DevOps/MLOps (MLflow, Kubeflow)

### Positionnement

> Le ML Engineer est à la **frontière entre Data Science et ingénierie logicielle** : plus orienté production et code robuste que le DS, plus orienté algorithmes que le MLOps.

### Salaire (France)

- Débutant : ~40-45 k€ ; expérimenté : 55-75 k€ ; senior/spécialisé : 80 k€+
- Formation type : Bac+5, ingénieur ou master IA/data science

---

## 4. ⚙️ DevOps / MLOps Engineer

**Rôle :** faire le lien entre les équipes qui conçoivent les modèles d'IA et leur exploitation en production. Automatiser, déployer et superviser les modèles de ML pour garantir des infrastructures IA **performantes, fiables et scalables**.

### Pourquoi c'est un métier à part ?

En dev classique, le code est stable une fois déployé. En IA, **un modèle peut se dégrader avec le temps même sans changer une ligne de code** (évolution des données). Il faut donc non seulement déployer, mais aussi **surveiller les performances dans la durée** (data drift, performance drift).

### Missions principales

- **Construire les pipelines de déploiement continu des modèles** (CI/CD)
- **Automatiser l'entraînement, les tests et la mise à jour** des modèles
- **Déployer les modèles en production** (conteneurs, orchestration)
- **Monitoring et surveillance** des modèles en production : détection de baisse de performance, dérive des données, planification de re-entraînements
- **Tester différentes configurations de modèles** et choisir les meilleures
- **Être le liant entre les métiers de l'IA** (Data Eng, ML Eng, Data Science) : normes, bonnes pratiques, documentation
- **Diagnostiquer les pannes** : le problème peut venir des données, de l'infrastructure ou du modèle

### Compétences clés

- Compréhension des algorithmes de ML (debugger, optimiser les hyperparamètres, diagnostiquer)
- Frameworks : TensorFlow, PyTorch, scikit-learn (maîtriser ≥ 2)
- Python + bonnes pratiques de dev
- **DevOps : Docker (packaging des modèles), Kubernetes** (déploiement, autoscaling, gestion des pannes)
- Plateformes MLOps : **MLflow, Kubeflow, Airflow**
- *Soft skills* : travail en équipe (rôle de pont), communication, résolution de problèmes, adaptation

### Salaire (France)

- Débutant : **40-55 k€** brut/an (souvent + stock options/BSPCE en startup)
- Senior (+5 ans) : **55-75 k€** brut/an
- États-Unis : 100 k$+ même pour des profils juniors
- Accès difficile sans expérience préalable (souvent issue du ML, de la data ou du DevOps)

---

## 🧭 Tableau comparatif synthétique

| | Data Engineer | Data Scientist | ML Engineer | MLOps |
|---|---|---|---|---|
| **Objet principal** | Infrastructure & pipelines | Analyse & modèles prédictifs | Modèles → services | Production & supervision |
| **Outils emblématiques** | Kafka, Spark, Airflow, dbt | pandas, scikit-learn, Power BI | PyTorch, FastAPI, Docker | Kubernetes, MLflow, CI/CD |
| **Livraison type** | Data fiables & exploitables | Insights & recommandations | Modèles en production | IA fiable & scalable |
| **Salaire France (moyen)** | ~47 k€ | ~46 k€ | ~55-75 k€ | ~55-75 k€ |
| **Rareté du profil** | Très demandé | Très demandé (titres dilués) | Demandé | **Rare → bien payé** |

---

## 📚 Sources

- [Data Scientist : missions et compétences 2025 — STID France](https://stid-france.fr/metier-de-data-scientist/)
- [Data Engineer : missions, compétences et formation — Planète Grandes Écoles](https://www.planetegrandesecoles.com/data-engineer-missions-competences-formation)
- [Machine Learning Engineer : fiche métier — Hellowork / Studyrama / 3W Academy](https://www.hellowork.com)
- [Ingénieur MLOps, un métier unique de l'IA — Alyra](https://alyra.fr/post/ingenieur-mlops-un-metier-unique-de-lia)
- [MLOps Engineer : missions & compétences — Free-Work, Careerhub](https://www.free-work.com)
