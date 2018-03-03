from brain.brain import Brain
from graph.graphic_neuron import GraphicNeuron
from brain.neuron import Neuron
from brain.neuron_factory import NeuronFactory


class GraphicNeuronFactory(NeuronFactory):

    def create_neuron(self, neuron_id, presentation, brain: Brain, layer=None) -> Neuron:
        return GraphicNeuron(neuron_id, presentation, brain, layer=layer, location=None)