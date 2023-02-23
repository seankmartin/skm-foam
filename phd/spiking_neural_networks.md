---
tags: neuroscience
date: 2023--02--23
type: note
---

# Spiking neural networks

See youtube tutorial by Dan goodman [here](https://www.youtube.com/watch?v=GTXTQ_sOxak&list=PL9YzmV9joj3EvcvT0eHoYwBMcV-V3exDV&index=1).

Part one shows how to use Brian to model a simple thing where a group of neurons in the ear generate spikes, and then you code how those are linked to a second set of neurons which decode information from those spikes.

There are also these Type 1 or 2 neurons that I have not come across before [here](https://neuronaldynamics.epfl.ch/online/Ch4.S4.html)

## The basics

1. Strengthen/weaken connections between neurons (synapses).
2. Add/remove synapses.
3. Add/remove neurons.
4. Other? Such as RNA being sent between neurons.
5. Change how neurons integrate informate (e.g. LIF).

## Plasticity (or learning in SNN)

Not great methods:

1. STDP - spike time dependent plasticity. Simple, but not scale that well.
2. Reward-modulated - again, not work that well for hard tasks.

Better methods:

1. Hebbian - if two neurons fire together, then increase the strength of the connection between them. This is a good method, but it is not clear how to implement it in a spiking neural network.
2. Reservoir computing (limited performance).
3. Evolutionary optimisation (computationally heavy).
4. Surrogate gradient descent.

## Why can't you use backprop for SNNs

Don't forget the Jacobian matrix vector version of the chain rule works for vectors.

The Heaviside function which is used for the LIF model (fires when v > some value) has almost zero gradient everywhere.
Idea 1: use a different function that has a gradient everywhere. This is not a good idea because it is not biologically plausible. Also slow.
Idea 2: surrogate gradient descent. Only smooth (sigmoid function) when performing backwards pass. However, when doing the forward pass keep the Heaviside function. This works, but it is still slow at the moment. 

To actually implement surrogate gradient descent, you can create a subclass of the torch autograd function and define a different forward and backward function, so that the forward still spikes, but the backward estimates using a smooth differentiable function.

## Ideas for projects

1. Can we make this more efficient (e.g. local learning)? It needs to run faster, be better scaling, and handle sparse connections (currently works for dense).
2. What are the computational advantages of SNNs? Could you use them for fast decision making? Be robust to noise, adversarial attacks, be more general, or use low power?
3. Related to biology - what are the roles of spikes? Are they just energy efficient or just use transmission. What about local learning rules? What is the interaction with synapse and neuron dynamics?

## Overall

This is very much like replacing a hidden layer in an ANN by a similar set of nodes, but instead of a same backward and forward step, they perform differently at each step.
HOWEVER, you can now do some stuff like perform neural analysing on your now fake neurons, which is very interesting.
Crazy idea, to create a huge 250ish author project.
