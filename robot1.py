from rgkit import rg

TARGET = (5, 5)


class Robot:
    def act(self, game):
        print('My robot')
        if self.location == TARGET:
            return ['guard']
        return ['move', rg.toward(self.location, TARGET)]
