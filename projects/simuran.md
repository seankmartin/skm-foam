# SIMURAN

I have a package called SIMURAN that is designed to help simplify large analysis in Python. I will see if I can get this to a state where it would be publishable. It certainly seems useful for Axona data. The big question is can it be used for other data, such as neuropixels for example. If it can, it may well be a goer!

Really I think the big push for this would be getting good use cases out there.

Here is a paper on a tool - I should also definitely check this out https://www.nature.com/articles/nmeth.3041 

The main aim of SIMURAN is to remove the need for people to code standard data management, file selection methods, batch coding, multiprocessing, etc. and simply focus on the analysis that they want to perform, facilitating performing large analyses on multi-region data.

To use it, one provides the program with a description of their data, how to load that data if it is not an already supported format, what analysis to perform on the data, and what to save from the analysis (by default it saves everything).

My original idea to do this was to extend neurochat, but neurochat is ill-suited to performing comparisons and handling data from multiple brain regions - such as comparing the LFPs from SUB and RSC.

The program is heavily inspired by:
 
1. NeuroChaT - Considering cells, lfps, spatial data, etc. as singular objects and coding the relationship between them to perform analyses.
2. Inviwo (https://inviwo.org/) - How to add your own custom code into a project. Inviwo's method is to provide you with a folder which you can simply drag and drop any additional analysis into, which is very convenient.
3. Sumatra (https://neuralensemble.org/sumatra/) - Keeping track of the code used to produce analyses. Basically it stores extra information when the code is run about the system used, time that was taken, code version, etc.
4. SpikeInterface (https://www.biorxiv.org/content/10.1101/796599v2) - The code is structured similarly to theirs, they aim to provide code that works with any spike sorting format. The idea here is to provide code that works with any electrophys format.

## Possible things to talk to

1. NeuroChaT
2. MNE
3. Elephant
4. NWB NC?

## Considerations

- Implement converters
- Delete output folder if -o passed
- Clear STDout log on program start.
- Save after functions to different place
- New mode where parameters are not written! A read only mode.
- Improve SIMURAN help.
- Support tdqm progress bar or none.
- Restructure the project to adhere to new PEP guidelines, especially with typing. Related to this, check how to handle default values in classes instead of just using None, so as to adhere to typing (e.g. empty containers instead of None).
- This would be very helpful to integrate into the code https://mypy.readthedocs.io/en/stable/introduction.html