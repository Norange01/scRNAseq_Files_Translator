import pandas as pd
from scipy.io import mmread
import zipfile

def getMatrixDF(matrixPath, featuresPath, barcodesPath):
    # Read in mtx file
    a = mmread(matrixPath)
    counts=pd.DataFrame(a.toarray())

    # Read in `features.tsv`
    genes = pd.read_csv(featuresPath, sep='\t', header=None)
    gene_ids = genes.iloc[:, 0]

    # Read in `barcodes.tsv`
    cell_ids = pd.read_csv(barcodesPath, sep='\t', header=None).iloc[:, 0]

    # Assign column names as the cell IDs and row names as the gene IDs
    counts_df = pd.DataFrame(counts.values)
    counts_df.index = gene_ids
    counts_df.columns = cell_ids

    # Return annotated matrix DataFrame
    return counts_df