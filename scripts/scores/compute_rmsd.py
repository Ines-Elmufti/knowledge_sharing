from bioblocks.blocks.model import Model
from bioblocks.align import usalign_models
from bioblocks.filters import is_backbone, is_canonical_amino_acid
from bioblocks.geometry import compute_rmsd
from bioblocks.io import read_model, write_model
from bioblocks.transform import filter_atoms, filter_chains, filter_residues, rename_chains

def rmsd_value(input_model1: Model, input_model2: Model, alignment_chain_ids:list) -> Model:
    """Align models and compute RMSD value .

    Args:
        input_model1 (model): First Bioblocks structure model
        input_model2 (int): Second Bioblocks structure model.
        alignment_chain_ids: shared chain used for alignment

    Raises:
        ValueError: If any chain ids in the input models are no identical.

    Returns:
        A new model in which all chains are reindexed consistently.
    """
   
    model_1 = read_model(input_model1, suppress_warnings=True)
    model_2 = read_model(input_model2, suppress_warnings=True)
    if all(chain_id in model_1.get_chains() for chain_id in alignment_chain_ids) and all(chain_id in model_2.get_chains() for chain_id in alignment_chain_ids):
        aligned_model_1 = usalign_models(
            moving_model=model_1,
            static_model=model_2,
            alignment_chain_ids=[alignment_chain_ids]
)
    else:
        raise ValueError(
            "chains don't match"
        )
    rmsd_value = rmsd.compute_rmsd_between_models(aligned_model_1, model_2, chain_ids=[alignment_chain_ids])

    return rmsd_value

