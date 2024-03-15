# Introduction

Dans le domaine de la biologie computationnelle et de la bioinformatique, l'alignement de deux modèles et le calcul des similarités sont des tâches fondamentales. Ce processus nous permet de comparer les structures de biomolécules, telles que les protéines ou les acides nucléiques, et d'identifier les similarités ou les différences qui peuvent fournir des informations sur leurs fonctions et leurs interactions.

Dans cette section, nous explorerons le concept d'alignement de deux modèles et de calcul des similarités dans le contexte de la bioinformatique et de la modélisation moléculaire.
![](./assets/Bioinformatics_Banner_1140x400.webp)
# Alignement de Deux Modèles et Calcul des Similarités

## Contexte

Lorsque l'on travaille avec des structures moléculaires ou tout autre modèle tridimensionnel, il est souvent nécessaire de les aligner pour comparer leurs similitudes ou différences. Une métrique courante utilisée pour quantifier la similarité structurale entre deux modèles est le RMSD (Root Mean Square Deviation, ou Écart quadratique moyen).

## Alignement des Modèles

L'alignement de deux modèles consiste à trouver la rotation et la translation optimales qui minimisent les différences entre leurs atomes ou points correspondants. Ce processus garantit que les parties similaires des modèles se chevauchent le plus étroitement possible.

Divers algorithmes peuvent être utilisés pour effectuer l'alignement des modèles, tels que l'algorithme de Kabsch ou les méthodes basées sur les quaternions. Ces algorithmes impliquent généralement le calcul de la matrice de rotation optimale et du vecteur de translation en fonction des coordonnées des atomes correspondants.

![](./assets/Alignment_of_thioredoxins2.fr.png)

L'image ci-dessus montre l'alignement structural des thioredoxines humaines et de la drosophile Drosophila melanogaster. Les protéines sont représentées sous forme de rubans, avec la protéine humaine en rouge et la protéine de la drosophile en jaune.
## Calcul du RMSD

Une fois que les modèles sont alignés, le RMSD peut être calculé pour quantifier l'écart moyen entre les atomes ou points correspondants. 
