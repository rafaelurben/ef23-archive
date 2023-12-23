from tqdm import tqdm

from pyworld import Tracks
from pyworld.Car import Car
from pyworld.Traces import clearTraces, saveTraces

from neural_network import NeuroLoader, Genome

import os.path

# --- TODO: EDIT HERE --- #

TRACKS = {
    "monaco": Tracks.monaco,
    "monaco_inverted": Tracks.monaco_inverted,
    # add more tracks here
}
TRACESPATH = os.getenv('TRACES_PATH', os.getcwd()) # change if desired
TIMESTEPS = 5000

# --- END EDIT --- #

NET_NAME = "carai_v5"
NET_FOLDER = os.path.join(os.path.dirname(os.path.dirname(__file__)), "networks", NET_NAME, "")


class CarGenome(Genome):
    def setup(self, track):
        self.obj = Car(track)

    def step(self):
        car = self.obj

        scans = car.getScans()
        acc, steer = self.feed_forward([*scans, car.v])
        car.acc = -1 + 2 * acc
        car.steer = -1 + 2 * steer
        car.move()
        car.updateScore()

        if car.checkCollision():
            return False
        return True

    def run_evaluation(self, generation: int = None):
        for _ in tqdm(range(TIMESTEPS)):
            if not self.step():
                return "Failed due to collision"
        return "Succeeded without collision"

myloader = NeuroLoader(name=NET_NAME, folder=NET_FOLDER)

print(f"Starting evaluation for {len(TRACKS)} tracks...")

for name, track in TRACKS.items():
    print(f"[{name}] Running evaluation... ({TIMESTEPS} timesteps)")
    genome = myloader.get_genome(CarGenome, track=track)
    message = genome.run_evaluation(TIMESTEPS)
    print(f"[{name}] Evaluation finished! Score: {genome.score} - Message: {message}")

    saveTraces([genome.obj], "_rafael_"+name, TRACESPATH)
