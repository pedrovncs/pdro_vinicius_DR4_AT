# Escreva um programa que receba uma lista de strings representando um log de acessos a um sistema, cada string contendo um endereço IP. 
# O programa deve construir um histograma utilizando um dicionário, contando quantos acessos vieram de cada IP, e então imprimir o dicionário.

import matplotlib.pyplot as plt

logs_list = ['192.168.0.100','192.168.433.123', '192.168.0.567', '192.168.100.132', '192.168.433.123', '192.168.0.0', '192.168.0.0', '192.168.100.132', '192.168.100.1', '192.168.433.123',]

def create_histogram(logs):
    histogram = {ip: logs.count(ip) for ip in logs}
    return histogram

histogram = create_histogram(logs_list)

ips = histogram.keys()
accesses= histogram.values()

plt.bar(ips, accesses)
plt.show()