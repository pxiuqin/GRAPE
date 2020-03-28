import time
import argparse
import sys
import os
import os.path as osp

import numpy as np
import torch
import pandas as pd

from mc.mc_subparser import add_mc_subparser
from uci.uci_subparser import add_uci_subparser

parser = argparse.ArgumentParser()
parser.add_argument('--seed', type=int, default=0)
parser.add_argument('--train_edge', type=float, default=0.7)
parser.add_argument('--train_y', type=float, default=0.7)
subparsers = parser.add_subparsers()
add_uci_subparser(subparsers)
add_mc_subparser(subparsers)
args = parser.parse_args()
print(args)

seed = args.seed
np.random.seed(seed)
torch.manual_seed(seed)

if args.domain == 'uci':
    from uci.uci_data import load_data
    data = load_data(args)
elif args.domain == 'mc':
    from mc.mc_data import load_data
    data = load_data(args)

# print(data)
print('node dim: ',data.num_node_features,' edge dim: ',data.edge_attr_dim)
for i,key in enumerate(data.keys):
	if torch.is_tensor(data[key]):
	    print(key,': ',data[key].shape)
	else:
		print(key,': ',data[key])