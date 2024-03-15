from bioblocks.blocks.model import Model
from bioblocks.align import usalign_models
from bioblocks.filters import is_backbone, is_canonical_amino_acid
from bioblocks.geometry import compute_rmsd
from bioblocks.io import read_model, write_model
from bioblocks.transform import filter_atoms, filter_chains, filter_residues, rename_chains

def filter_model_structure(input_model: Model, len_chain: int, atom_element:str) -> Model:
    """Filter your model from solvent molecules and non-canonical amino acids  .

    Args:
        input_model (model): Bioblocks structure model to be filtered
        len_chain: Eliminate all Chain objects whose length is greater than len_chain.
        atom_element:atom you wan to filter


    Returns:
        A new filtered model ready for alignment.
    """
  
    model = read_model(input_model, suppress_warnings=True)
    non_canonical_1 = sum(not is_canonical_amino_acid(residue) for residue in model.get_residues())
    print(f"{repr(model)} contains {non_canonical_1} non-canonical residues")
    cleaned_model_1 = filter_residues(model, residue_filter=is_canonical_amino_acid)
    non_canonical_1 = sum(not is_canonical_amino_acid(residue) for residue in cleaned_model_1.get_residues())
    print(f"{repr(cleaned_model_1)} contains {non_canonical_1} non-canonical residues")
    model_fc = filter_chains(non_canonical_1, chain_filter=lambda chain: len(chain) < len_chain)
    model_fa = filter_atoms(model_fc, atom_filter=lambda atom: atom.element == atom_element)


    return model_fa