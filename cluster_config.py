# cluster_config.py

from dask.distributed import LocalCluster

def create_local_cluster():
    cluster = LocalCluster(
        n_workers=16,
        threads_per_worker=1,
        processes=True,
        memory_limit='28GB',
        timeout="30s",
        dashboard_address=':8787'
    )
    return cluster
