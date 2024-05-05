# Shortest_path_on_map
Find shortest map with 3 algorithms: Dijistra, Bellman-Ford, Floyd warshall 

1. Khởi tạo dữ liệu ma trận từ bản đồ Google Maps, bao gồm một vùng diện tích ở khu vực Thành phố Hồ Chí Minh có ít nhất 100 đỉnh và 100 cạnh. (2 điểm)
2. Cài đặt ba thuật toán Dijkstra, Bellman-Ford, và Floyd-Warshall trên dữ liệu đã khởi tạo và đưa ra đánh giá về hiệu suất khi chọn ngẫu nhiên các cặp đỉnh. (3 điểm)
3. Tạo chức năng nhập điểm đầu và điểm cuối trên bản đồ và xuất ra ba đường đi ngắn nhất. Minh họa ba đường đi này trên bản đồ Google Maps. (4 điểm)
4. So sánh kết quả của các thuật toán với dữ liệu thực tế từ Google. (1 điểm)

Reference code:
 
https://stackoverflow.com/questions/76483447/adding-custom-nodes-in-osmnx-map

https://github.com/TrafficGCN/optimal_path_dijkstra_for_data_science/blob/main/dijkstra_map.py

https://towardsdatascience.com/find-and-plot-your-optimal-path-using-plotly-and-networkx-in-python-17e75387b873

https://github.com/gboeing/osmnx-examples/tree/main/notebooks

https://github.com/vraj152/googlemapsastar?fbclid=IwAR1iBcZcaQtAJ4I0VzrCECIILYlb1XqxhykNkMmY26-0RJpdj1GwT0NepVE

# Setup

Python: 3.10.12
OS: wsl2 (window)
Library: 
- streamlit==1.33.0
- streamlit_folium 
- leafmap==0.31.9
- osmnx==1.9.2
- networkx==3.1
- geopy==2.4.1
- folium==0.16.0

To setup lib, run command
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt


First we need to create a map with osm. 
1. Open the link https://www.openstreetmap.org/export#map=17/18.68012/105.66745
2. Choose "Manually select a different area"
3. Click Export
4. Save file `.osm` and save in data folder

Here I have data with 380 nodes and 810 edges in Ho Chi Minh city. 

# How to run code

Move to the folder having the project and run command
  streamlit run app.py

It will open the streamlit web app


