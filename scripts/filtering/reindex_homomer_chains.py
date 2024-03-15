from bioblocks.io import read_model, write_model
from bioblocks.transform import reindex_chains
from pathlib import Path
from bioblocks.blocks.model import Model

from argparse import Namespace, ArgumentParser
import logging

def reindex_homomer_model_chains(input_model: Model, starting_index: int) -> Model:
    """Renumber all the chains in a homomer structure with the same starting index.

    Args:
        input_model (model): Bioblocks structure model to renumber
        starting_index (int): New index to start residue numbering from.

    Raises:
        ValueError: If any chain sequence in the input model is not identical.

    Returns:
        A new model in which all chains are reindexed consistently.
    """
    # Check that we have been given a homomer: All chain sequences must be identical,
    # otherwise an error must be raised.
    list_chain_ids_sequences = [
        (chain.id, chain.sequence) for chain in input_model.get_chains()
    ]
    first_sequence = list_chain_ids_sequences[0][1]
    if all(sequence == first_sequence for _, sequence in list_chain_ids_sequences):
        list_chain_ids = [chain_id for chain_id, _ in list_chain_ids_sequences]
    else:
        raise ValueError(
            "Not all chains have the same sequence. Only homomers are accepted"
        )
    # Assign the same starting index to all chains in the model.
    dict_chain_starting_index = {chain: starting_index for chain in list_chain_ids}
    logger.info(f"Reindexing chains {list_chain_ids} starting from {starting_index}")
    reindexed_model = reindex_chains(
        model=input_model, starting_residue_indices=dict_chain_starting_index
    )
    return reindexed_model