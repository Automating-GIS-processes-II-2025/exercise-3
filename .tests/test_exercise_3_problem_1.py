from points_decorator import points
import inspect
import os
import pandas as pd
import geopandas as gpd
import pyproj

class TestProblem1:
    @points(1, "Problem 1, Part 1: Did you create the file `shopping_centres.txt` ?")
    def test_problem_1_part_1(self, problem1):

        data_folder = os.path.join(os.getcwd(), "data")
        file_path = os.path.join(data_folder, "shopping_centres.txt")
        assert os.path.isfile(file_path)


    @points(1, "Problem 1, Part 2: Did you create a dataframe `shopping_centres` with the correct values?")
    def test_problem_1_part_2(self, problem1):
        section_data, namespace = problem1
        section = "Part 2"
        variables = section_data[section]['variables']

        assert isinstance(variables['shopping_centres'], pd.DataFrame)
        assert len(variables['shopping_centres']) == 7


    @points(1, "Problem 1, Part 3: Did you geocode the addresses?")
    def test_problem_1_part_3_geocode(self, problem1):
        section_data, namespace = problem1
        section = "Part 3"
        source = section_data[section]['source']
        variables = section_data[section]['variables']

        assert "geocode" in source
        assert 'geometry' in variables['shopping_centres'].columns
        
        

    @points(0, "Problem 1, Part 3: Did you reproject the layer to EPSG:3879 ?")
    def test_problem_1_part_3_crs(self, problem1):
        section_data, namespace = problem1
        section = "Part 3"
        source = section_data[section]['source']
        variables = section_data[section]['variables']

        assert variables['shopping_centres'].crs == pyproj.CRS("EPSG:3879")


    @points(1, "Problem 1, Part 4: Did you export the file `shopping_centres.gpkg`?")
    def test_problem_1_part_4(self, problem1):
        section_data, namespace = problem1
        section = "Part 4"
        source = section_data[section]['source']

        assert "to_file" and "shopping_centres.gpkg" in source
