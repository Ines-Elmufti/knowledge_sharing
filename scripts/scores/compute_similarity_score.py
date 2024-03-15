from Bio import pairwise2
from bioblocks.blocks.model import Model
from bioblocks.io import read_model, write_model


def similarity_score(input_model1: Model, input_model2: Model) -> tuple:
    """Align models and compute RMSD value .

    Args:
        input_model1 (model): First Bioblocks structure model
        input_model2 (int): Second Bioblocks structure model.


    Returns:
        A tuple contains 2 similarity scores computed (identity_score,similarity_score)
    """
   
    model_1 = read_model(input_model1, suppress_warnings=True)
    model_2 = read_model(input_model2, suppress_warnings=True)
    alignments = pairwise2.align.globalms(model_1, model_2, 2, -1, -0.5, -1)
    alignment_score = 0
    # calculates the percentage of identical residues between the aligned sequences.
    for align in alignments:
        alignment_score += align[0].count("-")  # Count gaps in sequence 1
        alignment_score += align[1].count("-")  # Count gaps in sequence 2
        alignment_score = len(model_1) - alignment_score  # Subtract gaps from total length

    identity_score = (alignment_score / len(model_1)) * 100
    similarity_score = alignments[0][2]
    return (identity_score,similarity_score)

