import GEOparse

gse = GEOparse.get_GEO(
    geo="GSE5281",
    destdir="data/raw"
)

print("Downloaded GSE5281 successfully!")