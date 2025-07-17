---
tags: PhD
date: 2022--05--04
type: note
---

# Neural Ensembles 2022

## Assorted notes and thoughts

## Zebrafish imaging with Mishra Ahrens

- Whole brain cellular light sheet imaging in zebrafish (120000 neurons, 20000 glia) - see Vladimirov Nature Methods 2014
- They performed online data analysis on the cluster.
- Zebrafish swim against the waterflow, but remember where they are.
- By ablation of cells in SLO-MO, the memory is gone.
- However, activation of cells in SLO-MO mimics memory and makes the fish swim.
- SLO-MO projects to the inferior olive (GABAergic - inhibitory cells)
- Yang et al. 2021 Biorxiv
- SLO-MO might have an analogy in mammals.
- About 300 cells in area SLO-MO, which are part of a multi-region network. Ablating Inferior olive - SLO-MO still functions.
- SLO-MO -> IO -> Cerrebellum -> Motor area -> (the encoded signal becomes closer and closer to behavioural output).
- IDEA: Ablate random number of cells until you lose the memory (what would be % be and what would the robustness be).

## Control of neural networks with high precision - Valentina Emiliani

- Classically optogenetic activation turns on many cells at the same time.
- Trying to transition from whole region optogenetics to circuit optogenetics to manipulate single targets (or a few targets of choice).
- Holographic illumination (light shaping).

## Geometry of neural activity - Carsen stringer

- Ahrens at al 2013 (zebrafih)
- RNA sequencing (Tasic at al 2018, see kobak and berens 2019)
- FLYEM team
- Behavioural data (lots of it)
- Variance vs PC dimensions (eigenspectrum) - it follows a power-law decay, top few PC dimensions are not enough.
- t-SNE or autoencoders for unsupervised approaches. or the clustering output.
- The resulting method from this is Rastermap.
- Step 1 - cluster the data with k-means
- Step 2 - Rearrange clusters by similarity - sort the matrix of similarities between cluster activity. (keep power-law decay of PC variances) - iterative optimisation (NP HARD)
- Step 3 - Upsample cluster centers (lin interp I think)
- Step 4 - Assign neurons and sort (done)
- Benchmarks with neighbour metrics (local score) and also intermediate and global score of distances. [the idea is neighbours in Nspace vs those in linspace or 3dspace]
- Can visualise the behavioural predictions of (behaviour estimate neural activity).
- Ahrens lab zebrafish data - can colour neurons in the brain.
- Churchland lab - visualise widefield imaging data.
- Can compute clusters in lagged time
- Rastermap taking a space filling curve through the data?
- Check out the rastermap GUI (how does it load the data?)
- For CI imaging they cluster the deconvolved data. (long decay time of the sensor, you can get rid of the decay by deconvolution - increase SNR due to bleedthrough)
- It is integrated into Suite2p.

## Reading the mind of a Cnidarian - Rafeal Yuste

- CNidarians (no central brain) - bilaterians (a bilateral brain)
- Genetic code was broken in (codons)
- Hydra vulgaris (200 - 2000 neurons) with 11 neuronal cell types, two nets formed.
- Can see evry spike from every neuron in such a behaving animal with calcium imaging.
- Spontaneous correlated (ryhtmic) activity during relaxing.
- It seems there are about 12 ensembles - they are non-overlapping.
- Dupre and Yuste 2017.
- Can also image the activity of every muscle cell in the ectoderm and endoderm.
- gcamp in one, rcamp in the other circuit.
- Neural activity, muscle activity, behaviour (all can be measured).
- So one can link all the matrices (adrienne fairhall currently working on this).
- Goal is to explain how all the 12 ensembles work.
- You can also take apart the animal and it will reform. (it self assembles)
- Contraction bursts.

## David Anderson