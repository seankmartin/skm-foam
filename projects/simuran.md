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

## GUI requirements

1. Dynamically adding nodes either via another window or a popup menu.
2. Support custom nodes.
3. Set parameters on nodes and use these for computation.
4. Show plots on right click.
5. Show tooltips of variables.

Currently planning to implement in dear pygui, but check https://www.blenderfreak.com/tutorials/node-editor-tutorial-series/ if not working out.

## Best GUI tool

- Likely the best thing to use is to continue with pyside (maybe use 6), which is basically pyqt.
- OR use https://github.com/hoffstadt/DearPyGui - dear py gui, which actually looks really good and might save me a lot of time. It even has in built support for nodes. Just need to make sure it works without a GPU.

## Considerations

- Implement converters
- This looks well written, should compare my program to it https://github.com/mouseland/cellpose.
- Phy would be another good place to check UI on https://github.com/cortex-lab/phy.
- Check how to add to colab e.g. https://colab.research.google.com/drive/1Qp7RAnPFj8zrhfEGkV7nHbzFiQ8w-4FX?usp=sharing for YASS.
- Check out integration of things like https://github.com/KordingLab/spykes.
- Should integrate decoding https://github.com/KordingLab/Neural_Decoding.
- Add code coverage statistics for the test suite.
- Delete output folder if -o passed
- Clear STDout log on program start.
- Save after functions to different place
- New mode where parameters are not written! A read only mode.
- Improve SIMURAN help.
- Support tdqm progress bar or none.
- Restructure the project to adhere to new PEP guidelines, especially with typing. Related to this, check how to handle default values in classes instead of just using None, so as to adhere to typing (e.g. empty containers instead of None).
- This would be very helpful to integrate into the code https://mypy.readthedocs.io/en/stable/introduction.html
- When complete this work, try run with num_workers 4 and see if all results are same and evaluate time benefits.
- Really consider getting the code to work well within colab, or at least with data from the cloud.
- Clearer caching of results.
- Need to convert SIMURAN logging to rich https://github.com/willmcgugan/rich.
- Covert CLI to https://typer.tiangolo.com/.

## Paragraph from Shane

The results will be graphically displayed, as will the processing method. A click and drag interface will allow processing flow-charts to be constructed and reconstructed while the consequent results are seamlessly displayed and updated. Multi-route and branched flow-charts will be possible, allowing for easy comparison of different processing methods and different processing parameters. Dialogue boxes will offer explanation and detailed customisation of processing units. The automation will be done within Python, which has the advantage that many of the analysis tools already have freely available Python implementations.