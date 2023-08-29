---
tags: PhD LFP
---


# Beth LFP

## TODO

- Update the paper.
- Combine Matheus code with mine and think about how to share data.
- Consider the animal notes and adding more animals
- Compare histology to animal notes
- Why is there zero power in some signals (see process_lfp.log) - is the normalising?

## Consideration for NWB

- Perhaps consider a separate conversion and picking process for the muscimol data? It can obviously use a lot from the original conversion, but I don't think I can do a direct conversion.

## Snakemake conversion checklist

- [x] Speed theta check plot
- [x] Speed IBI (not doing this for now)
- [x] LFP plot (normalised LFP)
- [x] Spike LFP (openfield and muscimol)
- [ ] T maze coherence
- [ ] Hypothesis tests.
- [ ] Fix snakemake tests.
- [x] Fix conversion of NWB data without units for many cases.

## Papers

- Lots of information on speed and LFP (in HC, but still relevant) https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3366345/

## Meetings

### 19/07/2021

With Shane and Matheus.

Perhaps equal contribution.

Do the proper controls and the proper statistics.
Also speed LFP not being a combination of two things.

Perpendicular to RSC (PFC is the same), slight angle of the LFP
Parallel in SUB
Ask Beth about histology.

Make a shared doc, and lets start writing methods and results into that.
Just tell the story of things (cut and paste).
E.g. take Jneuro paper and take methods from that.

### 27/05/2021

Questions:

- Do we want to consider CA1 in this from Matheus? I don't have the LFP data, only the spikes.
- Why was recording performed in the RSC? It seems an interesting area but its function is still disputed. What was the rationale for RSC? Is it due to evidence from lesion studies? Why RSP over say EC? Looking for a link, like a conductor region similar to Ham's idea of what CLA does? In that case directed coherence should be checked.
- Does anyone remember if we deleted any figures related to LFP from the first paper?
- Thoughts on what to include - seems a lot of the cells were from habituation (I guess from the tetrode lowering). Do we want to consider those or the more stable non-habituation since probes no move. Or both?

What I have been doing
I was very caught up by literature review and progress meeting doc + pres.
Fully focused on this now though.
- Cleaning up what I have done - publication ready, takes surprisingly long
- LFP rate map - I just can't figure out any mistakes in it but it shows very little, CLA specific? Check vs cells, though by the literature a cell shouldn't dominate LFP. Could check in CA1 for comparison.
- Much better code to work from to clean the signals. Considering the two LFP wires (Matheus did Beth get back to you, are they thicker?) as average is not fully appropriate (signals can cancel out). Mind you, I don't think it makes a big difference to relative powers, just absolute powers - promising. Hence others doing z-scores, but then lose absolute power.
	
Notes from meeting:
Matheus seems to have no difference
Lauren Frank very careful investigator (2009 nature neuro)
Cortical theories of consolidation during sleep. - how does sleep play a role in the consolidation.
Matheus think record CA1 and SUB with EMG along with ATNx (plasticity LTP)
Perhaps not looking in the right place - theta generators
Compensatory idea (happens from a lesion) - loss of tonic input for e.g.
HC as interosceptive.
Animal models of type I
Katherine sweeny reed
Think about the right animal model and using the ventral HC for assessing internal state.
E.g. Apple are introducing a watch that measures internal glucose from sweat.

WT gone
Type I Diabetes - with glucose
SFI with lipid state (glucose sensor and transporter) - can do cortisol sensing as well
Up until the 31st of Oct

I'll send on documents
Will share the recording of Tingley

IDEA now LTP in ATN SUB CA1 etc. (with lesions, that is the full experiment)
