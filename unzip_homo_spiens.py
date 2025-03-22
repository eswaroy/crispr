import gzip
import shutil
with gzip.open("Homo_sapiens.GRCh38.dna.primary_assembly.fa.gz", "rb") as f_in:
    with open("Homo_sapiens.GRCh38.dna.primary_assembly.fa", "wb") as f_out:
        shutil.copyfileobj(f_in, f_out)