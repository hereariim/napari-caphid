import numpy as np
# import pytest
from napari.types import LabelsData

from napari_caphid import process_func

# @pytest.fixture
# def masks_stacks_func():
#     masks_stacks = np.zeros((10,1920,2560))
#     for ix in range(10):
#         masks_stacks[ix,:,:] = np.random.randint(6,size=(1920,2560))
#     return LabelsData(masks_stacks)

# def get_er(*args, **kwargs):
#     er_func = process_func()
#     return er_func(*args, **kwargs)

# # We run a test to check if output is numpy array and binary
# def test_process_func(masks_stacks_func):
#     my_widget_thd = get_er(masks_stacks_func,path_to_raw_table_,Country_='belgium')
#     #check if output is numpy array
#     assert type(my_widget_thd)==np.ndarray
#     #check if output is binary
#     assert len(np.unique(my_widget_thd))==2