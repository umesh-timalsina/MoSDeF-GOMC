import pdb
import itertools

import numpy as np

from atom import Atom
from bond import Bond
from compound import Compound

def load_mol2(filename):
    """
    """
    component = Compound()
    atom_list = list()

    with open(filename, 'r') as mol2_file:
        data = dict((key, list(grp)) for key, grp in itertools.groupby(mol2_file, _parse_mol2_sections))

    for idx, atom in enumerate(data['@<TRIPOS>ATOM\n'][1:]):
        _, _, x, y, z, kind, _, _, _ = atom.split()
        position = np.array([float(x), float(y), float(z)])
        new_atom = Atom(kind, position)
        component.add(new_atom, label="{0}_{1}".format(kind, idx+1))
        atom_list.append(new_atom)

    for bond in data['@<TRIPOS>BOND\n'][1:]:
        _, atom1_idx, atom2_idx, _ = bond.split()
        atom1 = atom_list[int(atom1_idx) - 1]
        atom2 = atom_list[int(atom2_idx) - 1]
        component.add(Bond(atom1, atom2))

    return component

def write_mol2(component, filename='mbuild.mol2'):
    """
    """
    n_atoms = len(list(component.atoms()))
    n_bonds = len(list(component.bonds()))

    with open(filename, 'w') as mol2_file:
        mol2_file.write("@<TRIPOS>MOLECULE\n")
        mol2_file.write("Generated by mBuild\n")
        mol2_file.write("{0} {1} 0 0 0\n".format(n_atoms, n_bonds))
        mol2_file.write("SMALL\n")
        mol2_file.write("NO_CHARGES\n")
        mol2_file.write("\n")

        mol2_file.write("@<TRIPOS>ATOM\n")
        id_to_idx = dict()
        for atom_idx, atom in enumerate(component.atoms()):
            id_to_idx[id(atom)] = atom_idx + 1
            x, y, z = atom.pos
            mol2_file.write("{0} {1} {2:8.3f} {3:8.3f} {4:8.3f} {5}\n".format(
                    atom_idx + 1, atom.kind[0], x, y, z, atom.kind))

        if n_bonds:
            mol2_file.write("@<TRIPOS>BONDS\n")
            for bond_idx, bond in enumerate(component.bonds()):
                mol2_file.write("{0} {1} {2} 1\n".format(
                        bond_idx + 1, id_to_idx[id(bond.atom1)], id_to_idx[id(bond.atom2)]))

def _parse_mol2_sections(x):
    """
    """
    if x.startswith('@<TRIPOS>'):
        _parse_mol2_sections.key = x
    return _parse_mol2_sections.key

if __name__ == "__main__":
    import pdb
    component = load_mol2('ethanol.mol2')
    write_mol2(component, 'ethanol_out.mol2')



