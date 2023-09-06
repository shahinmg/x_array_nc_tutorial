### xarray tutorial for KU glaciology
This is a tutorial mostly from Xarray's [Xarray in 45 minutes](https://tutorial.xarray.dev/overview/xarray-in-45-min) and [Data Tidying](https://tutorial.xarray.dev/data_cleaning/ice_velocity.html) tutorials with a few different data sets

## installation

To use this repo first clone the repository and change the directory where the repo is located
```
git clone https://github.com/shahinmg/x_array_nc_tutorial.git

cd x_array_nc_tutorial
```

Within the `x_array_nc_tutorial` directory, install the packages in the `environment.yml` in a conda environment or create a new environment and install with `conda env create --file environment.yml` and activate the environment
Note: This can take a long time to create the environment

```
conda env create --file environment.yml

conda activate xarray_tutorial
```

In the `x_array_nc_tutorial` directory run

```
jupyter lab
```
and open the `xarray_ku_glaciology_tutorial.ipynb` notebook

The precipitatin data is not included with this repo because the file size is too large. If you would like to use this data in the repo floow the instructions below
## precipitation data

The precipitation data used in `xarray_ku_glaciology_tutorial.ipynb` is 8.2 gb. If you want to work with this data please download it [here](https://drive.google.com/file/d/1X7kWek8digimbxoMqxY8RtWgMR2ouLt-/view?usp=sharing)
and download it in the `precip_nc` directory.
