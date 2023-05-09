import unittest
import sys

sys.path.append("/home/labex/project")
from print_specific_number import *
class TestStep1(unittest.TestCase):
    
    def test_step1_default_values(self):
        expected_output = "2002,2009,2016,2023,2037,2044,2051,2058,2072,2079,2086,2093,2107,2114,2121,2128,2142,2149,2156,2163,2177,2184,2191,2198,2212,2219,2226,2233,2247,2254,2261,2268,2282,2289,2296,2303,2317,2324,2331,2338,2352,2359,2366,2373,2387,2394,2401,2408,2422,2429,2436,2443,2457,2464,2471,2478,2492,2499,2506,2513,2527,2534,2541,2548,2562,2569,2576,2583,2597,2604,2611,2618,2632,2639,2646,2653,2667,2674,2681,2688,2702,2709,2716,2723,2737,2744,2751,2758,2772,2779,2786,2793,2807,2814,2821,2828,2842,2849,2856,2863,2877,2884,2891,2898,2912,2919,2926,2933,2947,2954,2961,2968,2982,2989,2996,3003,3017,3024,3031,3038,3052,3059,3066,3073,3087,3094,3101,3108,3122,3129,3136,3143,3157,3164,3171,3178,3192,3199"
        self.assertEqual(print_specific_number(), expected_output)
    
    def test_step1_custom_values(self):
        expected_output = "2107,2114,2121,2128,2142,2149,2156,2163,2177,2184,2191,2198"
        self.assertEqual(print_specific_number(2100, 2210), expected_output)
    
    def test_step1_empty_result(self):
        self.assertEqual(print_specific_number(10, 20), "14")
    
    def test_step1_same_start_end(self):
        self.assertEqual(print_specific_number(100, 100), "")
        
if __name__ == '__main__':
    unittest.main()
