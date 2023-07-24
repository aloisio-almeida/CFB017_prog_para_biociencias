import re

class Analisys:

    def read_orca_output(file_path):
        # Dicionário para armazenar as energias dos orbitais
        orbital_energies = {}

        # Padrão de expressão regular para encontrar linhas relevantes no arquivo de saída do ORCA
        pattern = r"^\s*(\d+)\s+(\S+)\s+(\S+)\s+(\S+)\s*$"

        # Lê o arquivo de saída do ORCA
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Itera pelas linhas do arquivo
        for line in lines:
            # Verifica se a linha corresponde ao padrão de expressão regular
            match = re.match(pattern, line)
            if match:
                # Extrai os dados relevantes da linha
                orbital_no = int(match.group(1))
                orbital_occ = float(match.group(2))
                orbital_energy_eh = float(match.group(3))
                orbital_energy_ev = float(match.group(4))

                # Armazena os dados no dicionário de orbital_energies
                orbital_energies[orbital_no] = {
                    'OCC': orbital_occ,
                    'E(Eh)': orbital_energy_eh,
                    'E(eV)': orbital_energy_ev
                }

        return orbital_energies

    def get_homo_lumo_gap(orbital_energies):
        # Encontra o HOMO (último orbital ocupado) e o LUMO (primeiro orbital não ocupado)
        homo = max([orbital_no for orbital_no, data in orbital_energies.items() if data['OCC'] > 0])
        lumo = min([orbital_no for orbital_no, data in orbital_energies.items() if data['OCC'] == 0])

        # Obtém as energias dos orbitais HOMO e LUMO
        energy_homo = orbital_energies[homo]['E(eV)']
        energy_lumo = orbital_energies[lumo]['E(eV)']

        # Calcula o gap HOMO-LUMO
        gap_homo_lumo = energy_lumo - energy_homo

        return gap_homo_lumo

    # Exemplo de uso:
    output_file_path = 'caminho/para/o/arquivo/output.orca'
    orbital_energies = read_orca_output(output_file_path)

    # Calcula o gap HOMO-LUMO
    resultado = get_homo_lumo_gap(orbital_energies)
    print("Gap HOMO-LUMO:", resultado, "eV")
