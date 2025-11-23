
class Band():

    def __init__(self, band_name,):
        self.band = []
        self.band_name = band_name


    def __repr__(self):
        """Return a string representation of a Musician, showing the variables."""
        return str(vars(self))

    def add(self, instrument):
        """Add an instrument to musician's collection."""
        self.band.append(instrument)
    def __str__(self):
        musicians_str = ", ".join(str(band_member) for band_member in self.band)
        return f"{self.band_name} ({musicians_str})"
    def play(self):
        for musician in self.band:
            if not musician.instruments:
                print (f"{musician.name} needs an instrument!")
            else:
                print (f"{musician.name} is playing: {musician.instruments}")

