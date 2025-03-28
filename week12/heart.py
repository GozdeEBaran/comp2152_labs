# Heart class for composition
class Heart:
    def _init_(self, bpm):

        self.beats_per_minute = 72

    def beat(self):
        print("Heart is beating at " +
              str(self.beats_per_minute) + " beats per minute.")

    def __del__(self):
        print("composition heart destructor")
