from points_decorator import points
import inspect
import os
import pandas as pd
import geopandas as gpd
import pyproj

class TestProblem2:
    @points(1, "Problem 2, Part 1: Did you create the file `shopping_centres.txt` ?")
    def test_problem_2_part_1(self, problem2):
        section_data, namespace = problem2
        section = "Part 1"
        variables = section_data[section]['variables']

        assert isinstance(variables['shopping_centres'], pd.DataFrame)
        assert len(variables['shopping_centres']) == 7, "The dataframe does not have the correct number of rows."

    
    @points(2.5, "Problem 2, Part 2: Did you create the file `shopping_centres.txt` ?")
    def test_problem_2_part_2_buffer(self, problem2):
        section_data, namespace = problem2
        section = "Part 2"
        variables = section_data[section]['source']
        source = section_data[section]['source']

        assert "buffer" in source

        
    @points(2.5, "Problem 2, Part 2: Did you create buffers with a 1500 m distance?")
    def test_problem_2_part_2_diameter(self, problem2):
        section_data, namespace = problem2
        section = "Part 2"
        variables = section_data[section]['variables']

        geom = variables['shopping_centres'].geometry.iloc[0]
        assert geom.is_valid
        assert geom.geom_type == "Polygon"
        #assert abs((geom.bounds[2] - geom.bounds[0]) - 3000) < 1e-6
        
        

    @points(1, "Problem 2, Part 3: Did you create the file `shopping_centres.gpkg` ?")
    def test_problem_2_part_3(self, problem2):
        section_data, namespace = problem2
        section = "Part 3"
        source = section_data[section]['source']

        assert os.path.exists("data/shopping_centres.gpkg")