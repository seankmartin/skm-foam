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