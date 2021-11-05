---
tags: neuroscience
date: 2021--08--14
type: note
---

# Book reviews

## The Spike - Mark Humphries

A very good description of spikes in the brain, wish I had this at the start of my PhD!
So far nothing really new to me, but however it is important to re-emphasise how many spikes are needed to make just one spike - and the inhibition excitation balance (inhibition is stronger but less of them).

Cells also (at least in VC) tend to be connected to other cells that respond to the same thing more regularly. This is because lots of cells would need to send this signal of hey I see and edge for it to create a new spike elsewhere.

So with place cells, they must be an ensemble of similar responding place cells that send the information to somewhere downstream. But where is the downstream, and what does it do with it? And if we recorded lots of cells, could we detect the ensemble and the downstream? Further there should really be downstreams.

So the way this must work is that ensembles really are the unit of computation not single cells. But what about those cells that respond alone? I think are some examples of hugely influential single cells (retinal ganglion?). Then these ensembles interact.

So you could have a bunch of ensembles that shouldn't interact for distinct sense/ideas, which then interact with other ensembles to send information (as a single spike would just get lost in the void.)

This would suggest that the analysis I should really be focusing on is either PCA (assuming a dim is an ensemble) or some form of ensemble detection + interacting (e.g. info theory) on these ensembles. It would want to be pretty automatic as well. I.e. you give it a matrix of spike times (problem 1, unless binned it is not a equal dim matrix) and then it computes directly from the matrix in easy manner with a few well controllable parameters.

ML could come into this perhaps. Is there a supervised manner in which this would be developed or would it have to be unsupervised based on identifying patterns in the data that might suggest that the neurons are acting as an ensemble.

### The future of spikes

1. The cortex is not everything, try recording from deeper areas simultaneously to test better.
2. Voltage imaging.
3. Thought experiment - what if we could record from every neuron in the brain, and capture every spike - what would we do with it?
4. Neural dust
5. A measure of population correlation could be the sum or product of region values where regions are made up of groups on neurons.
6. Spikes are not generally recorded in humans, so how can we hope to understand plans, aspirations, imagination etc.

## Models of the mind - Grace Lindsay

The first few chapters present knowledge I was already familiar with, though admittedly in a nice fashion - would have been good if this existed at the start of my time in neuroscience!
Some new things from this:
Cerrebellum and perceptron, Ring network head direction system

After this, here are some things I had forgotten or did not know:

- A neuron combines its inputs over about 20ms.
- Shannon information is in bits - the log base 2 of the inverse probability of a symbol occuring, and the entropy of a code (with is a set of symbols) is the sum of information times probability.

The final chapters however, pick up some ideas that I was not familiar with.

- The free energy principal in the brain, which is a fair idea but not fully testable, which state that the brain minimises the difference between prediction and reality in the brain.
- Numenta and the "thousand brains theory of intelligence". I don't like this one much, but the idea is that there are cortical columns in the brain that interact - so a cortical column would be the unit of computing. However, the neocortex is not uniform, I'm just not convinvced.
- IIT - integrated infromation theory, to quantify conciousness, which is very hard! For example, in the definition a thermometer can end up with (a very small) but non zero level of conciousness.
- SPAUN - a model of the brain that works.

However, there is an interesting point here. From evolution, biology took whatever route it needed to create functioning organisms, without regard to how understandable any part of them would be.
