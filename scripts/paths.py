import os


data_path = os.path.join('..', 'data')
os.makedirs(data_path, exist_ok=True)

input_path = os.path.join(data_path, 'input')
os.makedirs(input_path, exist_ok=True)

input_path_tab = os.path.join(input_path, 'tabs')
os.makedirs(input_path_tab, exist_ok=True)




output_path = os.path.join(data_path, 'output')
os.makedirs(output_path, exist_ok=True)

output_path_tabs = os.path.join(output_path, 'tabs')
os.makedirs(output_path_tabs, exist_ok=True)

output_path_geo = os.path.join(output_path, 'geo')
os.makedirs(output_path_geo, exist_ok=True)

output_path_maps = os.path.join(output_path, 'maps')
os.makedirs(output_path_maps, exist_ok=True)


