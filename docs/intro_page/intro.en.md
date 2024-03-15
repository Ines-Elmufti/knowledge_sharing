# Introduction

In the field of computational biology and bioinformatics, aligning two models and calculating similarities are fundamental tasks. This process allows us to compare the structures of biomolecules, such as proteins or nucleic acids, and identify similarities or differences that can provide insights into their functions and interactions.

In this section, we will explore the concept of aligning two models and calculating similarities in the context of bioinformatics and molecular modeling.
![](../assets/Bioinformatics_Banner_1140x400.webp)

# Aligning Two Models and Calculate Similarities

## Context

When working with molecular structures or any other three-dimensional models, it's often necessary to align them to compare their similarities or differences. One common metric used to quantify the structural similarity between two models is the RMSD (Root Mean Square Deviation).

## Aligning Models

Aligning two models involves finding the optimal rotation and translation that minimizes the differences between their corresponding atoms or points. This process ensures that similar parts of the models overlap as closely as possible.

Various algorithms can be used to perform model alignment, such as the Kabsch algorithm or quaternion-based methods. These algorithms typically involve calculating the optimal rotation matrix and translation vector based on the coordinates of corresponding atoms.

![](../assets/Alignment_of_thioredoxins2.png)

the image above shows structural alignment of thioredoxins from humans and the fly Drosophila melanogaster. The proteins are shown as ribbons, with the human protein in red, and the fly protein in yellow.
## RMSD Calculation

Once the models are aligned, the RMSD can be computed to quantify the average deviation between corresponding atoms or points. 
