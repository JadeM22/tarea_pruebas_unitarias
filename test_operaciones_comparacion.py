# test_operaciones_comparacion.py

import unittest
from operaciones_comparacion import es_mayor_que, es_menor_que, es_mayor_o_igual_que, es_menor_o_igual_que, son_iguales


class TestOperacionesComparacion(unittest.TestCase):

    def test_es_mayor_que(self):
        self.assertTrue(es_mayor_que(10, 5))
        self.assertFalse(es_mayor_que(3, 5))
        self.assertFalse(es_mayor_que(5, 5))

    def test_es_menor_que(self):
        self.assertTrue(es_menor_que(2, 4))
        self.assertFalse(es_menor_que(5, 2))
        self.assertFalse(es_menor_que(5, 5))

    def test_es_mayor_o_igual_que(self):
        self.assertTrue(es_mayor_o_igual_que(10, 5))
        self.assertTrue(es_mayor_o_igual_que(5, 5))
        self.assertFalse(es_mayor_o_igual_que(3, 5))

    def test_es_menor_o_igual_que(self):
        self.assertTrue(es_menor_o_igual_que(3, 5))
        self.assertTrue(es_menor_o_igual_que(5, 5))
        self.assertFalse(es_menor_o_igual_que(6, 5))

    def test_son_iguales(self):
        self.assertTrue(son_iguales(7, 7))
        self.assertFalse(son_iguales(7, 8))
        self.assertEqual(son_iguales(10, 10), True)
        self.assertEqual(son_iguales(1, 2), False)

if __name__ == '__main__':
    unittest.main()
