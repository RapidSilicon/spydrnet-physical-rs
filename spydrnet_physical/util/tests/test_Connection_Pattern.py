import unittest
from spydrnet_physical.util import ConnectPoint , ConnectPointList, ConnectionPattern


class test_Connection_Pattern(unittest.TestCase):

    def setUp(self) -> None:
        self.width = 11
        self.height = 11
        self.conn_manager = ConnectionPattern(self.width, self.height)
        self.conn_patt = self.conn_manager.connections
        self.conn_patt.cursor = (6, 0)
        self.conn_patt.move_y(steps=6)

    def test_get_htree(self):
        point_list = [(6, 0, 6, 1), (6, 1, 6, 2), (6, 2, 6, 3), (6, 3, 6, 4), (6, 4, 6, 5), (6, 5, 6, 6), (6, 6, 7, 6), 
        (7, 6, 8, 6), (8, 6, 9, 6), (9, 6, 9, 7), (9, 7, 9, 8), (9, 8, 9, 9), (9, 6, 9, 5), (9, 5, 9, 4), (9, 4, 9, 3), 
        (6, 6, 5, 6), (5, 6, 4, 6), (4, 6, 3, 6), (3, 6, 3, 7), (3, 7, 3, 8), (3, 8, 3, 9), (3, 6, 3, 5), (3, 5, 3, 4), 
        (3, 4, 3, 3)]
        Width = 10
        Height = 10
        conn_manager = ConnectionPattern(Width, Height)
        conn_patt = self.conn_manager.connections
        conn_patt.cursor = (6, 0)
        conn_patt.move_y(steps=6)
        htree = conn_patt.merge (conn_manager.get_htree(Width))
        htree_points = [points.connection for points in htree]
        self.assertListEqual (point_list, htree_points)

    def test_get_htree_2n(self):
        point_list = [(6, 0, 6, 1), (6, 1, 6, 2), (6, 2, 6, 3), (6, 3, 6, 4), (6, 4, 6, 5), (6, 5, 6, 6), (5, 5, 6, 5), (6, 5, 7, 5), (7, 5, 7, 6), (7, 6, 7, 7), (7, 5, 7, 4), (7, 4, 7, 3), (5, 5, 4, 5), (4, 5, 3, 5), (3, 5, 3, 6), (3, 6, 3, 7), (3, 5, 3, 4), (3, 4, 3, 3)]
        htree = self.conn_patt.merge (self.conn_manager.get_htree(self.width))
        htree_points = [points.connection for points in htree]
        self.assertListEqual (point_list, htree_points)

    def test_get_htree_root(self):
        point_list = [(6, 0, 6, 1), (6, 1, 6, 2), (6, 2, 6, 3), (6, 3, 6, 4), (6, 4, 6, 5), (6, 5, 6, 6), 
        (6, 6, 7, 6), (7, 6, 8, 6), (8, 6, 9, 6), (9, 6, 10, 6), (10, 6, 10, 7), (10, 7, 10, 8), (10, 8, 10, 9), 
        (10, 6, 10, 5), (10, 5, 10, 4), (10, 4, 10, 3), (6, 6, 5, 6), (5, 6, 4, 6), (4, 6, 3, 6), (3, 6, 2, 6), 
        (2, 6, 2, 7), (2, 7, 2, 8), (2, 8, 2, 9), (2, 6, 2, 5), (2, 5, 2, 4), (2, 4, 2, 3)]

        htree = self.conn_patt.merge (self.conn_manager.get_htree(self.width, root = 1))
        htree_points = [points.connection for points in htree]
        self.assertListEqual (point_list, htree_points) 

    def test_get_htree_side(self):
        point_list = [(6, 0, 6, 1), (6, 1, 6, 2), (6, 2, 6, 3), (6, 3, 6, 4), (6, 4, 6, 5), (6, 5, 6, 6), (6, 6, 7, 6), (7, 6, 8, 6), (8, 6, 9, 6), (9, 6, 10, 6), (10, 6, 10, 7), (10, 7, 10, 8), (10, 8, 10, 9), (10, 9, 10, 10), (10, 6, 10, 5), (10, 5, 10, 4), (10, 4, 10, 3), (10, 3, 10, 2), (6, 6, 5, 6), (5, 6, 4, 6), (4, 6, 3, 6), (3, 6, 2, 6), (2, 6, 2, 7), (2, 7, 2, 8), (2, 8, 2, 9), (2, 9, 2, 10), (2, 6, 2, 5), (2, 5, 2, 4), (2, 4, 2, 3), (2, 3, 2, 2)]
        
        htree = self.conn_patt.merge (self.conn_manager.get_htree(self.width, root = 1, side = 1))
        htree_points = [points.connection for points in htree]
        self.assertListEqual (point_list, htree_points)            

    def test_get_htree_repeat(self):
        point_list = [(6, 0, 6, 1), (6, 1, 6, 2), (6, 2, 6, 3), (6, 3, 6, 4), (6, 4, 6, 5), (6, 5, 6, 6), (6, 6, 7, 6), (7, 6, 8, 6), (8, 6, 9, 6), (9, 6, 10, 6), (10, 6, 10, 7), (10, 7, 10, 8), (10, 8, 10, 9), (10, 9, 10, 10), (10, 6, 10, 5), (10, 5, 10, 4), (10, 4, 10, 3), (10, 3, 10, 2), (10, 6, 11, 6), (11, 6, 12, 6), (12, 6, 13, 6), (13, 6, 14, 6), (14, 6, 14, 7), (14, 7, 14, 8), (14, 8, 14, 9), (14, 9, 14, 10), (14, 6, 14, 5), (14, 5, 14, 4), (14, 4, 14, 3), (14, 3, 14, 2), (6, 6, 5, 6), (5, 6, 4, 6), (4, 6, 3, 6), (3, 6, 2, 6), (2, 6, 2, 7), (2, 7, 2, 8), (2, 8, 2, 9), (2, 9, 2, 10), (2, 6, 2, 5), (2, 5, 2, 4), (2, 4, 2, 3), (2, 3, 2, 2), (2, 6, 1, 6), (1, 6, 0, 6), (0, 6, -1, 6), (-1, 6, -2, 6), (-2, 6, -2, 7), (-2, 7, -2, 8), (-2, 8, -2, 9), (-2, 9, -2, 10), (-2, 6, -2, 5), (-2, 5, -2, 4), (-2, 4, -2, 3), (-2, 3, -2, 2)]
        htree = self.conn_patt.merge (self.conn_manager.get_htree(self.width, root = 1, side = 1, repeat = 2))
        htree_points = [points.connection for points in htree]
        self.assertListEqual (point_list, htree_points)  

    def test_get_fishbone(self):
        point_list = [(6, 0, 6, 1), (6, 1, 6, 2), (6, 2, 6, 3), (6, 3, 6, 4), (6, 4, 6, 5), (6, 5, 6, 6), (6, 0, 6, 1), (6, 1, 7, 1), (7, 1, 8, 1), (8, 1, 9, 1), (9, 1, 10, 1), (10, 1, 11, 1), (6, 1, 5, 1), (5, 1, 4, 1), (4, 1, 3, 1), (3, 1, 2, 1), (2, 1, 1, 1), (6, 1, 6, 2), (6, 2, 7, 2), (7, 2, 8, 2), (8, 2, 9, 2), (9, 2, 10, 2), (10, 2, 11, 2), (6, 2, 5, 2), (5, 2, 4, 2), (4, 2, 3, 2), (3, 2, 2, 2), (2, 2, 1, 2), (6, 2, 6, 3), (6, 3, 7, 3), (7, 3, 8, 3), 
        (8, 3, 9, 3), (9, 3, 10, 3), (10, 3, 11, 3), (6, 3, 5, 3), (5, 3, 4, 3), (4, 3, 3, 3), (3, 3, 2, 3), (2, 3, 1, 3), (6, 3, 6, 4), (6, 4, 7, 4), (7, 4, 8, 4), (8, 4, 9, 4), (9, 4, 10, 4), (10, 4, 11, 4), (6, 4, 5, 4), (5, 4, 4, 4), (4, 4, 3, 4), (3, 4, 2, 4), (2, 4, 1, 4), (6, 4, 6, 5), (6, 5, 7, 5), (7, 5, 8, 5), (8, 5, 9, 5), (9, 5, 10, 5), (10, 5, 11, 5), (6, 5, 5, 5), (5, 5, 4, 5), (4, 5, 3, 5), (3, 5, 2, 5), (2, 5, 1, 5), (6, 5, 6, 6), (6, 6, 7, 6), (7, 6, 8, 6), (8, 6, 9, 6), (9, 6, 10, 6), (10, 6, 11, 6), (6, 6, 5, 6), (5, 6, 4, 6), (4, 6, 3, 6), (3, 6, 2, 6), (2, 6, 1, 6), (6, 6, 6, 7), (6, 7, 7, 7), (7, 7, 8, 7), (8, 7, 9, 7), (9, 7, 10, 7), (10, 7, 11, 7), (6, 7, 5, 7), (5, 7, 4, 7), (4, 7, 3, 7), (3, 7, 2, 7), (2, 7, 1, 7), (6, 7, 6, 8), (6, 8, 7, 8), (7, 8, 8, 8), (8, 8, 9, 8), (9, 8, 10, 8), (10, 8, 11, 8), (6, 8, 5, 8), (5, 8, 4, 8), (4, 8, 3, 8), (3, 8, 2, 8), (2, 8, 1, 8), (6, 8, 6, 9), (6, 9, 7, 9), (7, 9, 8, 9), (8, 9, 9, 9), (9, 9, 10, 9), (10, 9, 11, 9), (6, 9, 5, 9), (5, 9, 4, 9), (4, 9, 3, 9), (3, 9, 2, 9), (2, 9, 1, 9), (6, 9, 6, 10), (6, 10, 7, 10), (7, 10, 8, 10), (8, 10, 9, 10), (9, 10, 10, 10), (10, 10, 11, 10), (6, 10, 5, 10), (5, 10, 4, 10), (4, 10, 3, 10), (3, 10, 2, 10), (2, 10, 1, 10), (6, 10, 6, 11), (6, 11, 7, 11), (7, 11, 8, 11), (8, 11, 9, 11), (9, 11, 10, 11), (10, 11, 11, 11), (6, 11, 5, 11), (5, 11, 4, 11), (4, 11, 3, 11), (3, 11, 2, 11), (2, 11, 1, 11), (6, 0, 6, 1), (6, 1, 6, 2), (6, 2, 6, 3), (6, 3, 6, 4), (6, 4, 6, 5), (6, 5, 6, 6), (6, 0, 6, 1), (6, 1, 7, 1), (7, 1, 8, 1), (8, 1, 9, 1), (9, 1, 10, 1), (10, 1, 11, 1), (6, 1, 5, 1), (5, 1, 4, 1), (4, 1, 3, 1), (3, 1, 2, 1), (2, 1, 1, 1), (6, 1, 6, 2), (6, 2, 7, 2), (7, 2, 8, 2), (8, 2, 9, 2), (9, 2, 10, 2), (10, 2, 11, 2), (6, 2, 5, 2), (5, 2, 4, 2), (4, 2, 3, 2), (3, 2, 2, 2), (2, 2, 1, 2), (6, 2, 6, 3), (6, 3, 7, 3), (7, 3, 8, 3), (8, 3, 9, 3), (9, 3, 10, 3), (10, 3, 11, 3), (6, 3, 5, 3), (5, 3, 4, 3), (4, 3, 3, 3), (3, 3, 2, 3), (2, 3, 1, 3), (6, 3, 6, 4), (6, 4, 7, 4), (7, 4, 8, 4), (8, 4, 9, 4), (9, 4, 10, 4), (10, 4, 11, 4), (6, 4, 5, 4), (5, 4, 4, 4), (4, 4, 3, 4), (3, 4, 2, 4), (2, 4, 1, 4), (6, 4, 6, 5), (6, 5, 7, 5), (7, 5, 8, 5), (8, 5, 9, 5), (9, 5, 10, 5), (10, 5, 11, 5), (6, 5, 5, 5), (5, 5, 4, 5), (4, 5, 3, 5), (3, 5, 2, 5), (2, 5, 1, 5), (6, 5, 6, 6), (6, 6, 7, 6), (7, 6, 8, 6), (8, 6, 9, 6), (9, 6, 10, 6), (10, 6, 11, 6), (6, 6, 5, 6), (5, 6, 4, 6), (4, 6, 3, 6), (3, 6, 2, 6), (2, 6, 1, 6), (6, 6, 6, 7), (6, 7, 7, 7), (7, 7, 8, 7), (8, 7, 9, 7), (9, 7, 10, 7), (10, 7, 11, 7), (6, 7, 5, 7), (5, 7, 4, 7), (4, 7, 3, 7), (3, 7, 2, 7), (2, 7, 1, 7), (6, 7, 6, 8), (6, 8, 7, 8), (7, 8, 8, 8), (8, 8, 9, 8), (9, 8, 10, 8), (10, 8, 11, 8), (6, 8, 5, 8), (5, 8, 4, 8), (4, 8, 3, 8), (3, 8, 2, 8), (2, 8, 1, 8), (6, 8, 6, 9), (6, 9, 7, 9), (7, 9, 8, 9), (8, 9, 9, 9), (9, 9, 10, 9), (10, 9, 11, 9), (6, 9, 5, 9), (5, 9, 4, 9), (4, 9, 3, 9), (3, 9, 2, 9), (2, 9, 1, 9), (6, 9, 6, 10), (6, 10, 7, 10), (7, 10, 8, 10), (8, 10, 9, 10), (9, 10, 10, 10), (10, 10, 11, 10), (6, 10, 5, 10), (5, 10, 4, 10), (4, 10, 3, 10), (3, 10, 2, 10), (2, 10, 1, 10), (6, 10, 6, 11), (6, 11, 7, 11), (7, 11, 8, 11), (8, 11, 9, 11), (9, 11, 10, 11), (10, 11, 11, 11), (6, 11, 5, 11), (5, 11, 4, 11), (4, 11, 3, 11), (3, 11, 2, 11), (2, 11, 1, 11)]
        htree = self.conn_patt.merge (self.conn_manager.get_fishbone())
        htree_points = [points.connection for points in htree]
        self.assertListEqual (point_list, htree_points)    

    def test_get_fishbone_margin_x(self):
        point_list = [(6, 0, 6, 1), (6, 1, 6, 2), (6, 2, 6, 3), (6, 3, 6, 4), (6, 4, 6, 5), (6, 5, 6, 6), (6, 0, 6, 1), (6, 1, 7, 1), (7, 1, 8, 1), (8, 1, 9, 1), (9, 1, 10, 1), (6, 1, 5, 1), (5, 1, 4, 1), (4, 1, 3, 1), (3, 1, 2, 1), (6, 1, 6, 2), (6, 2, 7, 2), (7, 2, 8, 2), (8, 2, 9, 2), (9, 2, 10, 2), (6, 2, 5, 2), (5, 2, 4, 2), (4, 2, 3, 2), (3, 2, 2, 2), (6, 2, 6, 3), (6, 3, 7, 3), (7, 3, 8, 3), (8, 3, 9, 3), (9, 3, 10, 3), (6, 3, 5, 3), (5, 3, 4, 3), (4, 3, 3, 3), (3, 3, 2, 3), (6, 3, 6, 4), (6, 4, 7, 4), (7, 4, 8, 4), (8, 4, 9, 4), (9, 4, 10, 4), (6, 4, 5, 4), (5, 4, 4, 4), (4, 4, 3, 4), (3, 4, 2, 4), (6, 4, 6, 5), (6, 5, 7, 5), (7, 5, 8, 5), (8, 5, 9, 5), (9, 5, 10, 5), (6, 5, 5, 5), (5, 5, 4, 5), (4, 5, 3, 5), (3, 5, 2, 5), (6, 5, 6, 6), (6, 6, 7, 6), (7, 6, 8, 6), (8, 6, 9, 6), (9, 6, 10, 6), (6, 6, 5, 6), (5, 6, 4, 6), (4, 6, 3, 6), (3, 6, 2, 6), (6, 6, 6, 7), (6, 7, 7, 7), (7, 7, 8, 7), (8, 7, 9, 7), 
        (9, 7, 10, 7), (6, 7, 5, 7), (5, 7, 4, 7), (4, 7, 3, 7), (3, 7, 2, 7), (6, 7, 6, 8), (6, 8, 7, 8), (7, 8, 8, 8), (8, 8, 9, 8), (9, 8, 10, 8), (6, 8, 5, 8), (5, 8, 4, 8), (4, 8, 3, 8), (3, 8, 2, 8), (6, 8, 6, 9), (6, 9, 7, 9), (7, 9, 8, 9), (8, 9, 9, 9), (9, 9, 10, 9), (6, 9, 5, 9), (5, 9, 4, 9), (4, 9, 3, 9), (3, 9, 2, 9), (6, 9, 6, 10), (6, 10, 7, 10), (7, 10, 8, 10), (8, 10, 9, 10), (9, 10, 10, 10), (6, 10, 5, 10), (5, 10, 4, 10), (4, 10, 3, 10), (3, 10, 2, 10), (6, 10, 6, 11), (6, 11, 7, 11), (7, 11, 8, 11), (8, 11, 9, 11), (9, 11, 10, 11), (6, 11, 5, 11), (5, 11, 4, 11), (4, 11, 3, 11), (3, 11, 2, 11), (6, 0, 6, 1), (6, 1, 6, 2), (6, 2, 6, 3), (6, 3, 6, 4), (6, 4, 6, 5), (6, 5, 6, 6), (6, 0, 6, 1), (6, 1, 7, 1), (7, 1, 8, 1), (8, 1, 9, 1), (9, 1, 10, 1), (6, 1, 5, 1), (5, 1, 4, 1), (4, 1, 3, 1), (3, 1, 2, 1), (6, 1, 6, 2), (6, 2, 7, 2), (7, 2, 8, 2), (8, 2, 9, 2), (9, 2, 10, 2), (6, 2, 5, 2), (5, 2, 4, 2), (4, 2, 3, 2), (3, 2, 2, 2), (6, 2, 6, 3), (6, 3, 7, 3), (7, 3, 8, 3), (8, 3, 9, 3), (9, 3, 10, 3), (6, 3, 5, 3), (5, 3, 4, 3), (4, 3, 3, 3), (3, 3, 2, 3), (6, 3, 6, 4), (6, 4, 7, 4), (7, 4, 8, 4), (8, 4, 9, 4), (9, 4, 10, 4), (6, 4, 5, 4), (5, 4, 4, 4), (4, 4, 3, 4), (3, 4, 2, 4), (6, 4, 6, 5), (6, 5, 7, 5), (7, 5, 8, 5), (8, 5, 9, 5), (9, 5, 10, 5), (6, 5, 5, 5), (5, 5, 4, 5), (4, 5, 3, 5), (3, 5, 2, 5), (6, 5, 6, 6), (6, 6, 7, 6), (7, 6, 8, 6), (8, 6, 9, 6), (9, 6, 10, 6), (6, 6, 5, 6), (5, 6, 4, 6), (4, 6, 3, 6), (3, 6, 2, 6), (6, 6, 6, 7), (6, 7, 7, 7), (7, 7, 8, 7), (8, 7, 9, 7), (9, 7, 10, 7), (6, 7, 5, 7), (5, 7, 4, 7), (4, 7, 3, 7), (3, 7, 2, 7), (6, 7, 6, 8), (6, 8, 7, 8), (7, 8, 8, 8), (8, 8, 9, 8), (9, 8, 10, 8), (6, 8, 5, 8), (5, 8, 4, 8), (4, 8, 3, 8), (3, 8, 2, 8), (6, 8, 6, 9), (6, 9, 7, 9), (7, 9, 8, 9), (8, 9, 9, 9), (9, 9, 10, 9), (6, 9, 5, 9), (5, 9, 4, 9), (4, 9, 3, 9), (3, 9, 2, 9), (6, 9, 6, 10), (6, 10, 7, 10), (7, 10, 8, 10), (8, 10, 9, 10), (9, 10, 10, 10), (6, 10, 5, 10), (5, 10, 4, 10), (4, 10, 3, 10), (3, 10, 2, 10), (6, 10, 6, 11), (6, 11, 7, 11), (7, 11, 8, 11), (8, 11, 9, 11), (9, 11, 10, 11), (6, 11, 5, 11), (5, 11, 4, 11), (4, 11, 3, 11), (3, 11, 2, 11)]
        htree = self.conn_patt.merge (self.conn_manager.get_fishbone(x_margin=(1, 1)))
        htree_points = [points.connection for points in htree]
        self.assertListEqual (point_list, htree_points)  


    def test_get_fishbone_margin_y(self):
        point_list = [(6, 0, 6, 1), (6, 1, 6, 2), (6, 2, 6, 3), (6, 3, 6, 4), (6, 4, 6, 5), (6, 5, 6, 6), (6, 0, 6, 2), (6, 2, 7, 2), (7, 2, 8, 2), (8, 2, 9, 2), (9, 2, 10, 2), (10, 2, 11, 2), (6, 2, 5, 2), (5, 2, 4, 2), (4, 2, 3, 2), (3, 2, 2, 2), (2, 2, 1, 2), (6, 2, 6, 3), (6, 3, 7, 3), (7, 3, 8, 3), (8, 3, 9, 3), (9, 3, 10, 3), (10, 3, 11, 3), (6, 3, 5, 3), (5, 3, 4, 3), (4, 3, 3, 3), (3, 3, 2, 3), (2, 3, 1, 3), (6, 3, 6, 4), (6, 4, 7, 4), (7, 4, 8, 4), (8, 4, 9, 4), (9, 4, 10, 4), (10, 4, 11, 4), (6, 4, 5, 4), (5, 4, 4, 4), (4, 4, 3, 4), (3, 4, 2, 4), (2, 4, 1, 4), (6, 4, 6, 5), (6, 5, 7, 5), (7, 5, 8, 5), (8, 5, 9, 5), (9, 5, 10, 5), (10, 5, 11, 5), (6, 5, 5, 5), (5, 5, 4, 5), (4, 5, 3, 5), (3, 5, 2, 5), (2, 5, 1, 5), (6, 5, 6, 6), (6, 6, 7, 6), (7, 6, 8, 6), (8, 6, 9, 6), (9, 6, 10, 6), (10, 6, 11, 6), (6, 6, 5, 6), (5, 6, 4, 6), (4, 6, 3, 6), (3, 6, 2, 6), (2, 6, 1, 6), (6, 6, 6, 7), (6, 7, 7, 7), (7, 7, 8, 7), (8, 7, 9, 7), (9, 7, 10, 7), (10, 7, 11, 7), (6, 7, 5, 7), (5, 7, 4, 7), (4, 7, 3, 7), (3, 7, 2, 7), (2, 7, 1, 7), (6, 7, 6, 8), (6, 8, 7, 8), (7, 8, 8, 8), (8, 8, 9, 8), (9, 8, 10, 8), (10, 8, 11, 8), (6, 8, 5, 8), (5, 8, 4, 8), (4, 8, 3, 8), (3, 8, 2, 8), (2, 8, 1, 8), (6, 8, 6, 9), (6, 9, 7, 9), (7, 9, 8, 9), (8, 9, 9, 9), (9, 9, 10, 9), (10, 9, 11, 9), (6, 9, 5, 9), (5, 9, 4, 9), (4, 9, 3, 9), (3, 9, 2, 9), (2, 9, 1, 9), (6, 9, 6, 10), (6, 10, 7, 10), (7, 10, 8, 10), (8, 10, 9, 10), (9, 10, 10, 10), (10, 10, 11, 10), (6, 10, 5, 10), (5, 10, 4, 10), (4, 10, 3, 10), (3, 10, 2, 10), (2, 10, 1, 10), (6, 10, 6, 11), (6, 11, 7, 11), (7, 11, 8, 11), (8, 11, 9, 11), (9, 11, 10, 11), (10, 11, 11, 11), (6, 11, 5, 11), (5, 11, 4, 11), (4, 11, 3, 11), (3, 11, 2, 11), (2, 11, 1, 11), (6, 0, 6, 1), (6, 1, 6, 2), (6, 2, 6, 3), (6, 3, 6, 4), (6, 4, 6, 5), (6, 5, 6, 6), (6, 0, 6, 2), (6, 2, 7, 2), (7, 2, 8, 2), (8, 2, 9, 2), (9, 2, 10, 2), (10, 2, 11, 2), (6, 2, 5, 2), (5, 2, 4, 2), (4, 2, 3, 2), (3, 2, 2, 2), (2, 2, 1, 2), (6, 2, 6, 3), (6, 3, 7, 3), (7, 3, 8, 3), (8, 3, 9, 3), (9, 3, 10, 3), (10, 3, 11, 3), (6, 3, 5, 3), (5, 3, 4, 3), (4, 3, 3, 3), (3, 3, 2, 3), (2, 3, 1, 3), (6, 3, 6, 4), 
        (6, 4, 7, 4), (7, 4, 8, 4), (8, 4, 9, 4), (9, 4, 10, 4), (10, 4, 11, 4), (6, 4, 5, 4), (5, 4, 4, 4), (4, 4, 3, 4), (3, 4, 2, 4), (2, 4, 1, 4), (6, 4, 6, 5), (6, 5, 7, 5), (7, 5, 8, 5), (8, 5, 9, 5), (9, 5, 10, 5), (10, 5, 11, 5), (6, 5, 5, 5), (5, 5, 4, 5), (4, 5, 3, 5), (3, 5, 2, 5), (2, 5, 1, 5), (6, 5, 6, 6), (6, 6, 7, 6), (7, 6, 8, 6), (8, 6, 9, 6), (9, 6, 10, 6), (10, 6, 11, 6), (6, 6, 5, 6), (5, 6, 4, 6), (4, 6, 3, 6), (3, 6, 2, 6), (2, 6, 1, 6), (6, 6, 6, 7), (6, 7, 7, 7), (7, 7, 8, 7), (8, 7, 9, 7), (9, 7, 10, 7), (10, 7, 11, 7), (6, 7, 5, 7), (5, 7, 4, 7), (4, 7, 3, 7), (3, 7, 2, 7), (2, 7, 1, 7), (6, 7, 6, 8), (6, 8, 7, 8), (7, 8, 8, 8), (8, 8, 9, 8), (9, 8, 10, 8), (10, 8, 11, 8), (6, 8, 5, 8), (5, 8, 4, 8), (4, 8, 3, 8), (3, 8, 2, 8), (2, 8, 1, 8), (6, 8, 6, 9), (6, 9, 7, 9), (7, 9, 8, 9), (8, 9, 9, 9), (9, 9, 10, 9), (10, 9, 11, 9), (6, 9, 5, 9), (5, 9, 4, 9), (4, 9, 3, 9), (3, 9, 2, 9), (2, 9, 1, 9), (6, 9, 6, 10), (6, 10, 7, 10), (7, 10, 8, 10), (8, 10, 9, 10), (9, 10, 10, 10), (10, 10, 11, 10), (6, 10, 5, 10), (5, 10, 4, 10), (4, 10, 3, 10), (3, 10, 2, 10), (2, 10, 1, 10), (6, 10, 6, 11), (6, 11, 7, 11), (7, 11, 8, 11), (8, 11, 9, 11), (9, 11, 10, 11), (10, 11, 11, 11), (6, 11, 5, 11), (5, 11, 4, 11), (4, 11, 3, 11), (3, 11, 2, 11), (2, 11, 1, 11)]
        htree = self.conn_patt.merge (self.conn_manager.get_fishbone(y_margin=(1, 1)))
        htree_points = [points.connection for points in htree]
        self.assertListEqual (point_list, htree_points) 

    

      