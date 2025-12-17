# business_logic.py

def calculate_initial_score(income: float, loan_amount: float, duration_months: int) -> int:
    """
    Calcule un score basé sur le taux d'endettement.
    Cité dans le rapport: 'Calculates initial scoring'
    """
    if income == 0:
        return 0

    monthly_payment = loan_amount / duration_months
    debt_ratio = monthly_payment / income

    if debt_ratio < 0.30:
        return 800  # Excellent dossier
    elif debt_ratio < 0.45:
        return 500  # Dossier moyen
    else:
        return 200  # Risqué

def check_eligibility(score: int) -> bool:
    """
    Vérifie si le score dépasse le seuil (Threshold).
    Voir le diagramme de séquence: '[Score >= Threshold]'
    """
    THRESHOLD = 450
    return score >= THRESHOLD

