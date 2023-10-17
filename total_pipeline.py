# import general outside package
import numpy as np
import os

# import utilities
from utils_ds.datasets_related.load_dataset_DS import load_dataset_DS
from utils_ds.rearrange_clusters import rearrange_clusters
from utils_ds.structures import ds_plot_options

# import optimization related method
from utils_ds.optimization_tool.optimize_P import optimize_P
from utils_ds.optimization_tool.optimize_A_b import optimize_lpv_ds_from_data

# import math related function
from utils_ds.math_tool.ds_related.compute_metrics import reproduction_metrics
from utils_ds.math_tool.ds_related.lpv_ds_function import lpv_ds

# import plotting related function
from utils_ds.plotting_tool.plot_reference_trajectories_DS import plot_reference_trajectories_DS
from utils_ds.plotting_tool.VisualizeEstimatedDS import VisualizeEstimatedDS
from utils_ds.plotting_tool.plot_lyapunov_and_derivatives import plot_lyapunov_and_derivatives

# from phys_gmm_python
from phys_gmm_python.fit_gmm import fit_gmm
from phys_gmm_python.utils.construct_est_option import construct_est_option

# Load Corresponding Data
pkg_dir = os.getcwd()
chosen_dataset = 7  # 6 # 4 (when conducting 2D test)
sub_sample = 2  # '>2' for real 3D Datasets, '1' for 2D toy datasets
nb_trajectories = 4  # Only for real 3D data
Data, Data_sh, att, x0_all, data, dt, traj_length = load_dataset_DS(pkg_dir, chosen_dataset, sub_sample,
                                                                    nb_trajectories)
Data_dim = int(Data.shape[0] / 2)

# Plot relative trajectories
vel_samples = 10
vel_size = 20
plot_reference_trajectories_DS(Data, att, vel_samples, vel_size)

# Get Mu, Prior and Sigma
est_options = construct_est_option(Data)
Priors, Mu, Sigma, est_labels = fit_gmm(Data[:Data_dim], Data[Data_dim:], est_options)

# re-arrange the data
ds_struct = rearrange_clusters(Priors, Mu, Sigma, att)

# optimize P from data
P_opt = optimize_P(Data_sh)

# optimize A_k, b_k from data and P
A_k, b_k = optimize_lpv_ds_from_data(Data, att, 2, ds_struct, P_opt, 0)

# compute reproduction metrics
rmse, e_dot, dwtd = reproduction_metrics(Data, A_k, b_k, traj_length, x0_all, ds_struct)

# create a handle function that could be used by the plotting function
ds_handle = lambda x_velo: lpv_ds(x_velo, ds_struct, A_k, b_k)
ds_opt_plot_option = ds_plot_options()
ds_opt_plot_option.x0_all = x0_all

# The plotting function for lyapunov only valid for data with 2 dimension
if Data_dim == 2:
    plot_lyapunov_and_derivatives(Data, ds_handle, att, P_opt)

# Visualized the reproduced trajectories
VisualizeEstimatedDS(Data[:Data_dim], ds_handle, ds_opt_plot_option)










