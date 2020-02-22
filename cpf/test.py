import unittest
from cpf import limparString, verificarTamanho, digito_10, digito_11, verificarCPF

class MyTest(unittest.TestCase):
    def test_limparString(self):
        self.assertEqual(limparString('123.123.133-33'), '12312313333')
        self.assertEqual(limparString('12312313333'), '12312313333')
        self.assertEqual(limparString('123 12..3--13-333'), '12312313333')
        self.assertEqual(limparString(''), '')
        self.assertEqual(limparString('-- -- '), '')
    
    def test_verificarTamanho(self):
        self.assertEqual(verificarTamanho('123.123.133-33'), True)
        self.assertEqual(verificarTamanho('12312313333'), True)
        self.assertEqual(verificarTamanho(''), False)
        self.assertEqual(verificarTamanho('123.123.13-33'), False)
        self.assertEqual(verificarTamanho('123.123.1223-33'), False)
    
    def test_digito10(self):
        self.assertEqual(digito_10('121.815.889-10'), '1')
        self.assertEqual(digito_10('13303170924'), '2')
        self.assertEqual(digito_10('117590839-84'), '8')
    
    def test_digito11(self):
        self.assertEqual(digito_11('121.815.889-10'), '0')
        self.assertEqual(digito_11('13303170924'), '4')
        self.assertEqual(digito_11('117590839-84'), '4')
    
    def test_verificarCPF(self):
        self.assertEqual(verificarCPF('121.815.889-10'), True)
        self.assertEqual(verificarCPF('13303170924'), True)
        self.assertEqual(verificarCPF('117590839-84'), True)
        self.assertEqual(verificarCPF('121.815.889-01'), False)
        self.assertEqual(verificarCPF('13303170944'), False)
        self.assertEqual(verificarCPF('117590839'), False)

if __name__ == '__main__':
    unittest.main()