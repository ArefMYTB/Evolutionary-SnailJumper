import copy
import random
from random import seed
from random import randint
from player import Player
import numpy as np

class Evolution:
    def __init__(self):
        self.game_mode = "Neuroevolution"

    def next_population_selection(self, players, num_players):
        """
        Gets list of previous and current players (μ + λ) and returns num_players number of players based on their
        fitness value.

        :param players: list of players in the previous generation
        :param num_players: number of players that we return
        """
        # TODO (Implement top-k algorithm here)
        players.sort(key=lambda x: x.fitness, reverse=True)
        # TODO (Additional: Implement roulette wheel here)
        # TODO (Additional: Implement SUS here)
        # TODO (Additional: Learning curve)
        most_fitness = players[0].fitness
        least_fitness = players[len(players)-1].fitness
        s = sum(x.fitness for x in players)
        average_fitness = s/len(players)
        # write data in a file.
        file = open("myfile.txt", "a")
        L = ["most fitness: ", str(most_fitness), ", least fitness: ", str(least_fitness), ", average fitness: ", str(average_fitness), "\n"]
        file.writelines(L)
        file.close()

        return players[: num_players]

    def generate_new_population(self, num_players, prev_players=None):
        """
        Gets survivors and returns a list containing num_players number of children.

        :param num_players: Length of returning list
        :param prev_players: List of survivors
        :return: A list of children
        """
        first_generation = prev_players is None
        if first_generation:
            return [Player(self.game_mode) for _ in range(num_players)]
        else:
            # TODO ( Parent selection and child generation )
            # parent selection
            new_players = []
            parents = []

            # TODO (Implement top-k algorithm here)
            # seed(1)
            # while len(parents) != 2 * num_players:
            #     p = randint(0, len(prev_players)-1)
            #     parents.append(prev_players[p])

            # TODO ( QT Algorithm)
            qt_parameter = 5
            p = 0.5
            while len(parents) != 2 * num_players:
                candidate = np.random.choice(prev_players, qt_parameter, replace=False).tolist()
                candidate.sort(key=lambda x: x.fitness, reverse=True)
                for i in range(len(candidate)):
                    if random.random() < p * (1 - p) ** i:
                        parents.append(candidate[i])
                        break

            # child generation
            for i in range(num_players):
                # mid_fit = (parents[i * 2].fitness + parents[i * 2 + 1].fitness)/2
                # if mid_fit > parents[i * 2].fitness or mid_fit > parents[i * 2 + 1].fitness:
                if random.random() < 0.4:
                    new_players.append(self.crossover(parents[i * 2], parents[i * 2 + 1]))
                else:
                    # if(parents[i * 2].fitness > parents[i * 2 + 1].fitness):
                    new_players.append(self.clone_player(parents[i * 2]))
                    # else:
                    #     new_players.append(self.clone_player(parents[i * 2 + 1]))
            for i in range(num_players):
                self.mutate(new_players[i])
            return new_players

    def clone_player(self, player):
        """
        Gets a player as an input and produces a clone of that player.        """
        new_player = Player(self.game_mode)
        new_player.nn = copy.deepcopy(player.nn)
        new_player.fitness = player.fitness
        return new_player

    def crossover(self, parent1, parent2):
        child = self.clone_player(parent1)
        child.fitness = (parent1.fitness + parent2.fitness) / 2
        for layer_number in parent1.nn.weights.keys():
            if layer_number % 2 == 0:
                child.nn.weights[layer_number] = parent2.nn.weights[layer_number]
                child.nn.biases[layer_number] = parent2.nn.biases[layer_number]
        return child

    def mutate(self, child):
        mutation_probability = .8
        noise_range = .3
        if random.random() < mutation_probability:
            for layer_number in child.nn.weights.keys():
                child.nn.weights[layer_number] += np.random.normal(0, noise_range, child.nn.weights[layer_number].shape)
                child.nn.biases[layer_number] += np.random.normal(0, noise_range, child.nn.biases[layer_number].shape)
        return child