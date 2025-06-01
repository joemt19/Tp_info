// MBANGA TSHIBANDA ---PREPOLYTECHNIQUE UNIKIN---
// TRAVAIL PRATIQUE D'INFORMATIQUE N°1
// QUESTION 3

#include <iostream>

#include <vector>
#include <map>
#include <tuple>

using namespace std;

typedef tuple<char, char, char> TransitionKey; // (état actuel, symbole lu)
typedef tuple<char, char, char> TransitionVal; // (état suivant, symbole écrit, direction)

class MachineTuring {
private:
    vector<char> ruban;
    int tete;
    char etat;
    map<pair<char, char>, tuple<char, char, char>> transitions;
    char etat_final;

public:
    MachineTuring(string entree, char etat_initial, char etat_final) {
        ruban = vector<char>(entree.begin(), entree.end());
        tete = 0;
        etat = etat_initial;
        this->etat_final = etat_final;
    }

    void ajouterTransition(char etat_actuel, char symbole_lu, char nouvel_etat, char symbole_ecrit, char direction) {
        transitions[{etat_actuel, symbole_lu}] = make_tuple(nouvel_etat, symbole_ecrit, direction);
    }

    void executer() {
        while (etat != etat_final) {
            char symbole = ruban[tete];
            if (transitions.find({etat, symbole}) == transitions.end()) {
                cout << "Aucune transition définie pour l'état " << etat << " avec le symbole " << symbole << endl;
                break;
            }

            auto [nouvel_etat, symbole_ecrit, direction] = transitions[{etat, symbole}];
            ruban[tete] = symbole_ecrit;
            etat = nouvel_etat;

            if (direction == 'R') tete++;
            else if (direction == 'L') tete--;

            // Étendre le ruban si nécessaire
            if (tete < 0) {
                ruban.insert(ruban.begin(), '_');
                tete = 0;
            } else if (tete >= ruban.size()) {
                ruban.push_back('_');
            }
        }
        afficherRuban();
    }

    void afficherRuban() {
        cout << "Ruban final : ";
        for (char c : ruban) cout << c;
        cout << endl;
    }
};

int main() {
    // Exemple : machine qui transforme tous les '1' en '0' jusqu'à trouver '_'
    MachineTuring mt("1111_", 'A', 'H');
    mt.ajouterTransition('A', '1', 'A', '0', 'R');
    mt.ajouterTransition('A', '_', 'H', '_', 'R');
    mt.executer();
    return 0;
}