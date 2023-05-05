import unittest
import sys

sys.path.append("/home/labex/project")
from step1 import *
class TestStep1(unittest.TestCase):
    
    def test_step1_default_values(self):
        expected_output = "2002,2009,2016,2023,2037,2044,2051,2058,2066,2073,2087,2094,2101,2108,2116,2123,2137,2144,2151,2158,2166,2173,2187,2194,2201,2208,2216,2223,2237,2244,2251,2258,2266,2273,2287,2294,2301,2308,2316,2323,2337,2344,2351,2358,2366,2373,2387,2394,2401,2408,2416,2423,2437,2444,2451,2458,2466,2473,2487,2494,2501,2508,2516,2523,2537,2544,2551,2558,2566,2573,2587,2594,2601,2608,2616,2623,2637,2644,2651,2658,2666,2673,2687,2694,2701,2708,2716,2723,2737,2744,2751,2758,2766,2773,2787,2794,2801,2808,2816,2823,2837,2844,2851,2858,2866,2873,2887,2894,2901,2908,2916,2923,2937,2944,2951,2958,2966,2973,2987,2994,3001,3008,3016,3023,3037,3044,3051,3058,3066,3073,3087,3094,3101,3108,3116,3123,3137,3144,3151,3158,3166,3173,3187,3194,3201"
        self.assertEqual(step1(), expected_output)
    
    def test_step1_custom_values(self):
        expected_output = "2107,2114,2121,2128,2135,2142,2149,2163,2170,2177,2184,2191,2198,2205"
        self.assertEqual(step1(2100, 2210), expected_output)
    
    def test_step1_empty_result(self):
        self.assertEqual(step1(10, 20), "")
    
    def test_step1_same_start_end(self):
        self.assertEqual(step1(100, 100), "")
        
if __name__ == '__main__':
    unittest.main()
