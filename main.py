# %%
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
from geopandas import GeoDataFrame
from shapely.geometry import Point

# %%
class Point(Point):
    def __init__(self, *args, value=None):
        super().__init__(*args)
        self.value = value


# %%
df = pd.read_csv("points.csv", delimiter=",", skiprows=0, low_memory=False)

# %%
geometry = [Point(x, y, value=v) for x, y, v in zip(df.longitude, df.latitude, df.value)]
gdf = GeoDataFrame(df, geometry=geometry)

map = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))

# %%
gdf.plot(ax=map.plot(figsize=(10, 6)), marker="o", markersize=1, c=[p.value for p in geometry])

# %%
plt.show()
