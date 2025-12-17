import json
import time
from business_logic import calculate_initial_score, check_eligibility

# nous allons simuler l'arrivée d'événements.

def process_loan_application(application_event):
    print(f"\n[Commercial Service] Reçu demande ID: {application_event['id']}")
    
    # Extraction des données
    income = application_event['client_income']
    amount = application_event['loan_amount']
    duration = application_event['duration']

    print(f"   -> Analyse: Revenu {income}, Montant {amount}")

    # Appel de la logique métier (calcul score) 
    score = calculate_initial_score(income, amount, duration)
    print(f"   -> Score calculé: {score}")

    # Vérification éligibilité 
    is_eligible = check_eligibility(score)

    # Génération de l'événement de sortie
    result_event = {
        "application_id": application_event['id'],
        "score": score,
        "status": "APPROVED" if is_eligible else "REJECTED",
        "timestamp": time.time()
    }

    if is_eligible:
        print(f"   -> SUCCÈS: Événement 'Initial Scoring Completed' publié vers Kafka.")
        print(f"   -> Payload: {json.dumps(result_event)}")
    else:
        print(f"   -> ÉCHEC: Événement 'Loan Rejected' publié.")

# Simulation d'une boucle d'écoute d'événements
if __name__ == "__main__":
    print("--- Commercial Service Démarré (Python) ---")
    print("En attente d'événements Kafka...\n")

    # Données de test (Simule les messages venant de l'API Gateway/Loan Service)
    mock_kafka_stream = [
        {"id": "REQ-001", "client_income": 4000, "loan_amount": 10000, "duration": 24}, # Bon dossier
        {"id": "REQ-002", "client_income": 1500, "loan_amount": 50000, "duration": 12}, # Mauvais dossier
    ]

    for event in mock_kafka_stream:
        time.sleep(2)
        process_loan_application(event)
