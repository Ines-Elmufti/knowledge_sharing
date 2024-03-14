# Alignement de Deux Modèles et Calcul du RMSD

## Introduction

Lorsque l'on travaille avec des structures moléculaires ou tout autre modèle tridimensionnel, il est souvent nécessaire de les aligner pour comparer leurs similitudes ou différences. Une métrique courante utilisée pour quantifier la similarité structurale entre deux modèles est le RMSD (Root Mean Square Deviation, ou Écart quadratique moyen).

## Alignement des Modèles

L'alignement de deux modèles consiste à trouver la rotation et la translation optimales qui minimisent les différences entre leurs atomes ou points correspondants. Ce processus garantit que les parties similaires des modèles se chevauchent le plus étroitement possible.

Divers algorithmes peuvent être utilisés pour effectuer l'alignement des modèles, tels que l'algorithme de Kabsch ou les méthodes basées sur les quaternions. Ces algorithmes impliquent généralement le calcul de la matrice de rotation optimale et du vecteur de translation en fonction des coordonnées des atomes correspondants.

![alt text for screen readers](../assets/Alignment_of_thioredoxins2.png)

L'image ci-dessus montre l'alignement structural des thioredoxines humaines et de la drosophile Drosophila melanogaster. Les protéines sont représentées sous forme de rubans, avec la protéine humaine en rouge et la protéine de la drosophile en jaune.
## Calcul du RMSD

Une fois que les modèles sont alignés, le RMSD peut être calculé pour quantifier l'écart moyen entre les atomes ou points correspondants. La formule du RMSD est donnée par :

