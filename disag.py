from disaggregators import Disaggregator
from datasets import load_dataset
import pandas as pd

dataset = load_dataset("imdb", split="train")
disaggregator = Disaggregator("pronouns", column="text")

ds = dataset.map(disaggregator.get_function())  # New boolean columns are added for she/her, he/him, and they/them

print(pd.DataFrame(ds).head())

