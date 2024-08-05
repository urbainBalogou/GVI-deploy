document.addEventListener('DOMContentLoaded', function() {
    const nombreFeuilletsInput = document.getElementById('id_nombre_de_feuillets');
    const nombreValeursInput = document.getElementById('id_nombre_de_valeur_feuillet_ou_carnet');
    const valeurFacialeInput = document.getElementById('id_type_valeur');
    const montantTotalInput = document.getElementById('id_montant_total');

    function calculateMontantTotal() {
        const nombreFeuillets = parseInt(nombreFeuilletsInput.value) || 0;
        const nombreValeurs = parseInt(nombreValeursInput.value) || 0;

        // On suppose que la valeur faciale est récupérée correctement en tant qu'entier.
        const valeurFaciale = parseInt(valeurFacialeInput.options[valeurFacialeInput.selectedIndex].text.split('-')[1]) || 0;

        // Calcul du montant total
        const montantTotal = nombreFeuillets * nombreValeurs * valeurFaciale;
        montantTotalInput.value = montantTotal;
    }

    // Ajout des écouteurs d'événements
    nombreFeuilletsInput.addEventListener('input', calculateMontantTotal);
    nombreValeursInput.addEventListener('input', calculateMontantTotal);
    valeurFacialeInput.addEventListener('change', calculateMontantTotal);
});
