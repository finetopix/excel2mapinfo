import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Create a GeoDataFrame with sample coordinates
    coords = [(145.20431, -38.037975), (145.20531, -38.035975)]
    geometry = [Point(coord) for coord in coords]

    gdf = gpd.GeoDataFrame(geometry=geometry)
    gdf_wgs84 = gdf.to_crs(epsg=4326)

    # Customize point style
    gdf.plot(marker='s', color='red', markersize=10, label='My Points')


    # Add labels or other plot elements if needed
    plt.title('Customized Point Style')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.legend()

    # Show the plot
    plt.show()

    output_path = r'C:\Users\T1603086\OneDrive - TPG Telecom\Documents\01-scripts\excel2mapinfo\output_file.TAB'
    gdf.to_file(output_path, driver='MapInfo File')
