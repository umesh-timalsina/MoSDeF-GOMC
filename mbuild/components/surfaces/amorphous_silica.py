import numpy as np

import mbuild as mb


class AmorphousSilica(mb.Compound):
    """ """
    def __init__(self, surface_roughness=1.0):
        super(AmorphousSilica, self).__init__()

        if surface_roughness == 1.0:
            # TODO: description of how this surface was generated/citation
            mb.load('amorphous_silica_sr1.0.pdb', compound=self,
                    relative_to_module=self.__module__)
            self.periodicity = np.array([5.4366, 4.7082, 0.0])
        else:
            raise ValueError('Amorphous silica input file with surface '
                             'roughness of {0:.1f} does not exist. If you have '
                             'this structure, please submit a pull request to'
                             'add it! '.format(surface_roughness))
        count = 0
        for atom in self.atoms:
            if atom.kind == 'OB':
                count += 1
                port = mb.Port(anchor=atom)
                mb.rotate_around_x(port, np.pi/2)
                mb.translate(port, atom + np.array([0, 0, .1]))
                self.add(port, 'port_{}'.format(count))

if __name__ == "__main__":
    single = AmorphousSilica()
    multiple = mb.TiledCompound(single, n_tiles=(2, 1, 1), kind="tiled")
    multiple.visualize(show_ports=True)
