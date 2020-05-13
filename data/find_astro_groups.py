#!/usr/bin/python3
import numpy as np
import pandas as pd
import sys

if __name__ == "__main__":
    fname = sys.argv[1]
    data = pd.read_csv(fname)
    astro = data['NME_GRUPO_GR'].str.contains('Astro') 
    data[astro].to_csv('ASTRO_'+fname, encoding='utf-8')
