import mbuild as mb


class CH2(mb.Compound):
    """A methylene bridge. """
    def __init__(self):
        super(CH2, self).__init__(self)

        mb.load('ch2.pdb', compound=self, relative_to_module=self.__module__)
        mb.translate(self, -self.C[0])  # Move carbon to origin.

        self.add(mb.Port(anchor=self.C[0]), 'up')
        mb.translate(self.up, [0, 0.07, 0])

        self.add(mb.Port(anchor=self.C[0]), 'down')
        mb.translate(self.down, [0, -0.07, 0])

if __name__ == '__main__':
    m = CH2()
    m.visualize(show_ports=True)

