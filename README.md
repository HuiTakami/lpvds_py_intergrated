# lpvds_py_intergrated
**This is the version with the clustering package and dynamical system optimization process**
**clustering package: https://github.com/penn-figueroa-lab/phys_gmm_python (already included)**
## How to use
* Pull the package
* Install the requirement
* Mark the phys_gmm_python folder as the source root
* run total_pipeline.py

## Dataset Setting
```
chosen_dataset = 7 # load_dataset_DS.py contains the the correspondence between dataset and number, please check
sub_sample = 2  # '>2' for real 3D Datasets, '1' for 2D toy datasets
nb_trajectories = 4  # Only for real 3D data
```
## Plugging your own clustering result / algorithm
```
# Get Mu, Prior and Sigma
est_options = construct_est_option(Data)
Priors, Mu, Sigma, est_labels = fig_gmm(Data[:Data_dim], Data[Data_dim:], est_options)
```
You could change this block of code to any code that could produce Prior, Mu, Sigma with shape Priors (1xK) Mu(K x dim) Sigma (K x dim x dim), where K is the number of cluster

## Gallary
![35321697563002_ pic](https://github.com/HuiTakami/lpvds_py_intergrated/assets/97799818/3a7123b2-f40d-4bac-af37-d10110cf80ff)
![35311697562993_ pic](https://github.com/HuiTakami/lpvds_py_intergrated/assets/97799818/afb66106-db8f-41a8-9cf2-6e8377152667)
![35331697563030_ pic](https://github.com/HuiTakami/lpvds_py_intergrated/assets/97799818/075034b7-028e-4bc4-b096-706197cdc4b1)
