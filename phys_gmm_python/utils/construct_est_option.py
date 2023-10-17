from phys_gmm_python.Structs import Est_options


def construct_est_option(Data):
    est_options = Est_options()
    est_options.type = 0  # GMM Estimation Algorithm Type
    # If algo 1 selected:
    est_options.maxK = 10
    est_options.fixed_K = []

    # If algo 0 or 2 selected:
    est_options.samplerIter = 30
    est_options.do_plots = 1
    # Size of sub-sampling of trajectories
    # 1/2 for 2D datasets, >2/3 for real
    nb_data = len(Data[0])
    sub_sample = 1
    if nb_data > 500:
        sub_sample = 2
    elif nb_data > 1000:
        sub_sample = 3
    est_options.sub_sample = sub_sample
    # Metric Hyper-parameters
    est_options.estimate_l = 1
    est_options.l_sensitivity = 2
    est_options.length_scale = []
    return est_options