from pyworld import Tracks
from pyworld.Car import Car
from pyworld.Traces import clearTraces, saveTraces

from neural_network import loader, training, network, gui

import os.path

name = "carai_fixed_acc_fast_steer_v1"
folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), "networks", name, "")
hidden_layers = [4, 2]

training_mode = True

steermultiplier = 3

class CarGenome(training.Genome):
    def setup(self, track):
        self.obj = Car(track)

    def step(self):
        car = self.obj

        scans = car.getScans()
        steer = self.feed_forward([*scans, car.v])[0]
        car.acc = 1
        car.steer = -steermultiplier + 2 * steermultiplier * steer
        car.move()
        car.updateScore()

        self.last_scores.append(car.score)
        if car.checkCollision():
            return False
        if len(self.last_scores) > 20 and self.last_scores[-1] <= self.last_scores[-20]:
            return False
        return True

    def run_evaluation(self, generation: int = None):
        if generation:
            timestepamount = min(2000 + (generation * 100), 5000)
        else:
            timestepamount = 5000

        self.last_scores = []

        for _ in range(timestepamount):
            if not self.step():
                break

        return self.obj.score


if training_mode:
    class CarTrainer(training.NeuroEvolution):
        def _get_default_network(self):
            defaultnet = network.NeuralNetwork([6]+hidden_layers)
            defaultnet.add_layer(1, default_acfunc="sigmoid")
            return defaultnet

    trainer = CarTrainer(CarGenome, track=Tracks.monaco,
                         name=name, folder=folder)
    trainer.population_size = 100
    trainer.learning_rate_base = 0.05
    trainer.learning_rate_factor = 0.99
    trainer.mutation_chance = 0.25
    trainer.setup_auto()

    clearTraces()

    tk = gui.TrainingGUI(trainer)

    def afterrun():
        saveTraces([genome.obj for genome in trainer.genomes],
                   gen_or_name=trainer.generation)
        trainer.save_to_file()

    tk.nn_afterrun = afterrun
    tk.mainloop()
else:
    clearTraces()

    myloader = loader.NeuroLoader(name=name, folder=folder)
    carai = myloader.get_genome(CarGenome, track=Tracks.monaco)
    carai.run_evaluation()
    print(carai.score)

    saveTraces([carai.obj])
