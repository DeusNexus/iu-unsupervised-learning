# Disclamer the following notebooks will use Dask Distributed to work with the complete dataset and require at least 50GB of RAM.
# This was done with AMD® Ryzen 7 5800h with radeon graphics × 16, 32GB RAM + 64GB SWAP Memory.

# Reproduction Steps
# 1. Clone the repo
# 2. Download arxiv-metadata-oai-snapshot.json(3.97 GB) from https://www.kaggle.com/datasets/Cornell-University/arxiv and place it in arXiv folder
# 3. Create a venv using `python -m venv venv` and activate it using `source venv/bin/activate`.
# 4. Install the python modules using `pip install -r requirements.txt`
# 5. Run all cells in each notebook (1_eda,2_preprocessing,3_tfidf_scores,4_classification)



