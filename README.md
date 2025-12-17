# Commercial Service Module

Ce module implémente le service commercial du système de gestion de prêts. Il est responsable de l'évaluation initiale des demandes de crédit.

### Fonctionnalités
* **Analyse d'éligibilité** : Vérifie si le dossier respecte les critères de base.
* **Calcul du Scoring** : Calcule un score initial basé sur les revenus et le montant du prêt.
* **Architecture** : Simule un fonctionnement piloté par événements (Event-Driven) compatible avec une architecture Microservices.

### Comment exécuter
1.  Installer les dépendances : `pip install -r requirements.txt`
2.  Lancer le service : `python main.py`

### Exemple d'Output (Démonstration)
Voici la trace d'exécution montrant le traitement de deux demandes (une acceptée, une rejetée) :

```text
--- Commercial Service Démarré (Python) ---
En attente d'événements Kafka...


[Commercial Service] Reçu demande ID: REQ-001
   -> Analyse: Revenu 4000, Montant 10000
   -> Score calculé: 800
   -> SUCCÈS: Événement 'Initial Scoring Completed' publié vers Kafka.
   -> Payload: {"application_id": "REQ-001", "score": 800, "status": "APPROVED", "timestamp": 1766008529.5372396}

[Commercial Service] Reçu demande ID: REQ-002
   -> Analyse: Revenu 1500, Montant 50000
   -> Score calculé: 200
   -> ÉCHEC: Événement 'Loan Rejected' publié.
