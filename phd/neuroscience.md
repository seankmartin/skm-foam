---
tags: neuroscience
date: 2021--08--02
type: note
---

# Neuroscience

Big note from Mark Humphries paper that I didn't really account for, calcium imaging is super low framerate! E.g. in the Carsen and Stringer paper, it is a 2Hz sampling rate - so there is no way this could be anything close to spikes.

## Resources

- Good human brain atlas [BRAIN ATLAS](http://helpthereisabraininmyhead.com/brain-atlas)
- Comp neuro book, in particular part II describes some gross anatomy [GitHub - CompCogNeuro/ed4: Computational Cognitive Neuroscience, Fourth Edition](https://github.com/CompCogNeuro/ed4)
- Neuromatch academy [Introduction — Neuromatch Academy: Computational Neuroscience](https://compneuro.neuromatch.io/tutorials/intro.html)
- Particularly the causality discussion [Network Causality — Neuromatch Academy: Computational Neuroscience](https://compneuro.neuromatch.io/tutorials/W3D5_NetworkCausality/chapter_title.html)

## Data

- [OpenNeuroA free and open platform for sharing MRI, MEG, EEG, iEEG, ECoG, ASL, and PET data - OpenNeuro](https://openneuro.org/)
- [DABI](https://dabi.loni.usc.edu/about)

## Interesting ideas

### Voltage imaging

Really interesting idea, especially considering that it kind of combines the ideas of calcium imaging and electrophys.
For instance, with calcium imaging you know where the neurons are, but a probe is blind.
In theory, you could imagine that you could know where the neurons you are recording are, and map these to a connectome.
In that way, you could have a kind of live connectome.

## Facts

- In the cortex and hippcompampus there are about 400 different types of cells (Allen Brain Institute). They have papers on cell types in the visual cortex and cell types in the motor cortex.
- Mammilian brains have between 10^8 and 10^11 neurons, which are organised with roughly 10^3 discrete cell types, and are recurrently and dynamically interconnected with 10^3 and 10^4 other neurons.
- As the system size increases, correlation and granger causality can't pick up the true underlying connectivity.