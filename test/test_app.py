# -*- coding: utf-8 -*-
import unittest
import json
from src.ipcontainer import IPContainer

with open('./src/json/ip.json') as f:
        data_ip = json.load(f)

with open('./src/json/dns.json') as f2:
        data_dns = json.load(f2)

class testIPContainer(unittest.TestCase):
    def test_a_vacia_tablas(self):
        IPContainer._dropUsers()
        self.assertEqual(IPContainer.getNumberOfUsers(), 0, "Tabla usuarios vaciada.")
        IPContainer._dropData()
        self.assertEqual(IPContainer.getNumberOfUsers(), 0, "Tabla datos vaciada.")

    def test_b_agrega_usuarios(self):
        IPContainer.addUser("test_user1")
        self.assertEqual(IPContainer.existUser("test_user1"), True, "Usuario 1 agregado correctamente.")
        IPContainer.addUser("test_user2")
        self.assertEqual(IPContainer.existUser("test_user2"), True, "Usuario 2 agregado correctamente.")

    def test_c_elimina_usuario(self):
        IPContainer.removeUser("test_user2")
        self.assertEqual(IPContainer.existUser("test_user2"), False, "Usuario eliminado correctamente.")
        self.assertEqual(IPContainer.getNumberOfUsers(), 1, "Usuario test_user2 borrado.")

    def test_d_elimina_usuario_que_no_existe(self):
        self.assertEqual(IPContainer.removeUser("test_user5"), False, "No elimina usuario que no existe.")

    def test_e_crea_red(self):
        IPContainer.createNetwork("test_user1", "dns")
        self.assertEqual(IPContainer.existNetwork("test_user1", "dns") , True, "Nueva red creada correctamente")

    def test_f_crea_red_que_ya_existe(self):
        self.assertEqual(IPContainer.createNetwork("test_user1", "dns"), False, "Red existente no creada")

    def test_g_agrega_ip_a_red_existente(self):
        data = {"data":[{"dns1":"5.5.5.5", "dns2":"5.5.5.5", "nombre":"test"}]}
        data2 = {"data":[{"dns1":"10.10.10.10", "dns2":"10.10.10.10", "nombre":"test"}]}
        self.assertEqual(IPContainer.addIPtoNetwork("test_user1", "dns", data), True, "IP agregada 1 a la red existente correctamente")
        self.assertEqual(IPContainer.addIPtoNetwork("test_user1", "dns", data2), True, "IP agregada 2 a la red existente correctamente")

    def test_h_comprueba_tamanio_red(self):
        self.assertEqual(IPContainer.getNetworkSize("test_user1", "dns"), 2, "Tamanio de red correcto.")

    def test_i_elimina_ip_de_red_existente(self):
        self.assertEqual(IPContainer.removeIPfromNetwork("test_user1", "dns", "5.5.5.5"), True, "IP borrada de la red existente")

    def test_j_comprobar_numero_usuarios(self):
        self.assertEqual(IPContainer.getNumberOfUsers(), 1, "Numero de usuarios correcto. (1)")
        IPContainer.addUser("test_user3")
        self.assertEqual(IPContainer.getNumberOfUsers(), 2, "Numero de usuarios correcto. (2)")

    def test_k_comprobar_numero_redes(self):
        self.assertEqual(IPContainer.getNumberOfNetworks(), 1, "1 - Numero de redes correcto. (1)")
        IPContainer.createNetwork("test_user3", "wlan")
        self.assertEqual(IPContainer.getNumberOfNetworks(), 2, "2 - Numero de redes correcto. (2)")

if __name__ == '__main__':
	unittest.main()
