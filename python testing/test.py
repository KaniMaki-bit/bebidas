import unittest
import my_func

class TestFunc(unittest.TestCase):
    def test1_alphabetic_name(self):
        data = 'te, 1, 2, 3'
        self.assertTrue(my_func.add(data))
        
    def test2_non_alphabetic_name(self):
        data = 'te1, 1, 2, 3'
        self.assertFalse(my_func.add(data))
        
    def test3_too_short_name(self):
        data = 't, 1, 2, 3'
        self.assertFalse(my_func.add(data))
        
    def test4_in_range_name1(self):
        data = 'ca, 1, 2, 3'
        self.assertTrue(my_func.add(data))
        
    def test5_in_range_name2(self):
        data = 'coca cola zero sug, 1, 2, 3'
        self.assertTrue(my_func.add(data))
        
    def test6_in_range_name3(self):
        data = 'coca cola, 1, 2, 3'
        self.assertTrue(my_func.add(data))
        
    def test7_too_long_name(self):
        data = 'coca cola zero sugar, 1, 2, 3'
        self.assertFalse(my_func.add(data))
    
    def test8_too_short_size(self):
        data = 'te, 0, 2, 3'
        self.assertFalse(my_func.add(data))
        
    def test9_in_range_size(self):
        data = 'te, 1, 29, 48'
        self.assertTrue(my_func.add(data))
        
    def test10_too_long_size(self):
        data = 'te, 1, 2, 49'
        self.assertFalse(my_func.add(data))
    
    def test11_non_int_size1(self):
        data = 'te, 1.3, 2, 3'
        self.assertFalse(my_func.add(data))
    
    def test12_non_int_size2(self):
        data = 'te, 1/3, 2, 3'
        self.assertFalse(my_func.add(data))
    
    def test13_non_int_size3(self):
        data = 'te, -1, 2, 3'
        self.assertFalse(my_func.add(data))
        
    def test14_non_int_size4(self):
        data = 'te, uno, 2, 3'
        self.assertFalse(my_func.add(data)) 
    
    def test15_ascending_sizes(self):
        data = 'te, 1, 2, 3'
        self.assertTrue(my_func.add(data))
        
    def test16_non_ascending_sizes(self):
        data = 'te, 4, 2, 3'
        self.assertFalse(my_func.add(data))
    
    def test17_no_sizes1(self):
        data = 'te'
        self.assertFalse(my_func.add(data))
    
    def test18_no_sizes2(self):
        data = 'te,'
        self.assertFalse(my_func.add(data))
    
    def test19_enough_sizes1(self):
        data = 'te, 1'
        self.assertTrue(my_func.add(data))
        
    def test20_enough_sizes2(self):
        data = 'te, 1, 2, 3, 4, 5'
        self.assertTrue(my_func.add(data))
    
    def test21_more_than_5_sizes(self):
        data = 'te, 1, 2, 3, 4, 5, 6'
        self.assertFalse(my_func.add(data))
        
    def test22_name_not_first(self):
        data = '1, te, 2, 3'
        self.assertFalse(my_func.add(data))
        
    def test23_more_than_a_comma(self):
        data = 'te,, 1, 2, 3'
        self.assertFalse(my_func.add(data))
    
    def test24_extra_comma(self):
        data = 'te, 1, 2, 3,'
        self.assertFalse(my_func.add(data))
    
    def test25_ignores_blanks1(self):
        data = 't e, 1, 2, 3'
        self.assertTrue(my_func.add(data))
    
    def test25_ignores_blanks2(self):
        data = 't   e , 1   ,  2 ,  3'
        self.assertTrue(my_func.add(data))
            
if __name__ == '__main__':
    unittest.main()