#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 13:20:29 2023

@author: laserglaciers
"""

import xarray as xr
import rioxarray as rxr
import geopandas as gpd
import matplotlib.pyplot as plt


pr_path = './pr_CESM2_historical_r10i1p1f1_gn_BCSDm_fine_monthly.nc'
nepal_path = '/media/laserglaciers/upernavik/x_array_nc_tutorial/nepal/nepal.shp'

gdf = gpd.read_file(nepal_path)
# precip_xr = xr.open_dataset(pr_path)
pecip = rxr.open_rasterio(pr_path)
pecip.rio.write_crs('EPSG:4326',inplace=True)
pecip_1 = pecip.pr.sel(time=slice('2000','2013'))

nepal_precip = pecip_1.rio.clip(gdf.geometry.values,gdf.crs,drop=True,invert=False)


mean_per_time = nepal_precip.mean(axis=(1,2))
time_i = xr.CFTimeIndex(mean_per_time.time.values)
time_pd = time_i.to_datetimeindex()

fig, ax = plt.subplots()

ax.plot(time_pd,mean_per_time.values)
ax.set_title('Nepal Precipitation')
ax.set_ylabel('mm d$^{-1}$')
plt.tight_layout()
# plt.savefig('./nepal_precip.png', dpi=300)